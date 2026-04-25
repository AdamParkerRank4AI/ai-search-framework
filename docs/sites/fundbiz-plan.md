# FundBiz — site plan

Last updated: 2026-04-25
Site: FundBiz — UK business loans broker / transactional lead-gen,
licensed to flex into adjacent SMB finance (cards, accounts, MCA, asset
finance, VAT loans, insurance). Sister site: BBL (editorial / review).
Sits above `docs/sites/fundbiz.md` (deep-dive). Lead-gen focus, no forms
in this phase — CTAs are placeholders only and will be wired to forms
later.

Companion docs: `docs/niche-brief.md`, `docs/route-to-market.md`,
`docs/regulatory-notes.md`, `docs/sites/synthesis.md`,
`docs/sites/fundbiz.md`.

Operational rule (from `regulatory-notes.md`): Ltd / PLC / LLP /
partnerships of 4+ only. Sole traders and ≤3-partner partnerships are
filtered out at the eligibility step (deferred — no forms in this
phase) and directed elsewhere (Start Up Loans / British Business Bank).
FCA permission is **not** required for this scope. No 8–12 week gating.

---

## 1. Information architecture (the silos)

Eight top-level silos plus a thin trust layer and a homepage. Each silo
is a true pillar (its own hub URL with internal-link spokes). The
**post-decline silo and the sector silo are the two revenue engines**
and get the densest internal-link weight; the adjacent-flex silo is the
20% bridge that exists to capture buyers already on a loans journey.

| Silo | URL prefix | Job | Pillar URL |
|---|---|---|---|
| Post-decline | `/declined/` | "Diagnose-the-decline" hub + reason-specific landers (CCJ, bad credit, missed payments, first-year-trading, by-bank). The wedge. | `/declined/` |
| Sectors | `/sectors/` | ~25–35 sector landers (hospitality, e-commerce, salons, gyms, dental, recruitment, construction etc.) — sector matcher + sector-specific FAQ + calculator stub | `/sectors/` |
| Products | `/products/` | Loan / MCA / asset finance / RBF / invoice-finance referral / VAT loan / R&D advance / commercial mortgage hubs and sub-pages | `/products/` |
| By-amount | `/by-amount/` | "£10k business loan", "£50k business loan", "£100k business loan", "£250k business loan" — head-term volume capture | `/by-amount/` |
| Calculators | `/calculators/` | Loan calc, MCA factor-rate calc, asset finance calc, VAT loan calc — AIO citation magnets, internal funnel hubs (calculator stubs only this phase) | `/calculators/` |
| Lenders | `/lenders/` | **Redirects (301) to BBL `/reviews/[lender]/`** — FundBiz never hosts editorial reviews. Internal link target only. | redirects to BBL |
| Adjacent | `/adjacent/` | The 20% flex: business credit cards, business bank accounts, business insurance, accountancy software, business energy — each tied back to the loans funnel | `/adjacent/` |
| Guides | `/guides/` | Informational pillars (eligibility, application process, repayment, glossary, regulation) — citation surface, internal-link out to converting pages | `/guides/` |
| Trust | `/about/`, `/how-we-work/`, `/contact/` | Organization schema, broker-introducer disclosure, transparency on commercial relationships | `/about/` |

**Flow.** Top-of-funnel guides and the calculator stubs feed pillars.
Pillars feed leaf pages (sector lander / decline-reason lander /
product page). Every leaf page contains (i) a CTA placeholder ("Get
matched with lenders" — to be wired to a form later), (ii) a
sister-site bridge (BBL editorial in for citation; MarketInvoice for
invoice-finance journeys; CardMachines for card-acceptance journeys),
and (iii) the diagnose-the-decline cross-link back to `/declined/`.
The `/lenders/` slug exists only as a 301 to BBL — FundBiz refuses to
duplicate BBL editorial.

---

## 2. Full sitemap (table)

~120 pages across the eight silos. Priority is wave 1–4 (waves 1–3 are
the 90-day plan from section 7; wave 4 is the 6-month roadmap). All
URLs are placeholders — final slugs to confirm during build.

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/` | Home | Home / hub | 1 |
| `/declined/` | Declined | Declined hub | 1 |
| `/declined/bad-credit/` | Declined | Declined-help | 1 |
| `/declined/with-ccj/` | Declined | Declined-help | 1 |
| `/declined/first-year-trading/` | Declined | Declined-help | 1 |
| `/declined/missed-payments/` | Declined | Declined-help | 1 |
| `/declined/thin-file/` | Declined | Declined-help | 2 |
| `/declined/pre-revenue/` | Declined | Declined-help | 2 |
| `/declined/personal-credit/` | Declined | Declined-help | 2 |
| `/declined/no-collateral/` | Declined | Declined-help | 2 |
| `/declined/poor-business-performance/` | Declined | Declined-help | 3 |
| `/declined/by-bank/lloyds/` | Declined | Declined-help (per-bank) | 1 |
| `/declined/by-bank/natwest/` | Declined | Declined-help (per-bank) | 1 |
| `/declined/by-bank/hsbc/` | Declined | Declined-help (per-bank) | 1 |
| `/declined/by-bank/barclays/` | Declined | Declined-help (per-bank) | 2 |
| `/declined/by-bank/santander/` | Declined | Declined-help (per-bank) | 2 |
| `/declined/by-bank/starling/` | Declined | Declined-help (per-bank) | 3 |
| `/declined/by-bank/tide/` | Declined | Declined-help (per-bank) | 3 |
| `/declined/by-bank/metro/` | Declined | Declined-help (per-bank) | 4 |
| `/declined/by-bank/co-operative/` | Declined | Declined-help (per-bank) | 4 |
| `/declined/second-chance/` | Declined | Declined-help | 1 |
| `/declined/after-bank-referral-scheme/` | Declined | Declined-help | 2 |
| `/declined/with-defaults/` | Declined | Declined-help | 3 |
| `/declined/with-iva/` | Declined | Declined-help | 4 |
| `/declined/with-bankruptcy-discharged/` | Declined | Declined-help | 4 |
| `/sectors/` | Sectors | Sector hub | 1 |
| `/sectors/hospitality/` | Sectors | Sector lander | 1 |
| `/sectors/restaurants/` | Sectors | Sector lander | 1 |
| `/sectors/cafes/` | Sectors | Sector lander | 2 |
| `/sectors/pubs-and-bars/` | Sectors | Sector lander | 1 |
| `/sectors/hotels-bnb/` | Sectors | Sector lander | 2 |
| `/sectors/takeaways-fast-food/` | Sectors | Sector lander | 3 |
| `/sectors/dark-kitchens/` | Sectors | Sector lander | 4 |
| `/sectors/food-trucks/` | Sectors | Sector lander | 4 |
| `/sectors/e-commerce/` | Sectors | Sector lander | 1 |
| `/sectors/shopify-merchants/` | Sectors | Sector lander | 2 |
| `/sectors/amazon-sellers/` | Sectors | Sector lander | 3 |
| `/sectors/retail/` | Sectors | Sector lander | 2 |
| `/sectors/off-licence/` | Sectors | Sector lander | 4 |
| `/sectors/florists/` | Sectors | Sector lander | 4 |
| `/sectors/construction/` | Sectors | Sector lander | 1 |
| `/sectors/scaffolding/` | Sectors | Sector lander | 3 |
| `/sectors/electricians/` | Sectors | Sector lander | 3 |
| `/sectors/plumbers/` | Sectors | Sector lander | 3 |
| `/sectors/beauty-salons/` | Sectors | Sector lander | 1 |
| `/sectors/barbers/` | Sectors | Sector lander | 3 |
| `/sectors/nail-salons/` | Sectors | Sector lander | 4 |
| `/sectors/gyms-and-fitness/` | Sectors | Sector lander | 1 |
| `/sectors/personal-trainers/` | Sectors | Sector lander | 4 |
| `/sectors/dental-practices/` | Sectors | Sector lander | 1 |
| `/sectors/vet-practices/` | Sectors | Sector lander | 2 |
| `/sectors/pharmacies/` | Sectors | Sector lander | 2 |
| `/sectors/gp-practices/` | Sectors | Sector lander | 3 |
| `/sectors/care-homes/` | Sectors | Sector lander | 3 |
| `/sectors/transport-haulage/` | Sectors | Sector lander | 2 |
| `/sectors/taxi-private-hire/` | Sectors | Sector lander | 3 |
| `/sectors/recruitment-agencies/` | Sectors | Sector lander | 2 |
| `/sectors/professional-services/` | Sectors | Sector lander | 3 |
| `/sectors/legal-firms/` | Sectors | Sector lander | 4 |
| `/sectors/accountancy-firms/` | Sectors | Sector lander | 4 |
| `/sectors/marketing-agencies/` | Sectors | Sector lander | 4 |
| `/sectors/manufacturing/` | Sectors | Sector lander | 2 |
| `/sectors/agriculture-farming/` | Sectors | Sector lander | 3 |
| `/sectors/franchises/` | Sectors | Sector lander | 2 |
| `/sectors/childcare-nurseries/` | Sectors | Sector lander | 4 |
| `/sectors/dry-cleaners/` | Sectors | Sector lander | 4 |
| `/products/` | Products | Product hub | 1 |
| `/products/business-loan/` | Products | Product page | 1 |
| `/products/unsecured-business-loan/` | Products | Product page | 2 |
| `/products/secured-business-loan/` | Products | Product page | 2 |
| `/products/short-term-business-loan/` | Products | Product page | 2 |
| `/products/merchant-cash-advance/` | Products | Product page (hub) | 1 |
| `/products/revenue-based-finance/` | Products | Product page | 2 |
| `/products/asset-finance/` | Products | Product page (hub) | 2 |
| `/products/equipment-finance/` | Products | Product page | 3 |
| `/products/vehicle-finance/` | Products | Product page | 3 |
| `/products/hire-purchase/` | Products | Product page | 3 |
| `/products/invoice-finance-referral/` | Products | Cross-product (referral to MarketInvoice) | 2 |
| `/products/vat-loan/` | Products | Product page | 2 |
| `/products/corporation-tax-loan/` | Products | Product page | 3 |
| `/products/r-and-d-advance/` | Products | Product page | 2 |
| `/products/working-capital-loan/` | Products | Product page | 2 |
| `/products/growth-finance/` | Products | Product page | 3 |
| `/products/commercial-mortgage/` | Products | Product page | 4 |
| `/products/bridging-loan/` | Products | Product page | 4 |
| `/products/start-up-loan/` | Products | Product page (referral) | 2 |
| `/products/government-backed-loan/` | Products | Product page | 3 |
| `/by-amount/` | By-amount | Hub | 2 |
| `/by-amount/10000/` | By-amount | Cross-product | 2 |
| `/by-amount/25000/` | By-amount | Cross-product | 2 |
| `/by-amount/50000/` | By-amount | Cross-product | 2 |
| `/by-amount/100000/` | By-amount | Cross-product | 2 |
| `/by-amount/250000/` | By-amount | Cross-product | 3 |
| `/by-amount/500000/` | By-amount | Cross-product | 4 |
| `/calculators/` | Calculators | Calculator hub | 1 |
| `/calculators/business-loan/` | Calculators | Calculator stub | 1 |
| `/calculators/merchant-cash-advance/` | Calculators | Calculator stub | 2 |
| `/calculators/asset-finance/` | Calculators | Calculator stub | 2 |
| `/calculators/vat-loan/` | Calculators | Calculator stub | 3 |
| `/calculators/repayment/` | Calculators | Calculator stub | 3 |
| `/calculators/affordability/` | Calculators | Calculator stub | 4 |
| `/lenders/` | Lenders | 301 to BBL `/reviews/` | 1 |
| `/adjacent/business-credit-cards/` | Adjacent | Cross-product | 2 |
| `/adjacent/business-credit-cards/after-loan-decline/` | Adjacent | Cross-product | 2 |
| `/adjacent/business-credit-cards/vs-business-loan/` | Adjacent | Cross-product | 3 |
| `/adjacent/business-bank-accounts/` | Adjacent | Cross-product | 2 |
| `/adjacent/business-bank-accounts/for-borrowing/` | Adjacent | Cross-product | 2 |
| `/adjacent/business-bank-accounts/tide-vs-starling/` | Adjacent | Cross-product | 3 |
| `/adjacent/business-insurance/` | Adjacent | Cross-product | 3 |
| `/adjacent/business-insurance/by-trade/` | Adjacent | Cross-product | 3 |
| `/adjacent/accountancy-software/` | Adjacent | Cross-product | 4 |
| `/adjacent/accountancy-software/connect-for-faster-decisions/` | Adjacent | Cross-product | 4 |
| `/adjacent/business-energy/` | Adjacent | Cross-product | 4 |
| `/adjacent/grants/` | Adjacent | Cross-product | 3 |
| `/guides/` | Guides | Guide hub | 2 |
| `/guides/business-loan-eligibility/` | Guides | Guide | 1 |
| `/guides/how-to-apply/` | Guides | Guide | 2 |
| `/guides/what-lenders-look-for/` | Guides | Guide | 2 |
| `/guides/personal-guarantees/` | Guides | Guide | 3 |
| `/guides/business-credit-score/` | Guides | Guide | 2 |
| `/guides/improve-business-credit/` | Guides | Guide | 3 |
| `/guides/secured-vs-unsecured/` | Guides | Guide | 3 |
| `/guides/mca-vs-loan/` | Guides | Guide | 2 |
| `/guides/asset-finance-explained/` | Guides | Guide | 3 |
| `/guides/glossary/` | Guides | Guide | 4 |
| `/guides/regulatory/who-can-apply/` | Guides | Guide | 2 |
| `/about/` | Trust | Trust | 2 |
| `/how-we-work/` | Trust | Trust | 2 |
| `/contact/` | Trust | Trust | 2 |

---

## 3. Top 50 page briefs (full)

TBD

---

## 4. Post-decline funnel — separate detail

TBD

---

## 5. Sector landers — the matrix

TBD

---

## 6. Adjacent-vertical flex pages (the 20% allowed)

TBD

---

## 7. Build sequence

TBD

---

## 8. Targets

TBD

---

## 9. Schema strategy summary

TBD

---

## 10. Open questions

TBD
