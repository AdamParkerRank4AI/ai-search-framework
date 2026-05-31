# Invoice Finance — 2nd Domain to Scale

Goal: add a second domain alongside **marketinvoice.co.uk** that *scales* the
invoice-finance play instead of splitting its traffic.

## Decision: build a Comparison Hub (not a 2nd broker)

marketinvoice.co.uk is a **broker brand** (captures branded + general
"invoice finance" intent, funnels to eCapital). The 2nd domain must own a
*different query class* so the two assets compound instead of cannibalising.

**Role:** comparison / "best companies" / quotes hub targeting bottom-funnel
intent: `compare invoice finance`, `best invoice factoring companies`,
`invoice finance quotes`.

Why this scales:
- Distinct, high-converting query class marketinvoice doesn't own.
- Different content type → no cannibalisation.
- It's the Capalona / Swoop model (comparison hub + white-label widget = the
  distribution engine, not just SERP chasing).
- Can list multiple lenders (more monetisation routes) AND route overflow to
  marketinvoice → the two sites feed each other.

## Domain pick

| Priority | Domain | Why |
|---|---|---|
| 1 | `InvoiceFactoringCompanies.co.uk` | Clean slate (no spam baggage), exact match for a high-volume query — ideal for a listing/comparison site. Surfaced in the deleted-domains pool. |
| Alt | `compareinvoicefinance.co.uk` / `.com` | "Compare" intent, fresh registration |
| Alt | `invoicefinancequotes.co.uk` | Quote/lead intent, matches marketinvoice funnel |
| Alt | `bestinvoicefinance.co.uk` | "Best" listicle/comparison intent |

> The free expired-domain pool for invoice finance is ~all spam (good
> on-topic domains don't drop — owners renew or sell them). So for the 2nd
> domain, a **clean exact-match (fresh or clean-slate) + the build below**
> beats a higher-metric aged domain whose links you'd have to disavow.

## Vetting rule (before registering any aged candidate)

Pre-filter from the ExpiredDomains table — skip if:
- **BL >> DP** (e.g. 1.2K BL / 19 DP) = sitewide/farm links
- **High BL, tiny ACR (crawls)** = links but no real site = PBN
- **No ABY / 0 crawls** = never a real site

Then a 30-second Ahrefs check on survivors:
1. Dofollow % — 60–90% natural; **98%+ = manipulated**
2. Top referring pages — real directories/sites vs `businessXX.htm` farm clones
3. Anchors — branded/varied (good) vs repeated exact-match commercial (bad)

Two gotchas learned in the hunt:
- **Majestic DP (ExpiredDomains) ≠ Ahrefs "linking websites".** Different
  indexes; Majestic often inflates with stale/dead links. When they disagree,
  trust the tool that lets you *inspect the referring pages* (Ahrefs) — a count
  you can't see is worthless.
- **"Factors" is a homonym trap.** Searching `factors` pulls motor factors
  (car parts), diet products (Venus Factor, Fat Loss Factors) and generic
  "success/human factors" — not invoice *factoring*. Use `invoice`,
  `factoring`, `discounting`, `cashflow` instead.

(Reference: `factoring-quote.co.uk` failed all three — link-farm footprint.
`aonefinance.co.uk` passed — Yell DR91 link, branded anchor, 70% dofollow,
180 real referring domains — but it's a *loans* domain, off-vertical for IF.)

## Separation rules (running two brands)

- Different registrant footprint; **no heavy cross-linking**.
- A light, natural "compared on…" mention is fine; reciprocal sitewide links
  read as a PBN and trigger the graph-drift penalty.
- Keep each entity's identity language consistent and distinct.

## Build outline (comparison hub)

1. Core: a lender comparison table / "best invoice factoring companies" listing
   (the exact-match query as the money page).
2. Lead capture → route to eCapital (same as marketinvoice) + optional
   multi-lender affiliate links.
3. Reuse the planned white-label comparison **widget** (one engine, themed skin)
   for partner embeds (accountants, recruitment/construction bodies).
4. Distribution: NACFB listing, comparison-hub features, the Late-Payment Index
   data-PR for clean relevant links.
5. Cross-feed: comparison/overflow traffic → marketinvoice broker conversion.

## Getting a Google head-start from an aged domain

An expired domain is a **Google lever, not an AI/ChatGPT lever** (AI
recommendation is built via the five signals, not inherited from a dead
domain). Only three things deliver a Google head-start:

1. **Age** — real history beats a day-old registration.
2. **Clean, relevant, authoritative backlinks** — a few real finance/business
   links beat thousands of farm links (which count for zero or negative).
3. **No penalty** — a flagged domain is a head-start in reverse.

Buy-decision checks (real Google signals, not Ahrefs estimates):
- **Ahrefs Organic keywords / traffic history** — did it ever rank for real,
  relevant terms? (best pre-purchase proxy)
- **Wayback** — genuinely a finance site, not repurposed spam?
- **`site:thedomain.com`** — fully deindexed despite past content = penalty smell.
- **After acquiring → Google Search Console → Manual Actions** — the only place
  a penalty is confirmed. Add it day one, before building.

Deploy:
- **Rebuild on it** (preferred for scaling): build the comparison hub directly
  on the aged domain, preserving any URLs that held links — age + equity accrue
  to the asset.
- **301 into an existing site**: only if topically aligned (clean *factoring*
  domain → marketinvoice). Off-topic 301s get discounted as soft-404s.

Realistic sizing: from the free pool the head-start is age + a few clean
relevant links + an exact-match keyword — a few months' jump, not instant
page 1. Content + the distribution playbook still do the heavy lifting. A
bigger jump means paying for a quality aged domain via a broker/marketplace.
