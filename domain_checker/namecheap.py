"""NameCheap Domain Availability & Backorder API client."""

import xml.etree.ElementTree as ET

import requests


class NameCheapClient:
    """Check domain availability, pricing, and backorder via NameCheap API."""

    BASE_URL = "https://api.namecheap.com/xml.response"

    def __init__(self, api_user: str, api_key: str, client_ip: str, username: str | None = None):
        self.params = {
            "ApiUser": api_user,
            "ApiKey": api_key,
            "UserName": username or api_user,
            "ClientIp": client_ip,
        }

    def _request(self, command: str, extra_params: dict | None = None) -> ET.Element:
        params = {**self.params, "Command": command}
        if extra_params:
            params.update(extra_params)
        resp = requests.get(self.BASE_URL, params=params)
        resp.raise_for_status()
        root = ET.fromstring(resp.text)
        status = root.attrib.get("Status", "")
        if status == "ERROR":
            errors = root.findall(".//{http://api.namecheap.com/xml.response}Error")
            if not errors:
                errors = root.findall(".//Error")
            msg = errors[0].text if errors else "Unknown NameCheap API error"
            raise RuntimeError(f"NameCheap API error: {msg}")
        return root

    def check_availability(self, domain: str) -> dict:
        """Check if a domain is available.

        Returns dict with keys: available, domain, price, currency, provider
        """
        root = self._request(
            "namecheap.domains.check",
            {"DomainList": domain},
        )

        # Parse response - namespace may vary
        result = (
            root.find(".//{http://api.namecheap.com/xml.response}DomainCheckResult")
            or root.find(".//DomainCheckResult")
        )

        available = False
        if result is not None:
            available = result.attrib.get("Available", "false").lower() == "true"

        # Get pricing separately
        price_info = self._get_pricing(domain)

        return {
            "provider": "namecheap",
            "domain": domain,
            "available": available,
            "price": price_info.get("registration_price"),
            "currency": "USD",
            "period": 1,
            "renewal_price": price_info.get("renewal_price"),
        }

    def check_availability_bulk(self, domains: list[str]) -> list[dict]:
        """Check availability for multiple domains (max 50 per call)."""
        root = self._request(
            "namecheap.domains.check",
            {"DomainList": ",".join(domains)},
        )

        results = (
            root.findall(".//{http://api.namecheap.com/xml.response}DomainCheckResult")
            or root.findall(".//DomainCheckResult")
        )

        out = []
        for r in results:
            domain = r.attrib.get("Domain", "")
            available = r.attrib.get("Available", "false").lower() == "true"
            out.append({
                "provider": "namecheap",
                "domain": domain,
                "available": available,
                "price": None,  # Bulk doesn't include pricing
                "currency": "USD",
                "period": 1,
            })
        return out

    def _get_pricing(self, domain: str) -> dict:
        """Get registration and renewal pricing for a domain's TLD."""
        tld = domain.rsplit(".", 1)[-1] if "." in domain else "com"
        try:
            root = self._request(
                "namecheap.users.getPricing",
                {
                    "ProductType": "DOMAIN",
                    "ProductCategory": "REGISTER",
                    "ActionName": "REGISTER",
                },
            )
            # Try to find pricing for the TLD
            products = (
                root.findall(".//{http://api.namecheap.com/xml.response}Product")
                or root.findall(".//Product")
            )
            for product in products:
                if product.attrib.get("Name", "").lower() == tld.lower():
                    price_elem = product.find(
                        ".//{http://api.namecheap.com/xml.response}Price"
                    ) or product.find(".//Price")
                    if price_elem is not None:
                        return {
                            "registration_price": float(price_elem.attrib.get("Price", 0)),
                            "renewal_price": float(price_elem.attrib.get("AdditionalCost", 0)),
                        }
        except Exception:
            pass
        return {"registration_price": None, "renewal_price": None}

    def get_backorder_price(self, domain: str) -> dict:
        """Get backorder pricing for a domain.

        NameCheap backorders are managed via their marketplace.
        This uses the namecheap.domains.check + marketplace APIs.
        """
        # NameCheap doesn't have a direct "backorder price" API endpoint.
        # Backorders are placed at a flat fee through their system.
        # Typical pricing: ~$0 to place backorder, standard registration if won.
        #
        # We check if the domain is taken (candidate for backorder) and return info.
        root = self._request(
            "namecheap.domains.check",
            {"DomainList": domain},
        )

        result = (
            root.find(".//{http://api.namecheap.com/xml.response}DomainCheckResult")
            or root.find(".//DomainCheckResult")
        )

        available = False
        if result is not None:
            available = result.attrib.get("Available", "false").lower() == "true"

        if available:
            return {
                "provider": "namecheap",
                "domain": domain,
                "backorder_available": False,
                "reason": "Domain is currently available for direct registration",
            }

        return {
            "provider": "namecheap",
            "domain": domain,
            "backorder_available": True,
            "backorder_fee": None,  # Flat fee, varies by promo
            "note": "NameCheap backorders are placed at a flat fee. "
                    "If won, standard registration price applies. "
                    "Place via namecheap.com/domains/backorder/",
        }
