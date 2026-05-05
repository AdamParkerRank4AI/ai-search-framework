# UK Gym & Fitness Hub — Colchester Pilot v0.1 (locked scope)

**Date:** April 2026
**Branch:** `claude/niche-development-setup-PJpQh`
**Companion to:** `docs/site-builds/gym-hub.md` (full UK ambition + master content model — to be written next), `docs/niche-shortlist-2026-04.md` #75, `docs/location-plays.md` §2.2.

This doc locks the v0.1 build scope. Single town: **Colchester**. The differentiator is **under-served review depth** — not "best gym in town" listicles. Once v0.1 ranks and converts, we expand using the master plan.

---

## 1. Locked geographic scope

| Town | Postcode coverage | County | Notes |
|---|---|---|---|
| Colchester | CO1, CO2, CO3, CO4 (CO5–CO7 rural — out of scope for v0.1) | Essex | All "Colchester" pages target the town as a whole; postcode used in map embed and gym address only |

---

## 2. The differentiator (this is why the site wins)

Generic UK gym ranking sites tell you which gym is cheapest. They don't tell you the things buyers actually want to know:

- **When is each gym quiet vs busy?** ("Best gym for early morning workouts" beats "Best gym in Colchester" on intent and on SERP weakness.)
- **Who actually goes there?** Estimated male / female / other split. Age bands. Beginner / intermediate / advanced ratio. Atmosphere read.
- **What's the equipment really like?** Cardio count, free-weight ceiling (kg), squat rack count, cable stations, condition, anything broken.
- **Which classes are good?** Class roster + named instructors + popularity.
- **What's it underrated for?** ("Genuinely empty 6–7am despite the 24/7 marketing", "unofficial women-friendly section in the back".)
- **What's it bad at?** ("Avoid Mondays 5–8pm — you'll wait 20 minutes for a squat rack.")

This is content AI Overviews can't write. Reddit has it scattered. Existing UK gym review sites (Which?, Student Beans listicles) don't have this depth. Capturing it once per gym, structuring it cleanly, refreshing seasonally — **that's the whole site's moat.**

---

## 3. Locked URL list (Colchester only)

The full modifier matrix from the master plan is reduced to the strongest **31 commercial intents** for v0.1, with PT directory dropped (Phase 2) and replaced with under-served-angle pages.

### A. Hub + main landings (3 URLs)

```
/                                            ← homepage (UK ambition stated, Colchester pilot)
/colchester/                                 ← Colchester hub: lists all gyms with at-a-glance cards
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
/student-gym-colchester/                     ← Essex Uni audience
/over-50s-gym-colchester/                    ← active retirement audience
```

### D. Brand reviews (8 URLs — verify Week 1 which actually exist in Colchester)

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

> **Verify before build (§7.1):** confirm which of these brands actually have a Colchester branch. Drop any that don't and add any independent gyms with material search volume.

### E. Specialism / boutique (5 URLs — PT directory dropped, Phase 2)

```
/crossfit-colchester/
/hyrox-prep-colchester/                      ← rising trend, weak SERP
/reformer-pilates-colchester/                ← rising trend
/climbing-wall-colchester/
/boxing-gym-colchester/
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

### H. Under-served angle pages (NEW — these are the differentiator) (4 URLs)

```
/quietest-gyms-colchester/                   ← when each gym is quiet by hour
/best-gym-classes-colchester/                ← class roster + named instructors comparison
/best-equipped-gym-colchester/               ← deepest equipment audit
/least-intimidating-gym-colchester/          ← for absolute beginners — almost zero competition
```

### I. Site-level (4 URLs)

```
/about/
/how-we-rate-gyms/                           ← trust + methodology page
/for-gyms/                                   ← gym signup landing for paid listings
/contact/
```

---

## 4. Total URL count v0.1

| Bucket | URLs |
|---|---|
| A. Hub + main landings | 3 |
| B. Tier / cost | 4 |
| C. Audience | 3 |
| D. Brand reviews | 8 (verify Week 1) |
| E. Specialism / boutique | 5 |
| F. Goal | 3 |
| G. Comparison | 1 |
| H. Under-served angle pages | 4 |
| I. Site-level | 4 |
| **v0.1 total** | **35 URLs** |

---

## 5. Page structure — every gym page (the under-served review template)

This is the page structure that captures the differentiator. Every `[brand]-colchester-review` page and every `/colchester/` gym profile uses this skeleton:

```
1. Title:          "[Gym name] Colchester Review 2026 — Honest take, busy times,
                    real equipment audit"
2. H1:             "[Gym name] Colchester — [one-line verdict]"

3. AT-A-GLANCE CARD (sticky on the right):
   - Tier:                     budget / mid / premium / luxury
   - Hours:                    24/7 or [specific]
   - £/month:                  £21.99 (no contract) / £35 (12-mo contract)
   - Joining fee:              £0 / £25
   - Distance from Town Hall:  1.2 miles
   - Vibe:                     quiet / medium / busy on average
   - Best for (3 tags):        e.g. "early-morning sessions", "serious lifters", "beginners"
   - CTA:                      [Get a free day pass] (Hussle affiliate link)

4. WHEN IT'S QUIET vs BUSY
   - Daily heatmap (07:00 → 22:00) sourced from Google Maps Popular Times API
   - Manual observation overlay (we visit, we measure)
   - One-line "best time to go if you hate crowds" call-out

5. WHO GOES THERE (the demographic profile section)
   - Gender split estimate: M / F / other %
   - Age bands: 18–25 / 26–40 / 41–55 / 56+
   - Beginner / intermediate / advanced split estimate
   - Atmosphere read: intimidation factor 1–5, music volume, mirror density,
     lunk-alarm-style policies if any

6. EQUIPMENT AUDIT
   - Cardio: count by type (treadmill / bike / rower / ski erg / stair / elliptical)
   - Free weights: dumbbell ceiling (kg), kettlebell range, barbell count
   - Racks: squat rack count, deadlift platform count, power cage count
   - Cable stations: count + condition
   - Functional zone: present / absent + size
   - Pool / sauna / steam: yes/no + condition
   - Anything broken or worn: noted

7. CLASS ROSTER + NAMED INSTRUCTORS
   - Class types and weekly schedule
   - Named instructors where known
   - Popularity rating per class
   - Are classes free with membership or extra?

8. BEST FOR (3–5 specific user types)
   - "Early-morning lifters — practically empty 6–7am"
   - "Serious deadlifters — only Colchester gym with two platforms"
   - "Postnatal recovery — quiet midday, good women's area"
   - etc.

9. UNDERRATED FOR (the surprising win nobody mentions)
   - 1–2 angles that almost no review surfaces
   - This is what makes the page citation-grade for AI Overviews

10. WORST FOR (2–3 user types this gym fails — DON'T SOFTEN)
    - "Avoid Mondays 17:00–20:00 — 20-minute waits for benches"
    - "No swim, no sauna — wrong gym if recovery matters"
    - This builds trust. Affiliate goodwill loss is more than offset by SEO win.

11. HONEST PROS / CONS (visible table)

12. PRICING + JOIN
    - Affiliate CTA placed only AFTER the visitor has all the facts
    - Multiple affiliate options: Hussle day pass + direct gym signup

13. MAP EMBED (Leaflet, OpenStreetMap, no Google API key)

14. RELATED GYMS IN COLCHESTER (internal link block, 4 alternatives)

15. FAQ BLOCK (FAQPage schema, 4–6 entries — district-specific)
```

Schema markup on every page:
- `LocalBusiness` (the gym)
- `Review` + `AggregateRating`
- `FAQPage`
- `Place` (Colchester)
- `BreadcrumbList`
- `OpeningHoursSpecification`

---

## 6. Data needed before build

### 6.1 Colchester gym dataset (~12–18 records)

For each gym, populate this JSON record:

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
  "open_hours_24_7": true,
  "open_hours_detail": {"mon": "00:00-24:00", ...},
  "monthly_price_2026_gbp": 21.99,
  "joining_fee_2026_gbp": 0,
  "no_contract": true,
  "facilities": ["weights", "cardio", "free_classes", "showers", "lockers"],
  "specialisms": [],

  "demographic_profile": {
    "gender_split_estimate": {"male": 60, "female": 38, "other": 2},
    "age_bands_estimate": {"18_25": 30, "26_40": 45, "41_55": 20, "56_plus": 5},
    "skill_split_estimate": {"beginner": 35, "intermediate": 50, "advanced": 15},
    "intimidation_factor_1_5": 2,
    "music_volume_1_5": 3,
    "atmosphere_notes": "Friendly, no peacocking culture, mostly committed regulars"
  },

  "popular_times": {
    "mon": [10, 15, 25, 40, 50, 65, 80, 90, 75, 60, 45, 35, 30, 25, 30, 50, 75, 95, 90, 70, 50, 35, 25, 15],
    "tue": [...],
    ...
  },

  "equipment_audit": {
    "treadmill_count": 12,
    "bike_count": 8,
    "rower_count": 6,
    "ski_erg_count": 2,
    "dumbbell_ceiling_kg": 50,
    "kettlebell_range_kg": "8-32",
    "barbell_count": 8,
    "squat_rack_count": 4,
    "deadlift_platform_count": 1,
    "power_cage_count": 2,
    "cable_station_count": 4,
    "functional_zone": "small",
    "pool": false,
    "sauna": false,
    "steam": false,
    "broken_or_worn": ["one treadmill out of order Mar-Apr 2026"]
  },

  "class_roster": [
    {"name": "Body Pump", "instructor": "Sarah K", "day": "Mon", "time": "18:30", "popularity": 5},
    {"name": "Legs Bums Tums", "instructor": "Lisa M", "day": "Tue", "time": "09:30", "popularity": 4}
  ],

  "best_for": ["early-morning lifters", "no-contract flexibility", "beginners"],
  "underrated_for": ["6-7am sessions are practically empty despite 24/7 marketing"],
  "worst_for": ["serious deadlifters (only one platform)", "swimmers (no pool)"],
  "honest_pros": [...],
  "honest_cons": [...],

  "review_count_google": 0,
  "review_avg_google": 0,
  "review_count_trustpilot": 0,
  "review_avg_trustpilot": 0,
  "last_data_refresh": "2026-04-28",
  "last_visit_date": null
}
```

The richness of this record is what every page on the site is rendered from. Generic gym sites don't capture this. **We do.**

### 6.2 Specialism / boutique studio dataset (~6–10 records)

Same shape as gym record, with `specialisms` populated and irrelevant fields blank. CrossFit box, Hyrox-prep gym, reformer pilates studios, climbing wall, boxing club.

### 6.3 Class data + instructor data

Sourced from each gym's website + Google Maps + Trustpilot reviews mining (looking for instructor names). Manual fill where needed.

### 6.4 Popular Times data

Google Maps Popular Times is publicly available per gym. Scrape weekly. ~12 gyms × 7 days × 16 hours = ~1,300 data points. Refresh quarterly minimum.

### 6.5 Manual visits (the moat, even small)

For at least the top 6 Colchester gyms, do a real visit during peak hours (Mon 18:00) and off-peak (Sat 09:00). Capture:
- Equipment count and condition (the audit)
- Atmosphere read (the demographic profile)
- A one-line "underrated for" angle nobody else has surfaced

12 visits total. ~2 hours each. Real ground-truth data. **This is what AI Overviews can't compete with.**

### 6.6 FAQ data

4–6 FAQs per page × 35 pages = ~150 entries. Most templated by category (all 8 brand-review pages share an FAQ template, swap brand-specific facts). Unique writing ≈ 25 templates.

### 6.7 Affiliate links setup (apply Week 1)

| Affiliate | Network | CPL / commission | Pages |
|---|---|---|---|
| The Gym Group | Awin | ~£8/signup | Brand review, cheap, 24-hour, day pass |
| PureGym | direct (apply) | ~£10/signup | Brand review, cheap, 24-hour, audience |
| Anytime Fitness | direct | ~£15/signup | Brand review, 24-hour |
| JD Gyms | Awin | ~£8/signup | Brand review |
| Hussle (gym pass) | direct | ~£10–20/signup | Day pass, no-contract, hub, every gym page |
| ClassPass | Impact | ~£20–40 first conversion | Boutique, reformer pilates, classes |
| MyProtein | Awin | 8% commission | Sidebar all pages |
| Gymshark | own affiliate (apply) | ~6% | Sidebar |
| Garmin / Whoop / Oura | Awin | £20–60/sale | Sidebar fitness pages |

Most need 5–10 days approval, hence Week 1 application.

---

## 7. Astro project structure (locked for v0.1)

```
findagym/
├── data/
│   ├── gyms.json                        # ~12–18 Colchester gyms (rich record)
│   ├── specialism-studios.json          # ~6–10 boutique
│   └── faq/
│       ├── tier-templates.json
│       ├── audience-templates.json
│       ├── brand-templates.json
│       ├── specialism-templates.json
│       ├── goal-templates.json
│       └── underserved-templates.json
├── src/
│   ├── pages/
│   │   ├── index.astro                  # homepage (UK ambition + Colchester pilot)
│   │   ├── colchester/index.astro       # Colchester hub
│   │   ├── best-gyms-colchester.astro
│   │   ├── cheap-gyms-colchester.astro
│   │   ├── luxury-gyms-colchester.astro
│   │   ├── 24-hour-gyms-colchester.astro
│   │   ├── gym-day-pass-colchester.astro
│   │   ├── womens-gym-colchester.astro
│   │   ├── student-gym-colchester.astro
│   │   ├── over-50s-gym-colchester.astro
│   │   ├── [brand]-colchester-review.astro     # generates 8 brand pages
│   │   ├── [specialism]-colchester.astro       # generates 5 specialism pages
│   │   ├── best-gym-[goal]-colchester.astro    # generates 3 goal pages
│   │   ├── puregym-vs-the-gym-group-colchester.astro
│   │   ├── quietest-gyms-colchester.astro      # under-served angle
│   │   ├── best-gym-classes-colchester.astro   # under-served angle
│   │   ├── best-equipped-gym-colchester.astro  # under-served angle
│   │   ├── least-intimidating-gym-colchester.astro  # under-served angle
│   │   ├── about.astro
│   │   ├── how-we-rate-gyms.astro
│   │   ├── for-gyms.astro
│   │   └── contact.astro
│   ├── components/
│   │   ├── AtAGlanceCard.astro          # sticky right-column card
│   │   ├── BusyHeatmap.astro            # popular-times heatmap
│   │   ├── DemographicProfile.astro     # gender / age / skill split
│   │   ├── EquipmentAudit.astro         # equipment table
│   │   ├── ClassRoster.astro            # classes + instructors
│   │   ├── BestForBlock.astro           # 3-5 specific user types
│   │   ├── UnderratedForBlock.astro     # the surprising angle
│   │   ├── WorstForBlock.astro          # 2-3 fail modes
│   │   ├── ProsConsTable.astro
│   │   ├── GymCard.astro                # used on listicles
│   │   ├── GymTable.astro               # sortable by price, distance, rating
│   │   ├── PriceComparator.astro
│   │   ├── MapEmbed.astro               # Leaflet, all gyms on one map
│   │   ├── LeadFormGym.astro            # gym membership enquiry
│   │   ├── LeadFormClass.astro          # class booking enquiry
│   │   ├── AffiliateBlock.astro
│   │   ├── FAQBlock.astro
│   │   └── TrustBlock.astro             # methodology / how-we-rate
│   └── layouts/
│       ├── BaseLayout.astro
│       └── GymPage.astro
└── astro.config.mjs
```

---

## 8. Build checklist (v0.1)

### Week 1 — Data + chassis

- [ ] **§7.1 Verify which gym brands are in Colchester** — drive-test the SERP for "PureGym Colchester", "JD Gyms Colchester", etc. Drop brands without a branch, add any independents
- [ ] Manual research: build `data/gyms.json` shell for ~12–18 Colchester gyms (Google Maps + brand sites + leisure centre)
- [ ] Build `data/specialism-studios.json` shell
- [ ] Apply to all affiliate programmes (Awin, Impact, direct: PureGym, Anytime Fitness, Gymshark)
- [ ] Init Astro project, Tailwind, Cloudflare Pages deploy
- [ ] Domain `findagym.co.uk` pointing
- [ ] Set up two Tally lead forms (gym enquiry + class enquiry)

### Week 2 — Templates + first pages

- [ ] Build `BaseLayout` + `GymPage` layouts
- [ ] Build all components from §7 (AtAGlanceCard, BusyHeatmap, DemographicProfile, EquipmentAudit, ClassRoster, BestForBlock, UnderratedForBlock, WorstForBlock, ProsConsTable, GymCard, GymTable, PriceComparator, MapEmbed, LeadFormGym, LeadFormClass, AffiliateBlock, FAQBlock, TrustBlock)
- [ ] Build `index.astro`, `colchester/index.astro` hub, `best-gyms-colchester.astro`
- [ ] Schema markup live (LocalBusiness × all gyms shown, FAQPage, Place, Review aggregate, OpeningHoursSpecification)
- [ ] First Cloudflare Pages deploy

### Week 3 — Manual visits + data fill + remaining pages

- [ ] **6 manual gym visits** — peak (Mon 18:00) + off-peak (Sat 09:00) for top 6 gyms. Capture equipment audit, demographic read, "underrated for" angle
- [ ] Scrape Google Maps Popular Times for all gyms
- [ ] Mine Google + Trustpilot reviews for class instructor names + atmosphere quotes
- [ ] All 8 brand review pages live (dynamic from `[brand]-colchester-review.astro`)
- [ ] All 5 specialism pages live (dynamic)
- [ ] All 3 goal pages live (dynamic)
- [ ] All 4 under-served-angle pages live (the differentiator pages)
- [ ] Comparison page (PureGym vs Gym Group Colchester)
- [ ] All 4 site-level pages
- [ ] Submit sitemap to Google Search Console

### Week 4 — Monitor + first iteration

- [ ] All 35 URLs indexed
- [ ] Search Console weekly review
- [ ] First affiliate clicks measured
- [ ] First lead-form fills measured (gym enquiries + class enquiries)
- [ ] Pitch first 3 local Colchester independent gyms for paid listings (£99–499/year)
- [ ] Iterate on under-performing pages — typically: thin "underrated for" / "worst for" sections, fix by visiting the gym again

---

## 9. v0.1 success criteria (locked before build)

| Metric | Week 4 | Week 8 |
|---|---|---|
| Pages indexed | 100% (35/35) | 100% |
| Pages ranked top 30 | 30% (~11) | 60% (~21) |
| Pages ranked top 10 | 15% (~5) | 30% (~11) |
| Affiliate clicks | ≥ 50 | ≥ 250 |
| Affiliate conversions | ≥ 2 | ≥ 12 |
| Lead-form fills | ≥ 4 | ≥ 18 |
| Local gym paying for premium listing | 0 | ≥ 1 |
| Avg time-on-page (review pages) | ≥ 90s | ≥ 150s |

Hit ≥ 5 of 8 by Week 8 → expand to 5 more towns (Chelmsford, Ipswich, Cambridge, Romford, Southend).
Hit ≥ 6 of 8 → expand to 25 towns.
Hit < 5 → diagnose before scaling.

The under-served-angle pages (§3.H) are the proxy for whether the differentiator works. If `/quietest-gyms-colchester/` and `/least-intimidating-gym-colchester/` rank top-10 fastest, the moat is real and we scale aggressively. If they don't, we need to add more depth before expanding.

---

## 10. Cash-out priority for v0.1

In order:

1. **Affiliate clicks → signups** (immediate, no relationships): Hussle, ClassPass, MyProtein, Gymshark, Garmin
2. **Brand affiliate** (need approval Week 1): Gym Group, PureGym, Anytime Fitness, JD Gyms
3. **Local gym premium listings** (£99–£499/year per gym): pitch direct to Colchester gyms in Week 4
4. **Class booking lead resale** (£10–25/lead per converted class booking): boutique studios that don't have direct affiliate
5. **Equipment / wearables affiliate** (sidebar revenue): Garmin / Whoop / Oura / Mirafit / JLL
6. **AdSense** below the fold once at 1k+ daily sessions (Month 3+)

PT directory monetisation (Phase 2 only).

---

## 11. Out of scope for v0.1 (explicit)

- **PT directory** (Phase 2 — separate page + listing model + lead resale)
- Any town other than Colchester
- The full 60-modifier matrix (using strongest 31 modifiers + 4 under-served-angle pages = 35 URLs)
- Gym equipment review section (Phase 2)
- Workout / programme content (Phase 2)
- Email list / newsletter (Phase 2)
- Recipe / nutrition content (Phase 2 — pairs with cold-plunge / supplement angle)
- Fleet cross-sell (gym-operator-side feed to Card Terminals + Asset Finance) — Phase 2 sales pitch once we have ranking data

---

## 12. Decisions — locked + open

### Locked (default decisions confirmed)

| # | Item | Locked answer |
|---|---|---|
| 1 | Domain | **`findagym.co.uk`** — UK-wide ambition; expansion to other towns won't need a new domain. (`.com` fallback if `.co.uk` is taken.) |
| 2 | Lead-form variants | **Two forms:** gym-membership enquiry (gym brand + intent) AND class-booking enquiry (boutique studios). PT enquiry is Phase 2. |
| 3 | Content tone | **Impartial, fact-led, willing to call out weaknesses.** "Worst for" and "Underrated for" sections are mandatory on every gym page. The trust premium beats short-term affiliate goodwill. |
| 4 | Reviews policy | **Honest reviews.** We use real Google + Trustpilot data + manual visits. We do NOT softpedal weaknesses to keep affiliate networks happy. If a gym is worn or crowded we say so — that's the whole moat. |
| 5 | Local listings outreach | **Week 4** (after first ranking data) — easier pitch with rankings already showing. |
| 6 | PT directory | **Phase 2** — drop from v0.1 to focus on under-served angle depth instead. |

### Still open (one item)

| # | Item | What we need from you |
|---|---|---|
| 7 | Manual visit appetite | The 6 manual gym visits in Week 3 are the moat. If you can do them yourself (you live in / near Colchester, presumably), great. If not, who does? Could be a student / freelancer for ~£200 total. |

---

## 13. Cross-references

- `docs/niche-shortlist-2026-04.md` #75 — UK Gym & Fitness Hub (master entry)
- `docs/location-plays.md` §2.2 — full UK ambition + modifier matrix
- `docs/site-builds/gym-hub.md` — full UK master plan (writing next, will live alongside this pilot doc)
- `docs/site-builds/findatradey-pilot-v0.md` — sister pilot, same Astro / Cloudflare infrastructure
- `docs/fleet-finance-plays.md` §3 — Card Terminals (gym operators are fleet feeders for Phase 2 cross-sell)
