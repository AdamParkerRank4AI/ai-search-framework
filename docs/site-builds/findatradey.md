# FindATradey — Project Plan

**Domain:** `findatradey.co.uk` (or `.com`)
**Status:** Pilot definition — April 2026
**One-line vision:** A UK-wide hyperlocal trade-finder that ranks for postcode-specific trade searches by combining open registers (Gas Safe, NICEIC, etc.) with structured local context — and routes form fills to multiple paying trade buyers per lead.

---

## 1. Two ideas, not one

This project contains **two separable assets** that need to be understood independently:

### Asset A — The Geo Engine (the real IP)

A standalone UK geo + demographics + open-register dataset, packaged as JSON/SQLite, kept fresh by automated pipelines. Once built, it powers every hyperlocal site we might want to launch — not just FindATradey.

It includes:
- 1,800 postcode districts → 9,500 wards → 391 councils → 650 constituencies
- ONS Census housing stock per district (Victorian terrace, 1930s semi, post-war estate, etc.)
- Lat/lng centroids for map embeds
- Open-register joins keyed on postcode (Gas Safe, NICEIC, Ofsted, FSA, CQC, NHS, DVSA, MCS)
- Refresh cron schedules per register (weekly / monthly / quarterly)

**Why this is its own asset:** Built once, this powers FindATradey *and* a postcode-level NHS dentist site, *and* an Ofsted childminder finder, *and* an MOT pass-rate site, *and* a flood risk site. The geo engine is the chassis; FindATradey is the first car off it.

### Asset B — FindATradey (the consumer site)

The first site that consumes the Geo Engine. Six trade verticals, programmatic per-postcode pages, lead form on every page, multi-buyer routing.

**Strategic implication:** if FindATradey works, the marginal cost of launching site #2 (e.g. `findadentist.co.uk`) is ~5 days, because the Geo Engine is already live. We are not building one site — we are building the foundation for an estate of sites.

---

## 2. The 6 trade verticals

Three "core" verticals launch first (Phase 1). Three more bolt on after the chassis is proven (Phase 2).

### Phase 1 — Core 3 (launch first)

| Trade | Why it's in Core 3 | Primary register |
|---|---|---|
| **Plumber** (emergency / leak / drainage) | Highest urgency CPL (£25–60), 24h intent, weekly refreshable register | Gas Safe + WaterSafe |
| **Electrician** (EICR / rewire / fault) | EICR mandatory for landlords (recurring annual demand), high-ticket rewire jobs | NICEIC + NAPIT + ELECSA |
| **Boiler / heating engineer** (install / service / breakdown) | Heat-pump grant trigger July 2026, breakdown emergency intent, £40–80 lead value | Gas Safe + OFTEC + MCS |

### Phase 2 — Add 3 more (after chassis proven)

| Trade | Why it's in Phase 2 | Primary register |
|---|---|---|
| **Tiler** (kitchen / bathroom / splashback) | Project-led search, high intent, less urgent | TTA member register + Companies House SIC 43.33 |
| **Painter & Decorator** (interior / exterior / Farrow & Ball) | Volume trade, repeat customers, easy lead capture | PDA + Companies House SIC 43.34 |
| **Roofer** (flat roof / pitched / lead / leak) | High-ticket emergency intent, insurance-claim adjacent | NFRC + CRC |

---

## 3. The geographic dimension

We are not picking 1,800 districts on day one. We pick **a small pilot list ourselves**, prove the model, then scale.

### Pilot district selection — your call

Pick **10 postcode districts** for the pilot. Recommended mix to stress-test the SERP across regions:

| Slot | Suggestion | Why this region matters to test |
|---|---|---|
| 1 | London urban (e.g. SW11 Battersea) | High-competition baseline |
| 2 | London inner (e.g. N1 Islington) | Repeat London test |
| 3 | Manchester urban (e.g. M14 Fallowfield) | Northern urban high-churn |
| 4 | Leeds urban (e.g. LS6 Headingley) | Northern student-heavy |
| 5 | Birmingham (e.g. B15 Edgbaston) | Midlands suburban |
| 6 | Nottingham (e.g. NG7) | Mid-size city |
| 7 | Edinburgh (e.g. EH3) | Scotland — different listing mix |
| 8 | Cardiff (e.g. CF24) | Wales — different listing mix |
| 9 | Bradford (e.g. BD3) | Cheaper Northern, less competitive |
| 10 | Truro (e.g. TR1) | Rural / Cornwall control |

Lock these (or your own 10) before build starts.

### Geographic hierarchy in the data

Each pilot district carries this minimum dataset shape:

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

This stays constant across all six trades — that's the point of the Geo Engine.

### Per-trade overlays (the Layer B data)

Each trade adds its own register-keyed payload per district:

```json
{
  "postcode_district": "SW11",
  "trade": "plumber",
  "registered_count": 47,
  "gas_safe_count": 31,
  "watersafe_count": 14,
  "average_emergency_callout_2026_gbp": 95,
  "median_hourly_rate_2026_gbp": 65,
  "top_3_by_proximity": [
    {"name": "...", "registration_id": "...", "phone": "...", "lat": "...", "lng": "..."}
  ],
  "last_register_refresh": "2026-04-28"
}
```

---

## 4. Search intent map per trade

This is the SEO playbook. Each trade has its own long-tail variants — the chassis generates them all from one template per trade.

### 4.1 Plumber

**Stem:** `[intent]-plumber-[district]`

| Intent | URL pattern | Example queries (volume) |
|---|---|---|
| Emergency / 24h | `/emergency-plumber/[district]/` | "emergency plumber sw11" (~250), "24 hour plumber n1" (~180) |
| Leak detection | `/leak-detection/[district]/` | "water leak detection ls6" (~80), "find a leak under floor m14" (~40) |
| Drainage / blockage | `/drain-unblocking/[district]/` | "blocked drain sw11" (~150), "drain unblocking near me cf24" (~70) |
| Boiler-adjacent (overlap with heating engineer) | route to heating template | — |

**Page-type per district:** 3 distinct URLs → 30 plumber URLs across the 10-district pilot.

**Why dormant:** Top 10 = Yell + Checkatrade + 2014 single-trader pages + Reddit. None say "47 Gas Safe engineers cover SW11, with 24h callout averaging £95."

### 4.2 Electrician

**Stem:** `[service]-electrician-[district]`

| Intent | URL pattern | Example queries (volume) |
|---|---|---|
| EICR (landlord-mandated) | `/eicr-electrician/[district]/` | "eicr cost sw11" (~120), "landlord eicr ls6" (~80) |
| Full rewire | `/house-rewire/[district]/` | "house rewire cost m14" (~90), "rewiring victorian terrace sw11" (~40) |
| Fault / emergency | `/emergency-electrician/[district]/` | "emergency electrician n1" (~150), "no power in house cf24" (~50) |
| Consumer unit / fuse box | `/consumer-unit/[district]/` | "fuse box upgrade ls6" (~60) |

**Page-type per district:** 4 URLs → 40 across pilot.

**Compliance angle:** EICR is now landlord-mandatory under PRS rules — this generates predictable annual demand. Pair with the Awaab's Law / damp & mould landlord audience.

### 4.3 Boiler / heating engineer

**Stem:** `[service]-boiler-[district]` or `[service]-heat-pump-[district]`

| Intent | URL pattern | Example queries (volume) |
|---|---|---|
| Boiler service | `/boiler-service/[district]/` | "boiler service sw11" (~200), "annual boiler service cost ls6" (~80) |
| Boiler breakdown | `/boiler-repair/[district]/` | "boiler not working m14" (~150), "no hot water sw11" (~120) |
| New boiler install | `/new-boiler-install/[district]/` | "new boiler quote sw11" (~250), "combi boiler installation ls6" (~80) |
| Heat pump installer (MCS) | `/heat-pump-installer/[district]/` | "heat pump installer near me bd3" (~70), "air source heat pump quote sw11" (~50) |

**Page-type per district:** 4 URLs → 40 across pilot.

**Trigger angle:** July 2026 BUS uplift to £9k for oil/LPG homes. Boiler-vs-heat-pump decision-tree pages catch the rural/off-grid audience.

### 4.4 Tiler (Phase 2)

**Stem:** `[room]-tiler-[district]`

| Intent | URL pattern | Example queries |
|---|---|---|
| Bathroom tiling | `/bathroom-tiler/[district]/` | "bathroom tiler sw11" |
| Kitchen / splashback | `/kitchen-tiler/[district]/` | "kitchen splashback tiler ls6" |
| Floor tiling | `/floor-tiler/[district]/` | "porcelain floor tiler m14" |
| Wet-room | `/wet-room-installer/[district]/` | "wet room installer sw11" |

### 4.5 Painter & decorator (Phase 2)

**Stem:** `[type]-painter-[district]`

| Intent | URL pattern |
|---|---|
| Interior painting | `/interior-painter-decorator/[district]/` |
| Exterior painting | `/exterior-painter/[district]/` |
| Wallpaper hanging | `/wallpaper-hanger/[district]/` |
| Specialist (Farrow & Ball, lime wash) | `/specialist-decorator/[district]/` |

### 4.6 Roofer (Phase 2)

**Stem:** `[type]-roofer-[district]`

| Intent | URL pattern |
|---|---|
| Roof leak / emergency | `/emergency-roofer/[district]/` |
| Flat roof repair | `/flat-roof-repair/[district]/` |
| Tile / slate replacement | `/roof-tile-repair/[district]/` |
| Lead flashing | `/lead-flashing-roofer/[district]/` |

---

## 5. Pilot URL count

| Phase | Trades | URLs per district | × 10 districts | Total URLs |
|---|---|---|---|---|
| Phase 1 (core 3) | Plumber + Electrician + Boiler | 3 + 4 + 4 = 11 | × 10 | **110 URLs** |
| Phase 2 (add 3) | + Tiler + Painter + Roofer | + 4 + 4 + 4 = 12 | × 10 | **+120 URLs** |
| Pilot complete | All 6 trades | 23 | × 10 | **230 URLs** |

If pilot succeeds and we scale to 1,800 districts:
**1,800 × 23 = 41,400 URLs** off the same chassis.

---

## 6. Page structure (every page, every trade)

The Astro template is one file per trade with the following block order. Built once, rendered 10 times in pilot, eventually 1,800 times.

```
1. <Title>: "[Service] [District] — [Town] | FindATradey"
2. <H1>: "[Service] in [District] ([Town])"
3. Live local-fact line:
     "47 Gas Safe registered engineers cover Battersea (SW11),
      with the closest 24h responders averaging £95 callout in 2026."
4. Lead form: phone-first, postcode pre-filled, 3 fields max
5. Sortable engineer/contractor table (top 3 by proximity)
6. Map embed (centred on district lat/lng)
7. Local context paragraph (housing stock + common job types)
     "SW11's housing stock is ~70% Victorian terrace.
      The most common emergency call-out in this district is..."
8. Average price ranges (sortable: callout / hourly / by job type)
9. FAQ block (FAQPage schema, 4–6 entries, district-specific)
10. Related districts (links to neighbouring postcode pages)
11. Related services (links to other trades on the same site)
12. Trust block: register logos, "verified weekly", last-refresh timestamp
```

Schema markup on every page:
- `LocalBusiness` × top 3 engineers
- `FAQPage`
- `Place` (the district)
- `Service` (the trade)
- `BreadcrumbList`

---

## 7. Data sources

### 7.1 Free / open

| Source | Coverage | Refresh | License |
|---|---|---|---|
| **ONS Postcode Directory** | All UK postcodes → district / ward / council / constituency / lat-lng | Quarterly | Open Government |
| **ONS Census 2021** | Population + housing stock per district | Static (next 2031) | Open Government |
| **Gas Safe Register** | All UK gas-safe engineers searchable by postcode | Weekly | Public search (rate-limit aware) |
| **NICEIC + NAPIT + ELECSA** | UK electricians by postcode | Weekly | Public search |
| **OFTEC** | Oil-firing engineers by postcode | Weekly | Public search |
| **MCS** | Renewable installers by postcode | Monthly | Open via api |
| **HM Land Registry Price Paid** | Property mix per postcode (build year, type) | Monthly | Open Government |
| **Companies House** | All UK trade companies by SIC code + postcode | Daily | Open via free API |

### 7.2 Crowd-sourced / scraped

| Source | What we extract | Notes |
|---|---|---|
| **Trustpilot** | Engineer review counts (per company name) | Display only; don't republish review text |
| **Google Maps** | NOT scraped (ToS) — but Place IDs OK | Use for map embed, not data |
| **Direct quote requests** | Real callout / hourly prices | Manual for pilot, automate later |

### 7.3 Refresh schedule

| Layer | Frequency | Mechanism |
|---|---|---|
| Geo Engine base | Quarterly | Cron pulling ONS update |
| Companies House overlay | Daily | API |
| Gas Safe / NICEIC / etc. | Weekly | Scrape with backoff |
| Land Registry housing | Monthly | API |
| Trustpilot review counts | Monthly | Scrape |
| Page rebuild | Triggered by any data change | Cloudflare Pages cron |

---

## 8. Monetisation

Every page has up to four revenue slots. Stack stack stack.

### 8.1 Direct lead resale (primary)

Pilot is manual:
- Form fill → Tally → Google Sheet + push notification to phone
- Within 5 minutes, you ring 3 local engineers in that district
- Engineer that takes the job pays £25 per converted lead (no conversion = no fee)

Target: 3 paying engineers per district. 30 across the 10-district pilot.

After pilot: automate via webhook → broadcast SMS to 3 buyers, first-to-claim wins, billing via Stripe weekly invoice. Per-lead price rises to £35–60 once we have data on conversion rate.

### 8.2 National lead-network fallback

Sign up as a lead seller to:
- **MyBuilder Pro** — pays per qualified lead, sets a floor while direct relationships build
- **Bark** — same model, broader category set
- **Checkatrade Premium** — slower onboarding but pays well per area

These are the safety net during the cold-engineer-outreach phase.

### 8.3 Affiliate (secondary)

Per-trade affiliate slots in the page sidebar:

| Trade | Affiliate offer | CPL |
|---|---|---|
| Plumber | HomeServe / British Gas Homecare / Hometree | £25–60 |
| Electrician | NICEIC training, EICR insurance, smoke alarm retail | £15–40 |
| Boiler | Boxt / Heatable boiler quote, BUS grant brokers | £15–60 |
| Tiler | Tile retailers (Topps Tiles, Walls and Floors) | 4–8% commission |
| Painter | Decor retail (Farrow & Ball, B&Q trade) | 3–6% commission |
| Roofer | Specialist insurance (NFRC member insurance), gutter cover | £20–50 |

### 8.4 AdSense fallback

Last priority. Below-the-fold display only. Never above the lead form. Estimated £8–15 RPM in trades vertical.

---

## 9. Tech stack

| Layer | Choice | Why |
|---|---|---|
| Static site generator | **Astro** | Best-in-class for templated programmatic; ships near-zero JS |
| Hosting | **Cloudflare Pages** | Free, fast global edge, generous build minutes |
| Domain registrar | Namecheap / Cloudflare Registrar | £10/yr |
| Form capture | **Tally** (free tier) | Webhook to Sheet + email |
| Lead routing | **Zapier** / **Make** | Webhook fan-out to SMS / email |
| Database (Phase 2) | **Cloudflare D1** | SQLite at the edge, free tier |
| Maps | OpenStreetMap (Leaflet) | No API key, no per-load cost |
| Analytics | **Plausible** or GA4 | GDPR-friendly default |
| CMS for FAQ overrides | Markdown files in repo | Cheapest possible CMS |

Repo structure:

```
findatradey/
├── data/
│   ├── geo/
│   │   ├── districts.json           # Geo Engine output
│   │   ├── housing-stock.json
│   │   └── neighbours.json
│   ├── registers/
│   │   ├── gas-safe.json
│   │   ├── niceic.json
│   │   ├── oftec.json
│   │   └── companies-house.json
│   └── pricing/
│       ├── plumber.json
│       ├── electrician.json
│       └── boiler.json
├── src/
│   ├── pages/
│   │   ├── emergency-plumber/[district].astro
│   │   ├── leak-detection/[district].astro
│   │   ├── drain-unblocking/[district].astro
│   │   ├── eicr-electrician/[district].astro
│   │   ├── house-rewire/[district].astro
│   │   ├── emergency-electrician/[district].astro
│   │   ├── consumer-unit/[district].astro
│   │   ├── boiler-service/[district].astro
│   │   ├── boiler-repair/[district].astro
│   │   ├── new-boiler-install/[district].astro
│   │   └── heat-pump-installer/[district].astro
│   ├── components/
│   │   ├── LeadForm.astro
│   │   ├── EngineerTable.astro
│   │   ├── PriceCard.astro
│   │   ├── MapEmbed.astro
│   │   └── FAQBlock.astro
│   └── layouts/
│       └── TradePage.astro
├── scripts/
│   ├── scrape-gas-safe.ts
│   ├── scrape-niceic.ts
│   ├── refresh-companies-house.ts
│   └── build-geo-engine.ts
└── astro.config.mjs
```

---

## 10. Build plan (12 weeks)

### Weeks 1–2: Geo Engine + chassis

- [ ] Build `data/geo/districts.json` for the 10 pilot districts
- [ ] Pull housing stock from ONS Census per district
- [ ] Scrape Gas Safe register for the 10 districts
- [ ] Set up Astro project, single dynamic route working end-to-end
- [ ] Lead form (Tally) live on one test page
- [ ] Cloudflare Pages deploy, domain pointing

**Exit criterion:** one test page (`/emergency-plumber/sw11/`) live, indexed, lead form working.

### Weeks 3–4: Phase 1 launch (core 3 trades)

- [ ] Generate 110 URLs across plumber + electrician + boiler × 10 districts
- [ ] All schema markup live (LocalBusiness + FAQPage + Place)
- [ ] Submit sitemap to Google Search Console
- [ ] Submit URLs for indexing

**Exit criterion:** 110 pages indexed by end of week 4.

### Weeks 5–6: Engineer outreach

- [ ] Cold-call 6 engineers per district per trade — that's 18 calls per district × 10 = 180 calls
- [ ] Target: 3 paying engineers per district per trade (90 in total)
- [ ] Backup: register as lead seller on MyBuilder Pro and Bark

**Exit criterion:** 30+ engineers signed up to receive leads at £25+ each.

### Weeks 7–10: Live + iterate

- [ ] Monitor Search Console weekly for ranking
- [ ] Fix content gaps on under-performing pages (typically: thin local context)
- [ ] Tune lead form (try shorter form, try phone-only CTA)
- [ ] Begin manual lead routing — measure conversion rate

**Exit criterion (week 10):** ≥ 30 form fills total, ≥ 10 paid leads delivered to engineers.

### Weeks 11–12: Decision gate

Hit the success criteria? → green-light Phase 2 (add tiler, painter, roofer; scale to 100 districts).
Missed criteria? → diagnose using the failure-mode table below before scaling.

---

## 11. Success criteria (locked before build)

| Metric | Week 8 | Week 12 |
|---|---|---|
| Pages indexed | 100% | 100% |
| Pages ranked top 30 | 50% | 70% |
| Pages ranked top 10 | 20% | 40% |
| Total form fills | ≥ 10 | ≥ 30 |
| Engineers paying ≥ £25/lead | ≥ 10 | ≥ 30 |
| Avg time-on-page | ≥ 90s | ≥ 120s |

Hit ≥ 4 of 6 by week 12 → scale.
Hit ≥ 5 of 6 → scale aggressively (jump to 500 districts).

---

## 12. Failure modes & responses

| Symptom | Likely cause | Fix |
|---|---|---|
| Pages indexed but not ranked | Thin / template-y | Beef up housing-stock context; add 2 unique paragraphs per district |
| Map pack owns SERP | Strong GBP signal eating organic | Pivot to a less GBP-saturated trade (EICR, heat pump) |
| Pages rank but no form fills | Form too far down / too long | Phone-first CTA above fold; one-field form |
| Form fills but trade won't pay £25 | Lead quality poor | Tighten qualification fields; reduce delivery time |
| Lead quality fine but trade won't pay | Wrong CPL anchor | Test £15 floor and £40 ceiling; find the market price |
| Pages rank in Bradford but not London | Authority gap | London pages need extra depth (more context, more reviews shown) |

---

## 13. Risks & open questions

| Risk | Mitigation |
|---|---|
| **Gas Safe / NICEIC ToS** restricts bulk display | Show *count* + *top 3 by proximity*, not full register dump |
| **Map-pack dominance** in some trades | Pilot data tells us which trades are vulnerable; pivot trade mix if needed |
| **Lead engineers don't pay** | Manual phone-back model uncovers the real price they'll pay |
| **Google's Helpful Content update** treating programmatic as spam | Layer C unique context (housing stock, common faults per era) keeps each page substantively different |
| **Trade spending power** in cost-of-living squeeze | Backup via MyBuilder Pro / Bark national networks |

---

## 14. The Geo Engine — what it becomes

Once FindATradey is live, the Geo Engine has been built. From that moment, **every future hyperlocal site we want to launch ships in days, not weeks**.

Sites already on the master register that consume the same Geo Engine:

- `findadentist.co.uk` — postcode-level NHS dentist accepting NHS patients (highest sustained UK distress search)
- `findachildminder.co.uk` — postcode Ofsted-registered childminders (monthly Ofsted refresh)
- `findaspot.co.uk` — postcode self-storage, allotments, parking
- `motpassrate.co.uk` — postcode MOT centre + pass-rate (DVSA dataset moat)
- `floodriskuk.co.uk` — postcode flood-resilience services
- `findatherapist.co.uk` — postcode BACP / UKCP / NCPS therapist finder

Each of these is a separate site. Each consumes the same Geo Engine. Each launches in **5–10 days** once the chassis is proven on FindATradey.

**The strategic insight:** FindATradey is a £30k–£100k/year revenue site. The Geo Engine that powers it is a 6-figure asset because it powers an estate of 10+ sites. Don't build FindATradey thinking it's the goal. Build it thinking it's the test rig.

---

## 15. Decisions still needed (your call)

Before build starts, lock these:

1. **The 10 pilot districts** — see §3 for a recommended mix; swap any you have a contact in
2. **Domain** — `findatradey.co.uk` confirmed?
3. **Phase 1 trade order** — recommended: plumber → electrician → boiler. Any change?
4. **Pilot CPL anchor** — recommended £25/lead. Comfortable starting there?
5. **Lead routing during pilot** — manual phone-back from you personally for first 30 leads?
6. **Existing trade contacts** — anyone we know who'd take leads on day one? (saves a week of cold outreach)

---

## 16. What "done" looks like at week 12

If pilot succeeds:
- 230 URLs live (6 trades × 10 districts × ~3.8 URLs avg)
- 30+ engineers paying £25+ per lead
- 30+ form fills, 10+ paid lead conversions
- Weekly recurring revenue from leads
- **Geo Engine validated** — ready to scale to 1,800 districts and to launch site #2

The decision at the end of the pilot isn't "did FindATradey work" — it's "is the Geo Engine real, and what site do we launch off it next?"
