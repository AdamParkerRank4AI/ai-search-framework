# CardMachines — site plan

Last updated: 2026-04-25
Site: CardMachines — UK card terminals, merchant accounts, payment processing.
Sits above `docs/sites/cardmachines.md` (deep-dive). Lead-gen, no forms yet.

Companion docs: `docs/niche-brief.md`, `docs/route-to-market.md`,
`docs/regulatory-notes.md`, `docs/sites/synthesis.md`,
`docs/sites/cardmachines.md`.

---

## 1. Information architecture (the silos)

Seven top-level silos plus a homepage and a thin trust layer. Each silo
is a true pillar (its own hub URL with internal-link spokes). All silos
cross-link via two patterns: (a) the **terminal recommendation block**
(every trade / high-risk / switching page recommends a reviewed terminal),
and (b) the **vertical bridge** (every high-risk page links to the same
trade page where one exists — e.g. `/high-risk/vape/` ↔ `/trade/vape-shop/`).

| Silo | URL prefix | Job | Pillar URL |
|---|---|---|---|
| Terminals | `/terminals/` and `/reviews/` | Single-model reviews + comparison hubs (countertop / mobile / Tap-to-Pay / EPOS) — AIO citation factory | `/terminals/` |
| High-risk | `/high-risk/` | UK high-risk merchant account verticals — biggest revenue line | `/high-risk/` |
| By trade | `/trade/` | "Card machine for [trade]" landers — generic trade matrix | `/trade/` |
| By hospitality | `/hospitality/` | Restaurant, pub, cafe, takeaway sub-niches with EPOS/booking integrations | `/hospitality/` |
| By retail | `/retail/` | Shop-floor verticals (off-licence, vape, convenience, florist, market stall) | `/retail/` |
| Switching | `/switch/` | Worldpay / Barclaycard / Elavon / Paymentsense exit content + calculator | `/switch/` |
| Tap to Pay | `/tap-to-pay-iphone/` | Soft-POS hub: per-provider, vs-card-reader, by-trade | `/tap-to-pay-iphone/` |
| Integrations | `/integrations/` | EPOS / accounting / booking system fits (Xero, Shopify, Phorest etc.) | `/integrations/` |
| Guides | `/guides/` and `/glossary/` | Definitions, fees, PCI, MTD — informational citation pages | `/guides/` |
| Reviews | `/reviews/` (terminals) and `/reviews/[provider]/` | Provider reviews (SumUp, Square, Dojo, Stripe, Worldpay) | `/reviews/` |
| Vs / comparisons | `/vs/` | Head-to-heads (Dojo vs Worldpay, SumUp vs Square) | `/vs/` |
| Trust | `/about/`, `/methodology/`, `/authors/` | Person + Organization schema, editorial process | `/about/` |

**Flow.** Top-of-funnel guides and definitions feed pillars. Pillars feed
single-vertical / single-model pages. Every leaf page contains (i) a
terminal recommendation block, (ii) a "compare quotes" CTA, (iii) a
sister-site bridge (BBL/FundBiz where the buyer also has loan / MCA
intent). Switching and high-risk silos are the **highest-revenue** silos
and get the densest internal-link weight.

---

## 2. Full sitemap (table)

TBD

---

## 3. Top 50 page briefs (full)

TBD

---

## 4. Build sequence within the site

TBD

---

## 5. Targets

TBD

---

## 6. Schema strategy summary

TBD

---

## 7. Open questions / decisions needed

TBD
