"""
RDAP/WHOIS Domain Checker
Checks domain registration details using public RDAP servers.
No API keys required.
"""

import json
import urllib.request
import urllib.error
from datetime import datetime, timezone
from dataclasses import dataclass, field, asdict
from typing import Optional


@dataclass
class DomainInfo:
    domain: str
    status: str = "unknown"  # registered, available, error
    registration_date: Optional[str] = None
    expiry_date: Optional[str] = None
    last_changed: Optional[str] = None
    registrar: Optional[str] = None
    nameservers: list = field(default_factory=list)
    age_years: Optional[float] = None
    days_until_expiry: Optional[int] = None
    error: Optional[str] = None

    def to_dict(self):
        return asdict(self)


# RDAP servers for different TLDs
RDAP_SERVERS = {
    "com": "https://rdap.verisign.com/com/v1/domain/",
    "net": "https://rdap.verisign.com/net/v1/domain/",
    "org": "https://rdap.org/domain/",
    "co.uk": "https://rdap.nominet.uk/",
    "uk": "https://rdap.nominet.uk/",
    "io": "https://rdap.nic.io/domain/",
    "info": "https://rdap.afilias.net/rdap/info/domain/",
}


def get_tld(domain: str) -> str:
    """Extract TLD from domain name."""
    parts = domain.lower().split(".")
    if len(parts) >= 3 and parts[-2] == "co":
        return f"{parts[-2]}.{parts[-1]}"
    return parts[-1]


def parse_rdap_response(data: dict, domain: str) -> DomainInfo:
    """Parse RDAP JSON response into DomainInfo."""
    info = DomainInfo(domain=domain, status="registered")

    # Parse events (registration, expiration, last changed)
    for event in data.get("events", []):
        action = event.get("eventAction", "")
        date_str = event.get("eventDate", "")
        if action == "registration":
            info.registration_date = date_str
        elif action == "expiration":
            info.expiry_date = date_str
        elif action == "last changed":
            info.last_changed = date_str

    # Calculate age
    if info.registration_date:
        try:
            reg_date = datetime.fromisoformat(info.registration_date.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            info.age_years = round((now - reg_date).days / 365.25, 1)
        except (ValueError, TypeError):
            pass

    # Calculate days until expiry
    if info.expiry_date:
        try:
            exp_date = datetime.fromisoformat(info.expiry_date.replace("Z", "+00:00"))
            now = datetime.now(timezone.utc)
            info.days_until_expiry = (exp_date - now).days
        except (ValueError, TypeError):
            pass

    # Parse registrar
    for entity in data.get("entities", []):
        if "registrar" in entity.get("roles", []):
            vcard = entity.get("vcardArray", ["vcard", []])
            if len(vcard) > 1:
                for item in vcard[1]:
                    if item[0] == "fn":
                        info.registrar = item[3]
                        break

    # Parse nameservers
    for ns in data.get("nameservers", []):
        ns_name = ns.get("ldhName", "")
        if ns_name:
            info.nameservers.append(ns_name.lower())

    return info


def check_domain(domain: str, timeout: int = 10) -> DomainInfo:
    """Check a single domain's registration details via RDAP."""
    domain = domain.lower().strip()
    tld = get_tld(domain)

    rdap_base = RDAP_SERVERS.get(tld)
    if not rdap_base:
        return DomainInfo(
            domain=domain,
            status="error",
            error=f"No RDAP server configured for TLD: .{tld}",
        )

    url = f"{rdap_base}{domain.upper()}"

    try:
        req = urllib.request.Request(
            url,
            headers={"Accept": "application/rdap+json"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode())
            return parse_rdap_response(data, domain)
    except urllib.error.HTTPError as e:
        if e.code == 404:
            return DomainInfo(domain=domain, status="available")
        return DomainInfo(
            domain=domain, status="error", error=f"HTTP {e.code}: {e.reason}"
        )
    except urllib.error.URLError as e:
        return DomainInfo(
            domain=domain, status="error", error=f"Connection error: {e.reason}"
        )
    except Exception as e:
        return DomainInfo(domain=domain, status="error", error=str(e))


def check_domains(domains: list[str], timeout: int = 10) -> list[DomainInfo]:
    """Check multiple domains and return their registration details."""
    results = []
    for domain in domains:
        result = check_domain(domain, timeout)
        results.append(result)
    return results


def format_report(results: list[DomainInfo]) -> str:
    """Format domain check results as a readable report."""
    lines = []
    lines.append("=" * 80)
    lines.append("DOMAIN AGE & AVAILABILITY REPORT")
    lines.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append("=" * 80)

    available = [r for r in results if r.status == "available"]
    registered = [r for r in results if r.status == "registered"]
    errors = [r for r in results if r.status == "error"]

    # Available domains
    if available:
        lines.append(f"\n--- AVAILABLE DOMAINS ({len(available)}) ---")
        for r in available:
            lines.append(f"  [AVAILABLE] {r.domain}")

    # Registered domains sorted by age (oldest first)
    if registered:
        registered.sort(key=lambda x: x.age_years or 0, reverse=True)
        lines.append(f"\n--- REGISTERED DOMAINS ({len(registered)}) ---")
        for r in registered:
            age_str = f"{r.age_years} years" if r.age_years else "unknown age"
            expiry_str = ""
            if r.days_until_expiry is not None:
                if r.days_until_expiry < 0:
                    expiry_str = " [EXPIRED]"
                elif r.days_until_expiry < 90:
                    expiry_str = f" [EXPIRING SOON: {r.days_until_expiry} days]"
                else:
                    expiry_str = f" [expires in {r.days_until_expiry} days]"
            registrar_str = f" via {r.registrar}" if r.registrar else ""
            lines.append(f"  {r.domain} - {age_str}{expiry_str}{registrar_str}")
            if r.registration_date:
                lines.append(f"    Registered: {r.registration_date[:10]}")
            if r.expiry_date:
                lines.append(f"    Expires:    {r.expiry_date[:10]}")

    # Errors
    if errors:
        lines.append(f"\n--- ERRORS ({len(errors)}) ---")
        for r in errors:
            lines.append(f"  {r.domain}: {r.error}")

    lines.append("\n" + "=" * 80)
    return "\n".join(lines)


if __name__ == "__main__":
    # Example: check some invoice finance domains
    test_domains = [
        "compare-invoice-factoring.com",
        "compareinvoicefactoring.com",
        "compareinvoicefactoring.co.uk",
        "invoicefinance.co.uk",
        "fundinvoice.co.uk",
    ]
    results = check_domains(test_domains)
    print(format_report(results))
