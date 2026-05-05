# UK Peptides Hub — Master Project Plan

**Working domain:** `findapeptide.co.uk` *(or whichever the pilot doc locks in)*
**Status:** Master plan — April 2026
**One-line vision:** A regulator-aware UK peptides resource that is both **the front door for women's wellness** (menopause, skin, hair, recovery) and an authoritative encyclopedia for biohacking + longevity audiences. Wins by being the first UK site to handle the four-tier peptides market honestly: cosmetic, food-grade collagen, prescription (GLP-1), and research-grade.

Pilot scope is locked separately in `docs/site-builds/peptides-pilot-v0.md` (target ~35 URLs across the four tiers).

---

## 1. The strategic question — standalone, or inside the women's hub?

This site has two viable deployment paths. The master plan supports both; the pilot doc locks in one.

**Path A — Standalone peptides hub (`findapeptide.co.uk` or similar)**
- Best for: speed of build, dedicated SEO authority, easier compliance management, easier monetisation (own product line possible)
- Cross-links to a future menopause/women's-health hub
- Cleaner brand for the regulatory-grey research-peptide content

**Path B — Major arm on a women's health hub**
- Best for: shared audience compounding, lower ecosystem cost
- Peptides becomes one of N pillars (alongside menopause, HRT, supplements, skincare)
- The "peptides" brand within a wider entity
- Riskier compliance shape — one bad section drags the whole site

**Master-plan recommendation:** standalone (Path A) for the build, with a content partnership strategy that feeds menopause-relevant peptide content into a sibling women's hub at launch. Best of both: clean SEO authority on peptides, audience compounding via cross-link.

---

## 2. The four-tier regulatory architecture (read this first)

Peptides is not a single market. It's **four overlapping markets** with very different regulatory shapes. Building one site that pretends they're the same is the fastest way to get an MHRA letter.

### Tier 1 — Cosmetic peptides (skincare)
- **What:** Argireline (Acetyl Hexapeptide-8), Matrixyl, Copper Peptides (GHK-Cu topical), Snap-8
- **Regulation:** EU/UK Cosmetics Regulation, CTPA-aware. Fully mainstream.
- **Examples:** The Ordinary, Paula's Choice, Elemis, Medik8, Drunk Elephant, Skinceuticals, Niod
- **Audience:** mass-market skincare buyer, women-skewing, ages 25–65
- **Site role:** safe, mainstream, SEO-friendly, big affiliate stack
- **Risk level:** **None.** Treat like any beauty content site.

### Tier 2 — Food-grade collagen peptides (oral supplements)
- **What:** Bovine, marine, vegan (microbial) hydrolysed collagen
- **Regulation:** Food law only. No specific peptide regulation.
- **Examples:** Vital Proteins, Absolute Collagen, Revive Collagen, Ingenious, Bare Biology, Holland & Barrett's range
- **Audience:** women-skewing, joint/skin/hair concerns, ages 35–65
- **Site role:** authoritative comparison + own white-label opportunity (UK supplement-factory infrastructure already mapped — see Pet Hub doc §4 supplier list)
- **Risk level:** **None for educational content; standard food-supplement law for own white-label.**

### Tier 3 — Prescription peptides (medical)
- **What:** GLP-1 agonists (semaglutide / Wegovy, tirzepatide / Mounjaro), insulin analogues, PT-141 (when prescribed for HSDD)
- **Regulation:** **POM in UK.** MHRA + GPhC. Telehealth providers must hold registered-pharmacy permissions and use registered prescribers.
- **Site role:** **referral content only.** No prescribing claims, no dosing advice, no comparisons with off-label/research-grade alternatives. Affiliate to authorised UK clinics.
- **Examples (UK affiliate):** Numan, Juniper UK, ZAVA, Boots Online Doctor, MANUAL, Voy
- **Risk level:** **Low if affiliate-only.** Zero if no prescribing/dosing content. Cross-link with NEW 5 MTD-tax content as the GLP-1 market converts more sole-traders into self-referrers.

### Tier 4 — Research peptides (the grey zone — read carefully)
- **What:** BPC-157, TB-500, MOTS-c, Ipamorelin, CJC-1295, Tesamorelin, GHK-Cu (injectable form), Epitalon, Selank, Semax, PT-141 (research label), and a long tail of ~40+ research-grade peptides
- **Regulation:** Sold legally in the UK *as research chemicals labelled "not for human consumption"*. The actual buying audience is biohackers / bodybuilders self-administering. **MHRA can intervene under the Human Medicines Regulations 2012 if a seller advertises human consumption.** UK enforcement has been patchy but is not zero — several US sellers have been actioned, a few UK sellers warned.
- **Channel risk:**
  - Google Ads, Meta Ads — won't run them
  - Stripe / PayPal — often refuse or freeze
  - Mainstream affiliate networks (Awin, Impact) — generally won't accept these advertisers
  - Direct relationships only with UK research-peptide companies
- **Site role on this site:** **encyclopedia + supplier-purity comparison only.** No human dosing, no stacking advice, no "for fat loss take X mg" content. Frame everything as research-grade purity and legitimate research applications. Disclaimers on every page.
- **Why it's worth covering despite the risk:**
  - Search demand is real and rising fast (UK Google Trends 4–8× since 2022 for major research peptides)
  - SERPs are dominated by US clinics and supplier sales pages — almost no UK-aware educational content
  - AI Overviews refuse or hedge — that is the AI Visibility Gap
  - One captured email lead is highly valuable across the legal Tier 1–3 product range
- **Risk level:** **Real but manageable** with disciplined content. Get a UK media-law / MHRA-aware lawyer to review the launch content. Budget £1,500–3,000 for a one-time content-pre-launch legal pass.

**Architectural rule:** every page must be in exactly one tier. The site's IA never blends them. A user reading "Argireline for fine lines" must never be one click away from "BPC-157 stack for fat loss".

---

## 3. The market

UK peptides search volume is large and growing across all four tiers:

- **Cosmetic peptides** — mass-market mature. The Ordinary's "Buffet" remains a baseline; copper peptides surging post-2024 trend cycles. UK-specific comparison content is thin.
- **Collagen supplements** — UK market grew ~25% YoY 2023–2025. Vital Proteins, Absolute Collagen, Revive Collagen all running TV ads in 2025–2026.
- **GLP-1 private prescription** — UK market estimated 600k+ users by Q1 2026 (largely on Mounjaro since the Boots/Numan retail rollout in 2024–25). Search demand for "Mounjaro UK private", "Wegovy UK cost", "Mounjaro vs Ozempic UK" all up 5–15× since 2023.
- **Research peptides** — UK Google Trends shows BPC-157 up ~4×, MOTS-c up ~6×, Tesamorelin up ~3× since 2022. Very long tail of niche peptides each at low volume but stacking to substantial combined demand.

**Women's health overlap (the strategic angle the brief flagged):**

Peptides genuinely relevant to a menopausal / perimenopausal audience:

| Peptide | Why it crosses over to menopause / women's wellness |
|---|---|
| Argireline / Matrixyl (cosmetic) | Skin-quality changes during perimenopause |
| Copper peptide (cosmetic + research) | Hair density, post-menopausal scalp health |
| Collagen (food-grade) | Joint, skin, hair changes |
| GHK-Cu (research, topical) | Hair density, skin elasticity |
| BPC-157 (research) | Recovery, joint pain |
| MOTS-c (research) | Mitochondrial function, metabolic shifts |
| Tesamorelin (research) | Visceral fat — post-menopausal interest |
| Selank / Semax (research) | Mood / cognition — peri-menopausal anxiety |
| PT-141 (research) | Female libido — HSDD adjunct |
| GLP-1s (prescription) | Weight management — post-menopausal metabolic shift |

A women's wellness audience is therefore a natural primary audience for the site. Master plan supports a women-skewing brand voice while keeping content available to other demographics.

---

## 4. The SERP today (where it's dormant, where AI is hedging)

For most peptide queries the UK Top 10 is one of three things:

- **Cosmetic peptide queries** — dominated by The Ordinary, Paula's Choice, Skincare-Edit, Cosmopolitan / Glamour beauty content. Authoritative but UK-pricing thin.
- **Collagen queries** — dominated by brand-owned content (Vital Proteins, Absolute Collagen) and Holland & Barrett. Comparison content thin and biased.
- **GLP-1 queries** — dominated by NHS, Boots, Numan, Juniper. Decent authority. Beatable on long-tail "Mounjaro vs Wegovy UK 2026", "Mounjaro cost private UK", "how to get Mounjaro UK private".
- **Research peptide queries** — **dominated by US clinics and US/global supplier sales pages.** UK-aware, MHRA-aware, regulator-honest content is **almost absent.** This is the largest SERP gap.

**AI Overview behaviour:** AIOs are extremely cautious on peptides. On research peptides, AIOs frequently refuse to answer or hedge with "speak to a doctor" copy. On GLP-1, AIOs cite NHS first then refuse off-label questions. On cosmetic and collagen, AIOs are happy to recommend brands. **The regulator-aware educational layer for tier 4 is the AI Visibility Gap of this whole space.**

---

## 5. The four-tier site architecture (practical IA)

```
findapeptide.co.uk/
├── /                                              # homepage — the four-tier story
├── /skincare/                                     # Tier 1 hub
│   ├── /skincare/argireline/
│   ├── /skincare/matrixyl/
│   ├── /skincare/copper-peptide/
│   ├── /skincare/best-peptide-serum-uk/           # listicle
│   ├── /skincare/best-peptide-moisturiser-uk/
│   ├── /skincare/the-ordinary-buffet-review/
│   └── /skincare/[brand]-review/                  # dynamic per brand
├── /collagen/                                     # Tier 2 hub
│   ├── /collagen/marine-vs-bovine-vs-vegan/
│   ├── /collagen/best-collagen-supplement-uk/
│   ├── /collagen/collagen-for-menopause/          # ← cross-links women's hub
│   ├── /collagen/[brand]-review/                  # dynamic per brand
├── /glp-1/                                        # Tier 3 hub — Mounjaro / Wegovy / Ozempic
│   ├── /glp-1/mounjaro-uk-private-cost/
│   ├── /glp-1/wegovy-uk-private-cost/
│   ├── /glp-1/mounjaro-vs-wegovy-vs-ozempic-uk/
│   ├── /glp-1/how-to-get-mounjaro-uk-private/
│   ├── /glp-1/mounjaro-side-effects-uk-2026/
│   ├── /glp-1/[clinic]-review/                    # dynamic per clinic
├── /research/                                     # Tier 4 hub — DISCIPLINED CONTENT ONLY
│   ├── /research/bpc-157/                         # encyclopedia
│   ├── /research/mots-c/
│   ├── /research/tesamorelin/
│   ├── /research/[peptide]/                       # dynamic per peptide (~40 entries)
│   ├── /research/uk-supplier-purity-comparison/   # research-grade purity, NOT human dosing
├── /for-women/                                    # cross-tier women's content
│   ├── /for-women/peptides-and-menopause/
│   ├── /for-women/skin-changes-perimenopause/
│   ├── /for-women/hair-density-after-40/
│   ├── /for-women/joint-pain-collagen/
│   └── /for-women/glp-1-for-women-uk/
├── /by-goal/                                      # cross-tier goal pages
│   ├── /by-goal/skin/
│   ├── /by-goal/hair/
│   ├── /by-goal/joint-recovery/
│   ├── /by-goal/sleep/
│   ├── /by-goal/weight/
│   └── /by-goal/cognition/
├── /about/
├── /how-we-review/                                # methodology
├── /editorial-policy/                             # MHRA-aware editorial promise
├── /tally-form/                                   # GLP-1 clinic-match form
└── /contact/
```

---

## 6. Programmatic scale (full-site potential)

| Cluster | Programmatic axis | Estimated URLs |
|---|---|---|
| Tier 1 cosmetic — peptide pages | per peptide ingredient × per claim | ~25 |
| Tier 1 cosmetic — brand reviews | per brand × per product line | ~120 |
| Tier 1 cosmetic — listicles | per claim × per skin concern | ~40 |
| Tier 2 collagen — brand reviews | per brand | ~30 |
| Tier 2 collagen — listicles + cost guides | per format × per claim | ~25 |
| Tier 3 GLP-1 — clinic reviews | per UK clinic × per drug | ~80 |
| Tier 3 GLP-1 — comparison + cost guides | per drug × per intent | ~40 |
| Tier 4 research — peptide encyclopedia | per peptide | ~50 |
| Tier 4 research — UK supplier comparison | per peptide × per supplier | ~120 |
| Cross-tier — women's content | per peptide × women's concern | ~40 |
| Cross-tier — by-goal | per goal × ranked recommendations | ~25 |
| Site chrome | static | ~10 |
| **Total at full scale** | | **~600 URLs** |

Smaller than FindATradey's 41,400 or the gym hub's 16,000+ because peptides is **information-density-led** not geography-led. Each page carries far more depth than a hyperlocal trade page.

---

## 7. The data model

Per peptide (tier 4 research encyclopedia is the densest record):

```json
{
  "peptide_id": "bpc-157",
  "name": "BPC-157",
  "full_name": "Body Protective Compound 157",
  "tier": "research",
  "research_areas": ["gastric ulcer healing", "tendon healing", "anti-inflammatory"],
  "mechanism_summary": "...",
  "research_status_uk": "research-grade only — not licensed for human use in UK",
  "primary_research_papers": [
    { "title": "...", "year": 2014, "url": "..." }
  ],
  "uk_suppliers": [
    {
      "supplier_name": "Direct Sarms",
      "supplier_slug": "direct-sarms",
      "purity_claim": "≥99%",
      "coa_provided": true,
      "vial_size_mg": 5,
      "price_per_vial_2026_gbp": 32,
      "shipping": "tracked UK",
      "payment_methods": ["BTC", "bank transfer"],
      "last_verified": "2026-04-28"
    }
  ],
  "regulatory_notes_uk": "Sold for research purposes only. Marketing for human consumption is regulated by MHRA under Human Medicines Regulations 2012.",
  "common_research_dosing_in_literature": "Not provided on this site — see published research papers.",
  "related_peptides": ["tb-500", "mots-c"],
  "last_data_refresh": "2026-04-28"
}
```

Per cosmetic peptide (Tier 1 — looser data):

```json
{
  "peptide_id": "argireline",
  "name": "Argireline (Acetyl Hexapeptide-8)",
  "tier": "cosmetic",
  "claim_summary": "Reduces appearance of expression lines by inhibiting muscle micro-contraction at the dermal level.",
  "evidence_summary": "Some published studies, results modest, claims vary by formulation.",
  "uk_brands_using_it": [
    { "brand": "The Ordinary", "product": "Argireline Solution 10%", "price_gbp": 6.99, "affiliate_url": "..." }
  ]
}
```

Per UK GLP-1 clinic:

```json
{
  "clinic_id": "numan",
  "name": "Numan",
  "drugs_offered": ["mounjaro", "wegovy"],
  "monthly_cost_lowest_dose_gbp": 169,
  "consultation_required": true,
  "cqc_registered_pharmacy": true,
  "gphc_pharmacy_registration": "...",
  "private_prescriber_present": true,
  "affiliate_program": true,
  "affiliate_cpa_estimate_gbp": 100,
  "last_verified": "2026-04-28"
}
```

---

## 8. Data sources

### 8.1 Free / open

| Source | What we extract | Refresh |
|---|---|---|
| MHRA register | Licensed UK products containing each peptide | Quarterly |
| GPhC pharmacy register | Verifying GLP-1 clinic registrations | Quarterly |
| CQC register | Verifying UK clinic CQC status | Quarterly |
| Brand websites | Cosmetic + collagen + clinic brand prices, formulations, claims | Monthly |
| PubMed | Research-paper IDs per peptide for the encyclopedia | Annual |
| EMA + MHRA news | Regulatory action against peptide marketers | Monthly |
| Google Trends UK | Volume direction per peptide query | Monthly |

### 8.2 Direct verification

| Source | Why | How |
|---|---|---|
| UK research-peptide suppliers | Confirming purity claims, CoA practices, payment options | Direct contact + sample CoA review (do not buy product, just review CoA) |
| UK GLP-1 clinics | Verifying registered-pharmacy + prescriber status | Public-register cross-check |
| UK collagen brands | Source country, hydrolysis method, third-party testing | Direct contact + lab-test lookup |

### 8.3 What we will NOT capture or publish

- **Human dosing protocols for research peptides.** Not on this site, ever.
- **Off-label use claims for prescription peptides.** Not on this site, ever.
- **Personal anecdote / "I took X for Y weeks" content.** Not on this site, ever.
- **Direct human-consumption marketing for tier 4 suppliers.** We reference research-grade purity and legitimate research applications. Suppliers must not be advertised in a way that contradicts their own research-only labelling.

This is the editorial discipline. It's also our regulatory shield.

---

## 9. Monetisation

### 9.1 Tier 1 — Cosmetic peptides (affiliate)

| Partner | Network | Estimated commission |
|---|---|---|
| The Ordinary / Deciem | Awin | 6–10% |
| Paula's Choice | Awin | 8–12% |
| Lookfantastic | Awin | 5–10% |
| Cult Beauty | Awin | 6–10% |
| Drunk Elephant | Impact | 8% |
| Skinceuticals | direct / Awin | 5–8% |
| Boots, John Lewis | Awin | 1–4% |
| Niod / Hada Labo | Awin | 6% |

### 9.2 Tier 2 — Collagen peptides (affiliate + own white-label)

| Partner | Channel | Estimated commission |
|---|---|---|
| Vital Proteins | Awin | 5–8% |
| Absolute Collagen | direct | up to 25% recurring |
| Revive Collagen | direct / Awin | 10–15% |
| Bare Biology | direct | 10–15% |
| Holland & Barrett | Awin | 4% |
| MyProtein | Awin | 8% |
| **Own white-label (Phase 2)** | UK supplement-factory partners | 70–80% gross margin |

### 9.3 Tier 3 — GLP-1 / prescription (clinic affiliate)

Per converted prescription lead: typically £50–200 per first-month conversion.

| Partner | Channel |
|---|---|
| Numan | Awin / direct |
| Juniper UK | Awin / direct |
| ZAVA | direct |
| Boots Online Doctor | Awin |
| MANUAL | Awin |
| Voy | direct |

### 9.4 Tier 4 — Research peptides (constrained, direct only)

- Mainstream affiliate networks **will not list these advertisers** and we should not chase that route.
- Direct relationships with UK research-peptide companies are possible (Direct Sarms, Pure Peptides UK, Aquila Peptides, Pinnacle, Nooku) at typically 10–15% commission.
- Payment must be via bank transfer or alternative rails — **do not use Stripe / PayPal as the rail for research-peptide affiliate payouts** to avoid platform-risk knock-on.
- **Recommended approach**: encyclopedia + supplier-purity comparison content, with affiliate links only on the supplier-comparison page (one page of the site, clearly framed as research-grade purity comparison). Other tier-4 pages are **non-affiliate education**.

### 9.5 Display ads

Mediavine / Raptive eligibility at 50k monthly sessions. Beauty / wellness vertical RPM is moderate (£8–15). Ads run on Tier 1 + Tier 2 + cross-tier content only — **not on Tier 4 research-peptide pages** (some ad networks decline pages adjacent to research-chemical content).

### 9.6 Email + content product (Phase 2)

A women's-wellness email list is the highest-LTV asset on this stack. Phase 2 launches:
- Email course on perimenopause + supplements (free → email capture)
- Premium digital guide (£12–24)
- Eventually own white-label collagen + cosmetic peptide skincare line

---

## 10. Tech stack

Same chassis as the FindATradey + FindAGym sites (already scaffolded under `sites/`).

| Layer | Choice |
|---|---|
| Static-site generator | Astro 4 |
| Styling | Tailwind |
| Data | JSON files in `data/` (per-tier files: cosmetic.json, collagen.json, glp1.json, research.json) |
| Maps | none needed for this site (informational, not local) |
| Analytics | Plausible (GDPR-friendly) |
| Forms | Tally — clinic-match form, supplement-match form, email signup |
| Hosting | Cloudflare Pages |
| Content updates | Markdown files for editorial overrides + JSON for structured data |

---

## 11. Build sequence (post-pilot)

### Month 1 — Pilot v0.1 (~35 URLs, locked in pilot doc)
Scope across all four tiers — proves the architecture works.

### Month 2 — Tier 1 expansion (cosmetic)
Add 8 brand-review pages, 4 listicle pages, 4 ingredient deep-dives. ~16 new URLs.

### Month 3 — Tier 2 expansion (collagen)
Add 12 brand reviews, 4 cost guides, 4 women's-cross-link pages. ~20 new URLs. Apply for white-label collagen supplier samples.

### Month 4 — Tier 3 expansion (GLP-1)
Add 30 clinic-review URLs (programmatic per UK clinic), 6 cost-guide pages. Place affiliate contracts with Numan, Juniper, ZAVA. ~36 new URLs.

### Month 5 — Tier 4 expansion (research)
Add 20 peptide encyclopedia entries, 1 UK supplier-purity-comparison hub. Legal review pre-launch. ~21 new URLs.

### Month 6 — Cross-tier (women's content)
Add 12 women's-cross-link pages, 6 by-goal pages. ~18 new URLs.

### Month 9 — Full site
~600 URLs at full scale. Email list, Phase-2 white-label launch, Mediavine application.

---

## 12. Refresh cadence

| Layer | Refresh |
|---|---|
| Brand pricing (cosmetic + collagen) | Monthly |
| Clinic pricing (GLP-1) | Monthly — these are competitive prices and change |
| Research peptide supplier prices + CoA practice | Quarterly |
| MHRA / GPhC / CQC register cross-check | Quarterly |
| Regulatory news scan | Monthly (any MHRA action against a peptide marketer = immediate review) |
| Editorial review | Annual full pass + immediate on regulatory change |

---

## 13. Year 1 success criteria

| Metric | Month 6 | Month 12 |
|---|---|---|
| URLs live | ~150 | ~600 |
| Pages indexed | ≥ 95% | ≥ 95% |
| Pages ranked top 10 | ≥ 20% | ≥ 35% |
| Monthly affiliate revenue (Tier 1 + 2) | ≥ £1k | ≥ £8k |
| Monthly clinic-affiliate revenue (Tier 3) | ≥ £1k | ≥ £10k |
| Monthly research-peptide direct affiliate (Tier 4) | ≥ £200 | ≥ £2k |
| Monthly display-ad revenue (post-Mediavine) | ≥ £500 | ≥ £4k |
| Monthly sessions | ≥ 30k | ≥ 200k |
| Email list size | ≥ 2k | ≥ 25k |
| Total monthly revenue target | ≥ £2.7k | ≥ £24k |

---

## 14. Risks + mitigations

| Risk | Mitigation |
|---|---|
| **MHRA action on tier-4 content** | Editorial discipline (no human dosing, no off-label medical claims). Pre-launch legal review. Public-register-aware research-peptide content only. Be prepared to take down individual pages if MHRA contacts us. |
| **Affiliate network deplatforming** | Diversify across Awin + Impact + direct. Keep tier-4 affiliate revenue under 30% of total — not the foundation, just a bonus tier. |
| **Payment processor freeze** | Tier 4 affiliate payouts via bank transfer only. Stripe / PayPal handle Tier 1–3 only. |
| **GLP-1 clinic compliance change** | Cross-check GPhC + CQC register quarterly. Drop clinics that lose registration immediately. |
| **AI Overview refusal of research-peptide queries** | This is actually the gap we exploit — be the cleanest UK source so we get cited when AIO does answer. Schema-rich, citation-friendly passage structure on every encyclopedia page. |
| **Competitor sites cloning our content** | Original UK supplier purity-comparison data + UK clinic verification + first-party Trustpilot scrape = compounding moat over 12+ months. |
| **Reputational risk from being "the peptides site"** | Brand voice is wellness + women's health-led, not bro-biohacker. Editorial policy page visible. CQC + GPhC + CTPA + MHRA citations on every page. We're the *responsible* peptides site. |

---

## 15. The strategic insight

If executed with discipline, this site is **the front door for a women's wellness empire**:

- Tier 1 cosmetic + Tier 2 collagen audience = women, ages 30–65, willing to pay for quality
- Tier 3 GLP-1 audience = same demographic, higher AOV, ready to spend
- Email list compounds across all four tiers
- Cross-link with a future menopause / HRT / private-GP hub becomes mutual lift
- Phase 2 white-label collagen / cosmetic peptide skincare line = own-product margin (70–80%)
- Phase 3 own-brand peptide-aware skincare or supplement product = brand asset

`findapeptide.co.uk` (or whichever domain locks) is not just a niche site. It's the ground floor of a UK women's-wellness vertical that could comfortably do £500k–£2m revenue/year at maturity, with the same chassis powering several adjacent sites (menopause hub, perimenopause coach directory, HRT clinic finder).

Don't build it thinking it's a peptide affiliate site. Build it thinking it's the trust-led women's-wellness ground floor.

---

## 16. Cross-references

- `docs/site-builds/peptides-pilot-v0.md` — locked v0.1 pilot scope (~35 URLs)
- `docs/niche-shortlist-2026-04.md` #141 — UK Peptides Hub master entry
- `docs/niche-shortlist-2026-04.md` #53 — NEW 2 Menopause/HRT (sister site, mutual cross-link)
- `docs/site-builds/gym-hub.md` §9 — affiliate-stack patterns reused here
- `docs/fleet-finance-plays.md` — fleet cross-sell opportunities (clinic operators are SMEs that need card terminals + asset finance)
- `docs/reference/lead-resale-model.md` — three-layer revenue model (this site uses all three layers)
- `docs/reference/portable-prompts.md` — research prompts for finding adjacent women's-health niches
