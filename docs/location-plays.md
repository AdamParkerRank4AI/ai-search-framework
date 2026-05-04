# Location Plays — Hyperlocal Programmatic

**Date:** April 2026
**Branch:** `claude/niche-development-setup-PJpQh`

This doc covers **only** the plays where UK geography is the primary programmatic axis — postcode districts, councils, wards, towns, cities, regions. Fleet-finance plays live in `docs/fleet-finance-plays.md`. The full numbered index lives in `docs/niche-shortlist-2026-04.md`.

The location plays share a chassis: the **Geo Engine**. Built once for FindATradey, reused across every site below. That chassis is what makes 17,000+ programmatic pages economically viable on Astro + Claude Code.

---

## 1. The Geo Engine (the chassis — built once, reused everywhere)

Single UK geographic + demographic dataset, packaged as JSON / SQLite, kept fresh by automated pipelines. Every location play below consumes this same chassis.

### 1.1 What's in it

- **1,800 UK postcode districts** (e.g. SW1, M1, BD3) — primary template axis
- **3,000 postcode sectors** (e.g. SW1A 1) — sub-template axis
- **9,500 wards** — finer geographic axis
- **391 councils** (county + unitary + district + London borough) — administrative axis
- **650 parliamentary constituencies** — political axis
- **1,500 towns** + ~20,000 villages — search-friendly axis
- **Lat / lng centroids** — for map embeds
- **ONS Census 2021** — population, household count, housing-stock dominant type, median property year
- **Neighbouring-district graph** — for internal-link generation between adjacent areas

### 1.2 Refresh schedule

| Layer | Frequency | Source |
|---|---|---|
| Geo base (postcode → district / ward / council / constituency / lat-lng) | Quarterly | ONS Postcode Directory |
| Census housing stock | Static (next 2031) | ONS Census 2021 |
| Land Registry housing mix | Monthly | HM Land Registry Price Paid |
| Companies House SIC overlays | Daily | CH free API |
| Open registers (Gas Safe, NICEIC, OFTEC, MCS, CQC, Ofsted, FSA, NHS) | Weekly–monthly | Public search + scrapes with backoff |

### 1.3 Why it's a strategic asset, not just a dataset

Once the chassis exists, the marginal cost of launching a new hyperlocal site is **5–10 days**, not weeks. Build FindATradey thinking it's the test rig. The Geo Engine is the asset.

Detail in `docs/site-builds/findatradey.md` §1 + §7.

---

## 2. Active location plays

Each entry below is referenced by its master-index number from `docs/niche-shortlist-2026-04.md`.

### 2.1 FindATradey — Hyperlocal trade finder
**Master index #51 · Status: Active Priority · Pattern: Hyperlocal**

- **Geographic axis:** postcode district
- **Modifier axes:** trade type × intent (emergency, EICR, rewire, service, install, leak detect, drain unblock, etc.)
- **Pilot scope:** 10 districts × 6 trades × ~3.8 URLs avg = 230 pages
- **Full-scale (post-pilot):** 1,800 districts × 23 URLs = **41,400 pages**
- **Dataset overlays:** Gas Safe + NICEIC + NAPIT + ELECSA + OFTEC + MCS + Companies House SIC
- **Refresh:** weekly per register
- **Cash-out:** direct lead resale (£25–60/lead, multi-buyer), MyBuilder Pro / Bark fallback, affiliate stack per trade, AdSense
- **Fleet feed:** trades buying leads = SMEs → BBL + Asset Finance + Card Terminals + IF (see fleet doc §5.2)

Full project plan: `docs/site-builds/findatradey.md`.

### 2.2 NEW 24 — UK Gym & Fitness Hub
**Master index #75 · Status: Active Priority · Pattern: Dormant + Pivoting + Hyperlocal**

- **Geographic axis:** UK city / town (~250 strong)
- **Modifier axes (full matrix, ~25 strongest):**
  - Brand: PureGym, The Gym Group, Anytime Fitness, JD Gyms, énergie, Snap Fitness, Gymbox, Third Space, Equinox, Nuffield Health, David Lloyd, Virgin Active, Bannatyne, Total Fitness, Everlast, Better (council)
  - Tier: budget, low-cost, premium, luxury, boutique, independent, council leisure, private members
  - Specialism: 24-hour, women's-only, ladies-only, men's, CrossFit, Hyrox-prep, F45, Barry's, Orangetheory, reformer pilates, hot yoga, climbing, calisthenics, Olympic lifting, powerlifting, bodybuilding, MMA, boxing, swimming pool gym
  - Audience: students, over 50s, beginners, post-natal, accessible, autistic-friendly, LGBT-friendly
  - Hours: 24/7, early-bird, late-opening, weekend
  - Cost: under £20/month, no contract, monthly rolling, day pass, drop-in, PAYG
  - Goal: weight loss, muscle gain, marathon prep, Hyrox prep, post-injury, postnatal, fitness over 40 / 50
- **Programmatic scale:** 250 towns × 25 modifier combinations = **6,250 pages baseline**, plus chain-vs-chain pairwise (~80 pages) plus per-brand-per-city ("PureGym Manchester review" × 800+ locations) = **~7,000+ pages**
- **Underserved sub-niches:** Hyrox-prep gyms, reformer pilates studios, climbing walls, calisthenics parks, council leisure centres (programmatic per council = dormant goldmine)
- **Cash-out stack:** gym chain affiliate (Awin/Impact £8–25/signup), Hussle (£10–20), ClassPass (£20–40), home gym equipment affiliate (high AOV), wearables (Garmin / Whoop £50+/sale), PT certification courses (£100–500 lead), independent gym listing fees (£99–499/year), supplement affiliate (MyProtein, Bulk), apparel (Gymshark), AdSense at scale
- **Fleet feed:** gym operators = SMEs → Card Terminals + EPOS + Asset Finance for equipment (every cardio machine £2–10k) + BBL for fit-out

### 2.3 Site 2 — Wedding Venues at full modifier matrix
**Master index #45 · Status: Active Priority · Pattern: Dormant + Long-tail aggregation**

- **Geographic axis:** UK county (48) + city (30 mid-tier)
- **Modifier axes (60+ strongest, the full matrix you specified):**
  - Style / type: barn, castle, country house, hotel, pub, manor, mansion, estate, marquee, registry office, town hall, garden, woodland, beach, vineyard, riverside, lakeside, urban, industrial, warehouse, church, chapel
  - Budget: cheap, budget, affordable, mid-range, luxury, exclusive, premium, under £10k, under £15k, under £20k, under £25k, under £30k, under £50k
  - Capacity: small (<50), intimate (50–80), medium (80–150), large (150–250), huge (250+)
  - Hire model: dry hire, hire only, exclusive use, all-inclusive, package deal, with accommodation, with catering, with bar, BYO
  - Time: weekday, midweek, weekend, summer, winter, off-peak, peak, last-minute
  - Audience: LGBTQ+, gay-friendly, dog-friendly, kid-friendly, accessible, wheelchair, autism-friendly, multi-faith, civil ceremony, humanist, religious
  - Theme: rustic, modern, traditional, bohemian, vintage, country, urban
- **Programmatic scale:** 100 UK locations × 25 strongest modifiers = **2,500 pages baseline**; push to 200 locations × 60 modifiers = **12,000 pages**
- **Cash-out:** venue listing fees (£200–£2,000/year), Hitched / Bridebook / Guides for Brides lead resale (£20–50/lead), wedding-loan referral on every page, suit / ring / insurance / photography affiliate, display ads
- **Tool anchor:** wedding budget calculator with finance output (CPL-12 cross-link)

### 2.4 Care Home Finder
**Master index #76 · Status: Active · Pattern: Dormant + Hyperlocal**

- **Geographic axis:** ~320 UK areas (council level)
- **Modifier axes (30+ strongest):**
  - Care type: residential, nursing, dementia, respite, palliative, end-of-life, EMI, learning disability, Parkinson's, stroke, young adult disability
  - Quality / rating: best, top 10, CQC outstanding, CQC good, 5-star
  - Funding: self-funded, local authority, NHS-funded, Continuing Healthcare
  - Budget: cheap, affordable, mid-range, luxury, premium
  - Style: small home, large, modern, country house, urban, secure unit
  - Religion / culture: Christian, Catholic, Jewish, Muslim, kosher, halal, vegetarian
  - Other: pet-friendly, married couples, LGBT-friendly
- **Programmatic scale:** 320 areas × 30 modifiers = **~9,600 pages** + 1,500 individual care-home profile pages (CQC public data)
- **Dataset:** CQC public register (the unique data moat)
- **Cash-out:** care fee planning referrals (Eldercare, Symponia — £200–500 per qualified case — **finance funnel**), care home commission (some homes pay £500–£2,000/placement), AdSense, listing fees
- **Fleet feed:** care fee planning IS a finance funnel (equity release route, deferred payment agreements, care fee annuities)

### 2.5 Tutor / Private School Finder
**Master index #77 · Status: Active · Pattern: Dormant + Hyperlocal**

- **Geographic axis:** ~200 UK towns
- **Modifier axes:** subject (25) × level (5: GCSE, A-Level, 11+, GCSE retake, undergraduate) × format (in-person, online, group, 1-1) × £/hour band
- **Programmatic scale:** 200 × 25 × 5 = ~25,000 raw cells → compress to ~3,000–4,000 high-value pages
- **Dataset:** Tutorful + MyTutor + Superprof public listings, Independent Schools Council (ISC) for private school side
- **Cash-out:** Tutorful (~25% commission), MyTutor, Superprof affiliate, school fee planning advisor referrals (high-ticket)

### 2.6 Therapist / Counsellor Finder
**Master index #78 · Status: Active · Pattern: Dormant + Hyperlocal**

- **Geographic axis:** UK city + larger town
- **Modifier axes:** specialism (anxiety, depression, couples, addiction, trauma, CBT, EMDR, psychodynamic, integrative) × cost band × format (in-person / online) × identity-affirming flags (LGBTQ-affirming, neurodivergent-affirming, POC-affirming)
- **Programmatic scale:** ~5,000 pages
- **Dataset:** BACP + UKCP + NCPS public registers
- **Cash-out:** therapist listing fees (£15–40/month for premium listings — incumbent model used by Counselling Directory and Psychology Today), private medical insurance affiliate (Vitality, Bupa)

### 2.7 NEW 6 — Niche Cleaning Trades Directory
**Master index #57 · Status: Active Priority · Pattern: Dormant + Hyperlocal + Long-tail**

- **Geographic axis:** ~250 UK towns
- **Service axis (12 underserved cleaning trades):**
  - Oven cleaning
  - Gutter cleaning
  - Jet wash / pressure wash
  - Soft wash *(rising fast 2025–2026)*
  - Render cleaning
  - Roof cleaning
  - Conservatory cleaning
  - Patio / decking cleaning
  - BBQ cleaning *(weirdly underserved)*
  - Mattress / sofa cleaning
  - Carpet cleaning
  - Hot tub install / move
- **Programmatic scale:** 12 × 250 = **3,000 pages**
- **Cash-out:** Bark, MyBuilder, Quotatis lead resale (£8–25/lead × 2–3 sales each — multi-buyer), direct local-operator deals, AdSense
- **Fleet feed:** operators = SMEs → Asset Finance for vans + jet wash kit + soft wash kit + commercial vacs · Mobile card terminals · BBL for hiring/marketing

### 2.8 NEW 7 — Caravan / Motorhome Hub
**Master index #58 · Status: Active · Pattern: Dormant + Hyperlocal**

- **Geographic axis:** UK town (~250)
- **Service axis:** motorhome storage, caravan habitation check, motorhome service, touring caravan sites (per region)
- **Programmatic scale:** 4 services × 250 towns = ~1,000 pages + insurance + finance comparison ~200 pages = **~1,200 pages**
- **Cash-out:** local storage operators (£10–30/lead × 2–4 sales), Caravan Guard / Comfort affiliate, motorhome dealer leads (£30–100/lead), specialist finance comparison (Black Horse, MotoNovo, Premium Credit) — fleet asset-finance tie-in for buyers
- **Fleet feed:** dealer side could feed Asset Finance Hub (motorhome HP)

### 2.9 NEW 12 — Allotments + Smallholdings + Heritage Trades
**Master index #63 · Status: Active · Pattern: Dormant + Hyperlocal**

- **Allotments axis:** programmatic per UK council (300+) — "allotment waiting list [council]" (all public data, weak SERPs)
- **Heritage trades axis:** thatching, lime plastering, sash window restoration, drystone walling, wattle and daub, traditional lime mortar — programmatic per UK region
- **Programmatic scale:** ~600 pages
- **Cash-out:** gardening affiliate (Crocus, Sutton's, Marshalls), AdSense, heritage-trade lead resale (small but high-margin per deal)

### 2.10 NEW 19 — Pet Hydrotherapy / Behaviour / Bereavement Hub
**Master index #70 · Status: Active or merge into Site 4 · Pattern: Dormant + Hyperlocal**

- **Geographic axis:** UK region
- **Service axis:** hydrotherapy, behaviour, bereavement counselling
- **Dataset:** CFBA / IMDT register (behaviourists), CHA / IRVAP register (hydrotherapy)
- **Programmatic scale:** ~300 pages
- **Cash-out:** practitioner listing fees, pet insurance affiliate cross-sell (heavy here)

### 2.11 NEW 20 — UK Niche Community Sport Hub
**Master index #71 · Status: Active · Pattern: Resurfacing + Hyperlocal · Absorbs Padel (NEW 8)**

- **Geographic axis:** ~100 UK cities
- **Sport axis:** padel, pickleball, walking football, run clubs, parkrun-adjacent, climbing communities, calisthenics groups
- **Programmatic scale:** ~400 pages
- **Cash-out:** equipment affiliate (HEAD, Babolat, Bullpadel, NOX for padel; running brands), club listing fees, lesson / coaching lead resale, AdSense

### 2.12 NEW 21 — UK Private GP / Independent Doctor Directory
**Master index #72 · Status: Active · Pattern: Resurfacing + Hyperlocal · YMYL-light**

- **Geographic axis:** UK city
- **Service axis:** "private GP appointment [city]", "blood tests [city]", "weight management [city]", "ADHD-aware GP [city]" *(cross-links NEW 1)*
- **Cash-out:** PrivateDoc, Babylon (now eMed), Push Doctor, ZAVA, Numan partner referrals, private medical insurance affiliate (Vitality, Bupa, AXA Health)

### 2.13 C8 — Council tax band challenge
**Master index #118 · Status: Active standalone · Pattern: Hyperlocal + Long-tail**

- **Geographic axis:** programmatic per UK council (~390)
- **Dataset:** VOA public band data
- **Programmatic scale:** ~320 pages
- **Cash-out:** AdSense + tangential affiliate (energy switching, home insurance, mortgage leads)

---

## 3. Geo overlay on existing sites (the location layer added to non-location sites)

These aren't standalone location plays, but they layer geography on top of an existing site for additional URL count and local-intent capture.

### 3.1 Site 1 — Home Improvement Hub geo overlay
**Master index #44**

- **Angle 1 — cost calculators by project × region:** 12 UK regions × 8 project types × 3 size tiers = **1,152 pages**
- **Angle 3 — planning permission per UK council:** 320 councils × 6 project types = **1,920 pages**
- **Angle 5 — permitted development per council:** 320 councils × PD-rights matrix = **~330 pages**
- **Angle 6 — grants & schemes per council:** 320 councils × 4 schemes = **1,280 pages** (ECO4, GBIS, BUS, DFG)
- **Angle 8 — Disabled Facilities Grant per council:** 320 councils × DFG page = **320 pages**
- **Total Site 1 geo layer:** ~5,000 pages

### 3.2 A21 (existing fleet) — Local web design
**Master index #40**

- "[town] web design" × 100 UK towns = ~100 pages
- "Web design for [industry] [town]" × 60 industries × top 30 towns = ~600 pages

### 3.3 Fleet broker-language by city
**Cross-references fleet-finance-plays.md §1.13 / §2.7 / §3.12 / §4.8**

- BBL: "business loan broker [city]" × 100 cities = 100 pages
- BBL sector × city: "business loan broker for [sector] [city]" — selective, ~300 pages
- IF: "invoice finance broker [city]" × 100 = 100 pages
- Card terminals: "card machine broker [city]" × 50 = 50 pages
- Asset finance: "asset finance broker [city]" × 100 = 100 pages
- **Total fleet geo layer:** ~650 pages

---

## 4. Future Geo Engine spinoffs (post-FindATradey)

Once the FindATradey pilot proves the chassis, each of these can launch in **5–10 days**. All consume the same Geo Engine.

| Domain | What it does | Dataset moat | Cash-out |
|---|---|---|---|
| **findadentist.co.uk** | Postcode NHS dentist accepting NHS patients | NHS Dentist Search API + sustained UK distress search ("NHS dentist near me" is a top zero-click trigger) | Private dentist clinic PPL fallback, dental finance affiliate, oral hygiene affiliate |
| **findachildminder.co.uk** | Postcode Ofsted-registered childminders | Ofsted public register, monthly refresh | Childminder listing fees, childcare voucher affiliate, parental insurance |
| **findaspot.co.uk** | Postcode self-storage, allotments, parking, garage rental | Storage operator scrapes, council allotment data, JustPark / YourParkingSpace API | Storage operator PPL, JustPark affiliate, parking affiliate |
| **motpassrate.co.uk** | Postcode MOT centre + first-time pass rate | DVSA public dataset (the moat — single-source data) | MOT centre directory listing fees, car insurance affiliate, breakdown affiliate |
| **floodriskuk.co.uk** | Postcode flood-resilience services + Environment Agency risk overlay | EA flood-risk API + property-resilience installer scrapes | Flood-resilience installer PPL, flood insurance broker referral, sandbag affiliate |
| **findatherapist.co.uk** | Postcode BACP / UKCP / NCPS therapist finder (overlaps NEW Therapist Finder #78 — would merge or rationalise) | BACP + UKCP + NCPS registers | Therapist listing fees, private medical insurance affiliate |

---

## 5. Master geographic data spec (shared across all plays above)

Per-postcode-district minimum payload:

```json
{
  "postcode_district": "SW11",
  "town": "Battersea",
  "borough_council": "Wandsworth",
  "constituency": "Battersea",
  "region": "London",
  "country": "England",
  "lat": 51.4717,
  "lng": -0.1665,
  "population_2021": 87000,
  "households_2021": 38500,
  "housing_stock_dominant": "Victorian terrace",
  "median_property_year": 1895,
  "neighbouring_districts": ["SW8", "SW18", "SW6", "SW4"]
}
```

Per-service overlay (varies by site):

```json
{
  "postcode_district": "SW11",
  "service": "plumber",
  "registered_count": 47,
  "register_breakdown": {"gas_safe": 31, "watersafe": 14},
  "average_callout_2026_gbp": 95,
  "median_hourly_rate_2026_gbp": 65,
  "top_3_by_proximity": [...],
  "last_register_refresh": "2026-04-28"
}
```

Refresh schedule per data layer documented in `docs/site-builds/findatradey.md` §7.3.

---

## 6. Page count summary (location plays only)

| Site | Status | Programmatic pages |
|---|---|---|
| FindATradey (#51) | Active Priority | 41,400 at full scale (230 pilot) |
| NEW 24 Gym & Fitness (#75) | Active Priority | ~7,000 |
| Site 2 Wedding Venues (#45) | Active Priority | 2,500 baseline → 12,000 max |
| Care Home Finder (#76) | Active | ~9,600 + 1,500 profiles |
| Tutor / School Finder (#77) | Active | ~3,000–4,000 |
| Therapist Finder (#78) | Active | ~5,000 |
| NEW 6 Cleaning Trades (#57) | Active Priority | ~3,000 |
| NEW 7 Caravan / Motorhome (#58) | Active | ~1,200 |
| NEW 12 Allotments + Heritage (#63) | Active | ~600 |
| NEW 19 Pet Hydrotherapy (#70) | Active or merge | ~300 |
| NEW 20 Community Sport (#71) | Active | ~400 |
| NEW 21 Private GP Directory (#72) | Active | ~600 |
| C8 Council tax band challenge (#118) | Active | ~320 |
| **Subtotal — pure location sites** | | **~74,000+ pages** |
| Site 1 geo overlay | Layer on existing | ~5,000 |
| A21 web design geo | Layer on existing | ~700 |
| Fleet broker-language by city | Layer on existing | ~650 |
| **Subtotal — geo overlays** | | **~6,350 pages** |
| **Total location-play pages across all sites** | | **~80,000+ pages** |

That is what the Geo Engine unlocks.

---

## 7. Build sequence — location plays only

| Wave | Work |
|---|---|
| **W1–2** | Geo Engine v1 build (10 pilot postcode districts, ONS data, Census housing stock). FindATradey Astro project skeleton. Tally lead form. Cloudflare Pages deploy. |
| **W3–4** | FindATradey Phase 1 — 110 URLs across plumber + electrician + boiler × 10 districts. **NEW 6 Cleaning Trades** template seeded — first 3 services × 50 towns = 150 pages. |
| **W5–6** | FindATradey engineer outreach. **NEW 24 Gym & Fitness** — first 50 cities × top 10 modifiers = 500 pages. **Site 2 Wedding** — 48 county-level cost pages + 30 city-level. |
| **W7–10** | Geo Engine expand to 100 districts. FindATradey Phase 2 — add 3 more trades. **Care Home Finder** stand-up — 50 areas × top 10 modifiers = 500 pages. **NEW 6** complete — 12 services × 250 towns = 3,000 pages. **C8 Council tax** programmatic per council = 320 pages. |
| **W9–12** | FindATradey scale to 500 districts (if pilot passes). **NEW 24 Gym** scale to 250 cities × full modifier matrix. **Site 2 Wedding** modifier expansion to 2,500 pages. **NEW 7 Caravan/Motorhome** stand-up. **Site 1 Home Improvement** geo overlay (planning + grants + DFG per council, the programmatic monsters). |
| **W12–18** | **Tutor / School Finder**, **Therapist Finder**, **NEW 12 Allotments**, **NEW 19 Pet Hydrotherapy** (or merge into Site 4), **NEW 20 Community Sport**, **NEW 21 Private GP**. Fleet broker-language city layer added across BBL / FunBiz / Card Terminals / Asset Finance. |
| **Phase 2 (M5+)** | **Geo Engine spinoffs** — findadentist, findachildminder, findaspot, motpassrate, floodriskuk. Each ships in 5–10 days once chassis is proven. |

---

## 8. Cross-references

- `docs/site-builds/findatradey.md` — full FindATradey + Geo Engine project plan
- `docs/fleet-finance-plays.md` — fleet content plays (BBL / FunBiz / Card Terminals / Asset Finance) including geo overlays §1.13, §2.7, §3.12, §4.8
- `docs/niche-shortlist-2026-04.md` — master numbered index of all 140 plays
- `docs/niche-brief.md` — Mode 1 operating doc (Five Signal Model, QW/MT/LT thresholds)

---

## 9. What this is not

This doc is location-plays-only. The non-geographic plays (CPL tools, audience-driven niches like ADHD/Menopause/TRT, brand-driven niches, white-label products, broader fleet content) are tracked in their own docs.

The plays here all share the **Geo Engine chassis**. That chassis is the strategic asset; the individual sites are configurations of it.
