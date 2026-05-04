# FindATradey — Pilot v0.1 (locked scope)

**Date:** April 2026
**Branch:** `claude/niche-development-setup-PJpQh`
**Companion to:** `docs/site-builds/findatradey.md` (full project plan + Geo Engine spec)

This doc locks the v0.1 build scope. Anything not in this doc is out of scope for the first ship. Once v0.1 is live and indexing, we expand using `docs/site-builds/findatradey.md` as the master plan.

---

## 1. Locked geographic scope

### Towns (postcode-district level)

| # | Town | Primary postcode district | County | Council |
|---|---|---|---|---|
| 1 | Colchester | CO1 | Essex | Colchester City Council |
| 2 | Windsor | SL4 | Berkshire | Royal Borough of Windsor & Maidenhead |
| 3 | Camberley | GU15 | Surrey *(see note)* | Surrey Heath Borough Council |
| 4 | Guildford | GU1 | Surrey | Guildford Borough Council |
| 5 | Godalming | GU7 | Surrey | Waverley Borough Council |

> **County note:** Camberley, Guildford, and Godalming are all in **Surrey** (GU postcodes), not Hampshire. Windsor is in Berkshire. The county-level pages below reflect that. If you want Hampshire coverage instead, swap in Hampshire towns (Basingstoke, Aldershot, Farnborough, Winchester, Southampton) — let me know.

### County hub pages (aggregator pages, link out to constituent towns)

| # | County | Towns covered in v0.1 | Future towns to add |
|---|---|---|---|
| 6 | Berkshire | Windsor (SL4) | Reading (RG1, RG2, RG30), Slough (SL1), Bracknell (RG12), Maidenhead (SL6), Newbury (RG14) |
| 7 | Surrey | Camberley (GU15), Guildford (GU1), Godalming (GU7) | Woking (GU21), Farnham (GU9), Reigate (RH2), Epsom (KT17) |

If you want Hampshire **as well** (option b/c from chat), add it as a third county-hub page seeded with whichever Hampshire towns we agree.

---

## 2. Trade scope (Phase 1 only for v0.1)

Only the **core 3 trades** ship in v0.1:

1. **Plumber** — emergency, leak detection, drain unblocking
2. **Electrician** — EICR, full rewire, emergency, consumer unit
3. **Boiler / heating engineer** — service, repair, new install, heat pump installer (MCS)

Tiler / painter / roofer (Phase 2 from `findatradey.md`) are **out of scope** for v0.1.

---

## 3. URL list (locked)

Each town × trade × intent = one URL. All listed below.

### Colchester (CO1)

```
/emergency-plumber/colchester-co1/
/leak-detection/colchester-co1/
/drain-unblocking/colchester-co1/
/eicr-electrician/colchester-co1/
/house-rewire/colchester-co1/
/emergency-electrician/colchester-co1/
/consumer-unit/colchester-co1/
/boiler-service/colchester-co1/
/boiler-repair/colchester-co1/
/new-boiler-install/colchester-co1/
/heat-pump-installer/colchester-co1/
```
**11 URLs**

### Windsor (SL4)

```
/emergency-plumber/windsor-sl4/
/leak-detection/windsor-sl4/
/drain-unblocking/windsor-sl4/
/eicr-electrician/windsor-sl4/
/house-rewire/windsor-sl4/
/emergency-electrician/windsor-sl4/
/consumer-unit/windsor-sl4/
/boiler-service/windsor-sl4/
/boiler-repair/windsor-sl4/
/new-boiler-install/windsor-sl4/
/heat-pump-installer/windsor-sl4/
```
**11 URLs**

### Camberley (GU15)

```
/emergency-plumber/camberley-gu15/
/leak-detection/camberley-gu15/
/drain-unblocking/camberley-gu15/
/eicr-electrician/camberley-gu15/
/house-rewire/camberley-gu15/
/emergency-electrician/camberley-gu15/
/consumer-unit/camberley-gu15/
/boiler-service/camberley-gu15/
/boiler-repair/camberley-gu15/
/new-boiler-install/camberley-gu15/
/heat-pump-installer/camberley-gu15/
```
**11 URLs**

### Guildford (GU1)

```
/emergency-plumber/guildford-gu1/
/leak-detection/guildford-gu1/
/drain-unblocking/guildford-gu1/
/eicr-electrician/guildford-gu1/
/house-rewire/guildford-gu1/
/emergency-electrician/guildford-gu1/
/consumer-unit/guildford-gu1/
/boiler-service/guildford-gu1/
/boiler-repair/guildford-gu1/
/new-boiler-install/guildford-gu1/
/heat-pump-installer/guildford-gu1/
```
**11 URLs**

### Godalming (GU7)

```
/emergency-plumber/godalming-gu7/
/leak-detection/godalming-gu7/
/drain-unblocking/godalming-gu7/
/eicr-electrician/godalming-gu7/
/house-rewire/godalming-gu7/
/emergency-electrician/godalming-gu7/
/consumer-unit/godalming-gu7/
/boiler-service/godalming-gu7/
/boiler-repair/godalming-gu7/
/new-boiler-install/godalming-gu7/
/heat-pump-installer/godalming-gu7/
```
**11 URLs**

### County hub pages

```
/county/berkshire/                  ← lists Windsor; future-proofed for Reading, Slough, Bracknell, Maidenhead, Newbury
/county/surrey/                     ← lists Camberley, Guildford, Godalming; future for Woking, Farnham, Reigate, Epsom
```
**2 URLs**

### Site-level pages

```
/                                   ← homepage
/plumber/                           ← trade landing (links to all plumber-by-district pages)
/electrician/                       ← trade landing
/heating-engineer/                  ← trade landing
/about/
/how-we-vet-tradesmen/              ← trust page (register integrations explained)
/for-tradesmen/                     ← signup landing for engineers paying for leads
/contact/
```
**8 URLs**

---

## 4. Total URL count v0.1

| Bucket | URLs |
|---|---|
| 5 towns × 11 trade URLs | 55 |
| 2 county hub pages | 2 |
| Site-level pages | 8 |
| **v0.1 total** | **65 URLs** |

Compared to the master plan's 41,400 at full scale, this is a 0.16% slice — but it's enough to prove the chassis, prove the data pipeline, prove the lead-form conversion, prove the cold-engineer outreach, and prove the SERP can be won.

---

## 5. Data needed before build

### 5.1 Geo Engine — 5 districts

For each of CO1, SL4, GU15, GU1, GU7, build the JSON record per `findatradey.md` §3:

```json
{
  "postcode_district": "CO1",
  "town": "Colchester",
  "borough_council": "Colchester City Council",
  "constituency": "Colchester",
  "region": "East of England",
  "country": "England",
  "lat": 51.8959,
  "lng": 0.8919,
  "population_2021": 26500,
  "households_2021": 11800,
  "housing_stock_dominant": "Victorian terrace + Edwardian semi",
  "median_property_year": 1900,
  "neighbouring_districts": ["CO2", "CO3", "CO4"]
}
```

Five district records total.

### 5.2 Trade overlays per district per trade

For each district × each of the 3 trades, populate:

```json
{
  "postcode_district": "CO1",
  "trade": "plumber",
  "registered_count": 0,         // populate from Gas Safe + WaterSafe scrape
  "gas_safe_count": 0,
  "watersafe_count": 0,
  "average_emergency_callout_2026_gbp": 0,   // initial estimate, refine after first 10 leads
  "median_hourly_rate_2026_gbp": 0,
  "top_3_by_proximity": [],      // populate from register search
  "last_register_refresh": "2026-04-28"
}
```

5 districts × 3 trades = **15 trade-overlay records** to populate before launch.

### 5.3 Pricing seed data (initial estimates)

Seed each price field with regional 2026 averages from the master plan, then refine after the first 10 real leads in each district. Indicative seeds:

| Trade | Emergency callout | Hourly rate |
|---|---|---|
| Plumber | £85–115 | £55–75 |
| Electrician | £75–110 | £50–70 |
| Boiler engineer | £80–120 | £55–80 |

London/Surrey premium: +20–30%. Essex: baseline. Adjust per district once we have real data.

### 5.4 FAQ data (district-specific, 4–6 entries per page = ~75 FAQ entries to write)

Template per page: 4–6 FAQs per page × 55 trade pages = **~275 FAQ entries to draft**. Most can be templated (one FAQ template per trade × intent, swap district-specific facts) so the actual unique writing is ~30 templates.

---

## 6. Astro project structure (locked for v0.1)

```
findatradey/
├── data/
│   ├── geo/
│   │   └── districts.json              # 5 districts
│   ├── registers/
│   │   ├── gas-safe.json               # populate via Gas Safe scrape
│   │   ├── niceic.json                 # NICEIC + NAPIT + ELECSA combined
│   │   ├── oftec.json
│   │   └── companies-house.json        # SIC 43.22 (plumbing), 43.21 (electrical), 43.22 (gas)
│   └── pricing/
│       ├── plumber.json
│       ├── electrician.json
│       └── boiler.json
├── src/
│   ├── pages/
│   │   ├── index.astro
│   │   ├── plumber/index.astro
│   │   ├── electrician/index.astro
│   │   ├── heating-engineer/index.astro
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
│   │   ├── heat-pump-installer/[district].astro
│   │   ├── county/[county].astro
│   │   ├── about.astro
│   │   ├── how-we-vet-tradesmen.astro
│   │   ├── for-tradesmen.astro
│   │   └── contact.astro
│   ├── components/
│   │   ├── LeadForm.astro
│   │   ├── EngineerTable.astro
│   │   ├── PriceCard.astro
│   │   ├── MapEmbed.astro
│   │   ├── FAQBlock.astro
│   │   └── TrustBlock.astro
│   ├── layouts/
│   │   ├── BaseLayout.astro
│   │   └── TradePage.astro
│   └── content/
│       └── faq/                        # markdown overrides per district if needed
└── astro.config.mjs
```

11 dynamic-route page files (one per `[district]` URL pattern) + 7 static pages = 18 Astro page files. Each dynamic file generates 5 URLs (one per district) = 55 URLs from 11 templates.

---

## 7. Build checklist (v0.1)

### Week 1 — Geo Engine + chassis

- [ ] Resolve county question (Surrey vs Hampshire vs both) and update `data/geo/districts.json` accordingly
- [ ] Build `data/geo/districts.json` with the 5 records (CO1, SL4, GU15, GU1, GU7)
- [ ] Pull 2021 Census housing stock for each district from ONS
- [ ] Scrape Gas Safe for each district (5 districts × ~30 engineers = ~150 records)
- [ ] Scrape NICEIC + NAPIT + ELECSA for each district
- [ ] Scrape OFTEC + MCS for each district
- [ ] Companies House SIC 43.22 / 43.21 lookup per district
- [ ] Build `data/registers/*.json` files

### Week 2 — Astro + first page live

- [ ] Init Astro project, Tailwind for styling, Cloudflare Pages deploy
- [ ] Build the 11 dynamic page templates (one per trade × intent)
- [ ] Build the 7 static pages (homepage, trade landings, trust, contact)
- [ ] Wire Tally lead form on every trade page
- [ ] Add LocalBusiness + FAQPage + Place + Service + BreadcrumbList schema to every page
- [ ] Push first build to Cloudflare Pages
- [ ] Domain `findatradey.co.uk` pointing to Cloudflare Pages
- [ ] Submit sitemap to Google Search Console

### Week 3 — Engineer outreach + content fill

- [ ] Cold-call 6 engineers per district per trade — 5 × 3 × 6 = **90 calls**
- [ ] Target: 3 paying engineers per district per trade = **45 engineers signed up at £25/lead**
- [ ] Backup: register as lead seller on MyBuilder Pro and Bark
- [ ] Fill in district-specific FAQ entries (~75 unique entries from ~30 templates)
- [ ] Add 2 unique paragraphs of housing-stock context per district (Layer C uniqueness)

### Week 4 — Live + monitor

- [ ] All 65 URLs indexed by end of week 4
- [ ] Search Console weekly check-in for ranking signals
- [ ] First lead-form fills measured, manual phone-back to engineers within 5 minutes
- [ ] First paid leads delivered

---

## 8. v0.1 success criteria (locked before build)

| Metric | Week 4 | Week 8 |
|---|---|---|
| Pages indexed | 100% (65/65) | 100% |
| Pages ranked top 30 | 25% (~16) | 50% (~32) |
| Pages ranked top 10 | 10% (~6) | 25% (~16) |
| Form fills total | ≥ 5 | ≥ 20 |
| Engineers paying ≥ £25/lead | ≥ 10 | ≥ 30 |
| Avg time-on-page | ≥ 60s | ≥ 90s |

Hit ≥ 4 of 6 by Week 8 → expand to 25 districts (the next wave).
Hit ≥ 5 of 6 → expand to 100 districts.
Hit < 4 → diagnose using the failure modes table in `findatradey.md` §12 before scaling.

---

## 9. Out of scope for v0.1 (explicit)

- Phase 2 trades (tiler, painter, roofer)
- Multiple districts per town (only primary district per town)
- Hampshire (unless county-question is resolved as option b/c)
- Other counties (only Berkshire + Surrey)
- Geo Engine spinoffs (findadentist, findachildminder, etc.) — those wait for chassis validation
- Affiliate sidebar (lead form first; affiliates added Week 5+)
- AdSense (last priority, post-Week 8)
- D1 database (file-based JSON only for v0.1)

---

## 10. Decisions still needed before Week 1

1. **County question** — Berkshire + Surrey (option a) confirmed? Or add Hampshire (b/c)?
2. **Domain** — `findatradey.co.uk` confirmed? (As `.com` fallback if `.co.uk` unavailable.)
3. **CPL anchor** — £25/lead for the pilot confirmed?
4. **Lead routing** — manual phone-back from you personally for the first 30 leads?
5. **Existing trade contacts** — anyone we know in any of the 5 towns who'd take leads on day 1? (Saves 2–3 days of cold outreach.)
6. **Content tone** — utilitarian / facts-first (recommended), or warmer / story-led?

Lock these → I scaffold the Astro project + write the templates next.
