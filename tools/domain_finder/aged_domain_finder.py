#!/usr/bin/env python3
"""
Aged Domain Finder
Finds aged, available or expiring-soon domains in a given niche.
Uses RDAP (free, no API key needed) to check registration details.

Usage:
    python aged_domain_finder.py --niche invoice_finance
    python aged_domain_finder.py --niche invoice_finance --tlds .com .co.uk
    python aged_domain_finder.py --domains domains.txt
    python aged_domain_finder.py --kw1 invoice --kw2 finance factoring discounting
"""

import argparse
import json
import sys
import time
import concurrent.futures
from pathlib import Path

from rdap_checker import check_domain, DomainInfo, format_report
from domain_generator import generate_domains, NICHE_KEYWORDS


def check_domains_parallel(
    domains: list[str], max_workers: int = 5, delay: float = 0.2, timeout: int = 10
) -> list[DomainInfo]:
    """Check multiple domains in parallel with rate limiting."""
    results = []
    total = len(domains)

    print(f"\nChecking {total} domains (this may take a while)...\n")

    # Process in batches to be respectful to RDAP servers
    batch_size = max_workers
    for i in range(0, total, batch_size):
        batch = domains[i : i + batch_size]

        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            futures = {
                executor.submit(check_domain, domain, timeout): domain
                for domain in batch
            }
            for future in concurrent.futures.as_completed(futures):
                result = future.result()
                results.append(result)

                # Progress indicator
                checked = len(results)
                status_char = {
                    "available": "A",
                    "registered": "R",
                    "error": "X",
                }.get(result.status, "?")

                age_str = ""
                if result.age_years:
                    age_str = f" ({result.age_years}y)"

                print(
                    f"  [{checked}/{total}] [{status_char}] {result.domain}{age_str}"
                )

        # Rate limit between batches
        if i + batch_size < total:
            time.sleep(delay)

    return results


def filter_results(
    results: list[DomainInfo],
    min_age: float = 0,
    show_available: bool = True,
    show_expiring: bool = True,
    expiring_days: int = 180,
) -> dict:
    """Filter and categorise results."""
    available = []
    aged_available = []
    expiring_soon = []
    aged_registered = []

    for r in results:
        if r.status == "available":
            available.append(r)
        elif r.status == "registered":
            if r.days_until_expiry is not None and r.days_until_expiry < expiring_days:
                expiring_soon.append(r)
            if r.age_years and r.age_years >= min_age:
                aged_registered.append(r)

    # Sort by age descending
    aged_registered.sort(key=lambda x: x.age_years or 0, reverse=True)
    expiring_soon.sort(key=lambda x: x.days_until_expiry or 999)

    return {
        "available": available,
        "expiring_soon": expiring_soon,
        "aged_registered": aged_registered,
        "total_checked": len(results),
    }


def print_filtered_report(filtered: dict, min_age: float = 5):
    """Print a focused report on the most interesting finds."""
    print("\n" + "=" * 80)
    print("AGED DOMAIN FINDER - RESULTS")
    print("=" * 80)

    total = filtered["total_checked"]
    print(f"\nTotal domains checked: {total}")

    # Available domains (potential buys)
    available = filtered["available"]
    if available:
        print(f"\n{'='*60}")
        print(f"AVAILABLE TO REGISTER ({len(available)} domains)")
        print(f"{'='*60}")
        for r in available:
            print(f"  >>> {r.domain}")
    else:
        print("\n  No available domains found in this batch.")

    # Expiring soon (watch list)
    expiring = filtered["expiring_soon"]
    if expiring:
        print(f"\n{'='*60}")
        print(f"EXPIRING SOON - WATCH LIST ({len(expiring)} domains)")
        print(f"{'='*60}")
        for r in expiring:
            days = r.days_until_expiry
            age = r.age_years or 0
            exp_date = r.expiry_date[:10] if r.expiry_date else "unknown"
            print(f"  {r.domain}")
            print(f"    Age: {age} years | Expires: {exp_date} ({days} days)")
            if r.registrar:
                print(f"    Registrar: {r.registrar}")

    # Aged registered domains (potential approach targets)
    aged = [r for r in filtered["aged_registered"] if r.age_years and r.age_years >= min_age]
    if aged:
        print(f"\n{'='*60}")
        print(f"AGED DOMAINS ({min_age}+ YEARS) - POTENTIAL APPROACH ({len(aged)} domains)")
        print(f"{'='*60}")
        for r in aged:
            exp_str = ""
            if r.days_until_expiry is not None:
                exp_str = f" | Expires in {r.days_until_expiry} days"
            print(f"  {r.domain}")
            print(f"    Age: {r.age_years} years{exp_str}")
            if r.registrar:
                print(f"    Registrar: {r.registrar}")

    print("\n" + "=" * 80)
    print("TIP: Check domain authority scores at moz.com/link-explorer or ahrefs.com")
    print("TIP: Check backlink profiles before purchasing any aged domain")
    print("=" * 80)


def main():
    parser = argparse.ArgumentParser(
        description="Find aged, available or expiring domains in a niche",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  %(prog)s --niche invoice_finance
  %(prog)s --niche invoice_finance --tlds .com .co.uk --min-age 10
  %(prog)s --kw1 invoice --kw2 finance factoring --tlds .com
  %(prog)s --domains my_domains.txt
  %(prog)s --niche invoice_finance --output results.json

Available niches: {}
        """.format(
            ", ".join(NICHE_KEYWORDS.keys())
        ),
    )

    # Input options
    input_group = parser.add_mutually_exclusive_group(required=True)
    input_group.add_argument(
        "--niche",
        choices=list(NICHE_KEYWORDS.keys()),
        help="Pre-built niche keyword set",
    )
    input_group.add_argument(
        "--domains",
        type=str,
        help="Path to text file with one domain per line",
    )

    # Custom keywords (used with --niche or standalone)
    parser.add_argument("--kw1", nargs="+", help="Primary keywords")
    parser.add_argument("--kw2", nargs="+", help="Secondary keywords")
    parser.add_argument("--extra", nargs="+", help="Extra domain stems to check")

    # TLD and filtering options
    parser.add_argument(
        "--tlds",
        nargs="+",
        default=[".com", ".co.uk"],
        help="TLDs to check (default: .com .co.uk)",
    )
    parser.add_argument(
        "--min-age",
        type=float,
        default=5,
        help="Minimum domain age in years for 'aged' category (default: 5)",
    )
    parser.add_argument(
        "--expiring-days",
        type=int,
        default=180,
        help="Days until expiry for 'expiring soon' (default: 180)",
    )

    # Performance options
    parser.add_argument(
        "--workers",
        type=int,
        default=3,
        help="Parallel workers for RDAP lookups (default: 3)",
    )
    parser.add_argument(
        "--timeout",
        type=int,
        default=10,
        help="Timeout per RDAP lookup in seconds (default: 10)",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="Limit number of domains to check (0 = all, default: 0)",
    )

    # Output options
    parser.add_argument(
        "--output",
        type=str,
        help="Save results to JSON file",
    )

    args = parser.parse_args()

    # Build domain list
    if args.domains:
        # Read from file
        path = Path(args.domains)
        if not path.exists():
            print(f"Error: File not found: {args.domains}")
            sys.exit(1)
        domains = [
            line.strip()
            for line in path.read_text().splitlines()
            if line.strip() and not line.startswith("#")
        ]
    else:
        # Generate from niche/keywords
        domains = generate_domains(
            niche=args.niche,
            kw1_list=args.kw1,
            kw2_list=args.kw2,
            extra_terms=args.extra,
            tlds=args.tlds,
        )

    if args.limit > 0:
        domains = domains[: args.limit]

    print(f"Generated {len(domains)} candidate domains to check")

    # Run checks
    results = check_domains_parallel(
        domains, max_workers=args.workers, timeout=args.timeout
    )

    # Filter and report
    filtered = filter_results(
        results,
        min_age=args.min_age,
        expiring_days=args.expiring_days,
    )

    print_filtered_report(filtered, min_age=args.min_age)

    # Save JSON if requested
    if args.output:
        output_data = {
            "generated": time.strftime("%Y-%m-%d %H:%M"),
            "total_checked": len(results),
            "available": [r.to_dict() for r in filtered["available"]],
            "expiring_soon": [r.to_dict() for r in filtered["expiring_soon"]],
            "aged_registered": [r.to_dict() for r in filtered["aged_registered"]],
            "all_results": [r.to_dict() for r in results],
        }
        Path(args.output).write_text(json.dumps(output_data, indent=2))
        print(f"\nResults saved to: {args.output}")


if __name__ == "__main__":
    main()
