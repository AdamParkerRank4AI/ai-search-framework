"""
Domain Scanner — Find available domains with backlink strength scoring.

Checks:
1. RDAP — is the domain available, expired, or registered?
2. Tranco ranking — was the parent brand a top site? (proxy for traffic)
3. Majestic Million — referring subnets & IPs (proxy for backlinks)
4. HTTP status — is the site dead (503/403/timeout)?

Usage:
    python3 -m tools.domain_finder.domain_scanner --domains "bigmouthmedia.co.uk" "receptional.co.uk"
    python3 -m tools.domain_finder.domain_scanner --file domains.txt
    python3 -m tools.domain_finder.domain_scanner --keywords "seo,marketing,digital" --tlds "co.uk,com"
"""

import csv
import json
import os
import sys
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional
from tools.domain_finder.rdap_checker import check_domain, DomainInfo


MAJESTIC_CSV = os.path.join(os.path.dirname(__file__), "majestic_million.csv")


@dataclass
class DomainScore:
    domain: str
    status: str = "unknown"  # available, expired, registered
    age_years: Optional[float] = None
    days_until_expiry: Optional[int] = None
    expiry_date: Optional[str] = None
    registration_date: Optional[str] = None
    # Strength signals
    tranco_rank: Optional[int] = None  # lower = stronger (top 1M sites)
    tranco_parent_rank: Optional[int] = None  # rank of parent brand (.com version)
    majestic_rank: Optional[int] = None
    majestic_ref_subnets: Optional[int] = None  # referring subnets (≈ referring domains)
    majestic_ref_ips: Optional[int] = None
    majestic_parent_rank: Optional[int] = None  # parent brand (.com) majestic data
    majestic_parent_ref_subnets: Optional[int] = None
    majestic_parent_ref_ips: Optional[int] = None
    http_status: Optional[int] = None
    # Scoring
    strength_score: float = 0.0
    strength_reason: str = ""

    def to_dict(self):
        return asdict(self)


# ---------------------------------------------------------------------------
# Majestic Million lookup (local CSV)
# ---------------------------------------------------------------------------

_majestic_cache: Optional[dict] = None


def _load_majestic() -> dict:
    """Load Majestic Million CSV into a dict keyed by domain."""
    global _majestic_cache
    if _majestic_cache is not None:
        return _majestic_cache

    _majestic_cache = {}
    if not os.path.exists(MAJESTIC_CSV):
        print(f"  [!] Majestic Million CSV not found at {MAJESTIC_CSV}")
        print(f"      Download: curl -o {MAJESTIC_CSV} https://downloads.majestic.com/majestic_million.csv")
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
    print(f"  [✓] Loaded {len(_majestic_cache):,} domains from Majestic Million")
    return _majestic_cache


def check_majestic(domain: str) -> Optional[dict]:
    """Look up a domain in the Majestic Million (local CSV)."""
    data = _load_majestic()
    return data.get(domain.lower())


# ---------------------------------------------------------------------------
# Tranco lookup (API)
# ---------------------------------------------------------------------------

def check_tranco(domain: str, timeout: int = 5) -> Optional[int]:
    """Check if domain appears in Tranco top sites list."""
    try:
        url = f"https://tranco-list.eu/api/ranks/domain/{domain}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
            ranks = data.get("ranks", [])
            if ranks:
                return ranks[0].get("rank")
    except Exception:
        pass
    return None


# ---------------------------------------------------------------------------
# HTTP status check
# ---------------------------------------------------------------------------

def check_http_status(domain: str, timeout: int = 5) -> Optional[int]:
    """Quick HTTP check — is the site live, dead, or redirecting?"""
    for scheme in ["https", "http"]:
        try:
            url = f"{scheme}://{domain}"
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "Mozilla/5.0"},
                method="HEAD",
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.status
        except urllib.error.HTTPError as e:
            return e.code
        except Exception:
            continue
    return None  # totally dead — no response at all


# ---------------------------------------------------------------------------
# Strength scoring
# ---------------------------------------------------------------------------

def calculate_strength(score: DomainScore) -> DomainScore:
    """Calculate a strength score 0-10 based on available signals."""
    points = 0.0
    reasons = []

    # --- Majestic referring subnets (max 4 points) — best backlink proxy ---
    ref_subs = score.majestic_ref_subnets or score.majestic_parent_ref_subnets or 0
    ref_source = "domain" if score.majestic_ref_subnets else "parent"
    if ref_subs >= 5000:
        points += 4.0
        reasons.append(f"{ref_subs:,} ref subnets ({ref_source}, excellent)")
    elif ref_subs >= 2000:
        points += 3.5
        reasons.append(f"{ref_subs:,} ref subnets ({ref_source}, very strong)")
    elif ref_subs >= 1000:
        points += 3.0
        reasons.append(f"{ref_subs:,} ref subnets ({ref_source}, strong)")
    elif ref_subs >= 500:
        points += 2.0
        reasons.append(f"{ref_subs:,} ref subnets ({ref_source}, good)")
    elif ref_subs >= 200:
        points += 1.5
        reasons.append(f"{ref_subs:,} ref subnets ({ref_source}, fair)")
    elif ref_subs >= 100:
        points += 1.0
        reasons.append(f"{ref_subs:,} ref subnets ({ref_source}, modest)")

    # --- Domain age scoring (max 3 points) ---
    if score.age_years:
        if score.age_years >= 20:
            points += 3.0
            reasons.append(f"{score.age_years:.0f}yr age (excellent)")
        elif score.age_years >= 10:
            points += 2.0
            reasons.append(f"{score.age_years:.0f}yr age (strong)")
        elif score.age_years >= 5:
            points += 1.0
            reasons.append(f"{score.age_years:.0f}yr age (good)")
        elif score.age_years >= 2:
            points += 0.5
            reasons.append(f"{score.age_years:.0f}yr age (fair)")

    # --- Tranco ranking (max 2 points) — domain itself or parent ---
    tranco = score.tranco_rank or score.tranco_parent_rank
    tranco_source = "domain" if score.tranco_rank else "parent"
    if tranco:
        if tranco <= 10000:
            points += 2.0
            reasons.append(f"Tranco #{tranco:,} ({tranco_source}, top 10K)")
        elif tranco <= 50000:
            points += 1.5
            reasons.append(f"Tranco #{tranco:,} ({tranco_source}, top 50K)")
        elif tranco <= 100000:
            points += 1.0
            reasons.append(f"Tranco #{tranco:,} ({tranco_source}, top 100K)")
        elif tranco <= 500000:
            points += 0.5
            reasons.append(f"Tranco #{tranco:,} ({tranco_source}, top 500K)")

    # --- HTTP status scoring (max 1 point) ---
    # Dead site = good for us — means truly abandoned
    if score.http_status is None:
        points += 1.0
        reasons.append("Site dead (no response)")
    elif score.http_status in (503, 502, 500):
        points += 0.8
        reasons.append(f"Site dead ({score.http_status})")
    elif score.http_status == 403:
        points += 0.5
        reasons.append("Site blocked (403)")
    elif score.http_status == 200:
        points -= 0.5
        reasons.append("Site live (200) — may not be abandoned")

    # --- Status bonus ---
    if score.status == "expired":
        points += 0.5
        reasons.append("Expired — dropping soon")
    elif score.status == "available":
        points += 0.5
        reasons.append("Available now")

    score.strength_score = max(0.0, min(10.0, round(points, 1)))
    score.strength_reason = " | ".join(reasons)
    return score


# ---------------------------------------------------------------------------
# Domain scanning
# ---------------------------------------------------------------------------

def scan_domain(domain: str, check_parent: bool = True) -> DomainScore:
    """Full scan of a single domain: RDAP + Tranco + Majestic + HTTP."""
    ds = DomainScore(domain=domain)

    # 1. RDAP check
    rdap = check_domain(domain)
    ds.status = "expired" if (rdap.status == "registered" and rdap.days_until_expiry is not None and rdap.days_until_expiry < 0) else rdap.status
    ds.age_years = rdap.age_years
    ds.days_until_expiry = rdap.days_until_expiry
    ds.expiry_date = rdap.expiry_date
    ds.registration_date = rdap.registration_date

    # Only score available or expired domains
    if ds.status not in ("available", "expired"):
        if rdap.days_until_expiry is not None and rdap.days_until_expiry <= 120:
            ds.status = "expiring_soon"
        else:
            ds = calculate_strength(ds)
            return ds

    # 2. Majestic Million check (local, instant)
    maj = check_majestic(domain)
    if maj:
        ds.majestic_rank = maj["rank"]
        ds.majestic_ref_subnets = maj["ref_subnets"]
        ds.majestic_ref_ips = maj["ref_ips"]

    # 3. Tranco check (API)
    ds.tranco_rank = check_tranco(domain)
    time.sleep(0.3)

    # 4. Check parent brand (.com version if this is .co.uk, or vice versa)
    if check_parent:
        parent = None
        if domain.endswith(".co.uk"):
            parent = domain.replace(".co.uk", ".com")
        elif domain.endswith(".com"):
            # Check .co.uk variant too
            parent = domain.replace(".com", ".co.uk")

        if parent:
            if not ds.tranco_rank:
                ds.tranco_parent_rank = check_tranco(parent)
                time.sleep(0.3)

            parent_maj = check_majestic(parent)
            if parent_maj and not ds.majestic_ref_subnets:
                ds.majestic_parent_rank = parent_maj["rank"]
                ds.majestic_parent_ref_subnets = parent_maj["ref_subnets"]
                ds.majestic_parent_ref_ips = parent_maj["ref_ips"]

    # 5. HTTP status check
    ds.http_status = check_http_status(domain)

    # 6. Calculate strength
    ds = calculate_strength(ds)
    return ds


def scan_domains(domains: list[str], check_parent: bool = True) -> list[DomainScore]:
    """Scan multiple domains and return scored results."""
    # Pre-load Majestic data once
    _load_majestic()

    results = []
    total = len(domains)
    for i, domain in enumerate(domains, 1):
        print(f"  [{i}/{total}] Scanning {domain}...", end="", flush=True)
        result = scan_domain(domain, check_parent)
        status_icon = {"available": "✓", "expired": "⚠", "expiring_soon": "⏳", "registered": "✗"}.get(result.status, "?")
        print(f" {status_icon} {result.status} | score: {result.strength_score}/10")
        results.append(result)
    return results


def generate_domains(keywords: list[str], prefixes: list[str], suffixes: list[str], tlds: list[str]) -> list[str]:
    """Generate domain candidates from keyword combinations."""
    domains = set()
    for kw in keywords:
        for tld in tlds:
            domains.add(f"{kw}.{tld}")
            for pre in prefixes:
                domains.add(f"{pre}{kw}.{tld}")
                domains.add(f"{pre}-{kw}.{tld}")
            for suf in suffixes:
                domains.add(f"{kw}{suf}.{tld}")
                domains.add(f"{kw}-{suf}.{tld}")
    return sorted(domains)


def format_results(results: list[DomainScore], min_score: float = 0.0) -> str:
    """Format scan results as a readable report."""
    lines = []
    lines.append("=" * 90)
    lines.append("DOMAIN SCANNER REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 90)

    available = [r for r in results if r.status == "available" and r.strength_score >= min_score]
    expired = [r for r in results if r.status == "expired" and r.strength_score >= min_score]
    expiring = [r for r in results if r.status == "expiring_soon" and r.strength_score >= min_score]
    registered = [r for r in results if r.status == "registered"]

    if expired:
        expired.sort(key=lambda x: x.strength_score, reverse=True)
        lines.append(f"\n{'='*90}")
        lines.append(f"EXPIRED — BACKORDER NOW ({len(expired)})")
        lines.append(f"{'='*90}")
        for r in expired:
            lines.append(f"\n  [{r.strength_score}/10] {r.domain}")
            if r.age_years:
                lines.append(f"    Age: {r.age_years:.1f} years | Expired: {abs(r.days_until_expiry)} days ago")
            ref = r.majestic_ref_subnets or r.majestic_parent_ref_subnets
            if ref:
                lines.append(f"    Referring subnets: {ref:,}")
            lines.append(f"    Strength: {r.strength_reason}")

    if available:
        available.sort(key=lambda x: x.strength_score, reverse=True)
        lines.append(f"\n{'='*90}")
        lines.append(f"AVAILABLE — REGISTER NOW ({len(available)})")
        lines.append(f"{'='*90}")
        for r in available:
            lines.append(f"\n  [{r.strength_score}/10] {r.domain}")
            ref = r.majestic_ref_subnets or r.majestic_parent_ref_subnets
            if ref:
                lines.append(f"    Referring subnets: {ref:,}")
            if r.strength_reason:
                lines.append(f"    Strength: {r.strength_reason}")

    if expiring:
        expiring.sort(key=lambda x: x.days_until_expiry or 999)
        lines.append(f"\n{'='*90}")
        lines.append(f"EXPIRING SOON — PLACE BACKORDERS ({len(expiring)})")
        lines.append(f"{'='*90}")
        for r in expiring:
            lines.append(f"\n  [{r.strength_score}/10] {r.domain}")
            if r.age_years:
                lines.append(f"    Age: {r.age_years:.1f} years | Expires in: {r.days_until_expiry} days")
            ref = r.majestic_ref_subnets or r.majestic_parent_ref_subnets
            if ref:
                lines.append(f"    Referring subnets: {ref:,}")
            lines.append(f"    Strength: {r.strength_reason}")

    lines.append(f"\n{'='*90}")
    lines.append(f"SUMMARY: {len(available)} available, {len(expired)} expired, {len(expiring)} expiring soon, {len(registered)} registered (skipped)")
    lines.append("=" * 90)
    return "\n".join(lines)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Domain Scanner — find and score available domains")
    parser.add_argument("--domains", "-d", nargs="+", help="Specific domains to check")
    parser.add_argument("--file", "-f", help="File with domains (one per line)")
    parser.add_argument("--keywords", "-k", help="Comma-separated keywords to generate domains")
    parser.add_argument("--tlds", "-t", default="co.uk,com", help="Comma-separated TLDs (default: co.uk,com)")
    parser.add_argument("--min-score", type=float, default=0.0, help="Minimum strength score to show")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--no-parent", action="store_true", help="Skip parent brand checks")
    args = parser.parse_args()

    domains = []

    if args.domains:
        domains = args.domains
    elif args.file:
        with open(args.file) as f:
            domains = [line.strip() for line in f if line.strip() and not line.startswith("#")]
    elif args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",")]
        tlds = [t.strip() for t in args.tlds.split(",")]
        prefixes = ["the", "best", "top", "compare", "find"]
        suffixes = ["guide", "review", "hub", "agency", "media", "digital", "online", "pro"]
        domains = generate_domains(keywords, prefixes, suffixes, tlds)
        print(f"Generated {len(domains)} domain candidates")

    if not domains:
        print("No domains to check. Use --domains, --file, or --keywords")
        sys.exit(1)

    print(f"\nScanning {len(domains)} domains...\n")
    results = scan_domains(domains, check_parent=not args.no_parent)

    if args.json:
        output = [r.to_dict() for r in results]
        print(json.dumps(output, indent=2))
    else:
        print("\n" + format_results(results, min_score=args.min_score))
