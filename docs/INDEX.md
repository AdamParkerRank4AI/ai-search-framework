# Docs Index — Everything in one place

Every research artefact, plan, brief and reference doc, listed here so you can grab any of them to paste into another tool.

Last updated: 2026-04-26 · Branch: `claude/niche-development-setup-PJpQh`

---

## Reading order (if you've never seen this repo before)

1. **`niche-brief.md`** — the operating doc. Mode 1 framework, Five Signal Model rubric, QW/MT/LT thresholds, output template. Read this first.
2. **`niche-shortlist-2026-04.md`** — the master numbered index of every play (140 entries). Use this as the "where is X?" lookup.
3. **`fleet-finance-plays.md`** — fleet-only deep doc. BBL, FunBiz, Card Terminals, Asset Finance.
4. **`location-plays.md`** — every site where UK geography is the primary axis. Geo Engine spec.
5. **`site-builds/findatradey.md`** + **`site-builds/gym-hub.md`** — full UK master plans for the two sites we're building.
6. **`site-builds/findatradey-pilot-v0.md`** + **`site-builds/gym-colchester-pilot-v0.md`** — locked v0.1 pilot scopes.
7. **`reference/portable-prompts.md`** — six self-contained research prompts for hunting more niches in other terminals.
8. **`reference/lead-resale-model.md`** — the multi-buyer cash mechanic + cross-sell map.
9. **`reference/cpl-tools.md`** — twelve quick-CPL launch tools with affiliate stacks.

---

## File-by-file summary

### Operating layer

**`niche-brief.md`** (180 lines)
- Mode 1 (niche development partner) — default operating mode
- Five Signal Model rubric (Identity Clarity · Subject Authority · Meaning Architecture · Ecosystem Validation · Signal Consistency)
- Quick-win / Mid-term / Long-term thresholds (KD ranges, scope, signal-score gates)
- Output template Claude returns for every niche idea
- Per-platform optimisation cheat sheet (ChatGPT / Claude / Gemini / AI Overviews / Perplexity / Copilot)
- April 2026 reference data (citation behaviour, AIO statistics, etc.)

### Master inventory

**`niche-shortlist-2026-04.md`** (369 lines)
- Master numbered index — 140 entries
- Status legend (Active / Priority / Phase 2 / Parked / Dropped)
- Tag legend (QW / MT / LT / WL / YMYL / REG)
- Pattern legend (Dormant / Resurfacing / Pivoting / Long-tail / Hyperlocal / Fleet-aligned / Time-boxed / Anti-niche)
- Section 1: Existing fleet (43 entries — A-series across loans, IF, cards, agency)
- Section 2: Priority new builds (Sites 1–5)
- Section 3: High-ticket B2B + Tech (Asset Finance, Tech Directory, FindATradey)
- Section 4: NEW 1–24 (the dormant/pivoting/resurfacing wave)
- Section 5: Other active sites (Care Home Finder, Tutor Finder, Therapist Finder, British Made, Where to Buy, Trade-Only B2B, Industry Software)
- Section 6: Quick-CPL launch tools (CPL-1 to CPL-12)
- Section 7: Original B-series (kept on record)
- Section 8: Original C-series (kept on record)
- Section 9: Parked/dropped (HR, Telecoms, Cyber, Vehicle Tracking, SME Insurance, all property HT-1 to HT-7)
- Build sequence (waves W1–18+)
- April 2026 reference data

### Lane-specific deep docs

**`fleet-finance-plays.md`** (552 lines)
- §1 BBL — Business Loans (13 cluster sections, ~600 new pages on existing site)
- §2 FunBiz — Invoice Finance (7 sections, ~300 pages)
- §3 Card Terminals (13 sections including cross-sell layer, ~700 pages)
- §4 Asset Finance Hub (new build, 9 sections, ~2,000 pages)
- §5 Cross-fleet feeders (Tech Directory, FindATradey, Site 1, NEW 24 Gym, NEW 6 Cleaning, NEW 4 Visa, NEW 1–3 clinics)
- §6 Cross-sell stack table per lead source
- §7 Build sequence (fleet-only waves)
- §8 Page count summary (~3,600 new pages across the four fleet products)

**`location-plays.md`** (347 lines)
- §1 Geo Engine — the chassis (1,800 districts × 9,500 wards × 391 councils × 650 constituencies)
- §2 Active location plays (FindATradey, NEW 24 Gym, Site 2 Wedding, Care Home Finder, Tutor Finder, Therapist Finder, NEW 6 Cleaning, NEW 7 Caravan, NEW 12 Allotments, NEW 19 Pet Hydro, NEW 20 Community Sport, NEW 21 Private GP, C8 Council Tax)
- §3 Geo overlays on existing fleet sites (Site 1 planning per council, A21 web design per town, broker-language by city)
- §4 Future Geo Engine spinoffs (findadentist, findachildminder, findaspot, motpassrate, floodriskuk)
- §5 Master geographic data spec (JSON shapes)
- §6 Page count summary (~80,000+ pages across all location plays)
- §7 Build sequence (location-only waves)

### Per-site briefs (site-builds/)

**`site-builds/findatradey.md`** (524 lines)
- Full UK master plan for the trade-finder
- 16 sections: vision, two-asset framing, six trades, geographic dimension, search intent map per trade, page structure, data sources, monetisation, tech stack, 12-week build plan, success criteria, failure modes, risks, the Geo Engine, decisions, what-done-looks-like
- 41,400 URLs at full UK scale
- Companion to `findatradey-pilot-v0.md`

**`site-builds/findatradey-pilot-v0.md`** (486 lines)
- v0.1 locked scope
- 8 towns × 3 trades × 11 intents + 3 county hubs + 8 site pages = 99 URLs
- Towns: Colchester CO1, Windsor SL4, Camberley GU15, Guildford GU1, Godalming GU7, Basingstoke RG21, Aldershot GU11, Farnborough GU14
- Counties: Berkshire, Surrey, Hampshire, Essex
- Lead-gen value-prop section (the 3-vetted-engineers promise)
- Trust badges block, form-field spec
- Astro project structure (matches what's now scaffolded in `sites/findatradey/`)
- 4-week build checklist
- Success criteria + cash-out priority + out-of-scope list
- All decisions locked except existing-trade-contacts

**`site-builds/gym-hub.md`** (379 lines)
- Full UK master plan for the gym site
- 16 sections matching FindATradey's depth
- Two-asset framing (Under-Served Review Engine + findagym.co.uk)
- The differentiator: quiet times, demographics, equipment audit, best/underrated/worst-for
- Modifier matrix across 9 axes
- ~16,000 programmatic pages at full UK scale
- Data model + sources (manual visits are the moat)
- Monetisation stack (12+ affiliate partners + listing fees + display)
- 12-month build sequence (Colchester → Eastern cluster → Midlands → Scotland/Wales → full UK)
- Year 1 success criteria targeting £33k/month total revenue

**`site-builds/gym-colchester-pilot-v0.md`** (533 lines)
- Single-town locked pilot
- Strongest 28 modifier intents + 4 under-served-angle pages = 32 URLs
- Full page-template spec (at-a-glance card · busy heatmap · demographic profile · equipment audit · class roster · best/underrated/worst-for · honest pros/cons)
- Rich JSON schema per gym (the data model that powers everything)
- Manual-visits requirement (the actual moat — 6 visits per town)
- Astro project structure (matches what's now scaffolded in `sites/findagym/`)
- 4-week build checklist
- Affiliate stack with apply-Week-1 list
- All decisions locked except who-does-the-visits

**`site-builds/peptides-hub.md`** (~440 lines)
- Full UK master plan for the peptides hub (#141)
- 16 sections matching FindATradey + gym-hub depth
- **Four-tier regulatory architecture** — cosmetic / food-grade collagen / prescription GLP-1 / research-grade
- The strategic question: standalone vs inside women's-wellness umbrella (recommends standalone for Path A, with cross-link to future menopause hub)
- Audience: women 35–60 primary, longevity / biohacking secondary
- Modifier matrix per tier
- ~600 URLs at full UK scale
- Data model (per peptide / per cosmetic product / per collagen brand / per UK GLP-1 clinic / per research-supplier purity-comparison record)
- Editorial discipline rules (no human dosing on tier-4, ever)
- Monetisation stack (Awin/Impact for tier 1+2; clinic affiliate for tier 3; direct-supplier-only for tier 4; Phase-2 own white-label collagen)
- Risk register (MHRA action, affiliate deplatforming, payment-processor freeze, GLP-1 clinic compliance change, AI Overview refusal, reputational)
- Year-1 success criteria targeting £24k/month
- Strategic insight: the front door for a women's-wellness vertical worth £500k–£2m/year at maturity

**`site-builds/peptides-pilot-v0.md`** (~530 lines)
- v0.1 locked pilot scope: 35 URLs across all four tiers
- Locked: domain `findapeptide.co.uk`, brand voice (wellness-led, not bro-biohacker), editorial policy, pre-launch legal review (£1,500–3,000 budget) **required** before tier-4 pages go live
- 5 site-chrome + 8 cosmetic + 7 collagen + 8 GLP-1 + 4 research + 3 cross-tier women's = 35 URLs
- Per-tier page templates fully spec'd (TierBanner + ResearchStatusBanner the structural defenders)
- Astro project structure for `sites/findapeptide/`
- 4-week build checklist (Week 2 = legal review + editorial policy)
- v0.1 success criteria including **0 MHRA contact incidents** as the headline goal
- 4 decisions still open (lawyer choice, tier-4 risk appetite, supplier selection, writer capacity)

### Reference / portable

**`reference/portable-prompts.md`** (NEW)
- Six self-contained research prompts you can paste into another Claude / GPT / Perplexity terminal
- Prompt 1: Dormant / Resurfacing / Pivoting (generic)
- Prompt 2: Digital / tech / SaaS-focused
- Prompt 3: Long-tail aggregation / matrix patterns
- Prompt 4: Event / regulation / deadline-driven (recency window)
- Prompt 5: Anti-niche / competitor-traffic capture
- Prompt 6: Hyperlocal / per-postcode aggregation
- Each prompt fully fenced — copy-paste-ready

**`reference/lead-resale-model.md`** (NEW)
- The three-layer revenue model (big-ticket own-products / mid-ticket lead resale / low-ticket affiliate)
- Worked examples of multi-buyer routing per lead (£56–£220 per lead depending on niche)
- Cross-sell map per lead-source site
- Dormant / Resurfacing / Pivoting definitions in one place
- The "promise to the user" block that must appear above every form

**`reference/cpl-tools.md`** (NEW)
- 12 quick-CPL launch tools fully spec'd
- Affiliate stack per tool with realistic UK CPL ranges
- Build pattern (single-page tool + result page + email sequence + schema markup)
- 12-week build sequence (in waves of 3 alongside the bigger sites)
- Conservative revenue estimate (~£12k/month from CPL stack at maturity)

---

## Build artefacts (sites/)

The two sites are scaffolded in `sites/`, separate from the docs. README at `sites/README.md`.

- `sites/findatradey/` — Astro project, 99 URLs, 8 districts, 3 trades. ~51 files.
- `sites/findagym/` — Astro project, ~32 URLs, Colchester. ~38 files.

---

## Total inventory

| Category | Files | Lines |
|---|---|---|
| Operating layer | 1 | 180 |
| Master inventory | 1 | 380 |
| Lane-specific deep docs | 2 | 899 |
| Per-site briefs | 6 (FindATradey × 2, Gym × 2, Peptides × 2) | ~2,890 |
| Reference / portable | 3 | ~1,800 |
| **Docs total** | **13** | **~6,150** |
| Sites scaffolded | 89 source files (FindATradey + FindAGym) | ~10k LOC |
| **Repo total** | **102 files** | **~16k LOC** |

Every play we discussed in chat is now in a file. Every prompt is paste-ready. Every site (FindATradey, FindAGym, Peptides Hub) has a master plan + a pilot scope; FindATradey + FindAGym also have scaffolded code, Peptides Hub is docs-only awaiting your go-ahead.
