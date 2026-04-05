"""
Domain Scanner — Find available domains with backlink strength scoring.

Checks:
1. RDAP — is the domain available, expired, or registered?
2. Tranco ranking — was the parent brand a top site? (proxy for backlinks)
3. Domain age — older = more accumulated backlinks
4. HTTP status — is the site dead (503/403/timeout)?

Usage:
    python3 domain_scanner.py --keywords "seo,marketing,digital" --tlds "co.uk,com"
    python3 domain_scanner.py --file domains.txt
    python3 domain_scanner.py --patterns "agency,consultancy,media,group"
"""

import json
import sys
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, field, asdict
from datetime import datetime, timezone
from typing import Optional
from tools.domain_finder.rdap_checker import check_domain, DomainInfo


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
    http_status: Optional[int] = None
    # Scoring
    strength_score: float = 0.0
    strength_reason: str = ""

    def to_dict(self):
        return asdict(self)


def check_tranco(domain: str, timeout: int = 5) -> Optional[int]:
    """Check if domain appears in Tranco top sites list."""
    try:
        url = f"https://tranco-list.eu/api/ranks/domain/{domain}"
        req = urllib.request.Request(url)
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
            ranks = data.get("ranks", [])
            if ranks:
                # Return the most recent rank
                return ranks[0].get("rank")
    except Exception:
        pass
    return None


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


def calculate_strength(score: DomainScore) -> DomainScore:
    """Calculate a strength score 0-10 based on available signals."""
    points = 0.0
    reasons = []

    # Domain age scoring (max 4 points)
    if score.age_years:
        if score.age_years >= 20:
            points += 4.0
            reasons.append(f"{score.age_years:.0f}yr age (excellent)")
        elif score.age_years >= 10:
            points += 3.0
            reasons.append(f"{score.age_years:.0f}yr age (strong)")
        elif score.age_years >= 5:
            points += 2.0
            reasons.append(f"{score.age_years:.0f}yr age (good)")
        elif score.age_years >= 2:
            points += 1.0
            reasons.append(f"{score.age_years:.0f}yr age (fair)")

    # Tranco ranking (max 3 points) — domain itself
    if score.tranco_rank:
        if score.tranco_rank <= 10000:
            points += 3.0
            reasons.append(f"Tranco #{score.tranco_rank:,} (top 10K!)")
        elif score.tranco_rank <= 100000:
            points += 2.5
            reasons.append(f"Tranco #{score.tranco_rank:,} (top 100K)")
        elif score.tranco_rank <= 500000:
            points += 2.0
            reasons.append(f"Tranco #{score.tranco_rank:,} (top 500K)")
        elif score.tranco_rank <= 1000000:
            points += 1.5
            reasons.append(f"Tranco #{score.tranco_rank:,} (top 1M)")

    # Tranco parent brand ranking (max 2 points)
    # If the .com version of the brand is ranked, the .co.uk likely has backlinks
    if score.tranco_parent_rank and not score.tranco_rank:
        if score.tranco_parent_rank <= 10000:
            points += 2.0
            reasons.append(f"Parent brand Tranco #{score.tranco_parent_rank:,} (top 10K)")
        elif score.tranco_parent_rank <= 100000:
            points += 1.5
            reasons.append(f"Parent brand Tranco #{score.tranco_parent_rank:,} (top 100K)")
        elif score.tranco_parent_rank <= 500000:
            points += 1.0
            reasons.append(f"Parent brand Tranco #{score.tranco_parent_rank:,} (top 500K)")

    # HTTP status scoring (max 1 point)
    # Dead site (no response, 503, 403) = good for us — means it's truly abandoned
    if score.http_status is None:
        points += 1.0
        reasons.append("Site completely dead (no response)")
    elif score.http_status in (503, 502, 500):
        points += 0.8
        reasons.append(f"Site dead (HTTP {score.http_status})")
    elif score.http_status == 403:
        points += 0.5
        reasons.append("Site blocked (403)")
    elif score.http_status == 200:
        points -= 0.5
        reasons.append("Site still live (200) — may not be truly abandoned")

    # Bonus: already expired
    if score.status == "expired":
        points += 1.0
        reasons.append("Already expired — dropping soon")
    elif score.status == "available":
        points += 0.5
        reasons.append("Available for immediate registration")

    score.strength_score = min(10.0, round(points, 1))
    score.strength_reason = " | ".join(reasons)
    return score


def scan_domain(domain: str, check_parent: bool = True) -> DomainScore:
    """Full scan of a single domain: RDAP + Tranco + HTTP."""
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
        # For registered domains expiring soon, still score them
        if rdap.days_until_expiry is not None and rdap.days_until_expiry <= 120:
            ds.status = "expiring_soon"
        else:
            ds = calculate_strength(ds)
            return ds

    # 2. Tranco check — does/did this domain rank?
    ds.tranco_rank = check_tranco(domain)
    time.sleep(0.3)  # rate limit

    # 3. Check parent brand (.com version if this is .co.uk)
    if check_parent and domain.endswith(".co.uk"):
        parent = domain.replace(".co.uk", ".com")
        ds.tranco_parent_rank = check_tranco(parent)
        time.sleep(0.3)

    # 4. HTTP status check
    ds.http_status = check_http_status(domain)

    # 5. Calculate strength
    ds = calculate_strength(ds)
    return ds


def scan_domains(domains: list[str], check_parent: bool = True) -> list[DomainScore]:
    """Scan multiple domains and return scored results."""
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
            # keyword only
            domains.add(f"{kw}.{tld}")
            # with prefixes
            for pre in prefixes:
                domains.add(f"{pre}{kw}.{tld}")
                domains.add(f"{pre}-{kw}.{tld}")
            # with suffixes
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

    # Group by status
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
            lines.append(f"    Age: {r.age_years:.1f} years | Expired: {abs(r.days_until_expiry)} days ago")
            lines.append(f"    Strength: {r.strength_reason}")

    if available:
        available.sort(key=lambda x: x.strength_score, reverse=True)
        lines.append(f"\n{'='*90}")
        lines.append(f"AVAILABLE — REGISTER NOW ({len(available)})")
        lines.append(f"{'='*90}")
        for r in available:
            lines.append(f"\n  [{r.strength_score}/10] {r.domain}")
            if r.strength_reason:
                lines.append(f"    Strength: {r.strength_reason}")

    if expiring:
        expiring.sort(key=lambda x: x.days_until_expiry or 999)
        lines.append(f"\n{'='*90}")
        lines.append(f"EXPIRING SOON — PLACE BACKORDERS ({len(expiring)})")
        lines.append(f"{'='*90}")
        for r in expiring:
            lines.append(f"\n  [{r.strength_score}/10] {r.domain}")
            lines.append(f"    Age: {r.age_years:.1f} years | Expires in: {r.days_until_expiry} days")
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
    parser.add_argument("--no-parent", action="store_true", help="Skip parent brand Tranco check")
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
