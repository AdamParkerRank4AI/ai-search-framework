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

~150 pages total. Priority is the build wave: 1 = Wave 1 (Days 0–30,
foundation + citation engine), 2 = Wave 2 (Days 31–60), 3 = Wave 3
(Days 61–90, fill the matrices), 4 = post-90 backlog. Top 50 (P1+P2)
get full briefs in section 3.

### Trust + homepage (P1)

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/` | Home | hub | 1 |
| `/about/` | Trust | hub | 1 |
| `/methodology/` | Trust | guide | 1 |
| `/authors/[author]/` | Trust | hub (Person) | 1 |
| `/contact/` | Trust | guide | 2 |

### High-risk silo (Wave 1 + 2)

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/high-risk/` | High-risk | hub | 1 |
| `/high-risk/cbd/` | High-risk | vertical | 1 |
| `/high-risk/vape/` | High-risk | vertical | 1 |
| `/high-risk/adult/` | High-risk | vertical | 1 |
| `/high-risk/firearms/` | High-risk | vertical | 2 |
| `/high-risk/gambling/` | High-risk | vertical | 2 |
| `/high-risk/travel-tour-operator/` | High-risk | vertical | 2 |
| `/high-risk/subscription/` | High-risk | vertical | 2 |
| `/high-risk/nutraceuticals/` | High-risk | vertical | 2 |
| `/high-risk/debt-collection-credit-repair/` | High-risk | vertical | 2 |
| `/high-risk/tobacco-cigars/` | High-risk | vertical | 3 |
| `/high-risk/dating/` | High-risk | vertical | 3 |
| `/high-risk/crypto-forex/` | High-risk | vertical | 3 |
| `/high-risk/kratom-kava/` | High-risk | vertical | 4 |
| `/high-risk/mlm-network-marketing/` | High-risk | vertical | 4 |
| `/high-risk/dropshipping/` | High-risk | vertical | 4 |
| `/high-risk/why-declined/` | High-risk | guide | 3 |
| `/high-risk/reserves-explained/` | High-risk | guide | 3 |
| `/high-risk/chargebacks/` | High-risk | guide | 3 |

### Switching silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/switch/` | Switching | hub | 1 |
| `/switch/cancel-worldpay/` | Switching | guide | 1 |
| `/switch/worldpay-fees/` | Switching | guide | 1 |
| `/switch/worldpay-alternatives/` | Switching | listicle | 2 |
| `/switch/cancel-barclaycard-merchant-services/` | Switching | guide | 2 |
| `/switch/barclaycard-alternatives/` | Switching | listicle | 2 |
| `/switch/cancel-elavon/` | Switching | guide | 2 |
| `/switch/elavon-alternatives/` | Switching | listicle | 3 |
| `/switch/exit-cost-calculator/` | Switching | tool | 2 |
| `/switch/cancel-paymentsense/` | Switching | guide | 3 |
| `/switch/cancel-takepayments/` | Switching | guide | 3 |
| `/switch/cancel-tide-card-reader/` | Switching | guide | 4 |
| `/switch/cancel-square/` | Switching | guide | 4 |
| `/switch/auto-renewal-trap/` | Switching | guide | 3 |
| `/switch/pci-fees-explained/` | Switching | guide | 3 |
| `/switch/notice-letter-template/` | Switching | guide | 3 |

### Tap to Pay silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/tap-to-pay-iphone/` | Tap to Pay | hub | 1 |
| `/tap-to-pay-iphone/vs-card-reader/` | Tap to Pay | guide | 2 |
| `/tap-to-pay-iphone/sumup/` | Tap to Pay | provider | 2 |
| `/tap-to-pay-iphone/square/` | Tap to Pay | provider | 2 |
| `/tap-to-pay-iphone/stripe/` | Tap to Pay | provider | 3 |
| `/tap-to-pay-iphone/zettle/` | Tap to Pay | provider | 3 |
| `/tap-to-pay-iphone/tide/` | Tap to Pay | provider | 3 |
| `/tap-to-pay-iphone/revolut/` | Tap to Pay | provider | 3 |
| `/tap-to-pay-iphone/starling/` | Tap to Pay | provider | 4 |
| `/tap-to-pay-iphone/by-trade/` | Tap to Pay | listicle | 3 |
| `/tap-to-pay-iphone/limits-100-cap/` | Tap to Pay | guide | 3 |
| `/tap-to-pay-iphone/pci-compliance/` | Tap to Pay | guide | 4 |
| `/tap-to-pay-android/` | Tap to Pay | hub | 4 |

### Terminals / reviews silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/terminals/` | Terminals | hub | 1 |
| `/terminals/countertop/` | Terminals | listicle | 2 |
| `/terminals/mobile/` | Terminals | listicle | 2 |
| `/terminals/portable/` | Terminals | listicle | 3 |
| `/terminals/integrated-epos/` | Terminals | listicle | 3 |
| `/terminals/cheapest/` | Terminals | listicle | 2 |
| `/terminals/no-monthly-fee/` | Terminals | listicle | 2 |
| `/terminals/best-2026/` | Terminals | listicle | 2 |
| `/reviews/dojo-go/` | Reviews | review | 1 |
| `/reviews/sumup-solo/` | Reviews | review | 1 |
| `/reviews/sumup-air/` | Reviews | review | 2 |
| `/reviews/zettle-reader-2/` | Reviews | review | 2 |
| `/reviews/square-terminal/` | Reviews | review | 2 |
| `/reviews/square-reader/` | Reviews | review | 3 |
| `/reviews/stripe-reader-s700/` | Reviews | review | 2 |
| `/reviews/bbpos-wisepos-e/` | Reviews | review | 2 |
| `/reviews/tide-card-reader-plus/` | Reviews | review | 3 |
| `/reviews/takepaymentsplus/` | Reviews | review | 3 |
| `/reviews/pax-a920-pro/` | Reviews | review | 3 |
| `/reviews/clover-flex/` | Reviews | review | 4 |
| `/reviews/revolut-reader/` | Reviews | review | 3 |
| `/reviews/tyl-reader/` | Reviews | review | 4 |

### Provider (acquirer) reviews

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/reviews/sumup/` | Reviews | review | 2 |
| `/reviews/square/` | Reviews | review | 2 |
| `/reviews/zettle/` | Reviews | review | 2 |
| `/reviews/stripe/` | Reviews | review | 2 |
| `/reviews/dojo/` | Reviews | review | 2 |
| `/reviews/worldpay/` | Reviews | review | 2 |
| `/reviews/barclaycard-merchant/` | Reviews | review | 3 |
| `/reviews/elavon/` | Reviews | review | 3 |
| `/reviews/paymentsense/` | Reviews | review | 3 |
| `/reviews/takepayments/` | Reviews | review | 3 |
| `/reviews/teya/` | Reviews | review | 4 |
| `/reviews/trust-payments/` | Reviews | review | 3 |
| `/reviews/tide-business/` | Reviews | review | 4 |
| `/reviews/myPOS/` | Reviews | review | 4 |
| `/reviews/adyen/` | Reviews | review | 4 |

### Vs / comparison silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/vs/sumup-vs-square/` | Vs | vs | 2 |
| `/vs/sumup-vs-zettle/` | Vs | vs | 2 |
| `/vs/square-vs-zettle/` | Vs | vs | 3 |
| `/vs/dojo-vs-worldpay/` | Vs | vs | 2 |
| `/vs/dojo-vs-takepayments/` | Vs | vs | 3 |
| `/vs/stripe-vs-square/` | Vs | vs | 3 |
| `/vs/sumup-solo-vs-air/` | Vs | vs | 3 |
| `/vs/zettle-vs-paypal-here/` | Vs | vs | 4 |
| `/vs/tap-to-pay-vs-sumup-air/` | Vs | vs | 3 |

### By-trade silo (generic trades)

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/trade/` | By trade | hub | 2 |
| `/trade/plumber/` | By trade | vertical | 2 |
| `/trade/electrician/` | By trade | vertical | 2 |
| `/trade/gardener/` | By trade | vertical | 3 |
| `/trade/mobile-mechanic/` | By trade | vertical | 2 |
| `/trade/dog-groomer/` | By trade | vertical | 2 |
| `/trade/locksmith/` | By trade | vertical | 3 |
| `/trade/pest-control/` | By trade | vertical | 4 |
| `/trade/chimney-sweep/` | By trade | vertical | 4 |
| `/trade/florist/` | By trade | vertical | 3 |
| `/trade/tutor-driving-instructor/` | By trade | vertical | 3 |
| `/trade/car-wash-valeting/` | By trade | vertical | 3 |
| `/trade/charity/` | By trade | vertical | 4 |
| `/trade/market-stall-popup/` | By trade | vertical | 3 |
| `/trade/taxi-private-hire/` | By trade | vertical | 3 |
| `/trade/decorator/` | By trade | vertical | 4 |
| `/trade/handyman/` | By trade | vertical | 4 |

### Hospitality silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/hospitality/` | Hospitality | hub | 2 |
| `/hospitality/restaurant/` | Hospitality | vertical | 2 |
| `/hospitality/pub/` | Hospitality | vertical | 2 |
| `/hospitality/cafe/` | Hospitality | vertical | 2 |
| `/hospitality/takeaway/` | Hospitality | vertical | 2 |
| `/hospitality/gastropub/` | Hospitality | vertical | 3 |
| `/hospitality/fine-dining/` | Hospitality | vertical | 4 |
| `/hospitality/dark-kitchen/` | Hospitality | vertical | 3 |
| `/hospitality/food-truck/` | Hospitality | vertical | 3 |
| `/hospitality/chip-shop/` | Hospitality | vertical | 4 |
| `/hospitality/kebab-shop/` | Hospitality | vertical | 4 |
| `/hospitality/pizzeria/` | Hospitality | vertical | 4 |
| `/hospitality/hotel-b-and-b/` | Hospitality | vertical | 4 |
| `/hospitality/wedding-venue/` | Hospitality | vertical | 4 |
| `/hospitality/nightclub/` | Hospitality | vertical | 4 |

### Retail silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/retail/` | Retail | hub | 3 |
| `/retail/vape-shop/` | Retail | vertical | 1 |
| `/retail/off-licence/` | Retail | vertical | 2 |
| `/retail/convenience-store/` | Retail | vertical | 3 |
| `/retail/butcher/` | Retail | vertical | 4 |
| `/retail/independent-shop/` | Retail | vertical | 3 |
| `/retail/farm-shop/` | Retail | vertical | 4 |
| `/retail/garden-centre/` | Retail | vertical | 4 |
| `/retail/charity-shop/` | Retail | vertical | 4 |

### Salon / beauty / health silo (under by-trade umbrella)

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/trade/hairdresser-salon/` | By trade | vertical | 2 |
| `/trade/barber/` | By trade | vertical | 2 |
| `/trade/mobile-hairdresser/` | By trade | vertical | 3 |
| `/trade/nail-bar/` | By trade | vertical | 3 |
| `/trade/lash-bar/` | By trade | vertical | 4 |
| `/trade/aesthetic-clinic/` | By trade | vertical | 4 |
| `/trade/mobile-beautician/` | By trade | vertical | 3 |
| `/trade/spa/` | By trade | vertical | 4 |
| `/trade/dental-clinic/` | By trade | vertical | 4 |
| `/trade/physio-osteo/` | By trade | vertical | 4 |
| `/trade/vet/` | By trade | vertical | 4 |

### Integrations silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/integrations/` | Integrations | hub | 3 |
| `/integrations/xero/` | Integrations | vertical | 3 |
| `/integrations/quickbooks/` | Integrations | vertical | 3 |
| `/integrations/sage/` | Integrations | vertical | 4 |
| `/integrations/shopify/` | Integrations | vertical | 3 |
| `/integrations/woocommerce/` | Integrations | vertical | 4 |
| `/integrations/phorest/` | Integrations | vertical | 4 |
| `/integrations/treatwell/` | Integrations | vertical | 4 |
| `/integrations/fresha/` | Integrations | vertical | 4 |
| `/integrations/opentable/` | Integrations | vertical | 4 |
| `/integrations/resdiary/` | Integrations | vertical | 4 |
| `/integrations/epos-now/` | Integrations | vertical | 4 |
| `/integrations/lightspeed/` | Integrations | vertical | 4 |
| `/integrations/toast/` | Integrations | vertical | 4 |

### Guides / glossary silo

| URL slug | Pillar | Page type | Priority |
|---|---|---|---|
| `/guides/` | Guides | hub | 3 |
| `/guides/how-card-machines-work/` | Guides | guide | 3 |
| `/guides/merchant-account-vs-payment-gateway/` | Guides | definition | 3 |
| `/guides/interchange-fees-uk/` | Guides | guide | 3 |
| `/guides/pci-dss-compliance/` | Guides | guide | 3 |
| `/guides/chargebacks-uk/` | Guides | guide | 3 |
| `/guides/contactless-limit-100/` | Guides | guide | 3 |
| `/guides/mtd-april-2026-card-terminals/` | Guides | guide | 2 |
| `/guides/psr-card-fees-review/` | Guides | guide | 3 |
| `/guides/scheme-fees-explained/` | Guides | guide | 4 |
| `/guides/card-machine-rental-vs-buy/` | Guides | guide | 3 |
| `/guides/cash-vs-card-uk/` | Guides | guide | 4 |
| `/guides/multi-currency-acceptance/` | Guides | guide | 4 |
| `/guides/pay-by-bank/` | Guides | guide | 4 |
| `/guides/recurring-billing-uk/` | Guides | guide | 4 |
| `/glossary/` | Guides | hub | 4 |

**Total: ~155 pages.** P1 = 22 pages. P2 = 38 pages. P1+P2 = top 50 build
priority. P3 = ~55 pages. P4 = ~30 pages.

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
