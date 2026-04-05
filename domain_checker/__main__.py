"""CLI entry point: python -m domain_checker example.com"""

import argparse
import sys

from .checker import DomainChecker
from .config import load_config


def main():
    parser = argparse.ArgumentParser(
        description="Check domain availability and pricing across GoDaddy and NameCheap"
    )
    parser.add_argument("domains", nargs="+", help="Domain name(s) to check")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    config = load_config()

    # Filter out None values so DomainChecker can validate
    init_args = {k: v for k, v in config.items() if v is not None}

    try:
        checker = DomainChecker(**init_args)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        print(
            "\nSet environment variables for at least one provider:\n"
            "  GoDaddy:   GODADDY_API_KEY, GODADDY_API_SECRET\n"
            "  NameCheap: NAMECHEAP_API_USER, NAMECHEAP_API_KEY, NAMECHEAP_CLIENT_IP",
            file=sys.stderr,
        )
        sys.exit(1)

    if args.json:
        import json
        if len(args.domains) == 1:
            print(json.dumps(checker.check(args.domains[0]), indent=2))
        else:
            print(json.dumps(checker.check_bulk(args.domains), indent=2))
    else:
        for domain in args.domains:
            print(checker.compare_prices(domain))
            print()


if __name__ == "__main__":
    main()
