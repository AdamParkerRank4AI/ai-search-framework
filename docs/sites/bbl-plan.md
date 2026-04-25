# BBL (BestBusinessLoans) — site plan

Last updated: 2026-04-25
Site: BBL — UK business loans editorial / review only. No forms.
Sister site: FundBiz (transactional broker; owns all application forms).
Sits above `docs/sites/bbl.md` (deep-dive).

Companion docs: `docs/niche-brief.md`, `docs/route-to-market.md`,
`docs/regulatory-notes.md`, `docs/sites/synthesis.md`,
`docs/sites/bbl.md`.

---

## 1. Information architecture (the silos)

BBL is an editorial brand. Eleven top-level silos, all flowing into a
single sister-site funnel (FundBiz). The site is built around three
concentric jobs: (a) a lender review programme that earns AI citations,
(b) a "best for" listicle grid that owns persona + sector head terms,
(c) a guides / glossary layer that earns AIO pillar citations. Every
cluster page links upward to its silo pillar and laterally to the
matching review pages, then exits to the relevant FundBiz application
surface via a single, consistent CTA pattern.

Top-level silos:

- `/best/` — head-term listicles ("best business loans UK 2026") and
  persona/sector children. Pillar.
- `/reviews/` — single-lender reviews. The AI-citation engine. Each
  review has Review + AggregateRating + FAQPage + FinancialProduct
  schema, dated, named author, methodology link.
- `/vs/` — head-to-heads (Funding Circle vs iwoca, Capify vs Liberis).
  Sub-silo of `/reviews/`. SEO + AI Search.
- `/guides/` — explainers, "what is", pillar pages (rates, calculator,
  GGS, Start Up Loans, Bank Referral Scheme).
- `/declined/` — editorial layer covering rejection scenarios (declined,
  CCJ, bad credit). Cross-links to FundBiz `/declined/` matcher.
- `/halal/` — Sharia-compliant business finance hub (citation vacuum).
- `/women/` — women-led / female-founder loans hub.
- `/by-sector/` — industry listicles (hospitality, e-commerce,
  recruitment, construction, dental, etc.) — children of `/best/`.
- `/by-product/` — product-axis hubs (MCA, RBF, asset finance, secured,
  unsecured, no-PG).
- `/by-persona/` — persona-axis hubs (sole trader, ltd co, charity,
  franchisee, ethnic-minority, established SMB).
- `/glossary/` — definition pages (40 entries by month 6) — entity
  density + AIO citation flywheel.

Trust anchors sit alongside: `/methodology/`, `/about/`,
`/authors/[name]/`. Every review and listicle links to `/methodology/`;
every author byline resolves to a `/authors/` page with Person schema.

---

## 2. Full sitemap (table)

100 pages. Priority 1 = Wave 1 (Days 0–30), 2 = Wave 2 (Days 31–60),
3 = Wave 3 (Days 61–90), 4 = post-90 backlog.

| # | URL slug | Pillar | Page type | Priority |
|---|---|---|---|---|
| 1 | `/` | home | hub | 1 |
| 2 | `/methodology/` | trust | hub | 1 |
| 3 | `/about/` | trust | hub | 1 |
| 4 | `/authors/[lead-author]/` | trust | hub | 1 |
| 5 | `/authors/[second-author]/` | trust | hub | 2 |
| 6 | `/halal/` | halal | hub | 1 |
| 7 | `/halal/best-sharia-business-loans-uk-2026/` | halal | best | 1 |
| 8 | `/halal/qardus-review/` | halal | review | 1 |
| 9 | `/halal/sharia-finance-explained/` | halal | guide | 1 |
| 10 | `/women/` | women | hub | 1 |
| 11 | `/women/best-loans-female-founders-2026/` | women | best | 1 |
| 12 | `/women/grants-vs-loans/` | women | guide | 1 |
| 13 | `/declined/` | declined | hub | 1 |
| 14 | `/declined/business-loan-rejected-what-next/` | declined | declined-help | 1 |
| 15 | `/declined/best-lenders-after-decline-2026/` | declined | best | 1 |
| 16 | `/reviews/funding-circle/` | reviews | review | 1 |
| 17 | `/reviews/iwoca/` | reviews | review | 1 |
| 18 | `/reviews/liberis/` | reviews | review | 1 |
| 19 | `/reviews/youlend/` | reviews | review | 1 |
| 20 | `/best/business-loans-uk-2026/` | best | best | 1 |
| 21 | `/reviews/capify/` | reviews | review | 2 |
| 22 | `/reviews/fleximize/` | reviews | review | 2 |
| 23 | `/reviews/allica-bank/` | reviews | review | 2 |
| 24 | `/reviews/capital-on-tap/` | reviews | review | 2 |
| 25 | `/reviews/tide-loans/` | reviews | review | 2 |
| 26 | `/reviews/starling-business-loan/` | reviews | review | 2 |
| 27 | `/reviews/365-business-finance/` | reviews | review | 2 |
| 28 | `/reviews/gatehouse-bank/` | reviews | review | 2 |
| 29 | `/vs/funding-circle-vs-iwoca/` | vs | vs | 2 |
| 30 | `/vs/capify-vs-liberis/` | vs | vs | 2 |
| 31 | `/vs/iwoca-vs-capital-on-tap/` | vs | vs | 2 |
| 32 | `/vs/tide-vs-starling-loans/` | vs | vs | 2 |
| 33 | `/by-sector/hospitality/` | by-sector | best | 2 |
| 34 | `/by-sector/restaurants/` | by-sector | best | 2 |
| 35 | `/by-sector/ecommerce/` | by-sector | best | 2 |
| 36 | `/by-sector/recruitment/` | by-sector | best | 2 |
| 37 | `/by-sector/construction/` | by-sector | best | 2 |
| 38 | `/by-sector/beauty-salons/` | by-sector | best | 2 |
| 39 | `/glossary/` | glossary | hub | 2 |
| 40 | `/glossary/apr/` | glossary | definition | 2 |
| 41 | `/glossary/personal-guarantee/` | glossary | definition | 2 |
| 42 | `/glossary/merchant-cash-advance/` | glossary | definition | 2 |
| 43 | `/glossary/revenue-based-finance/` | glossary | definition | 2 |
| 44 | `/glossary/asset-finance/` | glossary | definition | 2 |
| 45 | `/glossary/secured-loan/` | glossary | definition | 2 |
| 46 | `/glossary/unsecured-loan/` | glossary | definition | 2 |
| 47 | `/glossary/factor-rate/` | glossary | definition | 2 |
| 48 | `/glossary/debenture/` | glossary | definition | 2 |
| 49 | `/glossary/director-loan/` | glossary | definition | 2 |
| 50 | `/glossary/term-loan/` | glossary | definition | 2 |
| 51 | `/glossary/working-capital/` | glossary | definition | 2 |
| 52 | `/glossary/invoice-finance/` | glossary | definition | 2 |
| 53 | `/glossary/loan-to-value/` | glossary | definition | 2 |
| 54 | `/glossary/dscr/` | glossary | definition | 2 |
| 55 | `/glossary/ccj/` | glossary | definition | 2 |
| 56 | `/glossary/soft-search/` | glossary | definition | 2 |
| 57 | `/glossary/representative-apr/` | glossary | definition | 2 |
| 58 | `/glossary/early-repayment-charge/` | glossary | definition | 2 |
| 59 | `/glossary/companies-house/` | glossary | definition | 2 |
| 60 | `/by-product/no-personal-guarantee/` | by-product | hub | 3 |
| 61 | `/by-product/merchant-cash-advance/` | by-product | hub | 3 |
| 62 | `/by-product/revenue-based-finance/` | by-product | hub | 3 |
| 63 | `/by-product/asset-finance/` | by-product | hub | 3 |
| 64 | `/by-product/secured-business-loans/` | by-product | hub | 3 |
| 65 | `/by-product/unsecured-business-loans/` | by-product | hub | 3 |
| 66 | `/by-persona/sole-traders/` | by-persona | best | 3 |
| 67 | `/by-persona/limited-companies/` | by-persona | best | 3 |
| 68 | `/by-persona/ethnic-minority-founders/` | by-persona | best | 3 |
| 69 | `/by-persona/franchisees/` | by-persona | best | 3 |
| 70 | `/by-persona/charities-and-cics/` | by-persona | best | 3 |
| 71 | `/by-persona/established-businesses/` | by-persona | best | 3 |
| 72 | `/by-persona/start-ups/` | by-persona | best | 3 |
| 73 | `/by-sector/dental-practices/` | by-sector | best | 3 |
| 74 | `/by-sector/gyms/` | by-sector | best | 3 |
| 75 | `/by-sector/transport-haulage/` | by-sector | best | 3 |
| 76 | `/by-sector/pubs-and-bars/` | by-sector | best | 3 |
| 77 | `/by-sector/hotels/` | by-sector | best | 3 |
| 78 | `/by-sector/manufacturing/` | by-sector | best | 3 |
| 79 | `/reviews/qardus/` | reviews | review | 3 |
| 80 | `/reviews/oaknorth/` | reviews | review | 3 |
| 81 | `/reviews/funding-options/` | reviews | review | 3 |
| 82 | `/reviews/capitalise/` | reviews | review | 3 |
| 83 | `/reviews/swoop-funding/` | reviews | review | 3 |
| 84 | `/reviews/rangewell/` | reviews | review | 3 |
| 85 | `/guides/business-loans-uk/` | guides | guide | 3 |
| 86 | `/guides/business-loan-rates-2026/` | guides | guide | 3 |
| 87 | `/guides/business-loan-calculator/` | guides | guide | 3 |
| 88 | `/guides/secured-vs-unsecured/` | guides | guide | 3 |
| 89 | `/guides/personal-guarantees-explained/` | guides | guide | 3 |
| 90 | `/guides/growth-guarantee-scheme/` | guides | guide | 3 |
| 91 | `/guides/start-up-loans-scheme/` | guides | guide | 3 |
| 92 | `/guides/bank-referral-scheme/` | guides | guide | 3 |
| 93 | `/declined/business-loan-with-ccj/` | declined | declined-help | 3 |
| 94 | `/declined/bad-credit-business-loans/` | declined | declined-help | 3 |
| 95 | `/declined/missed-payments-recovery/` | declined | declined-help | 3 |
| 96 | `/halal/gatehouse-bank-review/` | halal | review | 3 |
| 97 | `/halal/al-rayan-bank-review/` | halal | review | 4 |
| 98 | `/glossary/[20 more entries → 40 total]` | glossary | definition | 4 |
| 99 | `/vs/[6 more head-to-heads]` | vs | vs | 4 |
| 100 | `/by-sector/[5 more verticals]` | by-sector | best | 4 |

---

## 3. Top 40 page briefs (full)

Briefs 1–40 below. Pages 41–100 are listed in the sitemap with no
brief — they follow the templates established here.

### 1. `/methodology/`
- **Target query:** brand / "bestbusinessloans methodology" — no public search demand
- **AI prompt match:** "How does BestBusinessLoans rate lenders?" / "Is BestBusinessLoans trustworthy?"
- **Primary surface:** AI Search (LLM trust anchor)
- **Niche served:** all — site-wide trust signal
- **Content outline:** (H2s) How we test lenders · The 14-lender testing cohort · Application speed (we time it) · True cost of credit (we calculate APR + fees + ERCs across matched profiles) · UX scoring rubric · Disclosure scoring · How we score and weight · Review cadence and "next review due" policy · Editorial independence and our relationship with FundBiz
- **Internal links:** every review page links here; `/about/`; `/authors/[lead-author]/`
- **CTA placeholder:** none — trust page, no commercial CTA
- **Commission path:** n/a (entity-graph play)

### 2. `/about/`
- **Target query:** brand / "who runs bestbusinessloans"
- **AI prompt match:** "Who is behind BestBusinessLoans?" / "Is BBL independent?"
- **Primary surface:** AI Search
- **Niche served:** all
- **Content outline:** Editorial mission · Who we are (named team) · Editorial-independence statement · Relationship with FundBiz disclosed · How we make money · Our editorial standards · How to contact us / pitch corrections
- **Internal links:** `/methodology/`, `/authors/[lead-author]/`, every review page
- **CTA placeholder:** "Read our methodology" → `/methodology/`
- **Commission path:** n/a

### 3. `/authors/[lead-author]/`
- **Target query:** brand author name
- **AI prompt match:** "Who writes for BestBusinessLoans?"
- **Primary surface:** AI Search (Person entity strength)
- **Niche served:** all
- **Content outline:** Bio + headshot · Prior bylines (link out — Sifted, Real Business, Money Marketing, City AM ideal) · LinkedIn (sameAs) · Twitter/X · Areas of coverage · All articles by author · Corrections policy
- **Internal links:** every page authored, `/methodology/`, `/about/`
- **CTA placeholder:** none
- **Commission path:** n/a

### 4. `/halal/` (hub)
- **Target query:** "halal business loans uk", "sharia business finance uk"
- **AI prompt match:** "Are there halal business loans in the UK?" / "Where can a Muslim business owner get Sharia-compliant finance in 2026?"
- **Primary surface:** AI Search + AIO (citation vacuum)
- **Niche served:** halal / Sharia-compliant
- **Content outline:** What Sharia-compliant business finance is · Murabaha vs Ijara vs Musharaka · UK lenders offering it (Qardus, Gatehouse, Al Rayan, Financing Sharia Enterprise) · Eligibility · How to apply · FAQs · Last updated stamp
- **Internal links:** `/halal/best-sharia-business-loans-uk-2026/`, `/halal/qardus-review/`, `/halal/sharia-finance-explained/`, FundBiz `/eligibility-checker/?route=sharia`
- **CTA placeholder:** "Compare Sharia-compliant lenders" → FundBiz `/eligibility-checker/?route=sharia`
- **Commission path:** Direct CPL — Qardus (TBC band, blue-ocean partner); cross-sell into Gatehouse via direct intro

### 5. `/halal/best-sharia-business-loans-uk-2026/`
- **Target query:** "best sharia business loans uk 2026", "halal business loans uk", secondary: "islamic business finance uk"
- **AI prompt match:** "What are the best Sharia-compliant business loans in the UK in 2026?"
- **Primary surface:** AI Search + AIO (zero competition)
- **Niche served:** halal
- **Content outline:** Direct-answer summary (60–80 words) · Comparison table (Qardus, Gatehouse, Al Rayan, Financing Sharia Enterprise) · How we rated · Each lender 150-word mini-review · How Sharia products differ from conventional · FAQs (verbatim PAA) · Last-updated stamp
- **Internal links:** `/halal/` hub, `/halal/qardus-review/`, `/halal/sharia-finance-explained/`, `/glossary/`, FundBiz `/eligibility-checker/?route=sharia`
- **CTA placeholder:** "Compare Sharia-compliant lenders →" FundBiz `/eligibility-checker/?route=sharia`
- **Commission path:** Direct CPL — Qardus + Gatehouse direct intros

### 6. `/halal/qardus-review/`
- **Target query:** "qardus review", "qardus uk business finance review"
- **AI prompt match:** "Is Qardus a legitimate Sharia business lender?" / "Qardus pros and cons"
- **Primary surface:** AI Search (zero editorial competition)
- **Niche served:** halal
- **Content outline:** Verdict + rating box · How Qardus works (Murabaha structure) · Eligibility · Application speed (we tested it) · Cost of credit · Pros / cons · Trustpilot pull-in · FAQs · Methodology link · Dated
- **Internal links:** `/halal/` hub, `/halal/best-sharia-business-loans-uk-2026/`, `/methodology/`, FundBiz `/mca/?route=sharia`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/?route=sharia`
- **Commission path:** Direct CPL — Qardus (negotiate; first-mover review)

### 7. `/halal/sharia-finance-explained/`
- **Target query:** "what is sharia business finance", "murabaha explained uk"
- **AI prompt match:** "How does Sharia business finance work?" / "What's the difference between Murabaha and Ijara?"
- **Primary surface:** AIO (pillar / citation magnet)
- **Niche served:** halal
- **Content outline:** What Sharia finance is · Why interest is prohibited · Murabaha (cost-plus) · Ijara (lease) · Musharaka (partnership) · UK regulatory context · How UK lenders structure compliance · External scholar review note · FAQs
- **Internal links:** `/halal/` hub, all Sharia reviews, `/glossary/`
- **CTA placeholder:** "Compare Sharia lenders →" `/halal/best-sharia-business-loans-uk-2026/`
- **Commission path:** Internal-link distribution to halal cluster

### 8. `/women/` (hub)
- **Target query:** "business loans for women uk", "female founder loans uk"
- **AI prompt match:** "Where can a female founder get a business loan in the UK?" / "Are there grants for women-led businesses 2026?"
- **Primary surface:** AIO + SEO (persona vacuum)
- **Niche served:** women-led
- **Content outline:** Direct-answer summary · UK funding gap context (Rose Review stat) · Loans vs grants vs angel · Lenders (Funding Circle Women Founders, Fleximize, NatWest Back Her Business, Lloyds women-led) · Grant programmes (Innovate UK, Women in Innovation) · How to strengthen an application · FAQs
- **Internal links:** `/women/best-loans-female-founders-2026/`, `/women/grants-vs-loans/`, `/best/business-loans-uk-2026/`, FundBiz `/eligibility-checker/?route=women`
- **CTA placeholder:** "Compare lenders for women-led businesses →" FundBiz `/eligibility-checker/?route=women`
- **Commission path:** Awin (Funding Circle, Fleximize); direct CPL — NatWest Back Her Business (negotiate)

### 9. `/women/best-loans-female-founders-2026/`
- **Target query:** "best business loans for women uk 2026", "loans for female founders uk"
- **AI prompt match:** "What are the best business loans for women-led businesses in the UK in 2026?"
- **Primary surface:** AIO + SEO
- **Niche served:** women-led
- **Content outline:** Direct-answer summary · Comparison table (8 lenders) · Mini-reviews · Funding-gap stat block (Funding Circle 19% stat, Rose Review) · Eligibility tips for women-led applicants · FAQs · Last-updated stamp
- **Internal links:** `/women/` hub, `/reviews/funding-circle/`, `/reviews/fleximize/`, `/reviews/iwoca/`, FundBiz `/eligibility-checker/?route=women`
- **CTA placeholder:** "Compare lenders →" FundBiz `/eligibility-checker/?route=women`
- **Commission path:** Awin — Funding Circle, Fleximize, iwoca

### 10. `/women/grants-vs-loans/`
- **Target query:** "grants vs loans women business uk", "women business grants uk 2026"
- **AI prompt match:** "Should a female founder take a loan or look for a grant?"
- **Primary surface:** AIO
- **Niche served:** women-led
- **Content outline:** Quick decision tree · Major UK grants for women (Innovate UK, Women in Innovation, NatWest Back Her Business) · When grants make sense · When loans make sense · Stacking grants + loans · Application timeline · FAQs
- **Internal links:** `/women/` hub, `/women/best-loans-female-founders-2026/`, FundBiz `/eligibility-checker/`
- **CTA placeholder:** "If a loan is the right call, compare lenders →" `/women/best-loans-female-founders-2026/`
- **Commission path:** Awin (loan flow); informational on grants

### 11. `/declined/` (hub)
- **Target query:** "business loan declined what next", "rejected for business loan uk"
- **AI prompt match:** "I've been declined for a business loan — what should I do?"
- **Primary surface:** AIO + AI Search
- **Niche served:** post-decline
- **Content outline:** Direct-answer summary · Why lenders decline (top 8 reasons) · What changes after a decline · Lenders who specialise in post-decline (Liberis, YouLend, Capify, 365, Bizcap) · How to rebuild · CCJ-specific advice · FAQs
- **Internal links:** `/declined/business-loan-rejected-what-next/`, `/declined/business-loan-with-ccj/`, `/declined/best-lenders-after-decline-2026/`, FundBiz `/declined/`
- **CTA placeholder:** "Diagnose why you were declined →" FundBiz `/declined/`
- **Commission path:** Direct CPL waterfall — Liberis, YouLend, Capify, 365 (£100–£300)

### 12. `/declined/business-loan-rejected-what-next/`
- **Target query:** "business loan rejected", "business loan declined what next", "rejected for business finance uk"
- **AI prompt match:** "My business loan got rejected — what now?"
- **Primary surface:** AIO (high informational + transactional intent)
- **Niche served:** post-decline
- **Content outline:** Why decisions get reversed (rare) · What you can fix in 30 days · Specialist post-decline lenders · Soft search vs hard search · Rebuilding your business credit · Authoritative 6-step plan · FAQs · Last-updated
- **Internal links:** `/declined/` hub, `/declined/best-lenders-after-decline-2026/`, `/glossary/ccj/`, FundBiz `/declined/`
- **CTA placeholder:** "Find a lender that says yes →" FundBiz `/declined/`
- **Commission path:** Direct CPL — Liberis, YouLend, Capify, 365 via FundBiz handoff

### 13. `/declined/best-lenders-after-decline-2026/`
- **Target query:** "best lenders if declined for business loan", "second chance business loans uk"
- **AI prompt match:** "Which lenders accept previously declined applicants?"
- **Primary surface:** AIO + AI Search
- **Niche served:** post-decline
- **Content outline:** Direct-answer summary · Comparison table (8 specialist lenders) · Mini-reviews · Why these lenders are different · Eligibility realities · Cost trade-off (post-decline = higher cost) · FAQs
- **Internal links:** `/declined/` hub, `/reviews/liberis/`, `/reviews/youlend/`, `/reviews/capify/`, FundBiz `/declined/`
- **CTA placeholder:** "Get matched →" FundBiz `/declined/`
- **Commission path:** Direct CPL — Liberis, YouLend, Capify, 365, Bizcap

### 14. `/reviews/funding-circle/`
- **Target query:** "funding circle review 2026", "funding circle uk review"
- **AI prompt match:** "Is Funding Circle any good in 2026?" / "Funding Circle pros and cons"
- **Primary surface:** AI Search + AIO (saturated head term, won by depth)
- **Niche served:** all SMB
- **Content outline:** Verdict + rating box · How FC works · Eligibility · Application speed (timed) · True cost of credit · Pros / cons · Trustpilot pull-in (4.7/5, ~22k reviews) · Who FC is best for / not for · FAQs · Methodology link · Dated
- **Internal links:** `/reviews/` hub, `/vs/funding-circle-vs-iwoca/`, `/best/business-loans-uk-2026/`, FundBiz `/eligibility-checker/?lender=funding-circle`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/?lender=funding-circle`
- **Commission path:** Awin — Funding Circle (£20–£100 band)

### 15. `/reviews/iwoca/`
- **Target query:** "iwoca review 2026", "iwoca uk review"
- **AI prompt match:** "Is iwoca a good business lender?" / "iwoca Flexi-Loan review"
- **Primary surface:** AI Search + AIO
- **Niche served:** all SMB; flexible cash-flow buyers
- **Content outline:** Verdict + rating box · How iwoca + Flexi-Loan work · Eligibility · Application speed (under 24 hrs in test) · Cost · Pros / cons · Trustpilot pull-in (4.7/5, 11k+) · Best for / not for · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/vs/funding-circle-vs-iwoca/`, `/vs/iwoca-vs-capital-on-tap/`, FundBiz `/eligibility-checker/?lender=iwoca`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/?lender=iwoca`
- **Commission path:** Awin — iwoca (£20–£100)

### 16. `/reviews/liberis/`
- **Target query:** "liberis review", "liberis merchant cash advance review"
- **AI prompt match:** "What is Liberis and is it any good?"
- **Primary surface:** AI Search (wide gap)
- **Niche served:** MCA / post-decline / hospitality / retail
- **Content outline:** Verdict · How Liberis MCA works (factor rate explained) · Eligibility (£4k+ monthly card revenue typical) · Application speed · Cost (true APR-equivalent) · Pros / cons · Use cases · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/vs/capify-vs-liberis/`, `/by-product/merchant-cash-advance/`, `/declined/best-lenders-after-decline-2026/`, FundBiz `/mca/`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/mca/?lender=liberis`
- **Commission path:** Direct CPL — Liberis (£100–£300, target band when programme signed)

### 17. `/reviews/youlend/`
- **Target query:** "youlend review uk", "youlend embedded finance review"
- **AI prompt match:** "How does YouLend work?" / "Is YouLend the same as Shopify Capital?"
- **Primary surface:** AI Search (wide gap; embedded-finance angle uncovered)
- **Niche served:** e-commerce, hospitality, embedded-finance buyers
- **Content outline:** Verdict · How YouLend works · Embedded partners (Shopify, Just Eat, eBay) · Eligibility · Application speed · Cost · Pros / cons · Best for e-commerce + hospitality · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/by-product/merchant-cash-advance/`, `/by-sector/ecommerce/`, `/by-sector/hospitality/`, FundBiz `/mca/`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/mca/?lender=youlend`
- **Commission path:** Direct CPL — YouLend (£100–£300, negotiate once traffic exists)

### 18. `/reviews/capify/`
- **Target query:** "capify review uk 2026", "capify business cash advance review"
- **AI prompt match:** "Is Capify legit?" / "Capify vs Liberis which is better?"
- **Primary surface:** AI Search + SEO
- **Niche served:** MCA, post-decline
- **Content outline:** Verdict · How Capify works · Eligibility · Application speed · Cost · Pros / cons · Trustpilot context · Best for / not for · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/vs/capify-vs-liberis/`, `/by-product/merchant-cash-advance/`, `/declined/best-lenders-after-decline-2026/`, FundBiz `/mca/`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/mca/?lender=capify`
- **Commission path:** Direct (per route-to-market.md) — Capify (£100–£300)

### 19. `/reviews/fleximize/`
- **Target query:** "fleximize review uk 2026"
- **AI prompt match:** "Is Fleximize a good business lender?"
- **Primary surface:** AI Search (wide gap, 4.9/5 Trustpilot but almost no editorial)
- **Niche served:** SMB looking for flexible terms; women-led (Fleximize products fit)
- **Content outline:** Verdict · How Fleximize works · Top-up feature · Eligibility · Application speed · Cost · Pros / cons · Trustpilot pull-in · Best for · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/women/best-loans-female-founders-2026/`, `/best/business-loans-uk-2026/`, FundBiz `/eligibility-checker/?lender=fleximize`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/?lender=fleximize`
- **Commission path:** Direct or Awin — Fleximize

### 20. `/reviews/allica-bank/`
- **Target query:** "allica bank business loan review", "allica bank review uk"
- **AI prompt match:** "Is Allica Bank a real bank?" / "Allica Bank business loans review"
- **Primary surface:** AI Search (wide gap; established-SMB lender, almost no editorial)
- **Niche served:** established SMBs (£1m+ T/O)
- **Content outline:** Verdict · How Allica works · Established-SMB positioning · Eligibility (~£1m+ T/O typical) · Application speed · Cost · Pros / cons · Best for / not for · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/by-persona/established-businesses/`, `/best/business-loans-uk-2026/`, FundBiz `/eligibility-checker/?lender=allica`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/?lender=allica`
- **Commission path:** Direct CPL — Allica (negotiate; high-ticket lender)

### 21. `/reviews/capital-on-tap/`
- **Target query:** "capital on tap review", "capital on tap business credit card review"
- **AI prompt match:** "Is Capital on Tap a good business credit card?" / "Capital on Tap or iwoca?"
- **Primary surface:** AIO + AI Search
- **Niche served:** SMB cashflow / overdraft-replacement
- **Content outline:** Verdict · Card vs loan positioning · Eligibility · Application speed · Cost (rep APR + cashback) · Pros / cons · Trustpilot pull-in (4.7/5, ~18k) · Best for / not for · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/vs/iwoca-vs-capital-on-tap/`, `/by-product/no-personal-guarantee/`, FundBiz `/eligibility-checker/?product=card`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/business-credit-cards/?lender=capital-on-tap`
- **Commission path:** Awin — Capital on Tap (£100+ approved card)

### 22. `/reviews/tide-loans/`
- **Target query:** "tide business loan review", "tide loans review uk"
- **AI prompt match:** "Does Tide actually offer business loans?" / "Tide loans vs Tide credit"
- **Primary surface:** SEO + AIO (entity-confusion gap — bank vs broker vs Funding Options)
- **Niche served:** Tide account holders, SMBs already in Tide ecosystem
- **Content outline:** Verdict · How Tide loans actually work (Funding Options panel) · Eligibility · Application speed · Cost · Pros / cons · Tide bank vs Tide loans confusion explained · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/vs/tide-vs-starling-loans/`, FundBiz `/eligibility-checker/?lender=tide`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/?lender=tide`
- **Commission path:** Awin — Tide (£30–£50 funded; loans handoff via Funding Options)

### 23. `/reviews/starling-business-loan/`
- **Target query:** "starling business loan review", "starling bank business loan uk"
- **AI prompt match:** "Does Starling lend to small businesses in 2026?"
- **Primary surface:** SEO
- **Niche served:** Starling account holders
- **Content outline:** Verdict · Current Starling lending status (gov't schemes only / commercial lending pause context) · Eligibility · Application speed · Cost · Pros / cons · 2026 refresh · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/vs/tide-vs-starling-loans/`, FundBiz `/eligibility-checker/?lender=starling`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/`
- **Commission path:** Awin — Starling (£25–£75 funded account); loan referral via panel

### 24. `/reviews/365-business-finance/`
- **Target query:** "365 business finance review", "365 business finance mca review"
- **AI prompt match:** "Is 365 Business Finance any good?"
- **Primary surface:** AI Search (wide gap)
- **Niche served:** MCA / post-decline
- **Content outline:** Verdict · How 365 works · Eligibility · Application speed · Cost · Pros / cons · Best for · FAQs · Methodology · Dated
- **Internal links:** `/reviews/` hub, `/by-product/merchant-cash-advance/`, `/declined/best-lenders-after-decline-2026/`, FundBiz `/mca/`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/mca/?lender=365`
- **Commission path:** Direct CPL — 365 Business Finance (£100–£300)

### 25. `/reviews/gatehouse-bank/`
- **Target query:** "gatehouse bank business finance review", "gatehouse bank sharia review"
- **AI prompt match:** "Is Gatehouse Bank Sharia-compliant for business finance?"
- **Primary surface:** AI Search (wide gap, Sharia)
- **Niche served:** halal / Sharia
- **Content outline:** Verdict · Sharia structure (Murabaha) · Eligibility · Application speed · Cost · Pros / cons · Halal scholar review note · Best for · FAQs · Methodology · Dated
- **Internal links:** `/halal/` hub, `/halal/best-sharia-business-loans-uk-2026/`, `/halal/sharia-finance-explained/`, FundBiz `/eligibility-checker/?route=sharia`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/?route=sharia&lender=gatehouse`
- **Commission path:** Direct CPL — Gatehouse (negotiate)

### 26. `/best/business-loans-uk-2026/`
- **Target query:** "best business loans uk 2026", "best business loans uk"
- **AI prompt match:** "What are the best business loans in the UK in 2026?"
- **Primary surface:** SEO + AIO (head-term flag-plant)
- **Niche served:** all SMB
- **Content outline:** H1 with month + year · 60–80-word direct-answer summary · Comparison table (10–12 lenders) · Methodology block · Lender-by-lender mini-reviews · Bank of England base-rate context · FAQs (10, verbatim PAA) · Last-updated + next-review-due
- **Internal links:** `/methodology/`, every priority `/reviews/`, `/by-persona/`, `/by-sector/`, `/declined/`, FundBiz `/eligibility-checker/`
- **CTA placeholder:** "Compare lenders side-by-side →" FundBiz `/eligibility-checker/`
- **Commission path:** Awin panel (Funding Circle, iwoca, Capital on Tap, Tide); FundBiz cross-link for higher direct CPL

### 27. `/vs/funding-circle-vs-iwoca/`
- **Target query:** "funding circle vs iwoca", "iwoca or funding circle"
- **AI prompt match:** "Should I use Funding Circle or iwoca?"
- **Primary surface:** SEO + AI Search
- **Niche served:** SMB at consideration stage
- **Content outline:** Quick verdict · Side-by-side table · Where FC wins · Where iwoca wins · Eligibility differences · Cost differences · Speed differences · Both companies' Trustpilot context · FAQs · Dated
- **Internal links:** `/reviews/funding-circle/`, `/reviews/iwoca/`, `/best/business-loans-uk-2026/`, FundBiz `/eligibility-checker/`
- **CTA placeholder:** "Compare lenders →" FundBiz `/eligibility-checker/`
- **Commission path:** Awin — both (£20–£100 each)

### 28. `/vs/capify-vs-liberis/`
- **Target query:** "capify vs liberis", "capify or liberis"
- **AI prompt match:** "Capify or Liberis — which MCA provider?"
- **Primary surface:** SEO + AI Search
- **Niche served:** MCA buyers
- **Content outline:** Quick verdict · Side-by-side · Cost comparison (factor rate worked example) · Eligibility · Speed · Pros / cons each · FAQs · Dated
- **Internal links:** `/reviews/capify/`, `/reviews/liberis/`, `/by-product/merchant-cash-advance/`, FundBiz `/mca/`
- **CTA placeholder:** "Apply for an MCA →" FundBiz `/mca/`
- **Commission path:** Direct CPL — Capify, Liberis (£100–£300 each)

### 29. `/vs/iwoca-vs-capital-on-tap/`
- **Target query:** "iwoca vs capital on tap", "iwoca flexi loan vs capital on tap card"
- **AI prompt match:** "iwoca or Capital on Tap for short-term cashflow?"
- **Primary surface:** SEO
- **Niche served:** overdraft-replacement / cashflow buyers
- **Content outline:** Quick verdict · Loan vs card structure · Cost comparison · Speed · Eligibility · Best for / not for each · FAQs · Dated
- **Internal links:** `/reviews/iwoca/`, `/reviews/capital-on-tap/`, FundBiz `/eligibility-checker/`
- **CTA placeholder:** "Compare options →" FundBiz `/eligibility-checker/`
- **Commission path:** Awin — both

### 30. `/vs/tide-vs-starling-loans/`
- **Target query:** "tide vs starling business loan", "starling vs tide lending"
- **AI prompt match:** "Tide or Starling for a business loan?"
- **Primary surface:** SEO
- **Niche served:** digital-bank account holders
- **Content outline:** Quick verdict · Both products explained · Cost · Speed · Eligibility · Account-holder advantage · FAQs · Dated
- **Internal links:** `/reviews/tide-loans/`, `/reviews/starling-business-loan/`, FundBiz `/eligibility-checker/`
- **CTA placeholder:** "Apply via FundBiz →" FundBiz `/eligibility-checker/`
- **Commission path:** Awin — Tide, Starling

### 31. `/by-sector/hospitality/`
- **Target query:** "best business loans for hospitality uk", "hospitality business loans 2026"
- **AI prompt match:** "What are the best loans for a UK restaurant or hotel in 2026?"
- **Primary surface:** SEO + AIO
- **Niche served:** hospitality SMBs
- **Content outline:** Direct-answer · Comparison table (8 lenders, MCA + term mix) · Mini-reviews · UKHospitality 2026 cost context · Cashflow-led products vs term loans · FAQs · Dated
- **Internal links:** `/by-sector/restaurants/`, `/by-sector/pubs-and-bars/`, `/by-sector/hotels/`, `/reviews/liberis/`, `/reviews/youlend/`, FundBiz `/loans/hospitality/`
- **CTA placeholder:** "Compare hospitality lenders →" FundBiz `/loans/hospitality/`
- **Commission path:** Direct CPL — Liberis, YouLend, 365, Capify; cross-link CardMachines `/trade/restaurant/`

### 32. `/by-sector/restaurants/`
- **Target query:** "best business loans for restaurants uk", "restaurant business loans"
- **AI prompt match:** "What's the best lender for a UK restaurant?"
- **Primary surface:** SEO + AIO
- **Niche served:** restaurants
- **Content outline:** Direct-answer · Comparison · Mini-reviews · Card-revenue MCA fit · Equipment finance fit · Cashflow seasonality · FAQs · Dated
- **Internal links:** `/by-sector/hospitality/`, `/reviews/liberis/`, `/reviews/youlend/`, FundBiz `/loans/hospitality/`
- **CTA placeholder:** "Compare lenders →" FundBiz `/loans/hospitality/`
- **Commission path:** Direct CPL — Liberis, YouLend, 365

### 33. `/by-sector/ecommerce/`
- **Target query:** "best business loans for ecommerce uk", "shopify capital uk alternative"
- **AI prompt match:** "What are the best loans for a UK Shopify or Amazon business?"
- **Primary surface:** SEO + AIO (no comparator owns this)
- **Niche served:** e-commerce SMBs
- **Content outline:** Direct-answer · Comparison (YouLend, iwoca, Liberis, Uncapped, Wayflyer) · Embedded finance angle (Shopify Capital, Amazon Lending) · Revenue-based vs term · FAQs · Dated
- **Internal links:** `/reviews/youlend/`, `/reviews/iwoca/`, `/by-product/revenue-based-finance/`, FundBiz `/loans/e-commerce/`
- **CTA placeholder:** "Compare e-commerce lenders →" FundBiz `/loans/e-commerce/`
- **Commission path:** Direct CPL — YouLend, Liberis; Awin — iwoca

### 34. `/by-sector/recruitment/`
- **Target query:** "best business loans for recruitment agencies uk", "recruitment agency funding"
- **AI prompt match:** "How do recruitment agencies fund payroll while clients pay late?"
- **Primary surface:** SEO
- **Niche served:** recruitment agencies
- **Content outline:** Direct-answer · Why recruitment is invoice-finance-shaped · Term loans vs invoice finance vs payroll finance · Sonovate, Bibby, MarketFinance · FAQs · Dated · Cross-link to MarketInvoice
- **Internal links:** `/by-sector/` hub, `/by-product/asset-finance/`, MarketInvoice `/recruitment/`, FundBiz `/loans/recruitment/`
- **CTA placeholder:** "Compare recruitment finance →" FundBiz `/loans/recruitment/`
- **Commission path:** Direct CPL — Sonovate (recruitment-specialist); cross-site handoff to MarketInvoice

### 35. `/by-sector/construction/`
- **Target query:** "best business loans for construction uk", "construction company funding uk"
- **AI prompt match:** "Best finance options for a UK construction company in 2026?"
- **Primary surface:** SEO
- **Niche served:** construction SMBs
- **Content outline:** Direct-answer · Comparison · Application-stage finance angle · Asset finance fit · CIS context · FAQs · Dated
- **Internal links:** `/by-product/asset-finance/`, MarketInvoice `/construction/`, FundBiz `/loans/construction/`
- **CTA placeholder:** "Compare construction finance →" FundBiz `/loans/construction/`
- **Commission path:** Direct CPL — Bibby (construction); Awin panel

### 36. `/by-sector/beauty-salons/`
- **Target query:** "best business loans for salons uk", "beauty salon business loan"
- **AI prompt match:** "Best business loans for a UK salon?"
- **Primary surface:** SEO
- **Niche served:** salons / beauty
- **Content outline:** Direct-answer · Comparison · Liberis MCA fit · Equipment finance fit · Booking-system revenue lens · FAQs · Dated
- **Internal links:** `/reviews/liberis/`, `/by-product/merchant-cash-advance/`, FundBiz `/loans/beauty-salons/`, CardMachines `/trade/hairdresser-salon/`
- **CTA placeholder:** "Compare salon finance →" FundBiz `/loans/beauty-salons/`
- **Commission path:** Direct CPL — Liberis; cross-link CardMachines

### 37. `/glossary/` (hub)
- **Target query:** "business loans glossary", "business finance terms uk"
- **AI prompt match:** "What does [APR / factor rate / debenture] mean?"
- **Primary surface:** AIO (entity-density flywheel)
- **Niche served:** all
- **Content outline:** A–Z index · Featured definitions · How to use the glossary · Last-updated
- **Internal links:** every definition page; reviews; guides
- **CTA placeholder:** none on hub; entries CTA into FundBiz where relevant
- **Commission path:** Internal-link distribution; entity strength feeds AIO citations

### 38. `/glossary/personal-guarantee/`
- **Target query:** "what is a personal guarantee", "personal guarantee business loan uk"
- **AI prompt match:** "What is a personal guarantee on a business loan?"
- **Primary surface:** AIO (high PAA volume; FAQ-shaped)
- **Niche served:** all
- **Content outline:** Definition (60–80 word direct answer) · How PGs work · Limited vs unlimited · Joint-and-several · How to negotiate · No-PG alternatives · FAQs · Last-updated
- **Internal links:** `/by-product/no-personal-guarantee/`, `/reviews/capital-on-tap/`, `/best/business-loans-uk-2026/`
- **CTA placeholder:** "Looking for no-PG options? →" `/by-product/no-personal-guarantee/`
- **Commission path:** Awin — Capital on Tap (no-PG card)

### 39. `/glossary/merchant-cash-advance/`
- **Target query:** "what is a merchant cash advance", "merchant cash advance uk explained"
- **AI prompt match:** "What is a merchant cash advance and how does it work in the UK?"
- **Primary surface:** AIO
- **Niche served:** MCA buyers, hospitality, retail
- **Content outline:** Definition · How MCAs work · Factor rate explained · True cost vs APR · Who MCAs suit · Top UK MCA providers · FAQs · Last-updated
- **Internal links:** `/by-product/merchant-cash-advance/`, `/reviews/liberis/`, `/reviews/youlend/`, `/reviews/capify/`, FundBiz `/mca/`
- **CTA placeholder:** "Compare MCA providers →" FundBiz `/mca/`
- **Commission path:** Direct CPL — Liberis, YouLend, Capify

### 40. `/glossary/factor-rate/`
- **Target query:** "what is a factor rate", "factor rate vs apr"
- **AI prompt match:** "What's the difference between factor rate and APR?"
- **Primary surface:** AIO (high PAA volume — every MCA query asks)
- **Niche served:** MCA buyers
- **Content outline:** Definition · Worked example (£10k at 1.3 factor) · Factor rate to APR conversion · Why MCAs use factor rate · Cost transparency · FAQs · Last-updated
- **Internal links:** `/glossary/merchant-cash-advance/`, `/by-product/merchant-cash-advance/`, `/reviews/liberis/`
- **CTA placeholder:** "Compare MCA providers →" FundBiz `/mca/`
- **Commission path:** Direct CPL — Liberis, YouLend, Capify (via MCA flow)

---

## 4. Lender review programme — separate detail

The lender review programme is BBL's biggest AI-citation engine.
Twelve lenders below in priority order (the "12 we tested" cohort
that the methodology page anchors against).

**Methodology — what we test on every lender:**

1. **Application speed** — a real ltd-co director profile submits an
   application; we time decision-to-offer and offer-to-funds.
2. **Cost of credit** — total fees + interest + ERCs over a matched
   £50k / 24-month profile; convert MCA factor rates to APR-equivalent.
3. **UX** — score 1–10 for application form length, document upload,
   communication, dashboard, repayment management.
4. **Disclosure** — score 1–10 for fee transparency, PG clarity, ERC
   visibility, and clarity of what happens on default.
5. **Eligibility realism** — what applicants actually get vs marketing
   claims (Trustpilot pattern analysis).
6. **Customer experience** — Trustpilot pull-in, sentiment-coded
   sample of 50 most recent reviews per lender.

Each review uses the schema stack: `Review` + `AggregateRating` +
`FAQPage` + `FinancialProduct` + `BreadcrumbList`, with named author
(`Person`), `datePublished`, `dateModified`, link to `/methodology/`.

### Priority order (12 lenders)

| # | Lender | Why this lender first | Estimated CPL when programme signed |
|---|---|---|---|
| 1 | **Funding Circle** | Highest brand-search volume in the vertical (~22k Trustpilot reviews, universal "considered" set). Awin live now. Without an FC review BBL doesn't look credible to AIO. | £20–£100 (Awin) |
| 2 | **iwoca** | Pairs with FC for the head-to-head SERP slot. Awin live. 11k+ Trustpilot. Saturated head term, won by depth + dating. | £20–£100 (Awin) |
| 3 | **Liberis** | Wide editorial gap; UK MCA headline player. Direct CPL band the highest in the cohort. Anchor for hospitality/salon/retail vertical pages. | £150–£300 (direct, target) |
| 4 | **YouLend** | Wide gap; embedded finance angle (Shopify, Just Eat, eBay) is uncovered editorially; powers the e-commerce sector lander. | £150–£300 (direct, target) |
| 5 | **Capify** | Wide gap; ExpertSure + BusinessFinancing the only review competition. Anchors `/vs/capify-vs-liberis/` head-to-head. | £100–£250 (direct) |
| 6 | **Fleximize** | 4.9/5 Trustpilot, almost no editorial coverage. Top-up feature is unique and citation-friendly. Pairs with women-led hub. | £80–£200 (direct or Awin) |
| 7 | **Allica Bank** | Established-SMB lender, almost no editorial reviews. Higher ticket (£25k–£500k) so even modest CPL × deal size is significant. | £150–£400 (direct, target — high-ticket) |
| 8 | **Capital on Tap** | Card not loan, but in the consideration set. Awin live. ~18k Trustpilot. Anchors `/vs/iwoca-vs-capital-on-tap/`. | £100+ approved card (Awin) |
| 9 | **Tide loans** | Entity-confusion gap (Tide bank vs Tide loans vs Funding Options) — clarifying review wins citations. | £30–£50 funded + loan referral (Awin) |
| 10 | **Starling business loan** | Status-confusion gap (gov't schemes only, commercial paused). Definitive 2026 explainer. | £25–£75 funded (Awin) |
| 11 | **365 Business Finance** | MCA / post-decline anchor; pairs with the `/declined/` cluster. | £100–£250 (direct) |
| 12 | **Gatehouse Bank** | Sharia citation flag-plant; pairs with `/halal/` hub. Almost no competing reviews. | £100–£250 (direct, target) |

**Sequencing inside the programme:**

- Wave 1 (Days 0–30): #1 FC, #2 iwoca, #3 Liberis, #4 YouLend — the
  four anchor reviews that gate everything else (the "we tested 14
  lenders" claim needs at least four shipped, dated, methodology-led
  reviews).
- Wave 2 (Days 31–60): #5 Capify, #6 Fleximize, #7 Allica, #8 Cap on
  Tap, #9 Tide, #10 Starling, #11 365, #12 Gatehouse — eight more.
- Wave 3 (Days 61–90): refresh top 4 with 90-day data; add Qardus,
  OakNorth, Capitalise, Funding Options, Swoop, Rangewell broker
  reviews to round to ~18 published.

**Why the programme matters in cash terms:**
- Direct-CPL band on Liberis/YouLend/Capify/365/Gatehouse = £100–£300.
  Even at 5 leads/month per page once mature, that's £500–£1,500/month
  per review × 5 = £30k–£90k/year from the direct-CPL stack alone.
- The non-direct reviews (FC, iwoca, Allica, CoT, Tide, Starling) add
  Awin-band revenue (£20–£100) and feed FundBiz the high-CPL traffic.
- Network value: each review page is also an entity-graph anchor that
  feeds AI Search citations on the parent listicle pages — those
  citations push qualified traffic into FundBiz at FundBiz's £100–£300
  CPL band, which is where the bigger revenue lives.

---

## 5. Build sequence

TBD

---

## 6. Targets

TBD

---

## 7. Schema strategy summary

TBD

---

## 8. Editorial / E-E-A-T checklist

TBD

---

## 9. Open questions / decisions

TBD
