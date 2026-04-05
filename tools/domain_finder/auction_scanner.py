"""
GoDaddy Auction Scanner — Find expired domains with real backlink value.

Searches GoDaddy's expired domain auctions for domains with good SEO metrics.
Requires a GoDaddy API key (free to get).

Setup:
1. Go to https://developer.godaddy.com/keys
2. Create a Production API key
3. Set env vars: GODADDY_API_KEY and GODADDY_API_SECRET

Usage:
    python3 -m tools.domain_finder.auction_scanner --keyword "seo" --tf-min 15 --max-price 20
    python3 -m tools.domain_finder.auction_scanner --keyword "marketing" --da-min 20
    python3 -m tools.domain_finder.auction_scanner --keyword "digital" --age-min 5
    python3 -m tools.domain_finder.auction_scanner --all --tf-min 25 --max-results 50
"""

import argparse
import json
import os
import sys
import time
import urllib.request
import urllib.error
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class AuctionDomain:
    domain: str
    price: float = 0.0
    bids: int = 0
    end_time: str = ""
    domain_age: int = 0
    # SEO metrics (from GoDaddy auction data)
    traffic: Optional[int] = None
    valuation: Optional[float] = None
    auction_type: str = ""  # expired, closeout, etc.
    # Majestic metrics (checked separately)
    majestic_tf: Optional[int] = None
    majestic_cf: Optional[int] = None
    majestic_ref_subnets: Optional[int] = None
    majestic_rank: Optional[int] = None

    def to_dict(self):
        return asdict(self)


class GoDaddyAuctionClient:
    """Client for GoDaddy Aftermarket/Auctions API."""

    BASE_URL = "https://api.godaddy.com/v1"

    def __init__(self, api_key: str, api_secret: str):
        self.auth = f"sso-key {api_key}:{api_secret}"

    def _request(self, endpoint: str, params: dict = None) -> dict:
        url = f"{self.BASE_URL}{endpoint}"
        if params:
            query = "&".join(f"{k}={v}" for k, v in params.items() if v is not None)
            url = f"{url}?{query}"

        req = urllib.request.Request(url, headers={
            "Authorization": self.auth,
            "Accept": "application/json",
        })

        try:
            with urllib.request.urlopen(req, timeout=15) as resp:
                return json.loads(resp.read().decode())
        except urllib.error.HTTPError as e:
            error_body = e.read().decode() if e.fp else ""
            raise RuntimeError(f"GoDaddy API error {e.code}: {error_body}")

    def search_expired(self, keyword: str = None, max_price: float = None,
                       tld: str = None, limit: int = 100) -> list[dict]:
        """Search expired domain auctions."""
        params = {
            "type": "expired",
            "limit": min(limit, 200),
        }
        if keyword:
            params["q"] = keyword
        if max_price:
            params["maxPrice"] = int(max_price * 100)  # cents
        if tld:
            params["tld"] = tld

        return self._request("/aftermarket/listings", params)

    def search_closeout(self, keyword: str = None, limit: int = 100) -> list[dict]:
        """Search closeout auctions (fixed price $10-12)."""
        params = {
            "type": "closeout",
            "limit": min(limit, 200),
        }
        if keyword:
            params["q"] = keyword
        return self._request("/aftermarket/listings", params)

    def get_listing(self, domain: str) -> dict:
        """Get details for a specific auction listing."""
        return self._request(f"/aftermarket/listings/{domain}")


def load_majestic_lookup() -> dict:
    """Load Majestic Million for cross-referencing."""
    csv_path = os.path.join(os.path.dirname(__file__), "majestic_million.csv")
    if not os.path.exists(csv_path):
        return {}

    import csv
    data = {}
    with open(csv_path) as f:
        reader = csv.DictReader(f)
        for row in reader:
            domain = row.get("Domain", "").lower()
            if domain:
                data[domain] = {
                    "rank": int(row.get("GlobalRank", 0)),
                    "ref_subnets": int(row.get("RefSubNets", 0)),
                    "ref_ips": int(row.get("RefIPs", 0)),
                }
    return data


def search_auctions(client: GoDaddyAuctionClient, keywords: list[str] = None,
                     max_price: float = None, tld: str = None,
                     search_all: bool = False, limit: int = 50) -> list[AuctionDomain]:
    """Search GoDaddy auctions and enrich with Majestic data."""

    print("Loading Majestic Million for cross-referencing...")
    majestic = load_majestic_lookup()
    if majestic:
        print(f"  [✓] Loaded {len(majestic):,} domains from Majestic Million")

    results = []

    if search_all:
        keywords = [None]  # Search without keyword filter
    elif not keywords:
        keywords = ["seo", "search", "marketing", "digital", "review", "compare",
                     "tech", "agency", "content", "media", "web", "online"]

    for kw in keywords:
        kw_display = kw or "ALL"
        print(f"\n  Searching expired auctions: '{kw_display}'...")
        try:
            listings = client.search_expired(keyword=kw, max_price=max_price,
                                              tld=tld, limit=limit)
            if isinstance(listings, list):
                for item in listings:
                    domain = item.get("domain", "")
                    ad = AuctionDomain(
                        domain=domain,
                        price=item.get("price", 0) / 100 if item.get("price") else 0,
                        bids=item.get("bids", 0),
                        end_time=item.get("endTime", ""),
                        auction_type=item.get("type", "expired"),
                        traffic=item.get("traffic"),
                        valuation=item.get("valuation"),
                    )

                    # Cross-reference with Majestic
                    base_domain = domain.lower()
                    maj = majestic.get(base_domain)
                    if maj:
                        ad.majestic_rank = maj["rank"]
                        ad.majestic_ref_subnets = maj["ref_subnets"]

                    results.append(ad)

            print(f"    Found {len(listings) if isinstance(listings, list) else 0} listings")
        except Exception as e:
            print(f"    Error: {e}")

        # Also check closeout
        print(f"  Searching closeout auctions: '{kw_display}'...")
        try:
            listings = client.search_closeout(keyword=kw, limit=limit)
            if isinstance(listings, list):
                for item in listings:
                    domain = item.get("domain", "")
                    ad = AuctionDomain(
                        domain=domain,
                        price=item.get("price", 0) / 100 if item.get("price") else 0,
                        bids=item.get("bids", 0),
                        end_time=item.get("endTime", ""),
                        auction_type=item.get("type", "closeout"),
                        traffic=item.get("traffic"),
                        valuation=item.get("valuation"),
                    )

                    base_domain = domain.lower()
                    maj = majestic.get(base_domain)
                    if maj:
                        ad.majestic_rank = maj["rank"]
                        ad.majestic_ref_subnets = maj["ref_subnets"]

                    results.append(ad)

            print(f"    Found {len(listings) if isinstance(listings, list) else 0} listings")
        except Exception as e:
            print(f"    Error: {e}")

        time.sleep(0.5)

    # Deduplicate
    seen = set()
    unique = []
    for r in results:
        if r.domain not in seen:
            seen.add(r.domain)
            unique.append(r)
    results = unique

    return results


def format_auction_results(results: list[AuctionDomain], min_tf: int = 0,
                            min_da: int = 0, min_age: int = 0,
                            max_price: float = None) -> str:
    """Format auction results as a readable report."""
    # Filter
    filtered = results
    if max_price:
        filtered = [r for r in filtered if r.price <= max_price]

    # Sort by Majestic ref subnets (best proxy for real value), then by price
    with_majestic = [r for r in filtered if r.majestic_ref_subnets]
    without_majestic = [r for r in filtered if not r.majestic_ref_subnets]

    with_majestic.sort(key=lambda x: x.majestic_ref_subnets or 0, reverse=True)
    without_majestic.sort(key=lambda x: x.price)

    lines = []
    lines.append("=" * 90)
    lines.append("GODADDY AUCTION SCANNER REPORT")
    lines.append("=" * 90)

    if with_majestic:
        lines.append(f"\n{'='*90}")
        lines.append(f"DOMAINS IN MAJESTIC MILLION — Have confirmed backlinks ({len(with_majestic)})")
        lines.append(f"{'='*90}")
        for r in with_majestic:
            lines.append(f"\n  {r.domain}")
            lines.append(f"    Price: ${r.price:.2f} | Bids: {r.bids} | Type: {r.auction_type}")
            lines.append(f"    Majestic rank: #{r.majestic_rank:,} | Ref subnets: {r.majestic_ref_subnets:,}")
            if r.end_time:
                lines.append(f"    Ends: {r.end_time}")

    if without_majestic:
        lines.append(f"\n{'='*90}")
        lines.append(f"OTHER AUCTION DOMAINS ({len(without_majestic)})")
        lines.append(f"{'='*90}")
        for r in without_majestic[:30]:  # Limit output
            line = f"  {r.domain:40s} ${r.price:>7.2f}  bids: {r.bids}  type: {r.auction_type}"
            lines.append(line)
        if len(without_majestic) > 30:
            lines.append(f"  ... and {len(without_majestic) - 30} more")

    lines.append(f"\n{'='*90}")
    lines.append(f"TOTAL: {len(filtered)} domains ({len(with_majestic)} with Majestic data)")
    lines.append("=" * 90)
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="GoDaddy Auction Scanner")
    parser.add_argument("--keyword", "-k", help="Search keyword (e.g. 'seo', 'marketing')")
    parser.add_argument("--keywords", help="Comma-separated keywords")
    parser.add_argument("--all", action="store_true", help="Search all expired domains (no keyword filter)")
    parser.add_argument("--tld", help="Filter by TLD (e.g. 'com', 'co.uk')")
    parser.add_argument("--max-price", type=float, help="Maximum auction price in USD")
    parser.add_argument("--max-results", type=int, default=50, help="Max results per keyword")
    parser.add_argument("--tf-min", type=int, default=0, help="Minimum Trust Flow")
    parser.add_argument("--da-min", type=int, default=0, help="Minimum Domain Authority")
    parser.add_argument("--age-min", type=int, default=0, help="Minimum domain age in years")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    api_key = os.environ.get("GODADDY_API_KEY")
    api_secret = os.environ.get("GODADDY_API_SECRET")

    if not api_key or not api_secret:
        print("ERROR: GoDaddy API credentials required.", file=sys.stderr)
        print("\nSetup:", file=sys.stderr)
        print("  1. Go to https://developer.godaddy.com/keys", file=sys.stderr)
        print("  2. Create a Production API key", file=sys.stderr)
        print("  3. Set environment variables:", file=sys.stderr)
        print("     export GODADDY_API_KEY='your-key'", file=sys.stderr)
        print("     export GODADDY_API_SECRET='your-secret'", file=sys.stderr)
        sys.exit(1)

    client = GoDaddyAuctionClient(api_key, api_secret)

    keywords = None
    if args.keyword:
        keywords = [args.keyword]
    elif args.keywords:
        keywords = [k.strip() for k in args.keywords.split(",")]

    results = search_auctions(
        client,
        keywords=keywords,
        max_price=args.max_price,
        tld=args.tld,
        search_all=args.all,
        limit=args.max_results,
    )

    if args.json:
        print(json.dumps([r.to_dict() for r in results], indent=2))
    else:
        print("\n" + format_auction_results(
            results,
            min_tf=args.tf_min,
            min_da=args.da_min,
            min_age=args.age_min,
            max_price=args.max_price,
        ))


if __name__ == "__main__":
    main()
