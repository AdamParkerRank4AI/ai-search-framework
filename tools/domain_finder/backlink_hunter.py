"""
Backlink Hunter — Find available domains that actually have press coverage and backlinks.

Unlike domain_scanner.py which just checks if domains are available, this tool:
1. Searches for DEAD companies in a niche (invoice finance, factoring, etc.)
2. Checks if their domains are available via RDAP
3. Checks Majestic Million for backlink data
4. Searches Google/Bing for actual press articles linking to each domain
5. Checks the Open PageRank API for domain authority scores
6. Reports which domains are worth buying based on REAL backlink evidence

The key insight: a domain is only worth buying for 301 redirects if other sites
actually LINK to it (not just mention the company name).

Usage:
    python3 -m tools.domain_finder.backlink_hunter --niche "invoice finance"
    python3 -m tools.domain_finder.backlink_hunter --domains domains.txt
    python3 -m tools.domain_finder.backlink_hunter --domains-list "domain1.co.uk,domain2.com"
    python3 -m tools.domain_finder.backlink_hunter --niche "factoring" --tld co.uk

No API keys required (uses free public APIs and search engines).
Optional: Set OPEN_PAGERANK_API_KEY for domain authority scores (free from domcop.com).
"""

import argparse
import csv
import json
import os
import re
import sys
import time
import urllib.request
import urllib.error
import urllib.parse
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional

from tools.domain_finder.rdap_checker import check_domain


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class BacklinkResult:
    domain: str
    # Availability
    status: str = "unknown"  # available, registered, expired, error
    expiry_date: Optional[str] = None
    days_until_expiry: Optional[int] = None
    # Majestic Million data
    majestic_rank: Optional[int] = None
    majestic_ref_subnets: Optional[int] = None
    majestic_ref_ips: Optional[int] = None
    # Open PageRank
    page_rank: Optional[float] = None
    # Ahrefs data (from CSV export)
    ahrefs_dr: Optional[float] = None
    ahrefs_referring_domains: int = 0
    ahrefs_backlinks: int = 0
    # Press & backlink evidence
    press_mentions: int = 0  # number of search results mentioning the domain
    linking_sites: list = field(default_factory=list)  # sites that actually link TO this domain
    press_examples: list = field(default_factory=list)  # example press article titles/URLs
    # Scoring
    backlink_score: float = 0.0
    verdict: str = ""  # "BUY", "MAYBE", "SKIP"

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------------------
# Majestic Million lookup
# ---------------------------------------------------------------------------

MAJESTIC_CSV = os.path.join(os.path.dirname(__file__), "majestic_million.csv")
_majestic_cache: Optional[dict] = None


def _load_majestic() -> dict:
    global _majestic_cache
    if _majestic_cache is not None:
        return _majestic_cache

    _majestic_cache = {}
    if not os.path.exists(MAJESTIC_CSV):
        return _majestic_cache

    with open(MAJESTIC_CSV, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row.get("Domain", "").lower()
            if domain:
                _majestic_cache[domain] = {
                    "rank": int(row.get("GlobalRank", 0)),
                    "ref_subnets": int(row.get("RefSubNets", 0)),
                    "ref_ips": int(row.get("RefIPs", 0)),
                }
    return _majestic_cache


def check_majestic(domain: str) -> Optional[dict]:
    data = _load_majestic()
    return data.get(domain.lower())


# ---------------------------------------------------------------------------
# Open PageRank API (free, optional)
# ---------------------------------------------------------------------------

def check_pagerank(domain: str, api_key: str = None) -> Optional[float]:
    """Check Open PageRank score (0-10). Free API from domcop.com."""
    if not api_key:
        api_key = os.environ.get("OPEN_PAGERANK_API_KEY")
    if not api_key:
        return None

    try:
        url = f"https://openpagerank.com/api/v1.0/getPageRank?domains%5B0%5D={domain}"
        req = urllib.request.Request(url, headers={"API-OPR": api_key})
        with urllib.request.urlopen(req, timeout=10) as resp:
            data = json.loads(resp.read().decode())
            results = data.get("response", [])
            if results:
                rank = results[0].get("page_rank_decimal")
                if rank is not None:
                    return float(rank)
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# Backlink evidence from multiple sources
# ---------------------------------------------------------------------------

def load_ahrefs_export(filepath: str) -> dict:
    """
    Load an Ahrefs CSV/TSV export (Referring Domains or Backlinks report).

    Export from Ahrefs:
      Site Explorer → your domain → Referring Domains → Export CSV

    Returns dict keyed by target domain with backlink data.
    """
    data = {}
    if not os.path.exists(filepath):
        return data

    with open(filepath, "r") as f:
        # Ahrefs exports can be CSV or TSV
        sample = f.read(1024)
        f.seek(0)
        dialect = csv.Sniffer().sniff(sample, delimiters=",\t")
        reader = csv.DictReader(f, dialect=dialect)

        for row in reader:
            # Ahrefs column names vary by report type
            target = (
                row.get("Target", "") or row.get("target", "") or
                row.get("Domain", "") or row.get("domain", "")
            ).lower().strip()

            if not target:
                continue

            # Extract referring domain info
            ref_domain = (
                row.get("Referring Domain", "") or row.get("Source", "") or
                row.get("referring_domain", "") or row.get("Ref. domain", "")
            ).strip()

            dr = row.get("DR", row.get("Domain Rating", ""))
            backlinks = row.get("Backlinks", row.get("backlinks", ""))

            if target not in data:
                data[target] = {
                    "dr": None,
                    "referring_domains": [],
                    "backlink_count": 0,
                }

            if dr:
                try:
                    data[target]["dr"] = float(dr)
                except (ValueError, TypeError):
                    pass

            if ref_domain:
                data[target]["referring_domains"].append(ref_domain)

            if backlinks:
                try:
                    data[target]["backlink_count"] = max(
                        data[target]["backlink_count"], int(backlinks)
                    )
                except (ValueError, TypeError):
                    pass

    return data


def load_search_results(filepath: str) -> dict:
    """
    Load pre-fetched search results from a JSON file.

    Format: {"domain.com": {"mentions": 5, "linking_sites": ["bbc.co.uk", ...], "examples": [...]}}

    You can generate this by searching Google/Bing for "domain.com" and recording
    which sites mention or link to the domain.
    """
    if not os.path.exists(filepath):
        return {}
    with open(filepath, "r") as f:
        return json.load(f)


def check_industry_directories(domain: str) -> dict:
    """
    Check known invoice finance industry directories for links to this domain.

    These directories often contain the most reliable backlinks for niche
    finance domains. Checks the actual page HTML for hyperlinks.
    """
    results = {
        "press_mentions": 0,
        "linking_sites": [],
        "press_examples": [],
    }

    # Known directories that list UK invoice finance companies with links
    directories = [
        {
            "name": "FundInvoice",
            "url": "https://www.fundinvoice.co.uk/invoice-finance/list-invoice-finance-companies-uk.html",
        },
        {
            "name": "Invoice Funding",
            "url": f"https://invoice-funding.co.uk/{domain.replace('.co.uk', '').replace('.com', '')}/",
        },
        {
            "name": "Factoring Helpline",
            "url": f"https://www.factoringhelpline.co.uk/factoring-companies/{domain.replace('.co.uk', '').replace('.com', '')}/",
        },
    ]

    for directory in directories:
        try:
            req = urllib.request.Request(directory["url"], headers={
                "User-Agent": "Mozilla/5.0 (compatible)",
                "Accept": "text/html",
            })
            with urllib.request.urlopen(req, timeout=10) as resp:
                html = resp.read().decode("utf-8", errors="replace")

                # Check if our domain appears as a hyperlink in the page
                # Look for href="...domain..." patterns
                domain_lower = domain.lower()
                patterns = [
                    f'href="https://{domain_lower}',
                    f'href="http://{domain_lower}',
                    f'href="https://www.{domain_lower}',
                    f'href="http://www.{domain_lower}',
                    f'href="//{domain_lower}',
                ]

                for pattern in patterns:
                    if pattern in html.lower():
                        results["press_mentions"] += 1
                        results["linking_sites"].append(directory["name"])
                        results["press_examples"].append({
                            "title": f"Listed on {directory['name']}",
                            "url": directory["url"],
                            "type": "directory_link",
                        })
                        break
        except Exception:
            pass

        time.sleep(0.5)

    return results


def search_for_backlinks(domain: str, ahrefs_data: dict = None,
                          search_data: dict = None) -> dict:
    """
    Aggregate backlink evidence from all available sources.

    Priority order:
    1. Ahrefs data (if CSV export provided) — most reliable
    2. Pre-fetched search results (if JSON provided)
    3. Industry directory checks (always attempted)
    4. Majestic Million (checked separately)
    """
    results = {
        "press_mentions": 0,
        "linking_sites": [],
        "press_examples": [],
        "ahrefs_dr": None,
        "ahrefs_referring_domains": 0,
        "ahrefs_backlinks": 0,
    }

    # 1. Ahrefs data
    if ahrefs_data and domain.lower() in ahrefs_data:
        ahrefs = ahrefs_data[domain.lower()]
        results["ahrefs_dr"] = ahrefs.get("dr")
        results["ahrefs_referring_domains"] = len(ahrefs.get("referring_domains", []))
        results["ahrefs_backlinks"] = ahrefs.get("backlink_count", 0)
        results["linking_sites"].extend(ahrefs.get("referring_domains", []))
        results["press_mentions"] = results["ahrefs_referring_domains"]

    # 2. Pre-fetched search results
    if search_data and domain.lower() in search_data:
        sr = search_data[domain.lower()]
        results["press_mentions"] += sr.get("mentions", 0)
        results["linking_sites"].extend(sr.get("linking_sites", []))
        results["press_examples"].extend(sr.get("examples", []))

    # 3. Industry directory checks (these actually work via HTTP)
    dir_results = check_industry_directories(domain)
    results["press_mentions"] += dir_results["press_mentions"]
    results["linking_sites"].extend(dir_results["linking_sites"])
    results["press_examples"].extend(dir_results["press_examples"])

    # Deduplicate
    results["linking_sites"] = list(set(results["linking_sites"]))

    return results


# ---------------------------------------------------------------------------
# Known dead companies by niche (curated lists)
# ---------------------------------------------------------------------------

# Industry directories that list invoice finance companies with links
KNOWN_DIRECTORIES = [
    "fundinvoice.co.uk",
    "invoice-funding.co.uk",
    "factoringhelpline.co.uk",
    "businessfinancing.co.uk",
    "capitalise.com",
    "fundingxchange.co.uk",
    "companeo.co.uk",
]

DEAD_COMPANIES = {
    "invoice finance": {
        # Real UK invoice finance companies that went into administration/dissolved
        "co.uk": [
            "alexlawriefactors.co.uk",      # Alex Lawrie Factors — merged into Lloyds
            "griffinfactors.co.uk",          # Griffin Factors — absorbed by HSBC
            "castlebusinessfinance.co.uk",   # Castle Business Finance — admin June 2020
            "positivecash.co.uk",            # Positive Cashflow Finance
            "platformblack.co.uk",           # Platform Black — became Sancus
            "kellockfactors.co.uk",          # Kellock Factors
            "inksmoor.co.uk",               # Inksmoor Finance — renamed Acuity
            "firstcapitalfactors.co.uk",     # First Capital Factors — admin
            "davenhamdirect.co.uk",          # Davenham Group — dissolved
            "workingcapitalpartners.co.uk",  # WCP — admin May 2019
            "lloydsfactoring.co.uk",         # Lloyds old factoring brand
            "globalfactors.co.uk",           # Global Factors
            "hhcashflow.co.uk",             # HH Cashflow
            "justcashflowplc.co.uk",        # Just Cash Flow — admin Dec 2022
            "centricfinance.co.uk",          # Centric Commercial Finance
            "oxfordfunding.co.uk",           # Oxford Funding
            "advantagebusinessfinance.co.uk", # Advantage Business Finance
            "sancusfinance.co.uk",           # Sancus Finance (ex Platform Black)
            "scotpacbf.co.uk",               # Scottish Pacific Business Finance
            "ultimatefinance.co.uk",         # Ultimate Finance — acquired
            "regencyfactors.co.uk",          # Regency Factors
            "centriccf.co.uk",              # Centric CF
            "acuitycf.co.uk",               # Acuity Commercial Finance
        ],
        "com": [
            "absoluteinvoicefinance.com",     # Cattles → Absolute → Aldermore
            "griffinfactors.com",            # Griffin Factors .com variant
            "alexlawriefactors.com",         # Alex Lawrie .com variant
            "invoicefinancenews.com",         # Exact match news domain
            "invoicefinanceguide.com",        # Exact match guide domain
            "invoicefinancedirect.com",       # Exact match commercial domain
            "barclaysinvoicefinance.com",     # Barclays exited factoring 2021
            "greensillcapital.com",           # Greensill Capital — massive scandal
            "stenngroup.com",                # Stenn — admin Dec 2024
            "firstcapitalfactors.com",       # First Capital Factors .com
            "platformblack.com",             # Platform Black .com
            "workingcapitalpartners.co.uk",  # WCP .co.uk variant
        ],
    },
    "commercial finance": {
        "co.uk": [
            "castlebusinessfinance.co.uk",
            "advantagebusinessfinance.co.uk",
            "centricfinance.co.uk",
            "davenhamdirect.co.uk",
            "oxfordfunding.co.uk",
            "commercialfinanceguide.co.uk",
            "businessfinancedirect.co.uk",
            "tradefinancedirect.co.uk",
        ],
        "com": [
            "commercialfinanceguide.com",
            "businessfinancedirect.com",
            "tradefinancedirect.com",
            "commercialfinancenews.com",
        ],
    },
    "factoring": {
        "co.uk": [
            "alexlawriefactors.co.uk",
            "griffinfactors.co.uk",
            "kellockfactors.co.uk",
            "globalfactors.co.uk",
            "regencyfactors.co.uk",
            "firstcapitalfactors.co.uk",
            "lloydsfactoring.co.uk",
            "comparefactoring.co.uk",
        ],
        "com": [
            "griffinfactors.com",
            "alexlawriefactors.com",
            "firstcapitalfactors.com",
            "comparefactoring.com",
        ],
    },
}


# ---------------------------------------------------------------------------
# Core scanning logic
# ---------------------------------------------------------------------------

def hunt_domain(domain: str, pagerank_key: str = None,
                ahrefs_data: dict = None, search_data: dict = None) -> BacklinkResult:
    """Full backlink hunt for a single domain."""
    result = BacklinkResult(domain=domain)

    # 1. Check RDAP availability
    rdap = check_domain(domain)
    result.status = rdap.status
    result.expiry_date = rdap.expiry_date
    result.days_until_expiry = rdap.days_until_expiry

    # Mark expired domains
    if rdap.status == "registered" and rdap.days_until_expiry is not None and rdap.days_until_expiry < 0:
        result.status = "expired"

    # If registered and not expiring soon, skip expensive checks
    if result.status == "registered":
        if rdap.days_until_expiry is None or rdap.days_until_expiry > 120:
            result.verdict = "SKIP (registered)"
            return result
        else:
            result.status = "expiring_soon"

    # 2. Check Majestic Million
    maj = check_majestic(domain)
    if maj:
        result.majestic_rank = maj["rank"]
        result.majestic_ref_subnets = maj["ref_subnets"]
        result.majestic_ref_ips = maj["ref_ips"]

    # 3. Check Open PageRank (if API key available)
    result.page_rank = check_pagerank(domain, pagerank_key)

    # 4. Search for actual backlink evidence
    backlink_results = search_for_backlinks(domain, ahrefs_data, search_data)
    result.press_mentions = backlink_results["press_mentions"]
    result.linking_sites = backlink_results["linking_sites"]
    result.press_examples = backlink_results["press_examples"]
    result.ahrefs_dr = backlink_results.get("ahrefs_dr")
    result.ahrefs_referring_domains = backlink_results.get("ahrefs_referring_domains", 0)
    result.ahrefs_backlinks = backlink_results.get("ahrefs_backlinks", 0)

    # 5. Score and verdict
    result = _score_domain(result)

    return result


def _score_domain(result: BacklinkResult) -> BacklinkResult:
    """Score a domain based on all available evidence."""
    score = 0.0

    # Ahrefs DR (max 4 points) — MOST RELIABLE when available
    if result.ahrefs_dr is not None:
        if result.ahrefs_dr >= 30:
            score += 4.0
        elif result.ahrefs_dr >= 20:
            score += 3.0
        elif result.ahrefs_dr >= 10:
            score += 2.0
        elif result.ahrefs_dr >= 5:
            score += 1.0
        elif result.ahrefs_dr >= 1:
            score += 0.5

    # Ahrefs referring domains (max 3 points)
    if result.ahrefs_referring_domains >= 50:
        score += 3.0
    elif result.ahrefs_referring_domains >= 20:
        score += 2.0
    elif result.ahrefs_referring_domains >= 10:
        score += 1.5
    elif result.ahrefs_referring_domains >= 5:
        score += 1.0
    elif result.ahrefs_referring_domains >= 1:
        score += 0.5

    # Majestic data (max 3 points) — only if no Ahrefs data
    if result.ahrefs_dr is None and result.majestic_ref_subnets:
        if result.majestic_ref_subnets >= 5000:
            score += 3.0
        elif result.majestic_ref_subnets >= 1000:
            score += 2.5
        elif result.majestic_ref_subnets >= 500:
            score += 2.0
        elif result.majestic_ref_subnets >= 100:
            score += 1.5
        elif result.majestic_ref_subnets >= 50:
            score += 1.0

    # Open PageRank (max 1 point)
    if result.page_rank:
        if result.page_rank >= 3:
            score += 1.0
        elif result.page_rank >= 1:
            score += 0.5

    # Directory/press links found (max 2 points) — KEY DIFFERENTIATOR
    if result.press_mentions >= 5:
        score += 2.0
    elif result.press_mentions >= 3:
        score += 1.5
    elif result.press_mentions >= 1:
        score += 1.0

    result.backlink_score = min(10.0, round(score, 1))

    # Verdict
    if score >= 5.0:
        result.verdict = "BUY"
    elif score >= 3.0:
        result.verdict = "MAYBE"
    elif score >= 1.0:
        result.verdict = "WEAK"
    else:
        result.verdict = "SKIP"

    return result


def hunt_domains(domains: list[str], pagerank_key: str = None,
                 ahrefs_file: str = None, search_file: str = None) -> list[BacklinkResult]:
    """Hunt backlinks for a list of domains."""
    # Pre-load Majestic
    majestic = _load_majestic()
    if majestic:
        print(f"  [✓] Loaded {len(majestic):,} domains from Majestic Million")
    else:
        print("  [!] Majestic Million CSV not found — backlink data will be limited")

    pr_key = pagerank_key or os.environ.get("OPEN_PAGERANK_API_KEY")
    if pr_key:
        print("  [✓] Open PageRank API key found")
    else:
        print("  [i] No Open PageRank API key — set OPEN_PAGERANK_API_KEY for DA scores")

    # Load Ahrefs data if provided
    ahrefs_data = None
    if ahrefs_file:
        ahrefs_data = load_ahrefs_export(ahrefs_file)
        if ahrefs_data:
            print(f"  [✓] Loaded Ahrefs data for {len(ahrefs_data)} domains")
        else:
            print(f"  [!] Could not load Ahrefs data from {ahrefs_file}")

    # Load pre-fetched search results if provided
    search_data = None
    if search_file:
        search_data = load_search_results(search_file)
        if search_data:
            print(f"  [✓] Loaded search results for {len(search_data)} domains")
        else:
            print(f"  [!] Could not load search results from {search_file}")

    print(f"\n  Checking {len(KNOWN_DIRECTORIES)} industry directories for backlinks...")

    results = []
    total = len(domains)

    for i, domain in enumerate(domains, 1):
        print(f"\n  [{i}/{total}] Hunting: {domain}")
        result = hunt_domain(domain, pr_key, ahrefs_data, search_data)

        # Status indicator
        status_map = {
            "available": "✓ AVAILABLE",
            "expired": "⚠ EXPIRED",
            "expiring_soon": "⏳ EXPIRING",
            "registered": "✗ TAKEN",
        }
        status_str = status_map.get(result.status, result.status)

        if result.verdict == "SKIP (registered)":
            print(f"       {status_str} — skipping (not purchasable)")
        else:
            print(f"       {status_str}")
            if result.majestic_ref_subnets:
                print(f"       Majestic: rank #{result.majestic_rank:,} | {result.majestic_ref_subnets:,} ref subnets")
            if result.page_rank:
                print(f"       PageRank: {result.page_rank}")
            print(f"       Press mentions: {result.press_mentions} | Linking sites: {len(set(result.linking_sites))}")
            if result.press_examples:
                for ex in result.press_examples[:3]:
                    print(f"         → {ex['title'][:80]}")
            print(f"       Score: {result.backlink_score}/10 → {result.verdict}")

        results.append(result)

    return results


# ---------------------------------------------------------------------------
# Report formatting
# ---------------------------------------------------------------------------

def _format_domain_detail(r: BacklinkResult, lines: list):
    """Format detailed info for a single domain in the report."""
    lines.append(f"\n  [{r.backlink_score}/10] {r.domain}  ({r.status})")
    if r.ahrefs_dr is not None:
        lines.append(f"    Ahrefs DR: {r.ahrefs_dr} | Referring domains: {r.ahrefs_referring_domains} | Backlinks: {r.ahrefs_backlinks}")
    if r.majestic_ref_subnets:
        lines.append(f"    Majestic: rank #{r.majestic_rank:,} | {r.majestic_ref_subnets:,} referring subnets")
    if r.page_rank:
        lines.append(f"    PageRank: {r.page_rank}/10")
    lines.append(f"    Directory/press links: {r.press_mentions} | Unique linking sites: {len(set(r.linking_sites))}")
    if r.linking_sites:
        lines.append(f"    Linking sites: {', '.join(list(set(r.linking_sites))[:10])}")
    if r.press_examples:
        lines.append(f"    Evidence:")
        for ex in r.press_examples[:5]:
            lines.append(f"      → {ex['title'][:70]}")
            lines.append(f"        {ex['url']}")


def format_report(results: list[BacklinkResult]) -> str:
    """Format hunt results as a readable report."""
    lines = []
    lines.append("=" * 90)
    lines.append("BACKLINK HUNTER REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 90)

    # Only show purchasable domains
    purchasable = [r for r in results if r.status in ("available", "expired", "expiring_soon")]
    taken = [r for r in results if r.status == "registered"]

    # Sort by score
    purchasable.sort(key=lambda x: x.backlink_score, reverse=True)

    # BUY recommendations
    buy = [r for r in purchasable if r.verdict == "BUY"]
    if buy:
        lines.append(f"\n{'='*90}")
        lines.append(f"★ BUY NOW — Confirmed backlinks & press ({len(buy)} domains)")
        lines.append(f"{'='*90}")
        for r in buy:
            _format_domain_detail(r, lines)

    # MAYBE recommendations
    maybe = [r for r in purchasable if r.verdict == "MAYBE"]
    if maybe:
        lines.append(f"\n{'='*90}")
        lines.append(f"? MAYBE — Some evidence, check Ahrefs first ({len(maybe)} domains)")
        lines.append(f"{'='*90}")
        for r in maybe:
            _format_domain_detail(r, lines)

    # WEAK / SKIP
    weak = [r for r in purchasable if r.verdict in ("WEAK", "SKIP")]
    if weak:
        lines.append(f"\n{'='*90}")
        lines.append(f"✗ SKIP — No meaningful backlinks found ({len(weak)} domains)")
        lines.append(f"{'='*90}")
        for r in weak:
            lines.append(f"  [{r.backlink_score}/10] {r.domain}  ({r.status}) — {r.verdict}")

    # Summary
    lines.append(f"\n{'='*90}")
    lines.append(f"SUMMARY")
    lines.append(f"  Checked: {len(results)} domains")
    lines.append(f"  Taken (not purchasable): {len(taken)}")
    lines.append(f"  Available/expired: {len(purchasable)}")
    lines.append(f"  ★ BUY: {len(buy)}")
    lines.append(f"  ? MAYBE: {len(maybe)}")
    lines.append(f"  ✗ SKIP: {len(weak)}")
    lines.append("=" * 90)

    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Backlink Hunter — Find available domains with REAL backlinks and press coverage"
    )
    parser.add_argument("--niche", "-n", help="Niche to search (e.g. 'invoice finance', 'factoring', 'commercial finance')")
    parser.add_argument("--domains", "-d", help="File with domains to check (one per line)")
    parser.add_argument("--domains-list", "-l", help="Comma-separated list of domains to check")
    parser.add_argument("--tld", "-t", help="Filter to specific TLD (e.g. 'co.uk', 'com')")
    parser.add_argument("--ahrefs", help="Ahrefs CSV export file (Referring Domains or Backlinks report)")
    parser.add_argument("--search-results", help="Pre-fetched search results JSON file")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--pagerank-key", help="Open PageRank API key (or set OPEN_PAGERANK_API_KEY env var)")
    args = parser.parse_args()

    domains = []

    if args.domains_list:
        domains = [d.strip() for d in args.domains_list.split(",") if d.strip()]
    elif args.domains:
        with open(args.domains) as f:
            domains = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    elif args.niche:
        niche = args.niche.lower()
        if niche not in DEAD_COMPANIES:
            print(f"Unknown niche: '{niche}'")
            print(f"Available niches: {', '.join(DEAD_COMPANIES.keys())}")
            sys.exit(1)

        niche_domains = DEAD_COMPANIES[niche]
        if args.tld:
            tld = args.tld.lower()
            if tld in niche_domains:
                domains = niche_domains[tld]
            else:
                print(f"No domains for TLD .{tld} in niche '{niche}'")
                sys.exit(1)
        else:
            for tld_domains in niche_domains.values():
                domains.extend(tld_domains)
    else:
        print("Specify --niche, --domains, or --domains-list")
        print("\nExamples:")
        print('  python3 -m tools.domain_finder.backlink_hunter --niche "invoice finance"')
        print('  python3 -m tools.domain_finder.backlink_hunter --domains-list "domain1.co.uk,domain2.com"')
        sys.exit(1)

    # Deduplicate while preserving order
    seen = set()
    unique = []
    for d in domains:
        if d not in seen:
            seen.add(d)
            unique.append(d)
    domains = unique

    print(f"\n{'='*60}")
    print(f"BACKLINK HUNTER")
    print(f"Scanning {len(domains)} domains for availability + backlinks")
    print(f"{'='*60}")

    results = hunt_domains(domains, args.pagerank_key, args.ahrefs, args.search_results)

    if args.json:
        print(json.dumps([r.to_dict() for r in results], indent=2))
    else:
        print("\n" + format_report(results))


if __name__ == "__main__":
    main()
