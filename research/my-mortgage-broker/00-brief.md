# My Mortgage Broker Ltd — Site Build Brief

**Project:** New site build for post-merger entity (SEO + AI Search + AI Overviews)
**Framework:** Rank4AI Five Signal Model (see root `README.md`)
**Research date:** April 2026
**Branch:** `claude/research-seo-ai-search-dVqp6`

---

## Trigger

Client letter dated April 2026, signed by Rishi Bansropun and Oliver Gwinnell, announcing that **RB Financial Advisers Ltd** is merging into **My Mortgage Broker Ltd** from **1 April 2026**. Clients are instructed that they will begin to receive correspondence from the new firm. Going forward all activity consolidates under a single brand.

This is an **entity-consolidation event** — the highest-risk moment in the Rank4AI framework. Two pre-existing entities, each with their own identity graph, directory footprints, review histories, FCA references, registered addresses and client letters, must be merged into one coherent signal set without triggering graph drift (Signal 05) or misclassification (Signal 01).

## Post-merger entity (per client letter)

- **Trading name:** My Mortgage Broker Ltd
- **Trading address:** Lodge Park Business Centre, Lodge Lane, Langham, Colchester, CO4 5NE
- **Phone:** 01206 370 018
- **Directors:** Rishi Bansropun, Oliver Gwinnell
- **Mobiles:** 07816 168 807 (Rishi), 07971 008 896 (Oliver)
- **Email:** Rishi@mymortgagebroker.co.uk, Oliver@mymortgagebroker.co.uk
- **Claimed history:** "over 15 years of experience"; combined team "more than 60 years of industry expertise"

## Scope of this research pack

This folder contains the baseline research used to design the new site build:

| File | Purpose |
|------|---------|
| `00-brief.md` | This file |
| `01-entity-audit.md` | Entity facts, contradictions and reconciliation plan (Signal 01) |
| `02-digital-presence-audit.md` | Current websites, directories, reviews, socials (Signal 04) |
| `03-competitive-landscape.md` | Colchester / Essex mortgage broker SERP and AI answer field |
| `04-ai-search-sector-signals.md` | AI Overviews / YMYL / E-E-A-T signals specific to UK mortgage advice |
| `05-site-build-recommendations.md` | Signal-by-signal build plan mapped to Rank4AI |
| `06-sources.md` | Source URLs used during research |

## Headline findings (preview)

1. **Address mismatch risk.** Companies House registered office for My Mortgage Broker Limited (09296120) is recorded as *Unit 4 99 London Road, Stanway, Colchester CO3 0NY*, while the client letter and current website use *Lodge Park Business Centre, Lodge Lane, Langham, Colchester CO4 5NE*. Until Companies House is updated, NAP consistency cannot be claimed.
2. **FCA authorisation ambiguity.** Independent directory listings describe the firm as an Appointed Representative of Sesame (FCA 795866); the current About page text claims "Directly authorised by the FCA". This contradiction is the single largest identity risk for a YMYL firm and must be resolved before any new content is published.
3. **"15 years" claim.** Companies House incorporation is **5 November 2014** (~11 years). The 15-year claim most likely refers to Oliver's personal track record. Public-facing copy must phrase this precisely to survive fact-checking by AI systems that cross-reference Companies House.
4. **Two overlapping brands, two review graphs, one address.** RB Financial Advisers Ltd (19a London Road CO3 0NH, FCA 764864, ~5.0 on 34 Google reviews) and My Mortgage Broker Ltd (CO4 5NE, ~4.85 on 22 Trustpilot reviews) each carry independent reputational signals. Both must be preserved and redirected into the surviving entity.
5. **Colchester is a saturated market.** Strong incumbents include We Are Mortgages, Fitch & Fitch, Mortgage321, Woodhall Mortgages, HD Consultants and fee-free players like YesCanDo. Several already publish long-form educational content and have a denser schema stack. Displacement requires a clear subject-authority wedge rather than generic "Colchester mortgage broker" content.
6. **AI Overviews favour structured informational content.** Network brands (London & Country, Habito, John Charcol) dominate AI recommendations because of directory density and press citations. An independent local broker can compete only with tight E-E-A-T, explicit FCA validation, and RAG-ready passages.

See the individual files for evidence and recommended actions.
