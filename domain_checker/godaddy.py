"""GoDaddy Domain Availability API client."""

import requests


class GoDaddyClient:
    """Check domain availability and pricing via GoDaddy API."""

    BASE_URL = "https://api.godaddy.com/v1"

    def __init__(self, api_key: str, api_secret: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"sso-key {api_key}:{api_secret}",
            "Accept": "application/json",
        })

    def check_availability(self, domain: str) -> dict:
        """Check if a domain is available and return pricing.

        Returns dict with keys:
            available, domain, price, currency, period, definitive
        Price is returned in standard currency units (e.g. 12.99 USD).
        """
        resp = self.session.get(
            f"{self.BASE_URL}/domains/available",
            params={"domain": domain},
        )
        resp.raise_for_status()
        data = resp.json()

        price_raw = data.get("price", 0)
        return {
            "provider": "godaddy",
            "domain": data.get("domain", domain),
            "available": data.get("available", False),
            "price": price_raw / 10000 if price_raw else None,
            "currency": data.get("currency", "USD"),
            "period": data.get("period", 1),
            "definitive": data.get("definitive", False),
        }

    def check_availability_bulk(self, domains: list[str]) -> list[dict]:
        """Check availability for multiple domains at once."""
        resp = self.session.post(
            f"{self.BASE_URL}/domains/available",
            json=domains,
        )
        resp.raise_for_status()
        results = resp.json()

        out = []
        for item in results.get("domains", results) if isinstance(results, dict) else results:
            price_raw = item.get("price", 0)
            out.append({
                "provider": "godaddy",
                "domain": item.get("domain"),
                "available": item.get("available", False),
                "price": price_raw / 10000 if price_raw else None,
                "currency": item.get("currency", "USD"),
                "period": item.get("period", 1),
                "definitive": item.get("definitive", False),
            })
        return out
