"""Unified domain availability and backorder checker.

Queries GoDaddy and NameCheap in parallel, combines results into a
single comparison report with pricing from both providers.
"""

from concurrent.futures import ThreadPoolExecutor, as_completed

from .godaddy import GoDaddyClient
from .namecheap import NameCheapClient


class DomainChecker:
    """Unified checker that queries multiple providers and compares results."""

    def __init__(
        self,
        godaddy_key: str | None = None,
        godaddy_secret: str | None = None,
        namecheap_user: str | None = None,
        namecheap_key: str | None = None,
        namecheap_client_ip: str | None = None,
    ):
        self.providers = {}

        if godaddy_key and godaddy_secret:
            self.providers["godaddy"] = GoDaddyClient(godaddy_key, godaddy_secret)

        if namecheap_user and namecheap_key and namecheap_client_ip:
            self.providers["namecheap"] = NameCheapClient(
                namecheap_user, namecheap_key, namecheap_client_ip
            )

        if not self.providers:
            raise ValueError(
                "At least one provider must be configured. "
                "Supply GoDaddy (api_key + secret) or NameCheap (user + key + client_ip) credentials."
            )

    def check(self, domain: str) -> dict:
        """Check a single domain across all configured providers.

        Returns a combined report:
        {
            "domain": "example.com",
            "results": {
                "godaddy": { availability + pricing },
                "namecheap": { availability + pricing },
            },
            "cheapest": { provider, price, currency },
            "backorder": { namecheap backorder info if domain is taken },
        }
        """
        results = {}
        errors = {}

        with ThreadPoolExecutor(max_workers=len(self.providers)) as pool:
            futures = {}
            for name, client in self.providers.items():
                futures[pool.submit(client.check_availability, domain)] = name

            for future in as_completed(futures):
                name = futures[future]
                try:
                    results[name] = future.result()
                except Exception as e:
                    errors[name] = str(e)

        # Find cheapest available option
        cheapest = None
        for name, r in results.items():
            if r.get("available") and r.get("price") is not None:
                if cheapest is None or r["price"] < cheapest["price"]:
                    cheapest = {
                        "provider": name,
                        "price": r["price"],
                        "currency": r.get("currency", "USD"),
                    }

        # Check backorder if domain is taken and NameCheap is configured
        backorder = None
        is_taken = all(not r.get("available") for r in results.values()) if results else False
        if is_taken and "namecheap" in self.providers:
            try:
                backorder = self.providers["namecheap"].get_backorder_price(domain)
            except Exception as e:
                backorder = {"error": str(e)}

        report = {
            "domain": domain,
            "results": results,
            "cheapest": cheapest,
            "backorder": backorder,
        }
        if errors:
            report["errors"] = errors

        return report

    def check_bulk(self, domains: list[str]) -> list[dict]:
        """Check multiple domains across all providers."""
        return [self.check(domain) for domain in domains]

    def compare_prices(self, domain: str) -> str:
        """Return a human-readable price comparison for a domain."""
        report = self.check(domain)
        lines = [f"Domain: {report['domain']}", "=" * 50]

        for provider, result in report["results"].items():
            status = "AVAILABLE" if result.get("available") else "TAKEN"
            price = f"${result['price']:.2f}" if result.get("price") else "N/A"
            lines.append(f"  {provider.upper():12s}  {status:10s}  {price}/yr")

        if report.get("cheapest"):
            c = report["cheapest"]
            lines.append("")
            lines.append(f"  Best price: {c['provider'].upper()} at ${c['price']:.2f} {c['currency']}")

        if report.get("backorder"):
            bo = report["backorder"]
            lines.append("")
            if bo.get("backorder_available"):
                lines.append("  BACKORDER: Available via NameCheap")
                if bo.get("note"):
                    lines.append(f"  Note: {bo['note']}")
            elif bo.get("reason"):
                lines.append(f"  BACKORDER: {bo['reason']}")

        if report.get("errors"):
            lines.append("")
            for provider, err in report["errors"].items():
                lines.append(f"  ERROR ({provider}): {err}")

        return "\n".join(lines)
