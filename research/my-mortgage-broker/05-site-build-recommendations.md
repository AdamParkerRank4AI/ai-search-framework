# 05 — Site Build Recommendations (Rank4AI Five Signal Model)

This file translates the audit into a build plan, organised by the five signal layers. It is intentionally opinionated: the merger window is short, and the framework penalises partial implementation.

## Signal 01 — Identity Clarity

**Before any content is written, lock the entity fact block** (see `01-entity-audit.md`). Nothing ships until:

- [ ] Companies House registered office for 09296120 is confirmed and matches the trading address, or both are clearly labelled.
- [ ] FCA Register entry for FRN 795866 is captured verbatim; the website's regulatory statement quotes it word-for-word.
- [ ] The "over 15 years" claim is restated as an attributable composite (adviser-years, trading-years, founder-years).
- [ ] RB Financial Advisers Ltd's post-merger status (dormant, being struck off, or retained subsidiary) is documented on a merger page.

Site structure that serves Signal 01:

- `/` — homepage, one-sentence entity statement above the fold.
- `/about/` — directors, advisers (named, dated bios with qualifications).
- `/about/merger-2026/` — the canonical merger explainer described in `04-ai-search-sector-signals.md` §7.
- `/regulatory-information/` — FCA statement, FSCS, FOS, complaints, Consumer Duty summary, fees, data privacy principal.
- `/contact/` — single canonical address block, phone, email, hours.
- Footer on every page: company number, FCA reference, address, risk warning. Verbatim identical across every page.

Exclusion statements (as drafted in `01-entity-audit.md`) belong in About and in an FAQ schema block.

## Signal 02 — Subject Authority

Build topic clusters, not a content marketing calendar. Each cluster has one pillar page and 4–8 supporting pages. No page answers the same primary question as any other (Signal 02's "No Content Collision" rule).

Recommended opening clusters:

1. **First-time buyers in Essex**
   - Pillar: `/guides/first-time-buyer/`
   - Supporting: deposit sources, Lifetime ISA use, shared ownership in Essex, typical Colchester completion timeline, Help to Buy legacy unwinds.
2. **Remortgaging in 2026**
   - Pillar: `/guides/remortgaging/`
   - Supporting: end-of-fix decision framework, product transfer vs remortgage, rate-cycle explainer (with a BoE-sourced chart), early repayment charge mechanics.
3. **Buy-to-let around the University of Essex**
   - Pillar: `/guides/buy-to-let/`
   - Supporting: rental yield maths, limited-company vs personal BTL, consent-to-let, HMO and student let considerations, stress-test ratios in 2026.
4. **Mortgages for Colchester Garrison / Armed Forces**
   - Pillar: `/guides/armed-forces-mortgages/`
   - Supporting: Forces Help to Buy 2, FHTB repayment, postings and consent-to-let, overseas deployment and portability.
5. **Self-employed and contractor affordability**
   - Pillar: `/guides/self-employed-mortgages/`
   - Supporting: day-rate contractor treatment, limited-company director income, SA302 documentation, recently-self-employed criteria by lender.

Every page carries:

- Named author byline (Rishi, Oliver, or a named adviser), with a `/people/[slug]/` bio page and `Person` schema.
- "Last reviewed on [date] by [name]" line — the reviewing date refreshes quarterly for YMYL freshness.
- At least one external evidence link to FCA, BoE, HMRC, UK Finance, ONS or gov.uk.
- At least one quantified claim owned by the firm (case study, average completion time, success rate) with explicit date attribution.

Quarterly collision scan: a spreadsheet of "primary question answered" per URL, reviewed every 90 days. Duplicates are merged, not left to compete.

## Signal 03 — Meaning Architecture

Technical requirements for the new build:

- Clean URL hierarchy (`/guides/remortgaging/end-of-fix/`, not `/blog/post-id-482`).
- Single canonical per URL; `<link rel="canonical">` on every page.
- Strict 301 governance: a CSV-tracked redirect map covering:
  - Every rb-financial.com URL → closest MMB equivalent.
  - Any legacy mymortgagebroker.co.uk URL that changes in the rebuild.
  - Retained for 24 months minimum.
- XML sitemap segmented (`/sitemap-pages.xml`, `/sitemap-guides.xml`, `/sitemap-people.xml`).
- `robots.txt` permits GPTBot, ClaudeBot, Google-Extended, PerplexityBot, Bingbot, Amazonbot, Applebot-Extended.
- `llms.txt` at site root listing the 20–30 canonical pages.
- All content in server-rendered HTML or pre-rendered at build time. No JS-gated primary content.
- Core Web Vitals targeted: LCP <2.5s, INP <200ms, CLS <0.1.
- Image strategy: every image has descriptive filename, descriptive alt, and lives on the same domain.
- Accessibility: WCAG 2.2 AA as the floor (also a legal posture for a UK firm serving the public).

**RAG-ready passages** (Signal 03 verbatim requirement):

- Every page answers its primary question in the first 150 words.
- Zero Anaphora Protocol: no "it / this / they" in lead passages — always use the full subject.
- Paragraph length 40–80 words, one idea per paragraph, H2s that themselves read as questions.
- FAQ blocks on every guide, each Q/A standalone and 200–500 tokens, wrapped in `FAQPage` schema.

**Schema stack** (JSON-LD, served once per page, typed precisely):

- `Organization` on every page (with `@id` anchored to `https://mymortgagebroker.co.uk/#organization`).
- `FinancialService` as the primary business type — a `LocalBusiness` subtype — on the homepage and contact page. Populate `areaServed`, `priceRange`, `openingHoursSpecification`, `sameAs` (LinkedIn, Trustpilot, Unbiased, VouchedFor, Companies House profile, FCA Register URL). *Note: `MortgageBroker` is not an official schema.org subtype as of April 2026 — use `FinancialService` with a descriptive `@type` array and a `serviceType` of "Mortgage brokerage" until a more specific type is canonicalised.*
- `Person` for every adviser, linked from `Organization.employee` and from the byline.
- `Article` on every guide, with `author`, `reviewedBy`, `datePublished`, `dateModified`.
- `FAQPage` on pages with structured Q&A.
- `BreadcrumbList` on every non-home page.
- `Review` / `AggregateRating` referencing the genuine Trustpilot feed (do not self-host ratings that are not externally validated — Google penalises).

Every schema field must match the visible on-page text character-for-character.

## Signal 04 — Ecosystem Validation

Build the "Circle of Authority" deliberately, in this order:

1. **Registries**: Companies House record accurate; Wikidata item submitted once reconciled; OpenCorporates profile checked.
2. **FCA Register**: single, clean entry matching the site verbatim.
3. **Directories**: Unbiased, VouchedFor, financialadvisers.co.uk, mylocalmortgage.co.uk — each carrying the exact same entity block.
4. **Review platforms**: Trustpilot (retain current), Google Business Profile (merged), Feefo or Reviews.io optional.
5. **Professional networks**: LinkedIn company page re-branded; both directors' personal profiles updated; advisers' profiles aligned.
6. **Press**: pursue 3–5 genuine citations in mortgage trade press (Mortgage Solutions, Mortgage Strategy, FTAdviser) during year one — quote-worthy commentary on the merger itself is the hook.
7. **Video**: a short YouTube channel with adviser-fronted explainers for each pillar topic. Named person, plain set, descriptive titles.

The test that Signal 04 is working: paste the FCA number into ChatGPT and ask "who is this broker?" — the answer should include the post-merger name, the Colchester address, the directors and a first-line summary of services. If it returns RB Financial or the Stanway address, the signal has not yet landed.

## Signal 05 — Signal Consistency

Merger-specific consistency tasks:

- **Same-day cutover checklist**: Companies House, FCA, GBP, LinkedIn, Trustpilot, Unbiased, VouchedFor, rb-financial.com (301 live), mymortgagebroker.co.uk (new site live), email sigs, printed letterhead. A single day, a single script, no half-states.
- **Legacy content reconciliation**: every rb-financial.com page that had genuine substance is republished under the new brand with a clearly dated "Originally published by RB Financial Advisers Ltd" notice. Do not silently re-publish — AI systems track duplicate-content provenance.
- **Answer-format optimisation**:
  - Comparison questions get tables.
  - Step questions get ordered lists.
  - "What is X?" questions get a one-sentence definition before any elaboration.
- **Conversational alignment**: headings phrased as actual user questions ("Is a 2-year fix worth it in 2026?" not "2-year fixed-rate mortgages").
- **Multimodal signals**: every image used in adviser bios is the same image across the site, GBP, LinkedIn and Trustpilot.
- **Evidence compression**: a dated, versioned `/stats` or `/facts` page listing firm-level numbers (clients helped, volume advised, average completion, review counts) so AI systems have a single, stable place to pull quantitative claims from.

## Cadence

- **Weeks 0–2** (before anything is published): resolve entity contradictions, lock fact block, draft redirect map.
- **Weeks 2–6**: new site build, schema stack, regulatory pages, merger page, director and adviser bios.
- **Weeks 4–8**: first two content clusters (first-time buyer, remortgaging) live.
- **Weeks 8–12**: directory reconciliation, review graph consolidation, press outreach kick-off.
- **Month 3 onwards**: quarterly collision scans, freshness reviews, AI prompt-testing pipeline (sample of 40 prompts run monthly across Google AI Overviews, ChatGPT, Gemini, Perplexity, Claude — logged against inclusion rate and sentiment).

## Definition of done for phase 1

The site is "phase-1 complete" when:

- [ ] Every fact in `01-entity-audit.md` is resolved and reflected on-site, on Companies House, on the FCA Register and on every directory.
- [ ] The merger page is live and 301-linked from rb-financial.com.
- [ ] Five topic-cluster pillars plus at least three supporting guides per pillar are live.
- [ ] The schema stack validates in Google's Rich Results Test and Schema.org validator with zero errors.
- [ ] `llms.txt`, `robots.txt`, sitemaps are live and allow the main AI crawlers.
- [ ] A baseline AI Visibility audit (Rank4AI methodology) has been run, scored and the score recorded so that month-3 and month-6 deltas can be measured.
