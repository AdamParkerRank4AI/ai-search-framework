# Monorepo structure

Astro 5 + pnpm workspaces. Three brand sites + shared packages. Fleet
sites (multilingual / hyper-local) live in separate repos — see
`docs/niche-brief.md` for routing rules.

```
ai-search-framework/
├── apps/
│   ├── cardmachines/    # CardMachines — UK card terminals + payments
│   ├── bbl/             # BestBusinessLoans — UK business loans editorial
│   └── fundbiz/         # FundBiz — UK business loans broker / transactional
├── packages/
│   ├── ui/              # Shared Astro components (Hero, ComparisonTable, Listicle, Faq, Cta, MetaTags, AuthorByline, Pros, Cons)
│   ├── schema/          # Shared schema-org JSON-LD components (Organization, Person, Product, Review, FaqPage, Article, HowTo, Breadcrumb, WebApplication)
│   └── content-types/   # Shared Zod schemas for content collections (terminals, lenders, sectors, decline-reasons, products, etc.)
├── docs/                # Strategy, research, plans
│   ├── niche-brief.md
│   ├── route-to-market.md
│   ├── regulatory-notes.md
│   └── sites/
│       ├── bbl.md, bbl-plan.md
│       ├── fundbiz.md, fundbiz-plan.md
│       ├── cardmachines.md, cardmachines-plan.md
│       └── synthesis.md
└── _archive/            # Deprecated work kept for history
```

## Quickstart

```bash
# install
pnpm install

# dev — pick one
pnpm dev:cm    # CardMachines on :4321
pnpm dev:bbl   # BestBusinessLoans on :4322
pnpm dev:fb    # FundBiz on :4323

# build all
pnpm build

# build one
pnpm build:cm
```

## Conventions

- **Each app sets its own `site` URL in `astro.config.mjs`** — currently
  `cardmachines.co.uk`, `bestbusinessloans.co.uk`, `fundbiz.co.uk` (placeholder
  — confirm domain ownership and update).
- **Trailing slash always** — directory output, consistent canonical URLs.
- **Content collections** are typed via `@aisf/content-types` (Zod) and wired
  per-app in `src/content.config.ts`.
- **Schema partials** are imported from `@aisf/schema` — every page should
  render the appropriate JSON-LD via these (Article, Product, Review,
  FaqPage, Organization, Breadcrumb).
- **UI components** are imported from `@aisf/ui` — keep app-specific
  styling in `apps/<app>/src/styles/global.css` rather than inside shared
  components.
- **No application forms in this phase.** CTAs in CardMachines / BBL /
  FundBiz are placeholder labels; forms ship after monetisation contracts
  are signed (see `docs/route-to-market.md`).

## Brand sites vs Fleet — routing rules

The three apps in this repo are **brand sites**: English UK only, depth
on their 80% focus, AI-citation engines built for entity authority.

The **Fleet** is a separate network of satellite sites that route leads
back into the same monetisation paths but never share a domain or schema
graph with the brand sites:

- **All multilingual content** (Polish, Bengali, Urdu, Punjabi, Hindi,
  Gujarati, Turkish, Arabic, Romanian, Mandarin, Albanian, Portuguese,
  Tagalog, Ukrainian) lives on Fleet sites — never in `/pl/` subfolders
  on a brand site, because that dilutes the brand's English entity
  description in the LLM graph.
- **Hyper-local geographies** (postcode-level, single-town pages).
- **Single-niche microsites** that would clash with a brand site's
  positioning.

Fleet sites should be created as separate repos (or, if scale demands
it, additional `apps/*` entries with their own `site` URLs, but
defaulting to separate repos keeps schema clean).

See `docs/niche-brief.md` for the full routing model.

## What ships next

The CardMachines `/high-risk/` hub stub is the first real page (per
`docs/sites/synthesis.md`). Wave 1 build order is in
`docs/sites/cardmachines-plan.md` section 4.
