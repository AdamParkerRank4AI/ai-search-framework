# UK Peptides Hub — Pilot v0.1 (locked scope)

**Date:** April 2026
**Branch:** `claude/niche-development-setup-PJpQh`
**Companion to:** `docs/site-builds/peptides-hub.md` (full UK master plan + 4-tier architecture).

This doc locks the v0.1 build scope. Anything not in this doc is out of scope for the first ship.

---

## 1. Locked deployment

| | Locked |
|---|---|
| **Domain** | `findapeptide.co.uk` (`.com` fallback if `.co.uk` taken). Standalone — NOT inside a women's-wellness umbrella for v0.1. (Cross-link with future menopause hub once both exist.) |
| **Brand voice** | Wellness + women's-health-led. Not bro-biohacker. Editorial policy visible. Regulator citations on every relevant page. |
| **Audience** | Primary: women 35–60 (peri / menopausal / wellness). Secondary: longevity / biohacking enthusiasts. |
| **Tone** | Honest, specific, regulator-aware. Not preachy. Not snarky. Not hedge-everything-with-disclaimers. Think *Which?* meets *Stylist Wellness*. |
| **Editorial position** | We will say what each peptide is, what the evidence shows, what tier it sits in, what UK regulation applies, and where mainstream UK consumers can buy products that contain it (where applicable). We will **not** publish human-dosing protocols for tier-4 research peptides under any circumstances. |

---

## 2. Locked URL list (35 URLs across all four tiers)

### A. Site chrome (5 URLs)
```
/                                                # homepage — the four-tier story
/about/
/how-we-review/                                  # methodology
/editorial-policy/                               # MHRA-aware editorial promise
/contact/
```

### B. Tier 1 — Cosmetic peptides (8 URLs)
```
/skincare/                                       # Tier 1 hub
/skincare/argireline/                            # ingredient explainer
/skincare/matrixyl/                              # ingredient explainer
/skincare/copper-peptide/                        # GHK-Cu topical explainer
/skincare/best-peptide-serum-uk/                 # listicle (8–12 products)
/skincare/best-peptide-moisturiser-uk/           # listicle
/skincare/the-ordinary-buffet-review/            # individual product review
/skincare/medik8-liquid-peptides-review/         # individual product review
```

### C. Tier 2 — Collagen peptides (7 URLs)
```
/collagen/                                       # Tier 2 hub
/collagen/marine-vs-bovine-vs-vegan/             # decision-tree explainer
/collagen/best-collagen-supplement-uk/           # listicle
/collagen/collagen-for-menopause/                # cross-link to women's content
/collagen/absolute-collagen-review/              # individual review
/collagen/vital-proteins-review/                 # individual review
/collagen/revive-collagen-review/                # individual review
```

### D. Tier 3 — GLP-1 prescription (8 URLs)
```
/glp-1/                                          # Tier 3 hub
/glp-1/mounjaro-uk-private-cost/                 # cost guide
/glp-1/wegovy-uk-private-cost/                   # cost guide
/glp-1/mounjaro-vs-wegovy-vs-ozempic-uk/         # comparison
/glp-1/how-to-get-mounjaro-uk-private/           # process guide
/glp-1/numan-mounjaro-review/                    # clinic review
/glp-1/juniper-uk-mounjaro-review/               # clinic review
/glp-1/boots-online-doctor-mounjaro-review/      # clinic review
```

### E. Tier 4 — Research peptides (4 URLs — disciplined scope, encyclopedia + supplier comparison only)
```
/research/                                       # Tier 4 hub — clearly framed
/research/bpc-157/                               # encyclopedia entry
/research/mots-c/                                # encyclopedia entry
/research/uk-supplier-purity-comparison/         # supplier purity table
```

### F. Cross-tier women's content (3 URLs)
```
/for-women/                                      # women's hub
/for-women/peptides-and-menopause/               # cross-tier overview
/for-women/skin-changes-perimenopause/           # tier-1 + tier-2 angle
```

---

## 3. Total URL count v0.1

| Bucket | URLs |
|---|---|
| A. Site chrome | 5 |
| B. Tier 1 — Cosmetic | 8 |
| C. Tier 2 — Collagen | 7 |
| D. Tier 3 — GLP-1 | 8 |
| E. Tier 4 — Research | 4 |
| F. Cross-tier women's | 3 |
| **v0.1 total** | **35 URLs** |

Compared to the master plan's ~600 at full scale, this is ~6%. Enough to prove the architecture across all four regulatory tiers, validate the affiliate stack, and establish the editorial voice.

---

## 4. Page-template specs (per tier)

### 4.1 Tier 1 — Cosmetic peptide ingredient pages (e.g. `/skincare/argireline/`)

```
1. H1:           "Argireline (Acetyl Hexapeptide-8) — UK Guide 2026"
2. Verdict:      one-line stance — "Modest evidence, low irritation, mainstream-affordable. A reasonable expression-line product, not a wrinkle eraser."
3. What it is:   plain-English mechanism (200–300 words)
4. The evidence: published-study summary (200–300 words)
5. UK products containing it: table of 6–10 products (price, brand, formulation, affiliate link)
6. Who it suits: skin types and concerns it works for (and who it doesn't)
7. How to use it: morning / evening, layering with retinoids, common mistakes
8. FAQs:         4–6 schema-rich entries
9. Affiliate CTA: lowest-irritation pick + best-value pick + premium pick
```

### 4.2 Tier 1 — Cosmetic listicle pages (e.g. `/skincare/best-peptide-serum-uk/`)

```
1. H1, hero
2. Methodology box: "How we picked these 10 — testing notes, ingredient density, value-per-mL"
3. Ranked list of 8–12 products. Each: hero image, price, key claim, who it suits, affiliate CTA
4. Comparison table (sortable: price, peptide content, suitable skin types)
5. FAQs
6. Cross-tier links (collagen, women's content)
```

### 4.3 Tier 1 — Cosmetic brand-product reviews (e.g. `/skincare/the-ordinary-buffet-review/`)

```
1. Hero — product, price, our verdict
2. Ingredient breakdown
3. The science behind the claim
4. How it compares with 3 alternatives
5. Who it suits
6. How to use
7. FAQs
8. Buy-it CTA
```

### 4.4 Tier 2 — Collagen brand reviews

Same shape as 4.3 but with: collagen-source breakdown (bovine / marine / vegan), hydrolysis molecular weight, UK manufacturing claims if any, daily-cost-per-serve calculation, and a cross-link to the menopause page.

### 4.5 Tier 2 — Decision tree (`/collagen/marine-vs-bovine-vs-vegan/`)

```
1. H1
2. The 60-second answer
3. Side-by-side comparison table
4. Marine collagen — when it suits
5. Bovine collagen — when it suits
6. Vegan / microbial collagen — when it suits
7. Recommended UK brand per category
8. FAQs
```

### 4.6 Tier 3 — GLP-1 cost guide (e.g. `/glp-1/mounjaro-uk-private-cost/`)

```
1. H1, verdict (one-line on monthly cost range)
2. Cost-by-dose table (2.5mg / 5mg / 7.5mg / 10mg / 12.5mg / 15mg) per UK clinic
3. What's included in each clinic's price (consultation, tests, follow-up, app, pen vs vial)
4. NHS path explainer (eligibility, waiting times) — anchored against the private path
5. Total annual cost-of-ownership scenarios
6. Affiliate CTAs to 3 clinics with different value props
7. FAQs (side effects, contraindications — referenced from MHRA SmPC, not invented)
```

### 4.7 Tier 3 — Clinic reviews (e.g. `/glp-1/numan-mounjaro-review/`)

```
1. Verdict
2. Registered status (GPhC pharmacy reg, CQC if applicable, prescriber type)
3. Cost (current month) + what's included
4. Onboarding flow (consultation, tests, prescription release time)
5. Side-effect protocols (escalation, withdrawal)
6. Cancellation policy
7. Honest pros + cons
8. Trustpilot snapshot
9. Affiliate CTA
```

### 4.8 Tier 4 — Research peptide encyclopedia (e.g. `/research/bpc-157/`) — **READ THE EDITORIAL POLICY**

```
1. H1: "BPC-157 — UK Research Guide 2026"
2. STATUS BANNER (not collapsible): "This peptide is sold in the UK as a research chemical labelled 'not for human consumption'. It is not licensed for human use by the MHRA. This page covers research applications and supplier-purity comparison only. We do not publish human dosing protocols."
3. What it is — a 200-word factual mechanism summary
4. Research applications — what published research has examined (cite PubMed IDs)
5. UK regulatory status — plain English (cite Human Medicines Regulations 2012)
6. UK suppliers offering research-grade BPC-157 — table:
   - Supplier name | Purity claim | CoA available | Vial size | £ per vial | Last verified
   - NO usage advice. NO dosing. NO "best for fat loss" framing.
7. Why purity matters in research — context
8. Related research peptides (encyclopedia internal links)
9. References
```

### 4.9 Tier 4 — Supplier purity comparison (`/research/uk-supplier-purity-comparison/`)

```
1. H1
2. Methodology box: "We compare UK research-peptide suppliers on purity claims, certificate-of-analysis transparency, vial sizing, and supply consistency. We do not compare suppliers on suitability for human consumption."
3. Sortable supplier table
4. What "research grade" actually means
5. CoA red flags
6. Payment + shipping considerations
7. References
```

### 4.10 Cross-tier women's content (e.g. `/for-women/peptides-and-menopause/`)

```
1. H1
2. Verdict — which peptide categories actually have evidence relevant to perimenopause / menopause
3. Cosmetic peptides for skin changes (links to /skincare/...)
4. Collagen for joint/skin/hair (links to /collagen/...)
5. GLP-1 and post-menopausal weight management (links to /glp-1/...)
6. Research peptides — what research exists for women's health, what doesn't, regulatory status
7. Editorial honesty — what we can say with confidence, what's still emerging
8. Cross-link CTAs to deep dives in each tier
9. FAQs
```

---

## 5. Data needed before build

### 5.1 Tier 1 — Cosmetic data (~8 records)

For each product reviewed: brand, product, price, peptide active(s), full ingredient list, formulation type (serum / cream / oil / liquid), volume, price-per-mL, Awin/Impact affiliate URL, hero image URL, Trustpilot avg + count.

Source: brand websites, Lookfantastic / Cult Beauty / Boots / John Lewis listings, Trustpilot scrape.

### 5.2 Tier 2 — Collagen data (~6 records)

For each brand: collagen source (bovine / marine / vegan), hydrolysis MW (Da), grams per serve, daily cost-per-serve, UK manufacture y/n, third-party testing y/n, affiliate URL, Trustpilot snapshot.

Source: brand websites, Holland & Barrett listings, Trustpilot scrape.

### 5.3 Tier 3 — GLP-1 clinic data (~3 clinic records, each across 5 doses)

Per clinic: name, registered-pharmacy GPhC ID, CQC status, drugs offered, monthly cost per dose, what's included (consultation, app, follow-up), prescriber type, onboarding flow, cancellation policy, affiliate URL/CPA estimate, Trustpilot snapshot.

Source: clinic websites, GPhC public register cross-check, CQC public register cross-check.

### 5.4 Tier 4 — Research data (~2 peptide encyclopedia entries + 6 UK supplier records for the comparison page)

Per peptide: name, full IUPAC, mechanism summary, research applications (PubMed IDs cited), UK regulatory status, related peptides.

Per supplier (for the comparison page only): name, purity claim, CoA practice (available y/n, third-party labs used), vial size options, price per vial, payment methods accepted, shipping info, last-verified date.

Source: PubMed for research papers, MHRA news for regulatory action history, direct contact with each supplier requesting a sample CoA for review (do not buy product).

### 5.5 Cross-tier women's content (~3 long-form articles)

Original editorial — written by us, not templated. Each ~1,500–2,500 words, citing the per-peptide research where relevant.

---

## 6. Astro project structure (locked for v0.1)

Same chassis as `sites/findatradey/` and `sites/findagym/`. Repo location: `sites/findapeptide/`.

```
findapeptide/
├── data/
│   ├── cosmetic/
│   │   ├── ingredients.json       # argireline, matrixyl, copper-peptide
│   │   └── products.json          # 8–12 reviewed products
│   ├── collagen/
│   │   ├── brands.json            # 6 brand records
│   │   └── decision-tree.json     # marine vs bovine vs vegan
│   ├── glp1/
│   │   └── clinics.json           # 3 clinic records, dose-by-dose pricing
│   ├── research/
│   │   ├── peptides.json          # bpc-157, mots-c
│   │   └── uk-suppliers.json      # 6 supplier records for the comparison page
│   └── women/
│       └── articles/              # markdown articles for women's content
├── src/
│   ├── pages/
│   │   ├── index.astro
│   │   ├── about.astro
│   │   ├── how-we-review.astro
│   │   ├── editorial-policy.astro
│   │   ├── contact.astro
│   │   ├── skincare/
│   │   │   ├── index.astro
│   │   │   ├── [ingredient].astro     # argireline, matrixyl, copper-peptide
│   │   │   ├── best-peptide-serum-uk.astro
│   │   │   ├── best-peptide-moisturiser-uk.astro
│   │   │   └── [product]-review.astro # the-ordinary-buffet, medik8
│   │   ├── collagen/
│   │   │   ├── index.astro
│   │   │   ├── marine-vs-bovine-vs-vegan.astro
│   │   │   ├── best-collagen-supplement-uk.astro
│   │   │   ├── collagen-for-menopause.astro
│   │   │   └── [brand]-review.astro   # absolute-collagen, vital-proteins, revive
│   │   ├── glp-1/
│   │   │   ├── index.astro
│   │   │   ├── mounjaro-uk-private-cost.astro
│   │   │   ├── wegovy-uk-private-cost.astro
│   │   │   ├── mounjaro-vs-wegovy-vs-ozempic-uk.astro
│   │   │   ├── how-to-get-mounjaro-uk-private.astro
│   │   │   └── [clinic]-mounjaro-review.astro  # numan, juniper-uk, boots-online-doctor
│   │   ├── research/
│   │   │   ├── index.astro
│   │   │   ├── [peptide].astro             # bpc-157, mots-c
│   │   │   └── uk-supplier-purity-comparison.astro
│   │   └── for-women/
│   │       ├── index.astro
│   │       ├── peptides-and-menopause.astro
│   │       └── skin-changes-perimenopause.astro
│   ├── components/
│   │   ├── TierBanner.astro            # the regulatory-tier visible badge
│   │   ├── ResearchStatusBanner.astro  # hard banner on tier-4 pages
│   │   ├── IngredientCard.astro
│   │   ├── ProductReviewCard.astro
│   │   ├── ClinicReviewCard.astro
│   │   ├── PeptideEncyclopediaCard.astro
│   │   ├── SupplierComparisonTable.astro
│   │   ├── AffiliateBlock.astro
│   │   ├── EditorialPolicyBlock.astro
│   │   ├── CrossTierLinks.astro
│   │   ├── FAQBlock.astro
│   │   ├── Header.astro
│   │   └── Footer.astro
│   ├── layouts/
│   │   ├── BaseLayout.astro
│   │   ├── CosmeticPage.astro
│   │   ├── CollagenPage.astro
│   │   ├── GLP1Page.astro
│   │   └── ResearchPage.astro          # mandatory ResearchStatusBanner included
│   ├── lib/
│   │   ├── types.ts
│   │   ├── data.ts
│   │   ├── schema.ts
│   │   └── faqs.ts
│   └── styles/
│       └── global.css
└── astro.config.mjs
```

---

## 7. Build checklist (v0.1)

### Week 1 — Foundation + data
- [ ] Domain check + register (`findapeptide.co.uk`)
- [ ] Init Astro project, Tailwind, Cloudflare Pages
- [ ] Build all four `data/<tier>/*.json` skeletons matching the data spec in §5
- [ ] Apply to affiliate programmes — Awin (The Ordinary, Lookfantastic, Cult Beauty, Vital Proteins, Holland & Barrett), Impact (where appropriate), direct to Numan / Juniper / ZAVA / Absolute Collagen / Revive
- [ ] Apply to Direct Sarms / Pure Peptides UK / Aquila Peptides for the supplier-comparison page (research only, not human consumption framing)
- [ ] Set up Tally forms — clinic-match for GLP-1, supplement-match for cosmetic/collagen, email-signup
- [ ] Set up Plausible analytics

### Week 2 — Editorial + legal
- [ ] **Pre-launch legal review** by a UK media-law / MHRA-aware lawyer. Budget £1,500–3,000. Brief them on the editorial policy + tier-4 ResearchStatusBanner. They should sign off on at least the BPC-157 and MOTS-c encyclopedia entries + the UK supplier comparison page.
- [ ] Write `editorial-policy.astro` page in full — visible-link-from-every-page editorial promise
- [ ] Write `how-we-review.astro` — methodology
- [ ] Write `about.astro` — brand voice, positioning
- [ ] Build all components from §6 (TierBanner, ResearchStatusBanner, IngredientCard, ProductReviewCard, ClinicReviewCard, PeptideEncyclopediaCard, SupplierComparisonTable, etc.)
- [ ] Build the four tier layouts (CosmeticPage, CollagenPage, GLP1Page, ResearchPage)

### Week 3 — Content fill + tier 1 + tier 2 launch
- [ ] All Tier 1 cosmetic pages live (8 URLs)
- [ ] All Tier 2 collagen pages live (7 URLs)
- [ ] First three women's content articles drafted + reviewed editorially
- [ ] Sitemap submitted to Google Search Console
- [ ] Email-signup live

### Week 4 — Tier 3 + tier 4 launch
- [ ] All Tier 3 GLP-1 pages live (8 URLs) — clinic registrations cross-checked on GPhC + CQC public registers
- [ ] All Tier 4 research pages live (4 URLs) — legal review sign-off complete
- [ ] All cross-tier women's content live (3 URLs)
- [ ] Schema markup audit on every page (FAQPage, Article, MedicalWebPage where applicable, Product for cosmetic + collagen, Organization sitewide)
- [ ] Trustpilot scrapes complete and live on all reviewed brands/clinics

---

## 8. v0.1 success criteria (locked before build)

| Metric | Week 4 | Week 8 | Week 12 |
|---|---|---|---|
| URLs indexed | 100% | 100% | 100% |
| Tier 1 pages ranked top 30 | 30% | 60% | 75% |
| Tier 2 pages ranked top 30 | 25% | 55% | 70% |
| Tier 3 pages ranked top 30 | 20% | 45% | 60% |
| Tier 4 pages ranked top 30 | 30% (low-competition tier — should rank fastest) | 70% | 80% |
| Affiliate clicks (any tier) | ≥ 100 | ≥ 600 | ≥ 1500 |
| Affiliate conversions | ≥ 5 | ≥ 25 | ≥ 80 |
| GLP-1 clinic-match form submissions | ≥ 3 | ≥ 15 | ≥ 40 |
| Email list size | ≥ 50 | ≥ 250 | ≥ 750 |
| MHRA / regulatory contact incidents | 0 | 0 | 0 |

The final row is the most important. **One MHRA contact is a v0.1-failure event** that triggers immediate content review and likely takedown of one or more tier-4 pages. Build the editorial discipline so this doesn't happen.

---

## 9. Cash-out priority for v0.1

In order:

1. **Tier 1 + Tier 2 affiliate** — fastest, lowest friction, no relationships needed beyond Awin / Impact approvals
2. **Tier 3 GLP-1 clinic affiliate** — slowest to onboard but highest CPA (£50–200) per converted enquiry
3. **Email list growth** — front-loaded across all four tiers, payoff is Phase 2 product launches
4. **Tier 4 supplier-purity-comparison affiliate** — direct relationships only, expect commissions late Month 2 onwards once outreach lands
5. **AdSense / Mediavine** — Phase 2, post-50k sessions

---

## 10. Out of scope for v0.1 (explicit)

- **Own white-label collagen or skincare line** — Phase 2 (after Month 6, once email list is meaningful)
- **PT-141 / female libido tier-4 page** — Phase 2 only with full legal review (PT-141 is more sensitive than BPC-157 / MOTS-c on regulatory radar)
- **CJC-1295 / Ipamorelin / Tesamorelin / Selank / Semax encyclopedia** — Phase 2 (proceed only after tier-4 pilot pages get no MHRA contact for 90 days)
- **Hair-loss-specific peptide content** — Phase 2 (overlaps with mens-health TRT site if we build that)
- **Weight-loss-specific protocol content for GLP-1** — Phase 2 with dietitian byline
- **Programmatic per-UK-city content** — Phase 2 (not the natural shape of this site; education-led not geography-led)
- **Mobile app or interactive tools** — Phase 2

---

## 11. Decisions — locked + open

### Locked
| # | Item | Locked answer |
|---|---|---|
| 1 | Domain | `findapeptide.co.uk` (`.com` fallback) |
| 2 | Brand voice | Wellness + women's-health-led, regulator-aware, *Which?*-meets-*Stylist Wellness* |
| 3 | Tier-4 editorial policy | Encyclopedia + supplier-purity comparison only. No human dosing, ever. ResearchStatusBanner mandatory on every tier-4 page. |
| 4 | Pre-launch legal review | **Required** before tier-4 pages go live. £1,500–3,000 budget. |
| 5 | GLP-1 clinic affiliate path | Direct to clinics + Awin where available. Cross-check GPhC + CQC registers quarterly. |
| 6 | Cross-link with future menopause hub | Yes — when both exist. Standalone brand for v0.1. |

### Still open
| # | Item | What we need from you |
|---|---|---|
| 7 | Pre-launch lawyer | Pick a UK media-law firm with MHRA-aware practice. Recommendations: Brabners (media + healthcare), Lewis Silkin (advertising + healthcare), Bristows (life sciences + advertising). |
| 8 | Tier-4 risk appetite | The pilot includes BPC-157 + MOTS-c only — both well-researched, lower regulatory profile. Do you want to add Tesamorelin or Ipamorelin to v0.1? Pushes risk slightly higher; raises content depth. |
| 9 | Direct-supplier affiliate relationships | Direct Sarms / Pure Peptides UK / Aquila Peptides / Pinnacle / Nooku — open to all five for the comparison page, or be more selective? |
| 10 | Editorial / writing capacity | Tier 1 + Tier 2 + Tier 3 pages can be drafted by Claude with manual review. Tier 4 + women's-content articles benefit from a named human writer with a wellness/health background — do you have someone, or should we plan for freelance? |

---

## 12. Cross-references

- `docs/site-builds/peptides-hub.md` — full UK master plan + four-tier architecture detail
- `docs/niche-shortlist-2026-04.md` #141 — UK Peptides Hub master entry
- `docs/niche-shortlist-2026-04.md` #53 — NEW 2 Menopause / HRT (sister site, mutual cross-link)
- `docs/site-builds/findatradey-pilot-v0.md` — sister pilot, same Astro / Cloudflare infrastructure
- `docs/site-builds/gym-colchester-pilot-v0.md` — sister pilot
- `docs/reference/lead-resale-model.md` — three-layer revenue model (this site uses all three layers)
- `docs/reference/portable-prompts.md` — research prompts to find adjacent women's-wellness niches
