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

Briefing the 20 Wave 1 pages. Briefs 21–50 follow in next pass — same
template, slugs from the sitemap above.

### `/declined/` (hub — the wedge)
- **Target query:** `business loan declined what next`
- **Secondaries:** `business loan rejected UK`, `bank refused business loan`, `lender said no`
- **AI prompt:** "I was just declined for a business loan — what should I do?"
- **Primary surface:** SEO + AI Overviews
- **Niche served:** ~50% of UK SME loan applicants who get rejected — biggest single revenue line on the network
- **Outline:** Why banks decline (7 common reasons); the 30-day window; what to fix vs what to route around; the diagnose-the-decline matcher (placeholder); reason-specific lander block (links to all decline-help pages); per-bank lander block (links to /declined/by-bank/*); FAQ
- **Internal links:** every `/declined/*` page; from BBL `/declined/best-lenders-after-decline-2026/`; to `/products/merchant-cash-advance/`
- **CTA placeholder:** "Get matched with lenders who'll consider you"
- **Commission path:** Liberis + YouLend + Capify + 365 (direct CPL £100–300)

### `/declined/bad-credit/`
- **Target query:** `business loan with bad credit UK`
- **Secondaries:** `bad credit business loan`, `business loan poor credit history UK`
- **AI prompt:** "Can I get a business loan in the UK with bad credit?"
- **Primary surface:** SEO + AI Overviews
- **Niche served:** post-decline applicants with personal/business credit issues
- **Outline:** What "bad credit" means to a lender; lenders that look beyond credit score; revenue-based finance / MCA mechanics; what to fix first; eligibility checklist; FAQ
- **Internal links:** `/declined/`, `/products/merchant-cash-advance/`, `/products/revenue-based-finance/`, BBL `/declined/best-lenders-after-decline-2026/` (cross-link in)
- **CTA placeholder:** "See lenders that work with bad credit"
- **Commission path:** Liberis, YouLend, Capify, 365 — £100–250 CPL

### `/declined/with-ccj/`
- **Target query:** `business loan with CCJ`
- **Secondaries:** `business loan after CCJ UK`, `CCJ business funding`
- **AI prompt:** "Can I get business funding with a CCJ?"
- **Primary surface:** AI Overviews (specific intent, weak SERP)
- **Niche served:** post-CCJ applicants — narrow but high-intent
- **Outline:** What a CCJ does to applications; satisfied vs unsatisfied; lenders that consider CCJs (named); explaining the CCJ in your application; FAQ
- **Internal links:** `/declined/`, `/declined/bad-credit/`, `/products/merchant-cash-advance/`
- **CTA placeholder:** "Find a CCJ-tolerant lender"
- **Commission path:** Capify, Liberis — £150–300 CPL

### `/declined/first-year-trading/`
- **Target query:** `business loan less than 1 year trading UK`
- **Secondaries:** `new business loan UK`, `business loan first year`
- **AI prompt:** "Can I get a business loan if I've only been trading 6 months?"
- **Primary surface:** SEO + AI Overviews
- **Niche served:** newly incorporated companies that don't yet meet typical 12–24 month trading minimums
- **Outline:** Why most lenders want 12+ months; lenders that take younger businesses (Iwoca, Capify); Start Up Loans referral (BBB); MCA option (if there's card revenue); FAQ
- **Internal links:** `/declined/`, `/products/start-up-loan/`, `/products/merchant-cash-advance/`
- **CTA placeholder:** "Find a young-business-friendly lender"
- **Commission path:** Iwoca direct, Capify direct, BBB referral — £80–250 CPL

### `/declined/missed-payments/`
- **Target query:** `business loan with missed payments`
- **Secondaries:** `business funding after missed payment`, `late payment business loan UK`
- **AI prompt:** "Can I get a business loan if I've had missed payments?"
- **Primary surface:** AI Overviews
- **Niche served:** applicants flagged for late/missed payments
- **Outline:** How missed payments show up; the difference between defaults and arrears; lenders that look at recent rather than historical; how to explain it; FAQ
- **Internal links:** `/declined/`, `/declined/bad-credit/`, `/declined/with-defaults/`, `/products/revenue-based-finance/`
- **CTA placeholder:** "Find lenders that look at recent performance"
- **Commission path:** YouLend, Liberis — £100–250 CPL

### `/declined/by-bank/lloyds/`
- **Target query:** `Lloyds declined business loan`
- **Secondaries:** `Lloyds said no business loan`, `Lloyds rejected my business`
- **AI prompt:** "Lloyds declined my business loan — what next?"
- **Primary surface:** SEO (extremely specific intent, hot)
- **Niche served:** post-decline traffic from a single major bank
- **Outline:** Why Lloyds typically declines (their criteria); your options; alternative lenders by use-case; the Bank Referral Scheme (Lloyds is a designated bank); FAQ
- **Internal links:** `/declined/`, `/declined/after-bank-referral-scheme/`, sector landers if relevant
- **CTA placeholder:** "See lenders who'll consider what Lloyds wouldn't"
- **Commission path:** Liberis, YouLend, Capify — £100–300 CPL

### `/declined/by-bank/natwest/`
- **Target query:** `NatWest declined business loan`
- Mirrors Lloyds page with NatWest-specific criteria; same template, lenders, internal links.

### `/declined/by-bank/hsbc/`
- **Target query:** `HSBC declined business loan`
- Mirrors with HSBC-specific criteria.

### `/declined/second-chance/`
- **Target query:** `second chance business loan UK`
- **Secondaries:** `second chance business funding`, `business loan when banks say no`
- **AI prompt:** "What are second-chance business lenders in the UK?"
- **Primary surface:** AI Overviews
- **Niche served:** broad post-decline applicants searching with that specific phrase
- **Outline:** What "second chance" means in practice; lenders that specialise (Liberis, Capify, YouLend, 365); typical product types (MCA, RBF); typical rates and trade-offs; FAQ
- **Internal links:** `/declined/`, `/products/merchant-cash-advance/`, `/products/revenue-based-finance/`
- **CTA placeholder:** "Get matched with second-chance lenders"
- **Commission path:** Liberis, Capify, YouLend, 365 — £150–300 CPL

### `/sectors/hospitality/`
- **Target query:** `business loans for hospitality UK`
- **Secondaries:** `hospitality business funding`, `restaurant pub cafe loans`
- **AI prompt:** "What business loans are available for hospitality businesses in the UK?"
- **Primary surface:** SEO
- **Niche served:** the sector hub — splits into restaurants, pubs, cafés, takeaways, hotels
- **Outline:** Hospitality lending environment 2026; products that fit (MCA where card revenue is high, asset finance for kit, working capital); lenders specialising in hospitality (Liberis, YouLend, Funding Circle hospitality team); pulse on the sector pressures; sub-sector links
- **Internal links:** all hospitality sub-sectors; `/products/merchant-cash-advance/`; CardMachines `/hospitality/` (cross-site link)
- **CTA placeholder:** "Get matched with hospitality lenders"
- **Commission path:** Liberis, YouLend, 365 (MCA dominant in this sector) — £150–300 CPL

### `/sectors/restaurants/`
- **Target query:** `business loans for restaurants UK`
- **Secondaries:** `restaurant funding UK`, `loans for restaurants`
- **AI prompt:** "Best business loans for a UK restaurant"
- **Outline:** Restaurant-specific challenges (margins, seasonality); MCA mechanics on card revenue; equipment finance options; expansion finance; named lenders; FAQ
- **Internal links:** `/sectors/hospitality/`, `/products/merchant-cash-advance/`, `/declined/`, BBL `/best/business-loans-for-restaurants-2026/` (cross-in)
- **CTA placeholder:** "Find restaurant-friendly lenders"
- **Commission path:** Liberis, YouLend, Capify — £150–300 CPL

### `/sectors/pubs-and-bars/`
- **Target query:** `business loans for pubs UK`
- **Secondaries:** `pub finance UK`, `bar business loan`
- **AI prompt:** "Where can a UK pub get a business loan?"
- **Outline:** UK pub sector pressures; tied vs free houses; products that fit; specialist lenders (Just Cash Flow, 365); FAQ
- **Internal links:** `/sectors/hospitality/`, `/products/merchant-cash-advance/`
- **CTA placeholder:** "Find pub-friendly lenders"
- **Commission path:** 365, Liberis — £150–300 CPL

### `/sectors/e-commerce/`
- **Target query:** `business loans for e-commerce UK`
- **Secondaries:** `Shopify merchant funding`, `e-commerce growth finance UK`
- **AI prompt:** "Best funding options for a UK e-commerce business"
- **Primary surface:** AI Overviews
- **Niche served:** Shopify / Amazon / DTC sellers
- **Outline:** Why e-commerce is hard for traditional lenders; revenue-based finance (the right product); named lenders (YouLend, Wayflyer, Uncapped, Liberis); platform-integrated funding (Shopify Capital, Amazon Lending); FAQ
- **Internal links:** `/products/revenue-based-finance/`, `/sectors/shopify-merchants/`, `/sectors/amazon-sellers/`
- **CTA placeholder:** "Get matched with e-commerce lenders"
- **Commission path:** YouLend, Wayflyer, Uncapped — £200–400 CPL (highest sector CPL band)

### `/sectors/construction/`
- **Target query:** `business loans for construction UK`
- **Secondaries:** `construction firm funding UK`, `loans for builders`
- **AI prompt:** "Where can a UK construction firm get a loan?"
- **Outline:** Sector cash-flow challenge (long pay cycles, retention); product mix (working capital + invoice finance + asset finance); CIS scheme implications; named lenders (Bibby, Funding Circle, Iwoca); MarketInvoice cross-link for invoice finance
- **Internal links:** `/products/working-capital-loan/`, `/products/invoice-finance-referral/`, MarketInvoice cross-site
- **CTA placeholder:** "Find construction-friendly lenders"
- **Commission path:** Iwoca, Funding Circle — £100–250 CPL; cross-site MarketInvoice CPL

### `/sectors/beauty-salons/`
- **Target query:** `business loans for beauty salons UK`
- **Outline:** Salon cash flow; equipment finance; expansion; named lenders; FAQ
- **Internal links:** `/sectors/barbers/`, `/sectors/nail-salons/`, `/products/asset-finance/`
- **CTA placeholder:** "Find salon lenders"
- **Commission path:** Liberis, Iwoca, asset finance specialists — £100–250 CPL

### `/sectors/gyms-and-fitness/`
- **Target query:** `business loans for gyms UK`
- **Outline:** Gym/studio sector; membership-revenue lending; equipment finance; named lenders
- **Internal links:** `/products/revenue-based-finance/`, `/products/asset-finance/`
- **CTA placeholder:** "Find gym lenders"
- **Commission path:** YouLend, Liberis — £150–300 CPL

### `/sectors/dental-practices/`
- **Target query:** `dental practice loan UK`
- **Secondaries:** `dental practice finance UK`, `dentist business loan`
- **AI prompt:** "How do I finance a UK dental practice?"
- **Niche served:** dental owners — high-margin, lender-favoured, commission tier higher than average
- **Outline:** Dental-specific lenders (Wesleyan, Praxis, Christie Finance); practice acquisition finance; goodwill financing; equipment finance; FAQ
- **Internal links:** `/sectors/vet-practices/`, `/products/commercial-mortgage/`
- **CTA placeholder:** "Find dental practice lenders"
- **Commission path:** Specialist healthcare lenders — £200–500 CPL (highest)

### `/products/business-loan/`
- **Target query:** `business loan UK`
- **Secondaries:** `apply for business loan UK`, `business loans 2026`
- **AI prompt:** "How do I get a business loan in the UK?"
- **Primary surface:** SEO (head term)
- **Niche served:** broad transactional capture — must rank to be a credible site
- **Outline:** What a business loan is; secured vs unsecured; typical amounts and terms; eligibility; how to apply; lender map; cross-link to BBL editorial review; FAQ
- **Internal links:** all `/products/*` sub-pages; `/calculators/business-loan/`; BBL `/best/business-loans-uk-2026/` (cross-in)
- **CTA placeholder:** "Get matched with business lenders"
- **Commission path:** broad lender panel — £80–200 CPL

### `/products/merchant-cash-advance/`
- **Target query:** `merchant cash advance UK`
- **Secondaries:** `MCA UK`, `cash advance for business UK`, `business cash advance against card sales`
- **AI prompt:** "What is a merchant cash advance and how does it work in the UK?"
- **Primary surface:** AI Overviews + SEO
- **Niche served:** retail, hospitality, e-commerce — anyone with consistent card revenue
- **Outline:** What an MCA is (sale of future receivables, not a loan); factor rate maths worked through; eligibility; pros / cons; named providers (Liberis, YouLend, Capify, 365); calculator stub; FAQ
- **Internal links:** `/calculators/merchant-cash-advance/`, `/sectors/hospitality/`, `/sectors/e-commerce/`, `/declined/bad-credit/`
- **CTA placeholder:** "Get matched with MCA providers"
- **Commission path:** Liberis, YouLend, Capify, 365 — £150–300 CPL

### `/calculators/business-loan/`
- **Target query:** `business loan calculator UK`
- **Secondaries:** `business loan repayment calculator UK`, `how much business loan can I afford`
- **AI prompt:** "How do I calculate business loan repayments?"
- **Primary surface:** SEO + AI Overviews (calculator pages cite well)
- **Niche served:** mid-funnel evaluators
- **Outline:** Inputs (amount, term, rate); output (monthly repayment, total cost); contextual notes (APR vs flat rate); recommended next steps based on result range; FAQ
- **Internal links:** `/products/business-loan/`, `/calculators/affordability/`, `/products/merchant-cash-advance/` (when calculator says "MCA may suit better")
- **CTA placeholder:** "Get a personalised quote based on these numbers"
- **Commission path:** broad lender panel — £80–200 CPL

**Briefs 21–50 to follow in next pass.** Slugs from the sitemap; same
template — URL slug, target query, secondary queries, AI prompt, primary
surface, niche, outline, internal links, CTA placeholder, commission
path.

---

## 4. Post-decline funnel — separate detail

The single biggest revenue line on FundBiz. ~£225–360k/yr TAM at modest
share. 22 pages total. The diagnose-the-decline matcher is the central
hub; every page exits to either an MCA / RBF / second-chance
application path.

### Per-bank pages
Each follows the same template: target query is `[bank] declined business
loan`, content covers (a) the bank's typical criteria, (b) why
applications fail, (c) Bank Referral Scheme status, (d) alternative
lenders by use-case, (e) FAQ. Lender chain: Liberis, YouLend, Capify,
365 (MCA) + Iwoca (term loan) + BBB Start Up Loans (referral).

| URL | Target query | Wave |
|---|---|---|
| `/declined/by-bank/lloyds/` | `Lloyds declined business loan` | 1 |
| `/declined/by-bank/natwest/` | `NatWest declined business loan` | 1 |
| `/declined/by-bank/hsbc/` | `HSBC declined business loan` | 1 |
| `/declined/by-bank/barclays/` | `Barclays declined business loan` | 2 |
| `/declined/by-bank/santander/` | `Santander declined business loan` | 2 |
| `/declined/by-bank/starling/` | `Starling declined business loan` | 3 |
| `/declined/by-bank/tide/` | `Tide declined business loan` | 3 |
| `/declined/by-bank/metro/` | `Metro Bank declined business loan` | 4 |
| `/declined/by-bank/co-operative/` | `Co-operative Bank declined business loan` | 4 |

### Reason-specific pages

| URL | Target query | Wave |
|---|---|---|
| `/declined/bad-credit/` | `business loan with bad credit UK` | 1 |
| `/declined/with-ccj/` | `business loan with CCJ` | 1 |
| `/declined/first-year-trading/` | `business loan less than 1 year trading UK` | 1 |
| `/declined/missed-payments/` | `business loan with missed payments` | 1 |
| `/declined/thin-file/` | `business loan no credit history UK` | 2 |
| `/declined/pre-revenue/` | `pre-revenue business funding UK` | 2 |
| `/declined/personal-credit/` | `business loan personal credit issues UK` | 2 |
| `/declined/no-collateral/` | `unsecured business loan no collateral` | 2 |
| `/declined/poor-business-performance/` | `business loan declining sales` | 3 |
| `/declined/with-defaults/` | `business loan with defaults UK` | 3 |
| `/declined/with-iva/` | `business loan with IVA UK` | 4 |
| `/declined/with-bankruptcy-discharged/` | `business loan after discharged bankruptcy UK` | 4 |

### Hubs
- `/declined/` — main hub (template H2s above in section 3)
- `/declined/second-chance/` — generic post-decline searcher
- `/declined/after-bank-referral-scheme/` — for users who've gone through
  the BRS and need to know what's next

### Lender chain (typical waterfall on a decline page)

1. **MCA / RBF** (Liberis, YouLend, Capify, 365) — first because they
   tolerate credit issues and pay highest CPL (£150–300)
2. **Iwoca** — term loan with looser-than-bank criteria
3. **Funding Circle** — if turnover and trading history support it
4. **Specialist sector lenders** — only if the page is sector-specific
5. **Start Up Loans (BBB)** — referral, typically last for first-year
   traders

---

## 5. Sector landers — the matrix

~30 sector pages. Target query is always `business loans for [sector] UK`
(or close variant). Primary surface is SEO unless flagged otherwise.
Top 2–3 lenders per row are the highest-CPL match for that sector's
typical applicant.

| URL | Target query | Surface | Top lender chain | Wave |
|---|---|---|---|---|
| `/sectors/hospitality/` | business loans for hospitality UK | SEO | Liberis, YouLend, 365 | 1 |
| `/sectors/restaurants/` | business loans for restaurants UK | SEO | Liberis, YouLend, Capify | 1 |
| `/sectors/cafes/` | business loans for cafés UK | SEO | Liberis, Iwoca | 2 |
| `/sectors/pubs-and-bars/` | business loans for pubs UK | SEO | 365, Liberis, Just Cash Flow | 1 |
| `/sectors/hotels-bnb/` | hotel B&B business loans UK | SEO | Iwoca, Funding Circle | 2 |
| `/sectors/takeaways-fast-food/` | business loans for takeaways UK | SEO | Liberis, Capify | 3 |
| `/sectors/dark-kitchens/` | dark kitchen funding UK | AIO | YouLend, Wayflyer | 4 |
| `/sectors/food-trucks/` | food truck business loan UK | SEO | Iwoca, Capify | 4 |
| `/sectors/e-commerce/` | business loans for e-commerce UK | AIO | YouLend, Wayflyer, Uncapped | 1 |
| `/sectors/shopify-merchants/` | Shopify merchant funding UK | AI Search | Wayflyer, Shopify Capital | 2 |
| `/sectors/amazon-sellers/` | Amazon seller funding UK | AI Search | Wayflyer, Uncapped, Amazon Lending | 3 |
| `/sectors/retail/` | business loans for retail UK | SEO | Iwoca, Capify | 2 |
| `/sectors/off-licence/` | off-licence business loan UK | SEO | Capify, Liberis | 4 |
| `/sectors/florists/` | business loans for florists UK | SEO | Iwoca | 4 |
| `/sectors/construction/` | business loans for construction UK | SEO | Iwoca, Funding Circle, Bibby (cross-site) | 1 |
| `/sectors/scaffolding/` | scaffolding business loan UK | SEO | Iwoca, asset finance | 3 |
| `/sectors/electricians/` | electrician business loan UK | SEO | Iwoca | 3 |
| `/sectors/plumbers/` | plumber business loan UK | SEO | Iwoca, Capify | 3 |
| `/sectors/beauty-salons/` | beauty salon business loan UK | SEO | Liberis, Iwoca, asset finance | 1 |
| `/sectors/barbers/` | barber business loan UK | SEO | Liberis | 3 |
| `/sectors/nail-salons/` | nail salon business loan UK | SEO | Liberis, Capify | 4 |
| `/sectors/gyms-and-fitness/` | gym business loan UK | SEO | YouLend, Liberis, asset finance | 1 |
| `/sectors/personal-trainers/` | PT business loan UK | SEO | Iwoca | 4 |
| `/sectors/dental-practices/` | dental practice loan UK | AIO | Wesleyan, Praxis, Christie | 1 |
| `/sectors/vet-practices/` | vet practice loan UK | AIO | Wesleyan, Praxis | 2 |
| `/sectors/pharmacies/` | pharmacy business loan UK | AIO | NPA Pharmacy Mutual, Christie | 2 |
| `/sectors/gp-practices/` | GP practice loan UK | AIO | Wesleyan | 3 |
| `/sectors/care-homes/` | care home business loan UK | AIO | Christie, specialist healthcare | 3 |
| `/sectors/transport-haulage/` | haulage business loan UK | SEO | Iwoca, asset finance specialists | 2 |
| `/sectors/taxi-private-hire/` | taxi business loan UK | SEO | Iwoca, asset finance | 3 |
| `/sectors/recruitment-agencies/` | recruitment agency funding UK | SEO + AIO | Sonovate (cross to MarketInvoice), Iwoca | 2 |
| `/sectors/professional-services/` | business loans professional services UK | SEO | Iwoca, Funding Circle | 3 |
| `/sectors/legal-firms/` | law firm business loan UK | SEO | specialist + Funding Circle | 4 |
| `/sectors/accountancy-firms/` | accountancy firm loan UK | SEO | Iwoca | 4 |
| `/sectors/marketing-agencies/` | marketing agency loan UK | SEO | Iwoca, RBF | 4 |
| `/sectors/manufacturing/` | manufacturing business loan UK | SEO | Iwoca, asset finance | 2 |
| `/sectors/agriculture-farming/` | agriculture business loan UK | SEO | Oxbury, AMC | 3 |
| `/sectors/franchises/` | franchise business loan UK | AIO | Funding Circle, Iwoca | 2 |
| `/sectors/childcare-nurseries/` | nursery business loan UK | SEO | Iwoca | 4 |
| `/sectors/dry-cleaners/` | dry cleaner business loan UK | SEO | Iwoca | 4 |

---

## 6. Adjacent-vertical flex pages (the 20% allowed)

10 pages bridging the loans funnel into adjacent SMB finance.
Every page narratively ties back to "if a loan isn't right, here's
what is" or "while you're applying for a loan, also fix this".

| URL | Target query | Why on FundBiz | Commission path |
|---|---|---|---|
| `/adjacent/business-credit-cards/` | best business credit card UK 2026 | Cross-sell after a loan decline; many borrowers actually need a card line | Capital on Tap (£100+ approved), Awin |
| `/adjacent/business-credit-cards/after-loan-decline/` | business credit card after loan declined UK | Strong post-decline cross-sell | Capital on Tap, Capify card |
| `/adjacent/business-credit-cards/vs-business-loan/` | business credit card vs business loan | Decision-stage content with high commercial value | Capital on Tap |
| `/adjacent/business-bank-accounts/` | best business bank account UK 2026 | Lender-friendly account improves loan chances | Tide, Starling — Awin |
| `/adjacent/business-bank-accounts/for-borrowing/` | best business bank account for borrowing | Specific intent — open the right account before applying | Tide, Starling, Funding Circle's bank-account partners |
| `/adjacent/business-bank-accounts/tide-vs-starling/` | Tide vs Starling business account | High-volume head-to-head | Tide, Starling — both via Awin |
| `/adjacent/business-insurance/` | business insurance UK | Required by many lenders before drawdown | Superscript, Simply Business — Awin |
| `/adjacent/business-insurance/by-trade/` | business insurance for [trade] | Vertical insurance gates lender approval in some sectors | Superscript, Simply Business |
| `/adjacent/accountancy-software/` | accounting software for SME funding | Connecting Xero/QB to lenders speeds decisions | Xero, QuickBooks, FreeAgent direct |
| `/adjacent/accountancy-software/connect-for-faster-decisions/` | connect Xero to business lenders | Specific transactional intent | Xero, FundingXchange |
| `/adjacent/business-energy/` | switch business energy to fund growth | "Save here, borrow less" — soft cross-sell | Bionic, Love Energy Savings |
| `/adjacent/grants/` | UK business grants 2026 | Pre-loan content — "have you tried grants first?" | Affiliate to grant-listing services or pure citation |

---

## 7. Build sequence

### Wave 1 — Days 0–30 (post-decline foundation + Wave 1 sectors)
**~25 pages.** `/declined/` hub + 4 reason landers + 3 per-bank pages
+ `/declined/second-chance/` (9). `/sectors/` hub + 8 Wave 1 sector
landers (hospitality, restaurants, pubs, e-commerce, construction,
beauty, gyms, dental) (9). `/products/` hub + business loan + MCA
hubs (3). `/calculators/` hub + business loan calculator (2).
`/about/`, `/how-we-work/` trust pages (2).

- **Lever:** the post-decline funnel — biggest single revenue line —
  goes live with foundation content + lender chain. Wave 1 sectors
  cover the highest-CPL verticals.
- **Monetisation contracts to land:** Liberis direct, YouLend direct,
  Capify direct, 365 direct (these four make the post-decline
  waterfall work). Iwoca via Awin. Funding Circle via Awin.
- **Goal at end of Wave 1:** ~25 indexed pages, first AI Overview
  citations on `/declined/` and high-volume sector pages, first leads
  through placeholder forms (forms wired late-Wave-2 per user
  direction).

### Wave 2 — Days 31–60 (sector matrix + adjacent flex + remaining
declines)
**~30 pages.** Remaining 4 reason-decline landers + 2 more per-bank
pages + `/declined/after-bank-referral-scheme/` (7). 10 more sector
landers (cafés, hotels, retail, manufacturing, transport, vet,
pharmacy, recruitment, franchises, marketing) (10). 6 product pages
(unsecured, secured, asset finance, RBF, VAT loan, R&D advance) (6).
3 by-amount pages (£10k, £25k, £50k) (3). 4 adjacent flex pages
(business credit cards, bank accounts, insurance, accountancy
software) (4).

- **Lever:** breadth across sectors + first 20% adjacent-flex
  monetisation. Sector matrix hits enough verticals to dominate
  long-tail.
- **Monetisation contracts:** Wayflyer direct (e-commerce), Tide /
  Starling / Capital on Tap via Awin, Superscript / Simply Business
  via Awin, healthcare specialist lenders (Wesleyan, Praxis, Christie)
  direct.
- **Goal at end of Wave 2:** ~55 indexed pages, calculators wired,
  cross-link from BBL and CardMachines live, AI citations on every
  product page.

### Wave 3 — Days 61–90 (scale matrix + product depth + post-decline
detail)
**~30 pages.** Remaining sector landers (15+ — fill the long tail).
Remaining product pages. By-amount completed. Calculator stubs all
live. Guides expanded. Adjacent flex completed.

- **Lever:** matrix completion. By Day 90 we own the long-tail of
  sector + reason combinations.
- **Monetisation contracts:** Stripe Capital, Amazon Lending integration
  (referral), Bionic energy referral, Christie specialist healthcare
  finance.
- **Goal at end of Wave 3:** ~85 indexed pages, FundBiz-direct revenue
  £15–35k/month run-rate, post-decline funnel converting at 2%+ form-fill
  rate when forms are live.

---

## 8. Targets

Numbers grounded in the deep-dive sizing (£225–360k/yr post-decline TAM,
£430k/yr mid-scenario combined annual).

### 90 days
- **Indexed pages:** 85
- **Organic traffic:** 5k–12k monthly sessions
- **AI citations:** 60–180 per month
- **Form-fill leads (post-form-wire late-Wave-2):** 30–80 per month
- **Revenue:** £4k–£15k/month run-rate, dominated by post-decline (50%)
  + Wave 1 sectors (35%) + adjacent flex (15%)

### 6 months
- **Indexed pages:** 110
- **Organic traffic:** 18k–45k monthly sessions
- **AI citations:** 250–700 per month
- **Form-fill leads:** 150–400 per month
- **Revenue:** £20k–£50k/month run-rate

### 12 months
- **Indexed pages:** 120 (full sitemap)
- **Organic traffic:** 50k–120k monthly sessions
- **AI citations:** 1k–3k per month
- **Form-fill leads:** 400–900 per month
- **Revenue:** £36k/month low / £55k/month mid / £85k/month high =
  £430k–£1m/year (matches synthesis sizing)
- **Stretch:** ISO/Origination pre-arrangements with 2–3 lenders for
  white-labelled product flows (higher unit economics on a sub-segment)

---

## 9. Schema strategy summary

| Page type | Required schema | Notes |
|---|---|---|
| Sector lander | `Service` + `FAQPage` + `BreadcrumbList`; mention named lenders as `Organization` | The sector page is a "service offering" in schema terms. |
| Decline-help (`/declined/[reason]/`) | `Article` + `FAQPage` + `BreadcrumbList`; `mainEntity: FAQPage` | AIO-citation magnets. |
| Per-bank decline (`/declined/by-bank/*`) | `Article` + `FAQPage` + `BreadcrumbList` | Same pattern. |
| Product page | `LoanOrCredit` (where applicable) or `FinancialProduct` + `FAQPage` | UK MCAs are technically not a "Loan" in schema terms — use `FinancialProduct` with description. |
| Calculator stub | `WebApplication` + `FAQPage` | Even pre-form, declare it as a tool. |
| Guides / glossary | `Article` + `DefinedTerm` (per term) | Pure entity-graph fuel. |
| Adjacent flex | `Article` + `FAQPage` (cross-product comparisons get `Product` references) | Stays editorial, never `Service`. |
| Trust pages | `Organization` (sitewide) + `AboutPage` for `/about/` | Cross-site Organization decision pending — see open Q3. |
| Author / company | `Person` (placeholder) + `Organization` | Authors needed sitewide once named-author hire decision is made (Q in BBL plan). |

---

## 10. Open questions

1. **Domain.** `fundbiz.co.uk`? `fundbiz.uk`? Confirm before schema +
   sameAs go live. Same-week as the CardMachines domain decision.
2. **Eligibility-checker copy stance.** Operationally we restrict to
   Ltd / LLP / partnership of 4+. Confirm sole-trader deflection
   destination — Start Up Loans (BBB) referral, or a soft "we'll
   send you a guide" lead capture? Affects Q1 design when forms ship.
3. **Lender chain priority.** Default post-decline waterfall: Liberis →
   YouLend → Capify → 365 → Iwoca → BBB. Confirm or re-order based on
   negotiated CPL once contracts land.
4. **Cross-site Organization schema.** Single parent org with FundBiz +
   BBL + CardMachines + MarketInvoice + SEOCompare + WebsiteCo as
   `subOrganization`, or fully-separate brand graphs? Decision
   shared with the other site plans.
5. **`/lenders/` slug behaviour.** Currently set to 301-redirect to BBL
   `/reviews/`. Confirm — or do we keep a thin lender-list "where to
   apply" page on FundBiz so users on a transactional flow don't
   bounce to editorial mid-funnel?
6. **Post-decline matcher tool.** When Wave 3 ships, do we build the
   diagnose-the-decline interactive tool ourselves, or syndicate from
   a partner (e.g. iwoca's eligibility check)? In-house = better entity
   ownership, syndicated = faster.
7. **Adjacent flex limits.** Confirm we're not chasing business energy
   / accountancy software too hard — both fit in the 20% but neither
   converts to a loan revenue event. Worth keeping or kill?
8. **MarketInvoice cross-link convention.** When a sector page (e.g.
   `/sectors/recruitment-agencies/`) has a clear invoice-finance fit,
   what's the cross-link pattern? In-content link, sidebar block, or a
   dedicated `/products/invoice-finance-referral/` page that
   essentially redirects? Affects internal-link weight distribution.
