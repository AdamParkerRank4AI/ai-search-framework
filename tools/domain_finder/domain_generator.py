"""
Domain Name Generator
Generates candidate domain names for a given niche/industry.
Combines industry keywords with common domain patterns.
"""

from itertools import product


# Common patterns for niche comparison/information sites
PATTERNS = [
    "{kw1}{kw2}",
    "{kw1}-{kw2}",
    "compare{kw1}{kw2}",
    "compare-{kw1}-{kw2}",
    "{kw1}{kw2}compare",
    "{kw1}-{kw2}-compare",
    "best{kw1}{kw2}",
    "best-{kw1}-{kw2}",
    "{kw1}{kw2}guide",
    "{kw1}-{kw2}-guide",
    "{kw1}{kw2}uk",
    "{kw1}-{kw2}-uk",
    "uk{kw1}{kw2}",
    "uk-{kw1}-{kw2}",
    "my{kw1}{kw2}",
    "my-{kw1}-{kw2}",
    "the{kw1}{kw2}",
    "the-{kw1}-{kw2}",
    "{kw1}{kw2}broker",
    "{kw1}-{kw2}-broker",
    "{kw1}{kw2}quotes",
    "{kw1}-{kw2}-quotes",
    "{kw1}{kw2}solutions",
    "{kw1}-{kw2}-solutions",
    "{kw1}{kw2}experts",
    "{kw1}-{kw2}-experts",
    "{kw1}{kw2}direct",
    "{kw1}-{kw2}-direct",
    "{kw1}{kw2}online",
    "{kw1}-{kw2}-online",
    "{kw1}{kw2}finder",
    "{kw1}-{kw2}-finder",
    "{kw1}{kw2}hub",
    "{kw1}-{kw2}-hub",
    "{kw1}{kw2}info",
    "{kw1}{kw2}news",
]

# Common TLDs to check
DEFAULT_TLDS = [".com", ".co.uk", ".uk", ".net", ".org"]


# Pre-built niche keyword sets
NICHE_KEYWORDS = {
    "invoice_finance": {
        "kw1": [
            "invoice",
            "invoicing",
        ],
        "kw2": [
            "finance",
            "financing",
            "factoring",
            "discounting",
            "funding",
        ],
        "extra_terms": [
            "factoring",
            "cashflow",
            "cash-flow",
            "receivables",
            "debtfinance",
            "debt-finance",
            "tradefinance",
            "trade-finance",
            "assetfinance",
            "asset-finance",
            "asset-based-lending",
            "assetbasedlending",
        ],
    },
    "business_finance": {
        "kw1": [
            "business",
            "commercial",
            "sme",
            "company",
        ],
        "kw2": [
            "finance",
            "funding",
            "loans",
            "lending",
            "capital",
        ],
        "extra_terms": [
            "businessloans",
            "business-loans",
            "smefunding",
            "sme-funding",
        ],
    },
    "insurance": {
        "kw1": [
            "business",
            "commercial",
            "company",
            "trade",
        ],
        "kw2": [
            "insurance",
            "cover",
            "protection",
            "indemnity",
        ],
        "extra_terms": [],
    },
}


def generate_domains(
    niche: str = None,
    kw1_list: list[str] = None,
    kw2_list: list[str] = None,
    extra_terms: list[str] = None,
    tlds: list[str] = None,
    patterns: list[str] = None,
) -> list[str]:
    """
    Generate candidate domain names for a niche.

    Args:
        niche: Pre-built niche name (e.g. "invoice_finance")
        kw1_list: Custom primary keywords (overrides niche)
        kw2_list: Custom secondary keywords (overrides niche)
        extra_terms: Additional standalone domain stems to check
        tlds: TLDs to append (default: .com, .co.uk, .uk, .net, .org)
        patterns: Custom patterns (default: built-in PATTERNS list)

    Returns:
        List of candidate domain names
    """
    if tlds is None:
        tlds = DEFAULT_TLDS
    if patterns is None:
        patterns = PATTERNS

    # Load niche keywords if specified
    if niche and niche in NICHE_KEYWORDS:
        niche_data = NICHE_KEYWORDS[niche]
        if kw1_list is None:
            kw1_list = niche_data["kw1"]
        if kw2_list is None:
            kw2_list = niche_data["kw2"]
        if extra_terms is None:
            extra_terms = niche_data.get("extra_terms", [])

    if not kw1_list or not kw2_list:
        raise ValueError("Provide either a niche name or kw1_list + kw2_list")

    domains = set()

    # Generate from patterns
    for kw1, kw2 in product(kw1_list, kw2_list):
        for pattern in patterns:
            stem = pattern.format(kw1=kw1, kw2=kw2)
            for tld in tlds:
                domains.add(f"{stem}{tld}")

    # Add extra standalone terms
    if extra_terms:
        for term in extra_terms:
            for tld in tlds:
                domains.add(f"{term}{tld}")
            # Also add with common prefixes
            for prefix in ["compare", "compare-", "best", "best-", "uk", "uk-", "my", "the"]:
                for tld in tlds:
                    domains.add(f"{prefix}{term}{tld}")

    return sorted(domains)


def generate_invoice_finance_domains(tlds: list[str] = None) -> list[str]:
    """Convenience function for invoice finance niche."""
    return generate_domains(niche="invoice_finance", tlds=tlds)


if __name__ == "__main__":
    domains = generate_invoice_finance_domains(tlds=[".com", ".co.uk"])
    print(f"Generated {len(domains)} candidate domains for invoice finance:")
    for d in domains[:50]:
        print(f"  {d}")
    print(f"  ... and {len(domains) - 50} more" if len(domains) > 50 else "")
