# FindATradey

UK trade-finder built on Astro + Tailwind. Hyperlocal programmatic — postcode-district pages × trade × intent.

## v0.1 pilot scope

- 8 postcode districts (Colchester CO1, Windsor SL4, Camberley GU15, Guildford GU1, Godalming GU7, Basingstoke RG21, Aldershot GU11, Farnborough GU14)
- 3 trades (plumber, electrician, heating engineer / boiler)
- 11 trade × intent dynamic page templates → **88 trade pages**
- 3 county hubs (Berkshire, Surrey, Hampshire) + Essex auto-listed
- 7 static / trust pages
- **Total v0.1 URLs: 99**

Full master plan: `../../docs/site-builds/findatradey.md`. Pilot spec: `../../docs/site-builds/findatradey-pilot-v0.md`.

## Stack

- [Astro](https://astro.build) static-site generator
- [Tailwind CSS](https://tailwindcss.com) styling
- [Leaflet](https://leafletjs.com) + OpenStreetMap (free, no API key) for map embeds
- [Tally](https://tally.so) (planned) for the lead form
- [Cloudflare Pages](https://pages.cloudflare.com) deployment target

## Local dev

```bash
cd sites/findatradey
npm install
npm run dev
```

## Build

```bash
npm run build
npm run preview
```

Output is in `dist/` — point Cloudflare Pages at it.

## Data files

All site data lives in `data/`:

- `data/geo/districts.json` — 8 postcode-district records (lat/lng, council, council, housing stock, neighbours)
- `data/registers/gas-safe.json` — Gas Safe register counts + top-3-by-proximity per district
- `data/registers/niceic.json` — combined NICEIC + NAPIT + ELECSA
- `data/registers/oftec.json` — oil-firing engineers
- `data/registers/mcs.json` — MCS-certified renewable installers
- `data/pricing/plumber.json`, `electrician.json`, `boiler.json` — 2026 pricing seeds per district

Register `_last_refresh` is null until the first scrape runs. Pages render gracefully with empty `top_3` arrays.

## Tally form

Each `LeadForm` action attribute references `https://tally.so/r/REPLACE_WITH_TALLY_FORM_ID`. Replace with your real Tally form IDs:

- Homeowner job-enquiry form → `LeadForm.astro` (used on every trade × district page)
- Tradesman application form → `for-tradesmen.astro`

## Routing

Page-template files using `[district].astro` generate one URL per record in `data/geo/districts.json` via `getStaticPaths`. To add a new town, add a record to that JSON file — every dynamic template picks it up automatically. **No template changes needed to scale to 50, 500 or 1,800 districts.**

## Deployment

1. Cloudflare Pages → New project → connect this repo
2. Build command: `cd sites/findatradey && npm install && npm run build`
3. Build output: `sites/findatradey/dist`
4. Domain: `findatradey.co.uk`
5. Submit `https://findatradey.co.uk/sitemap-index.xml` to Google Search Console

## Where things live

```
sites/findatradey/
├── data/                # JSON datasets (not tracked-as-secrets)
├── public/              # static assets, robots.txt, favicon
├── src/
│   ├── components/      # 11 reusable components
│   ├── layouts/         # BaseLayout + TradePage
│   ├── lib/             # types, data loaders, schema generators, FAQ templates
│   ├── pages/           # 18 page files (11 dynamic + 7 static + index)
│   └── styles/          # global.css with Tailwind directives
├── astro.config.mjs
├── package.json
├── tailwind.config.cjs
└── tsconfig.json
```

## Phase 2 expansion path

- Add 17 more districts to `data/geo/districts.json` (Reading, Slough, Bracknell, Maidenhead, etc.) → instantly 187 more URLs
- Add 3 more trades (tiler, painter, roofer) → another ~96 URLs across the existing 8 districts
- Manual data refresh hooks for the register scrapes (cron job in Cloudflare Worker recommended)
- Replace the `top_3` placeholder arrays with real Gas Safe / NICEIC scraped data
