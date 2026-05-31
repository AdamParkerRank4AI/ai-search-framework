# Listings, Directories & Trust Signals — Market Finance & MerchantHQ

Action plan for building citation, entity and trust signals across two brands:

- **Market Finance** (marketinvoice.co.uk) — invoice finance
- **MerchantHQ** (merchanthq.co.uk) — card terminals / payments

## Approach (read first)

- **Gemini-first.** Gemini and Google AI Overviews are grounded in Google's
  Knowledge Graph + sources Google already trusts. So **entity verification +
  trusted-source citation beats directory link volume.**
- **Finance is YMYL** — trust/authority signals matter more than links.
- **Most directories are nofollow.** Value = citation consistency + AI/entity
  validation + leads, not ranking equity. The few dofollow ones are a bonus.
- **NAP rule:** identical Name / Address / Phone / description on *every*
  listing. Inconsistency = graph drift = lost trust.
- **Quality > volume.** ~80% of the value is in Tiers 1–3. Don't grind junk
  directories.
- **Only register where you legitimately qualify** (especially gov/regulated).

Legend: **D** dofollow · **N** nofollow · **E** entity/map signal · ✅ free ·
£ paid · Brand = Both / MF (Market Finance) / MHQ (MerchantHQ)

---

## Tier 1 — Official entity & compliance (do first; max trust, low/no backlink)

- [ ] **Companies House** — ✅ E — Both — auto-listed; make name/address/SIC accurate & consistent
- [ ] **ICO Register** (data-protection fee payers) — ✅ — Both — legally required (you run lead forms)
- [ ] **great.gov.uk** business profile (Dept for Business & Trade) — ✅ — Both
- [ ] **D-U-N-S number** (Dun & Bradstreet) — ✅ E — Both — global business identity used by Google/Apple/gov
- [ ] **Cyber Essentials** (NCSC/gov-backed cert) — ✅/low £ — Both — security-trust signal for handling card/personal data; listed in certified directory
- [ ] **UK IPO trademark** — low £ — Both — official record + brand protection
- [ ] _FCA Register — N/A — skip; eCapital holds the permissions_

## Tier 2 — Knowledge Graph & AI source pool (what Gemini actually cites)

- [ ] **Wikidata** — ✅ N — Both — directly feeds Google Knowledge Graph (highest-leverage free action)
- [ ] **Wikipedia** — ✅ — Both — only if notability met; build press coverage toward it
- [ ] **YouTube channel** — ✅ — Both — Google-owned; Gemini/AIO surface & cite video
- [ ] **Reddit** — ✅ — Both — AIO cites Reddit heavily; genuine participation (r/smallbusinessuk, r/UKPersonalFinance, r/business)
- [ ] **Quora** — ✅ — Both — answer real buyer questions; cited by Gemini
- [ ] **Crunchbase** — ✅ N — Both — structured entity DB Google ingests
- [ ] **Trustpilot** — ✅ N — Both — reviews/sentiment surfaced in AI Overviews

## Tier 3 — Authoritative & relevant directories

- [ ] **Yell.com** — ✅ N — Both — the one general directory Google genuinely trusts for UK business data
- [ ] **Smart Money People** — ✅ N — MF — finance-specific reviews (topical relevance)
- [ ] **Capterra / G2 / GetApp** — ✅ N — MHQ — for the EPOS/payments software angle
- [ ] **NACFB / businessfinance.co.uk** — £ D — MF — industry body listing (optional, paid, high relevance)

## Tier 4 — Free dofollow general directories (citation + light SEO)

- [ ] **FreeIndex** — ✅ D — Both
- [ ] **Cylex UK** — ✅ D — Both
- [ ] **UK Small Business Directory** — ✅ D — Both
- [ ] **iBegin** — ✅ D — Both
- [ ] **Lacartes** — ✅ D — Both
- [ ] **Brownbook** — ✅ D/varies — Both
- [ ] **Hotfrog** — ✅ varies — Both

## Tier 5 — Ethical accreditations (badge + listing; fits "nothing to hide")

- [ ] **Real Living Wage employer** — ✅ if eligible — Both — livingwage.org.uk directory
- [ ] **Good Business Charter** — Both — broad ethical accreditation + directory
- [ ] **Disability Confident** (gov employer scheme) — ✅ — Both
- [ ] **B Corp** — stretch — Both — gold-standard ethical directory

## Tier 6 — Public sector / procurement (if relevant)

- [ ] **Contracts Finder** — ✅ — Both — register as supplier
- [ ] **Find a Tender** — ✅ — Both — UK-wide higher-value tenders
- [ ] **Public Contracts Scotland / Sell2Wales / eTendersNI** — ✅ — Both — if operating there
- [ ] **British Business Bank** accredited-partner lists — MF — high bar, high credibility if eligible
- [ ] **Local Growth Hub** — ✅ — Both — gov-funded; sometimes links out
- [ ] **Local council business directory** — ✅ — Both — varies; some give a real link

## Tier 7 — Social / entity profiles (consistency signals)

- [ ] **LinkedIn** Company Page — ✅ N — Both
- [ ] **Facebook · X · Instagram · Pinterest · TikTok** — ✅ N — Both
- [ ] **Glassdoor / Indeed** company profile — ✅ — Both — employer entity signal

## Tier 8 — Lower-priority general directories (only if completist)

Yelp UK · Thomson Local · Scoot · 192.com · Touch Local · Misterwhat · Tupalo ·
Approved Business · Business Magnet · Europages · Foursquare · Kompass · Bark

> Skip Checkatrade and home-trade directories — wrong vertical, no relevant trust.

---

## The connective tissue (do this too)

Add **Organization schema** to each site with a **`sameAs`** array listing every
profile URL above (Wikidata, Crunchbase, YouTube, LinkedIn, Trustpilot,
Companies House, D-U-N-S, etc.). This tells Google's Knowledge Graph "these are
all the same entity" — for Gemini this matters more than the whole directory
list combined.

## Suggested do-order (first 10 actions)

1. Companies House — verify accurate & consistent
2. D-U-N-S number
3. ICO Register
4. great.gov.uk profile
5. Wikidata entity
6. Crunchbase profile
7. Trustpilot
8. Cyber Essentials certification
9. YouTube channel + start Reddit/Quora presence
10. Free dofollow trio: FreeIndex, Cylex, UK Small Business Directory
    → then add Organization `sameAs` schema linking them all.

Value drops off sharply after Tier 3 — if you only do Tiers 1–3 + schema,
you've banked the vast majority of the Gemini/trust upside.
