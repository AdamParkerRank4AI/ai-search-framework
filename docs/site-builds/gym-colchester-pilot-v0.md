# UK Gym & Fitness Hub — Colchester Pilot v0.1 (locked scope)

**Date:** April 2026
**Branch:** `claude/niche-development-setup-PJpQh`
**Companion to:** `docs/niche-shortlist-2026-04.md` #75 (NEW 24 — UK Gym & Fitness Hub) and `docs/location-plays.md` §2.2

This doc locks the v0.1 build scope. Single town: **Colchester**. Once v0.1 ranks and converts, we expand using the master Gym & Fitness Hub plan (250 UK towns × 25 modifier combinations).

---

## 1. Locked geographic scope

| Town | Postcode coverage | County | Notes |
|---|---|---|---|
| Colchester | CO1, CO2, CO3, CO4, (CO5–CO7 rural — out of scope for v0.1) | Essex | All "Colchester" pages target the town as a whole; postcode-level segmentation only used in the map embed |

---

## 2. Locked URL list (Colchester only)

The full modifier matrix from the master plan is reduced to the **strongest 28 commercial intents** for v0.1.

### A. Hub + main landings (3 URLs)

```
/                                            ← homepage (full UK ambition stated, Colchester pilot)
/colchester/                                 ← Colchester hub: lists all gyms, all sub-pages
/best-gyms-colchester/                       ← the headline SEO page
```

### B. Tier / cost (4 URLs)

```
/cheap-gyms-colchester/                      ← budget tier
/luxury-gyms-colchester/                     ← premium tier
/24-hour-gyms-colchester/                    ← always-open
/gym-day-pass-colchester/                    ← drop-in / no-contract
```

### C. Audience (3 URLs)

```
/womens-gym-colchester/                      ← also targets "ladies-only gym colchester"
/student-gym-colchester/                     ← Essex Uni student audience
/over-50s-gym-colchester/                    ← active retirement audience
```

### D. Brand reviews (8 URLs — adjust based on which brands are actually in Colchester)

```
/puregym-colchester-review/
/the-gym-group-colchester-review/
/anytime-fitness-colchester-review/
/jd-gyms-colchester-review/
/david-lloyd-colchester-review/
/bannatyne-colchester-review/
/energie-fitness-colchester-review/
/leisure-world-colchester-review/            ← Colchester's council leisure centre
```

> **Verify before build:** Confirm which of these brands actually have a Colchester branch (Week 1 task §6.1). Drop any that don't and add any independent gyms with material search volume.

### E. Specialism / boutique (6 URLs)

```
/crossfit-colchester/
/hyrox-prep-colchester/                      ← rising trend, weak SERP
/reformer-pilates-colchester/                ← rising trend
/climbing-wall-colchester/
/boxing-gym-colchester/
/personal-trainer-colchester/                ← PT directory page
```

### F. Goal (3 URLs)

```
/best-gym-weight-loss-colchester/
/best-gym-marathon-training-colchester/
/best-gym-postnatal-colchester/
```

### G. Comparison / vs (1 URL)

```
/puregym-vs-the-gym-group-colchester/
```

### H. Site-level (4 URLs)

```
/about/
/how-we-rate-gyms/                           ← trust + methodology
/for-gyms/                                   ← gym signup landing (paid listings, lead recipients)
/contact/
```

---

## 3. Total URL count v0.1

| Bucket | URLs |
|---|---|
| A. Hub + main landings | 3 |
| B. Tier / cost | 4 |
| C. Audience | 3 |
| D. Brand reviews | 8 (verify Week 1) |
| E. Specialism / boutique | 6 |
| F. Goal | 3 |
| G. Comparison | 1 |
| H. Site-level | 4 |
| **v0.1 total** | **32 URLs** |

Compared to the master plan's 7,000+ at full scale (250 towns × full modifier matrix), this is a 0.5% slice — enough to prove the template, prove the SERP can be won at town level, and validate the affiliate stack.

---

## 4. Data needed before build

### 4.1 Colchester gym dataset

For each gym in Colchester, populate this JSON record:

```json
{
  "gym_id": "puregym-colchester-stanway",
  "name": "PureGym Colchester Stanway",
  "brand": "PureGym",
  "tier": "budget",
  "address": "...",
  "postcode": "CO3 8LH",
  "lat": 51.8835,
  "lng": 0.8640,
  "phone": "...",
  "website": "...",
  "open_hours": {"24_7": true, ...},
  "monthly_price_2026_gbp": 21.99,
  "joining_fee_2026_gbp": 0,
  "no_contract": true,
  "facilities": ["weights", "cardio", "free_classes", "showers"],
  "specialisms": [],
  "audience_flags": {
    "womens_only": false,
    "ladies_only_hours": true,
    "student_discount": true,
    "over_50s_offering": false
  },
  "review_count_google": 0,
  "review_avg_google": 0,
  "review_count_trustpilot": 0,
  "review_avg_trustpilot": 0,
  "last_data_refresh": "2026-04-28"
}
```

Estimated ~12–18 gyms in Colchester (chains + leisure + independents). Each gets a record.

### 4.2 Specialism / boutique studio dataset

Same record shape as above but with the specialism flag set. Estimated ~6–10 boutique / specialist studios in Colchester (CrossFit box, Hyrox-prep gym, reformer pilates studios, climbing wall, boxing club, hot yoga).

### 4.3 Personal trainer directory seed

For the `/personal-trainer-colchester/` page:
- Source: REPS (Register of Exercise Professionals), CIMSPA, Companies House SIC 85.51, Bark / PTHub / Trainerize public profiles
- Initial seed: ~20 named PTs with specialism, hourly rate, location, contact

### 4.4 FAQ data per page

4–6 FAQs per page × 28 main pages = ~150 FAQ entries. Most templated by category (e.g. all 8 brand-review pages share an FAQ template, swapping brand-specific facts). Unique FAQ writing ≈ 30 templates.

### 4.5 Affiliate links setup

| Affiliate | Network | CPL / commission | Pages it appears on |
|---|---|---|---|
| The Gym Group | Awin | ~£8/signup | Brand review, cheap, 24-hour, day pass |
| PureGym | direct affiliate (apply) | ~£10/signup | Brand review, cheap, 24-hour, audience |
| Anytime Fitness | direct affiliate | ~£15/signup | Brand review, 24-hour |
| JD Gyms | Awin | ~£8/signup | Brand review |
| Hussle (gym pass) | direct affiliate | ~£10–20/signup | Day pass, no-contract, hub |
| ClassPass | Impact | ~£20–40 first conversion | Boutique, reformer pilates, classes |
| MyProtein | Awin | 8% commission | Sidebar all pages |
| Gymshark | own affiliate (apply) | ~6% | Sidebar |
| Garmin / Whoop / Oura | Awin | £20–60/sale | Sidebar fitness pages |
| Origym (PT cert) | direct | £100–500/lead | PT directory page |

Sign up to all affiliate programmes Week 1 — most need 5–10 days approval.

---

## 5. Astro project structure (locked for v0.1)

```
gym-colchester/
├── data/
│   ├── gyms.json                        # ~12–18 Colchester gyms
│   ├── specialism-studios.json          # ~6–10 boutique
│   ├── personal-trainers.json           # ~20 seed PTs
│   └── faq/
│       ├── tier-templates.json
│       ├── audience-templates.json
│       ├── brand-templates.json
│       ├── specialism-templates.json
│       └── goal-templates.json
├── src/
│   ├── pages/
│   │   ├── index.astro                  # homepage
│   │   ├── colchester/index.astro       # Colchester hub
│   │   ├── best-gyms-colchester.astro
│   │   ├── cheap-gyms-colchester.astro
│   │   ├── luxury-gyms-colchester.astro
│   │   ├── 24-hour-gyms-colchester.astro
│   │   ├── gym-day-pass-colchester.astro
│   │   ├── womens-gym-colchester.astro
│   │   ├── student-gym-colchester.astro
│   │   ├── over-50s-gym-colchester.astro
│   │   ├── [brand]-colchester-review.astro     # dynamic, generates 8 brand pages
│   │   ├── [specialism]-colchester.astro       # dynamic, generates 6 specialism pages
│   │   ├── best-gym-[goal]-colchester.astro    # dynamic, generates 3 goal pages
│   │   ├── puregym-vs-the-gym-group-colchester.astro
│   │   ├── personal-trainer-colchester.astro
│   │   ├── about.astro
│   │   ├── how-we-rate-gyms.astro
│   │   ├── for-gyms.astro
│   │   └── contact.astro
│   ├── components/
│   │   ├── GymCard.astro
│   │   ├── GymTable.astro                # sortable by price, distance, rating
│   │   ├── PriceComparator.astro
│   │   ├── MapEmbed.astro                # Leaflet, all gyms on Colchester map
│   │   ├── AffiliateBlock.astro
│   │   ├── FAQBlock.astro
│   │   └── TrustBlock.astro
│   └── layouts/
│       ├── BaseLayout.astro
│       └── GymPage.astro
└── astro.config.mjs
```

---

## 6. Build checklist (v0.1)

### Week 1 — Data + chassis

- [ ] **§6.1 Verify which gym brands are in Colchester** — drive-test the SERP for "PureGym Colchester", "JD Gyms Colchester", etc. Drop brands without a branch, add any independents we missed
- [ ] Build `data/gyms.json` with ~12–18 Colchester gyms (manual research: Google Maps + brand websites + leisure centre)
- [ ] Build `data/specialism-studios.json`
- [ ] Build `data/personal-trainers.json` (REPS / CIMSPA / Bark / Trainerize seed)
- [ ] Apply to all affiliate programmes (Awin, Impact, direct: PureGym, Anytime Fitness, Gymshark, Origym)
- [ ] Init Astro project, Tailwind, Cloudflare Pages deploy
- [ ] Domain pointing
- [ ] Tally lead form set up (gym membership enquiry / PT enquiry — two forms)

### Week 2 — Templates + first pages

- [ ] Build `BaseLayout` + `GymPage` layouts
- [ ] Build `GymCard`, `GymTable`, `PriceComparator`, `MapEmbed`, `AffiliateBlock`, `FAQBlock`, `TrustBlock` components
- [ ] Build `index.astro`, `colchester/index.astro` hub, `best-gyms-colchester.astro`
- [ ] Schema markup on every page (LocalBusiness × all gyms shown, FAQPage, Place, Review aggregate)
- [ ] First Cloudflare Pages deploy

### Week 3 — Fill out the URL list

- [ ] All 4 tier/cost pages live
- [ ] All 3 audience pages live
- [ ] All 8 brand review pages (dynamic from `[brand]-colchester-review.astro`)
- [ ] All 6 specialism pages (dynamic)
- [ ] All 3 goal pages (dynamic)
- [ ] Comparison page (PureGym vs Gym Group Colchester)
- [ ] PT directory page
- [ ] All 4 site-level pages
- [ ] Submit sitemap to Google Search Console

### Week 4 — Monitor + first iteration

- [ ] All 32 URLs indexed
- [ ] Search Console weekly review
- [ ] First affiliate clicks measured
- [ ] First lead-form fills measured (gym enquiries + PT enquiries)
- [ ] Iterate on under-performing pages (typically: thin local context — fix by adding more gym-specific facts)

---

## 7. v0.1 success criteria (locked before build)

| Metric | Week 4 | Week 8 |
|---|---|---|
| Pages indexed | 100% (32/32) | 100% |
| Pages ranked top 30 | 30% (~10) | 60% (~19) |
| Pages ranked top 10 | 15% (~5) | 30% (~10) |
| Affiliate clicks | ≥ 50 | ≥ 200 |
| Affiliate conversions | ≥ 2 | ≥ 10 |
| Lead-form fills | ≥ 3 | ≥ 15 |
| Local gym paying for premium listing | 0 | ≥ 1 |

Hit ≥ 5 of 7 by Week 8 → expand to 5 more towns (Chelmsford, Ipswich, Cambridge, Romford, Southend or wherever your existing relationships sit).
Hit ≥ 6 of 7 → expand to 25 towns.
Hit < 5 → diagnose before scaling.

---

## 8. Cash-out priority for v0.1

In order of priority:

1. **Affiliate clicks → signups** (immediate, no relationships needed): Hussle, ClassPass, MyProtein, Gymshark, Garmin
2. **Brand affiliate** (need approval, applied Week 1): Gym Group, PureGym, Anytime Fitness, JD Gyms
3. **Local gym premium listings** (£99–£499/year per gym): pitch direct to Colchester gyms in Week 4 once we have ranking data to show
4. **PT directory listings** (£15–40/month per PT): pitch in Week 6+
5. **AdSense** below the fold once at 1k+ daily sessions (probably Month 3+)

Lead resale (gym membership enquiries → gym chains) is **optional** for Colchester — most chains don't run pay-per-lead and prefer affiliate. Leads to PTs and boutique studios are different and worth resale (£10–25/lead each).

---

## 9. Out of scope for v0.1 (explicit)

- Any town other than Colchester
- Per-postcode-district pages within Colchester (treat the town as one)
- The full 60-modifier matrix (just the strongest 28)
- Gym equipment review section (Phase 2)
- Workout / programme content (Phase 2)
- Email list / newsletter (Phase 2)
- Recipe / nutrition content (Phase 2 — pairs with cold-plunge / supplement angle)
- Fleet cross-sell (gym-operator-side feed to Card Terminals + Asset Finance) — Phase 2 sales pitch once we have ranking data

---

## 10. Decisions still needed before Week 1

1. **Domain** — `gymcolchester.co.uk`? `colchestergym.co.uk`? `findagym.co.uk` (UK-wide ambition)? The third gives us room to expand without redirects later.
2. **Lead-form variants** — single "find a gym" enquiry, or split (gym enquiry + PT enquiry + class enquiry)?
3. **Content tone** — informational / no-bias review (recommended for trust), or punchier opinion-led ("the best gym in Colchester for £20/month")?
4. **First-pass review angle** — affiliate-friendly (no harsh critique), or genuinely impartial (we'll lose some affiliate goodwill but rank better)?
5. **Local listings outreach** — pitch local gyms for premium listings in Week 4 (after first ranking data) or wait until Week 8 (after first conversions)?
6. **PT directory monetisation** — paid listings only, or also lead-resale?

Lock these → I scaffold the Astro project and write the templates.

---

## 11. Cross-references

- `docs/niche-shortlist-2026-04.md` #75 — UK Gym & Fitness Hub (master entry)
- `docs/location-plays.md` §2.2 — full modifier matrix and full UK ambition
- `docs/site-builds/findatradey-pilot-v0.md` — sister pilot, same Astro/Cloudflare infrastructure
- `docs/fleet-finance-plays.md` §3 — Card Terminals (gym operators are fleet feeders for Phase 2 cross-sell)
