# FindAGym

Honest UK gym reviews on Astro + Tailwind. Pilot live in Colchester.

## v0.1 pilot scope

- Single town: **Colchester** (CO1–CO4)
- 4 gym profiles + 2 specialism studios in `data/gyms/colchester.json` (verify Week 1; add independents)
- 16 listicle pages from one shared template (`[listicle].astro` + `lib/listicles.ts`)
- 5 specialism pages from one shared template (`[specialism]-colchester.astro`)
- 4 brand-review pages from one shared template (`[brand]-colchester-review.astro`)
- 1 vs comparison (`puregym-vs-the-gym-group-colchester.astro`)
- Colchester town hub
- 4 site-level pages (about, how-we-rate, for-gyms, contact)
- **Total v0.1 URLs: ~31** (16 listicles + 5 specialisms + 4 brand reviews + 1 vs + 1 hub + 1 home + 4 trust = 32)

Full master plan: `../../docs/site-builds/gym-hub.md`. Pilot spec: `../../docs/site-builds/gym-colchester-pilot-v0.md`.

## The differentiator

Generic gym ranking sites tell you which is cheapest. We tell you what readers actually want to know:

- **Quiet times** — daily heatmap from Google Maps Popular Times + manual observation
- **Demographic profile** — gender split, age bands, beginner/intermediate/advanced ratio, atmosphere read, intimidation factor 1–5
- **Equipment audit** — cardio counts, dumbbell ceiling, squat racks, deadlift platforms, broken/worn notes
- **Best for / Underrated for / Worst for** — three honest blocks per gym, the "worst for" is the trust play
- **Honest pros & cons** — visible table

All rendered from one rich JSON record per gym. Page templates pull what they need.

## Stack

- [Astro](https://astro.build), [Tailwind](https://tailwindcss.com), [Leaflet](https://leafletjs.com) + OSM, [Tally](https://tally.so) (planned), Cloudflare Pages.

## Local dev

```bash
cd sites/findagym
npm install
npm run dev
```

## Build

```bash
npm run build
npm run preview
```

## Data files

- `data/gyms/colchester.json` — Colchester gyms + specialism studios with full schema
- (Future) `data/gyms/<town>.json` — one file per UK town as we expand

## Tally form

Replace `https://tally.so/r/REPLACE_WITH_GYM_FORM_ID` and `https://tally.so/r/REPLACE_WITH_GYM_OPERATOR_FORM_ID` once Tally forms are set up.

## Routing

- `[brand]-colchester-review.astro` → 1 page per `gym.brand_slug` in `data/gyms/colchester.json`
- `[listicle].astro` → 1 page per config in `lib/listicles.ts` (16 configs in v0.1)
- `[specialism]-colchester.astro` → 1 page per entry in the SPECIALISMS array in that file (5 in v0.1)

To add a new town, drop in a new `data/gyms/<town>.json` and clone the routes — full master plan in `gym-hub.md` walks the multi-town expansion.

## Deployment

1. Cloudflare Pages → New project → connect this repo
2. Build command: `cd sites/findagym && npm install && npm run build`
3. Build output: `sites/findagym/dist`
4. Domain: `findagym.co.uk`
5. Submit `https://findagym.co.uk/sitemap-index.xml` to Google Search Console

## Where things live

```
sites/findagym/
├── data/gyms/colchester.json    # rich gym dataset
├── public/                      # robots.txt, favicon
├── src/
│   ├── components/              # 11 components inc. AtAGlanceCard, BusyHeatmap, DemographicProfile, EquipmentAudit, HonestVerdict
│   ├── layouts/                 # BaseLayout + GymPage
│   ├── lib/                     # types, data loaders, schema, listicle config
│   ├── pages/                   # index, town hub, dynamic templates, static trust pages
│   └── styles/                  # global.css with Tailwind
├── astro.config.mjs
├── package.json
├── tailwind.config.cjs
└── tsconfig.json
```

## Phase 2 expansion path

- Add data/gyms/chelmsford.json, ipswich.json, etc. — one file per town
- Replicate Colchester URL patterns per town
- Manual visit at peak + off-peak per gym (the moat)
- User-submitted reviews (CMS via Cloudflare D1, Phase 2)
- PT directory (Phase 2)
- Equipment review section, workout content, recipes (Phase 2)
