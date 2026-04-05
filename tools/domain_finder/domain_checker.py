"""
Domain Checker — verify availability and pricing via GoDaddy and NameCheap APIs.

Requires API credentials set as environment variables:
  GoDaddy:   GODADDY_API_KEY, GODADDY_API_SECRET
  NameCheap: NAMECHEAP_API_USER, NAMECHEAP_API_KEY, NAMECHEAP_CLIENT_IP

Usage:
    python3 -m tools.domain_finder.domain_checker bigmouthmedia.co.uk receptional.co.uk --json
"""

import argparse
import json
import os
import sys
import xml.etree.ElementTree as ET
from concurrent.futures import ThreadPoolExecutor, as_completed

try:
    import requests
except ImportError:
    requests = None


def load_config() -> dict:
    return {
        "godaddy_key": os.environ.get("GODADDY_API_KEY"),
        "godaddy_secret": os.environ.get("GODADDY_API_SECRET"),
        "namecheap_user": os.environ.get("NAMECHEAP_API_USER"),
        "namecheap_key": os.environ.get("NAMECHEAP_API_KEY"),
        "namecheap_client_ip": os.environ.get("NAMECHEAP_CLIENT_IP"),
    }


class GoDaddyClient:
    BASE_URL = "https://api.godaddy.com/v1"

    def __init__(self, api_key: str, api_secret: str):
        self.session = requests.Session()
        self.session.headers.update({
            "Authorization": f"sso-key {api_key}:{api_secret}",
            "Accept": "application/json",
        })

    def check_availability(self, domain: str) -> dict:
        resp = self.session.get(f"{self.BASE_URL}/domains/available", params={"domain": domain})
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
        resp = self.session.post(f"{self.BASE_URL}/domains/available", json=domains)
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


class NameCheapClient:
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
        if root.attrib.get("Status", "") == "ERROR":
            ns = "{http://api.namecheap.com/xml.response}"
            errors = root.findall(f".//{ns}Error") or root.findall(".//Error")
            raise RuntimeError(f"NameCheap API error: {errors[0].text if errors else 'Unknown'}")
        return root

    def check_availability(self, domain: str) -> dict:
        root = self._request("namecheap.domains.check", {"DomainList": domain})
        ns = "{http://api.namecheap.com/xml.response}"
        result = root.find(f".//{ns}DomainCheckResult") or root.find(".//DomainCheckResult")
        available = False
        if result is not None:
            available = result.attrib.get("Available", "false").lower() == "true"
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
        root = self._request("namecheap.domains.check", {"DomainList": ",".join(domains)})
        ns = "{http://api.namecheap.com/xml.response}"
        results = root.findall(f".//{ns}DomainCheckResult") or root.findall(".//DomainCheckResult")
        out = []
        for r in results:
            out.append({
                "provider": "namecheap",
                "domain": r.attrib.get("Domain", ""),
                "available": r.attrib.get("Available", "false").lower() == "true",
                "price": None,
                "currency": "USD",
                "period": 1,
            })
        return out

    def _get_pricing(self, domain: str) -> dict:
        tld = domain.rsplit(".", 1)[-1] if "." in domain else "com"
        try:
            root = self._request("namecheap.users.getPricing", {
                "ProductType": "DOMAIN",
                "ProductCategory": "REGISTER",
                "ActionName": "REGISTER",
            })
            ns = "{http://api.namecheap.com/xml.response}"
            products = root.findall(f".//{ns}Product") or root.findall(".//Product")
            for product in products:
                if product.attrib.get("Name", "").lower() == tld.lower():
                    price_elem = product.find(f".//{ns}Price") or product.find(".//Price")
                    if price_elem is not None:
                        return {
                            "registration_price": float(price_elem.attrib.get("Price", 0)),
                            "renewal_price": float(price_elem.attrib.get("AdditionalCost", 0)),
                        }
        except Exception:
            pass
        return {"registration_price": None, "renewal_price": None}

    def get_backorder_price(self, domain: str) -> dict:
        root = self._request("namecheap.domains.check", {"DomainList": domain})
        ns = "{http://api.namecheap.com/xml.response}"
        result = root.find(f".//{ns}DomainCheckResult") or root.find(".//DomainCheckResult")
        available = result is not None and result.attrib.get("Available", "false").lower() == "true"
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
            "backorder_fee": None,
            "note": "NameCheap backorders are placed at a flat fee. If won, standard registration price applies.",
        }


class DomainChecker:
    def __init__(self, godaddy_key=None, godaddy_secret=None,
                 namecheap_user=None, namecheap_key=None, namecheap_client_ip=None):
        if requests is None:
            raise ImportError("requests library required: pip install requests")
        self.providers = {}
        if godaddy_key and godaddy_secret:
            self.providers["godaddy"] = GoDaddyClient(godaddy_key, godaddy_secret)
        if namecheap_user and namecheap_key and namecheap_client_ip:
            self.providers["namecheap"] = NameCheapClient(namecheap_user, namecheap_key, namecheap_client_ip)
        if not self.providers:
            raise ValueError(
                "At least one provider must be configured. Set env vars:\n"
                "  GoDaddy:   GODADDY_API_KEY, GODADDY_API_SECRET\n"
                "  NameCheap: NAMECHEAP_API_USER, NAMECHEAP_API_KEY, NAMECHEAP_CLIENT_IP"
            )

    def check(self, domain: str) -> dict:
        results, errors = {}, {}
        with ThreadPoolExecutor(max_workers=len(self.providers)) as pool:
            futures = {
                pool.submit(client.check_availability, domain): name
                for name, client in self.providers.items()
            }
            for future in as_completed(futures):
                name = futures[future]
                try:
                    results[name] = future.result()
                except Exception as e:
                    errors[name] = str(e)

        cheapest = None
        for name, r in results.items():
            if r.get("available") and r.get("price") is not None:
                if cheapest is None or r["price"] < cheapest["price"]:
                    cheapest = {"provider": name, "price": r["price"], "currency": r.get("currency", "USD")}

        backorder = None
        is_taken = all(not r.get("available") for r in results.values()) if results else False
        if is_taken and "namecheap" in self.providers:
            try:
                backorder = self.providers["namecheap"].get_backorder_price(domain)
            except Exception as e:
                backorder = {"error": str(e)}

        report = {"domain": domain, "results": results, "cheapest": cheapest, "backorder": backorder}
        if errors:
            report["errors"] = errors
        return report

    def check_bulk(self, domains: list[str]) -> list[dict]:
        return [self.check(d) for d in domains]

    def compare_prices(self, domain: str) -> str:
        report = self.check(domain)
        lines = [f"Domain: {report['domain']}", "=" * 50]
        for provider, result in report["results"].items():
            status = "AVAILABLE" if result.get("available") else "TAKEN"
            price = f"${result['price']:.2f}" if result.get("price") else "N/A"
            lines.append(f"  {provider.upper():12s}  {status:10s}  {price}/yr")
        if report.get("cheapest"):
            c = report["cheapest"]
            lines.append(f"\n  Best price: {c['provider'].upper()} at ${c['price']:.2f} {c['currency']}")
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
            for provider, err in report["errors"].items():
                lines.append(f"\n  ERROR ({provider}): {err}")
        return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(description="Check domain availability and pricing across GoDaddy and NameCheap")
    parser.add_argument("domains", nargs="+", help="Domain name(s) to check")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    config = load_config()
    init_args = {k: v for k, v in config.items() if v is not None}
    try:
        checker = DomainChecker(**init_args)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)

    if args.json:
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
