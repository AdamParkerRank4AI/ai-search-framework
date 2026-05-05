# Sites

Astro projects scaffolded from the niche development plan. Each site is independent — its own `package.json`, build, deploy target — but they share a top-level repo for now. Split into separate repos later if you want.

## v0.1 sites

| Folder | Domain | Status | Pilot URL count | Master plan |
|---|---|---|---|---|
| `findatradey/` | `findatradey.co.uk` | v0.1 scaffolded | 99 URLs (8 towns × 3 trades × 11 intents + 3 county hubs + 8 site pages) | `../docs/site-builds/findatradey.md` |
| `findagym/` | `findagym.co.uk` | v0.1 scaffolded | ~32 URLs (Colchester pilot, 16 listicles + 5 specialisms + 4 brand reviews + 1 vs + 6 chrome) | `../docs/site-builds/gym-hub.md` |

## Common stack

- [Astro 4](https://astro.build) — static site generator, near-zero JS, fast builds
- [Tailwind CSS](https://tailwindcss.com) — utility-first styling
- [Leaflet](https://leafletjs.com) + [OpenStreetMap](https://www.openstreetmap.org) — free maps, no API key
- [Tally](https://tally.so) — lead form (planned, replace form IDs)
- [Cloudflare Pages](https://pages.cloudflare.com) — deployment target

## Local dev

```bash
# pick a site
cd sites/findatradey   # or sites/findagym

npm install
npm run dev
```

Each site runs on its own port (default `4321`).

## Build

```bash
cd sites/findatradey
npm run build
npm run preview
```

Output is in `sites/<site-name>/dist/`.

## Deployment

Each site gets its own Cloudflare Pages project:

1. Cloudflare Pages → Create project → connect this repo
2. Set the **build command** to: `cd sites/findatradey && npm install && npm run build` (or `findagym`)
3. Set the **build output directory** to: `sites/findatradey/dist`
4. Point the custom domain to the Pages project

Run two Pages projects against the same repo — one per site.

## Repo layout (sites only — see top-level README for full repo)

```
sites/
├── findatradey/
│   ├── astro.config.mjs
│   ├── package.json
│   ├── tailwind.config.cjs
│   ├── tsconfig.json
│   ├── data/                # JSON datasets (geo, registers, pricing)
│   ├── public/              # static assets, robots.txt, favicon
│   └── src/
│       ├── components/      # LeadForm, EngineerTable, FAQBlock, etc.
│       ├── layouts/
│       ├── lib/             # types, data loaders, schema, FAQ generators
│       ├── pages/
│       └── styles/
└── findagym/
    ├── astro.config.mjs
    ├── package.json
    ├── tailwind.config.cjs
    ├── tsconfig.json
    ├── data/gyms/           # rich gym datasets (one file per town)
    ├── public/
    └── src/
        ├── components/      # AtAGlanceCard, BusyHeatmap, DemographicProfile, EquipmentAudit, HonestVerdict, GymCard, etc.
        ├── layouts/
        ├── lib/             # types, data, schema, listicles config
        ├── pages/
        └── styles/
```

## Phase 2 — expansion paths

Both sites are **dataset-driven**. To add a new town to FindATradey, add a record to `sites/findatradey/data/geo/districts.json` — every dynamic template picks it up. To add a new town to FindAGym, add `sites/findagym/data/gyms/<town>.json` and clone the route patterns.

That's the whole expansion model. The chassis stays the same.
