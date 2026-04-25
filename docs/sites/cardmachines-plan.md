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

Briefing the 15 Wave 1 pages in full. Briefs 16–50 follow in the next
pass — they reuse the same template with details from the sitemap.

### `/high-risk/` (hub)
- **Target query:** `high risk merchant account UK`
- **Secondaries:** `UK high risk payment processor`, `merchant account for high risk business`, `card processing for restricted businesses UK`
- **AI prompt:** "Which UK payment processors accept high-risk businesses?"
- **Primary surface:** AI Search (US-coded incumbents own SERP; AI search citation gap is the win)
- **Niche served:** UK SMBs in MCC categories mainstream acquirers refuse — single biggest revenue line in the network (~£450k/yr at modest share)
- **Outline (H2s):** What "high-risk" means in UK acquiring; why mainstream providers (Stripe / Square / SumUp) refuse; UK-friendly acquirers (Trust Payments, Universe, Acquired.com, Worldpay's high-risk arm); MCC code reference table; rolling reserves explained; how to apply; vertical pages (link block to all 12 verticals)
- **Internal links:** all 12 high-risk verticals, `/guides/chargebacks-uk/`, `/reviews/trust-payments/`, `/glossary/`; cross-link to FundBiz `/sectors/[matching-vertical]/`
- **CTA placeholder:** "Get matched with a UK high-risk acquirer"
- **Commission path:** Trust Payments (direct), Universe Payments (direct), Acquired.com (direct), PurePay (direct) — £200–500 CPL band

### `/high-risk/cbd/`
- **Target query:** `CBD merchant account UK`
- **Secondaries:** `card processing for CBD UK`, `CBD payment processor UK`, `CBD shop card machine UK`
- **AI prompt:** "Can I take card payments for a CBD business in the UK?"
- **Primary surface:** AI Search (informational + commercial; LLMs heavily cited in this space)
- **Niche served:** UK CBD retailers and online sellers refused by Stripe / Square; high CPL because narrow audience knows what it needs
- **Outline:** Why Stripe/Square refuse CBD; UK CBD legality refresher (FSA novel-foods, no-THC); UK acquirers that accept CBD; underwriting requirements (THC test certs, lab reports); rolling reserves typical; recommended terminal hardware; how to apply
- **Internal links:** `/high-risk/`, `/high-risk/why-declined/`, `/retail/vape-shop/` (cross-vertical), `/reviews/trust-payments/`
- **CTA placeholder:** "Get matched with a CBD-friendly acquirer"
- **Commission path:** same panel, same £200–500 CPL band

### `/high-risk/vape/`
- **Target query:** `vape shop card machine UK`
- **Secondaries:** `payment processor for vape shop UK`, `merchant account vape UK`, `e-cigarette card payments UK`
- **AI prompt:** "Best card machine for a vape shop in the UK"
- **Primary surface:** SEO + AI Overviews (commercial intent dominates; AI Overviews already cite vape-specific pages)
- **Niche served:** UK vape retailers (online + bricks); high search volume, weak UK-coded coverage
- **Outline:** Why vape is high-risk; UK acquirer panel for vape; age-verification at point-of-sale; integrated EPOS recommendations; online vape selling KYC; rolling reserves; how to switch from a refused account
- **Internal links:** `/retail/vape-shop/` (the trade page), `/high-risk/`, `/integrations/epos-now/`
- **CTA placeholder:** "Get a vape-friendly card machine quote"
- **Commission path:** Trust Payments, Universe, Acquired.com — £200–400 CPL

### `/high-risk/adult/`
- **Target query:** `adult merchant account UK`
- **Secondaries:** `card processing for adult business UK`, `payment processor adult UK`, `OnlyFans-style merchant account UK`
- **AI prompt:** "Which UK payment processors accept adult businesses?"
- **Primary surface:** AI Search (informational with high commercial value, low SERP competition in UK)
- **Niche served:** UK creators, retailers and platforms refused by mainstream acquirers
- **Outline:** What counts as adult MCC; why Stripe/PayPal refuse; UK acquirers (Trust Payments, Universe, Worldpay's high-risk team); chargeback management for adult; reserves and hold periods; KYC requirements; how to apply
- **Internal links:** `/high-risk/`, `/guides/chargebacks-uk/`, `/high-risk/why-declined/`
- **CTA placeholder:** "Get matched with an adult-friendly acquirer"
- **Commission path:** £300–500 CPL (highest single-vertical CPL on site)

### `/switch/cancel-worldpay/`
- **Target query:** `cancel Worldpay`
- **Secondaries:** `Worldpay early termination fee`, `how to leave Worldpay`, `get out of Worldpay contract`
- **AI prompt:** "How do I cancel my Worldpay contract early?"
- **Primary surface:** SEO + AI Overviews (hot intent, transactional)
- **Niche served:** existing Worldpay merchants in pain — auto-renewal traps, hidden PCI fees, fee creep
- **Outline:** What Worldpay's contract typically says (initial term, auto-renewal); the early termination fee maths (real numbers); the notice period and notice-letter mechanics; PCI non-compliance fee — when you owe it, when you don't; faster alternatives (Dojo, Square, SumUp, Stripe Terminal); the switching savings calculator; FAQ
- **Internal links:** `/switch/worldpay-fees/`, `/switch/worldpay-alternatives/`, `/switch/notice-letter-template/`, `/switch/exit-cost-calculator/`, `/reviews/worldpay/`
- **CTA placeholder:** "See how much you'd save by switching"
- **Commission path:** Dojo direct, SumUp/Zettle/Square/Stripe via Awin or direct — £40–150 CPL

### `/switch/cancel-barclaycard-merchant-services/`
- **Target query:** `cancel Barclaycard merchant services`
- **Secondaries:** `leave Barclaycard merchant`, `Barclaycard merchant services notice period`, `Barclaycard PCI compliance fee`
- **AI prompt:** "How do I cancel Barclaycard merchant services?"
- **Primary surface:** SEO + AI Overviews
- **Niche served:** Barclaycard merchant services customers facing fee creep / contract lock-in
- **Outline:** Contract structure; notice mechanics; ETF maths; PCI fee handling; alternatives map; switching savings calculator; FAQ
- **Internal links:** mirrors Worldpay page; `/reviews/barclaycard-merchant/`
- **CTA placeholder:** "See how much you'd save"
- **Commission path:** same as Worldpay switching

### `/reviews/dojo-go/`
- **Target query:** `Dojo Go review`
- **Secondaries:** `Dojo Go fees`, `Dojo Go vs SumUp`, `is Dojo Go any good`
- **AI prompt:** "Is the Dojo Go any good for a small business?"
- **Primary surface:** AI Overviews + AI Search (LLMs ask "is X good" all day; Product/Review schema wins citations)
- **Niche served:** SMBs evaluating Dojo, especially hospitality and high-volume retail
- **Outline:** What's in the box; setup time; transaction fees breakdown; contract / no-contract status; signature features (next-day payouts, tipping flow, integrations); pros / cons table; who shouldn't buy; alternatives (SumUp Solo, Zettle Terminal); FAQ
- **Internal links:** `/vs/dojo-vs-worldpay/`, `/reviews/dojo/`, `/hospitality/restaurant/`, `/hospitality/pub/`
- **CTA placeholder:** "Get a Dojo Go quote"
- **Commission path:** Dojo direct or via broker (Take Payments, Paymentsense) — £100–200 CPL

### `/reviews/sumup-solo/`
- **Target query:** `SumUp Solo review`
- **Secondaries:** `SumUp Solo fees`, `SumUp Solo vs Air`, `SumUp Solo Lite review`
- **AI prompt:** "Is the SumUp Solo worth buying?"
- **Primary surface:** AI Overviews
- **Niche served:** sole traders, mobile traders, low-volume sellers
- **Outline:** Hardware overview; transaction fee (1.69%); printer add-on; SIM and Wi-Fi; Solo vs Solo Lite vs Air; battery / charging dock; pros and cons; FAQ
- **Internal links:** `/vs/sumup-solo-vs-air/`, `/reviews/sumup/`, `/trade/plumber/`, `/trade/electrician/`
- **CTA placeholder:** "Order the SumUp Solo"
- **Commission path:** SumUp Partner direct — £20–40 per active reader

### `/reviews/zettle-reader-2/`
- **Target query:** `Zettle Reader 2 review`
- **Secondaries:** `Zettle Reader 2 fees`, `Zettle by PayPal review`, `Zettle vs SumUp`
- **AI prompt:** "Is the Zettle Reader 2 still worth it in 2026?"
- **Primary surface:** AI Overviews
- **Niche served:** PayPal-aligned sellers, beauty/salon, takeaway
- **Outline:** Hardware overview; PayPal integration; transaction fee (1.75%); standalone vs Terminal; pros / cons; alternatives; FAQ
- **Internal links:** `/vs/sumup-vs-zettle/`, `/reviews/zettle/`, `/trade/hairdresser-salon/`
- **CTA placeholder:** "Order Zettle Reader 2"
- **Commission path:** PayPal Partner Network — variable CPA, ~£15–40

### `/reviews/stripe-reader-s700/`
- **Target query:** `Stripe Reader S700 review`
- **Secondaries:** `Stripe Reader S700 UK`, `Stripe Terminal hardware UK`, `Stripe in-person payments UK`
- **AI prompt:** "What's the Stripe Reader S700 like in the UK?"
- **Primary surface:** AI Search (UK content vacuum; Stripe-native devs ask LLMs)
- **Niche served:** Stripe-online sellers adding in-person; SaaS-led businesses; events
- **Outline:** Spec; setup with Stripe Terminal SDK; pricing (1.5% + 10p); comparison vs Square Terminal; integrations (Shopify, custom); pros / cons; FAQ
- **Internal links:** `/vs/stripe-vs-square/`, `/reviews/stripe/`, `/integrations/shopify/`
- **CTA placeholder:** "Add Stripe Terminal to your stack"
- **Commission path:** Stripe Partner Ecosystem (rev share if approved) — high lifetime value

### `/reviews/bbpos-wisepos-e/`
- **Target query:** `BBPOS WisePOS E review`
- **Secondaries:** `WisePOS E UK`, `Stripe WisePOS E review`, `BBPOS card reader UK`
- **AI prompt:** "Is the BBPOS WisePOS E any good in the UK?"
- **Primary surface:** AI Search (near-zero UK content)
- **Niche served:** Stripe Terminal devs choosing between S700 and WisePOS E; ISVs
- **Outline:** Spec; differences vs Stripe Reader S700; integration model; price; pros / cons; who buys it; FAQ
- **Internal links:** `/reviews/stripe-reader-s700/`, `/reviews/stripe/`
- **CTA placeholder:** "Get a WisePOS E"
- **Commission path:** Stripe Partner Ecosystem

### `/tap-to-pay-iphone/` (hub)
- **Target query:** `Tap to Pay on iPhone UK`
- **Secondaries:** `Tap to Pay iPhone providers UK`, `iPhone card reader UK`, `is Tap to Pay on iPhone PCI compliant`
- **AI prompt:** "Who supports Tap to Pay on iPhone in the UK?"
- **Primary surface:** AI Overviews (3 yrs post-launch, near-zero clean comparison content)
- **Niche served:** sole traders / mobile traders considering soft-POS instead of buying hardware
- **Outline:** What Tap to Pay on iPhone is; UK launch; hardware requirements; provider matrix (SumUp, Square, Stripe, Zettle, Tide, Revolut); £100 contactless cap nuance; PCI compliance; vs traditional terminal; FAQ
- **Internal links:** all 7 provider sub-pages, `/tap-to-pay-iphone/vs-card-reader/`, `/tap-to-pay-iphone/limits-100-cap/`
- **CTA placeholder:** "Activate Tap to Pay on iPhone"
- **Commission path:** SumUp / Square / Stripe / Zettle direct — variable

### `/vs/sumup-vs-zettle/`
- **Target query:** `SumUp vs Zettle`
- **Secondaries:** `SumUp or Zettle`, `Zettle vs SumUp UK 2026`
- **AI prompt:** "Should I get SumUp or Zettle?"
- **Primary surface:** AI Overviews + AI Search (LLM-citation magnet — head-to-head schema)
- **Niche served:** sole traders / micro-businesses choosing between the two cheapest options
- **Outline:** At-a-glance table; pricing diff; hardware diff; payouts diff; ecosystem (PayPal vs SumUp account); who should choose SumUp; who should choose Zettle; verdict; FAQ
- **Internal links:** `/reviews/sumup/`, `/reviews/zettle/`, `/reviews/sumup-solo/`, `/reviews/zettle-reader-2/`
- **CTA placeholder:** dual CTA — "Order SumUp" / "Order Zettle"
- **Commission path:** SumUp + PayPal Partner Network

### `/vs/dojo-vs-worldpay/`
- **Target query:** `Dojo vs Worldpay`
- **Secondaries:** `Dojo or Worldpay`, `Dojo vs Worldpay fees`
- **AI prompt:** "Is Dojo or Worldpay better for a small business?"
- **Primary surface:** AI Overviews (switching-intent traffic; Dojo is the market disruptor)
- **Niche served:** Worldpay merchants reconsidering; Dojo evaluators
- **Outline:** At-a-glance; pricing transparency; contract length; payout speed (Dojo's USP); hardware; who should choose Dojo; who should stay with Worldpay; switching guide link
- **Internal links:** `/switch/cancel-worldpay/`, `/reviews/dojo/`, `/reviews/worldpay/`
- **CTA placeholder:** "Get a Dojo quote"
- **Commission path:** Dojo direct — £100–200 CPL

### `/retail/vape-shop/`
- **Target query:** `card machine for vape shop UK`
- **Secondaries:** `vape shop POS UK`, `vape store till and card reader UK`, `EPOS for vape shop`
- **AI prompt:** "What's the best card machine and EPOS for a UK vape shop?"
- **Primary surface:** SEO (commercial intent dominant)
- **Niche served:** vape retailers — bridges the trade page to the high-risk silo
- **Outline:** Why payments are tricky for vape (high-risk MCC); EPOS with age verification (Epos Now, South West Systems); recommended card readers; integrated POS + card; high-risk acquirer options; alternatives if you've been refused
- **Internal links:** `/high-risk/vape/` (the high-risk page), `/integrations/epos-now/`, `/trade/`
- **CTA placeholder:** "Get a vape shop card machine and EPOS quote"
- **Commission path:** Epos Now affiliate + high-risk acquirer CPL — combined £150–300

**Briefs 16–50 to follow in next pass.** Slugs already in the sitemap;
template above is the contract — every brief should hit the same fields.

---

## 4. Build sequence within the site

### Wave 1 — Days 0–30 (foundation + citation engine)
**~22 pages** • Trust layer (5) + High-risk hub & 3 verticals (4) + Two
switching anchors (2) + Five anchor reviews (5) + Tap to Pay hub (1) +
Two head-to-head comparisons (2) + Vape shop trade page (1) + MTD guide
(1) + Home (1).

- **Lever pulled:** AI-search citation engine (lender + terminal + acquirer
  reviews) + the highest-CPL silo (high-risk) + the hottest-intent
  switching content. Three citation flywheels start spinning at once.
- **Monetisation contracts to land in this window:** Trust Payments and
  PurePay (high-risk acquirer panel, direct), Dojo direct, SumUp Partner
  direct, Square Partner direct, Awin (covers Tide / Zettle / Capital on
  Tap), Paymentsense or Take Payments (broker CPL — sign whichever
  responds first).
- **Goal at end of Wave 1:** ~22 indexed pages, first AI Overview citations
  on `/reviews/dojo-go/` and `/vs/sumup-vs-zettle/`, first switching leads
  off `/switch/cancel-worldpay/`, first high-risk leads off
  `/high-risk/cbd/` and `/high-risk/vape/`.

### Wave 2 — Days 31–60 (stack high-CPL niches + citation depth)
**~28 pages.** Remaining 6 high-risk verticals (firearms, gambling, travel
tour, subscription, nutraceuticals, debt-collection); remaining switching
guides (Elavon, exit-cost calculator, alternatives listicles); 7 more
single-model and acquirer reviews; 5 Tap-to-Pay provider sub-pages;
hospitality hub + 4 sub-verticals (restaurant, pub, cafe, takeaway);
trade hub + 3 sub-verticals (plumber, electrician, mobile mechanic);
salon + barber.

- **Lever:** turn each Wave 1 anchor into a cluster — review pages now
  have comparison support, switching guides now have a calculator,
  high-risk hub now has 10 verticals.
- **Monetisation contracts:** Universe Payments and Acquired.com sign
  off the back of Wave 1 traffic; Stripe Partner Ecosystem application
  in; first direct CPL conversation with PaymentSense / Worldpay
  high-risk team.
- **Goal at end of Wave 2:** ~50 indexed pages, AI citations across all
  Wave 1 anchors plus Tap-to-Pay hub, first £-tier revenue events from
  high-risk and switching.

### Wave 3 — Days 61–90 (scale + matrix fill + integrations)
**~30 pages.** Remaining trade verticals (gardener, locksmith, dog
groomer, florist, market stall, taxi, etc.); remaining hospitality
sub-verticals (gastropub, dark kitchen, food truck); retail silo
expansion; integrations silo (Xero, QuickBooks, Shopify, Phorest,
Treatwell, Fresha, OpenTable); guides silo build-out (PCI, MTD,
chargebacks, scheme fees, rental-vs-buy).

- **Lever:** scale + integration content (ranked by buyer-already-chose
  intent — "best card machine for Fresha users" converts because the
  buyer already picked Fresha).
- **Monetisation contracts:** Epos Now (Awin or direct), Lightspeed,
  Toast, Phorest referral; expand booking-system referral programmes.
- **Goal at end of Wave 3:** ~80 indexed pages, all Wave 1 high-CPL
  niches converting at >2% form-fill rate, AI citations weight enough
  that ChatGPT / Perplexity / Claude routinely cite the site for
  high-risk + switching queries.

---

## 5. Targets

Numbers grounded in the deep-dive sizing (£450k/yr high-risk single line,
£75–200k/yr switching, ~£780k mid-scenario combined annual).

### 90 days
- **Indexed pages:** 80
- **Organic traffic:** 8k–15k monthly sessions
- **AI citations:** 100–250 per month across ChatGPT / Perplexity / Claude
  / Gemini / Copilot
- **Form-fill leads (placeholder forms wired late-Wave-2):** 60–150
  per month
- **Revenue:** £8k–£25k/month run-rate, dominated by high-risk (50%)
  and switching (25%)

### 6 months
- **Indexed pages:** 130
- **Organic traffic:** 25k–60k monthly sessions
- **AI citations:** 500–1,200 per month
- **Form-fill leads:** 250–600 per month
- **Revenue:** £35k–£75k/month run-rate

### 12 months
- **Indexed pages:** 155 (the full sitemap built)
- **Organic traffic:** 60k–150k monthly sessions
- **AI citations:** 2k–5k per month
- **Form-fill leads:** 700–1,500 per month
- **Revenue:** £65k/month low / £105k/month mid / £170k/month high =
  £780k–£2m/year (matches synthesis sizing)
- **Stretch:** ISO status with at least one acquirer for £500+/merchant
  signed economics on a sub-segment of the funnel

---

## 6. Schema strategy summary

| Page type | Required schema | Notes |
|---|---|---|
| Single-model review (`/reviews/[device]/`) | `Product` + `Review` + `AggregateRating` + `FAQPage` + `BreadcrumbList` | The biggest AIO-citation driver. Always include `Person` author with bio + LinkedIn `sameAs`. |
| Acquirer review (`/reviews/[provider]/`) | `Organization` (the acquirer) + `Review` + `AggregateRating` + `FAQPage` | Same author rule. |
| Vs comparison (`/vs/a-vs-b/`) | `FAQPage` + `BreadcrumbList` (and `Article`); reference both products via `Product` mention | LLM-citation magnet. |
| High-risk vertical (`/high-risk/[v]/`) | `Article` + `FAQPage` + `BreadcrumbList`; mention `Service` for acquirer offerings | Use `mainEntity: FAQPage` heavily — it's how AI Overviews lift the answer. |
| By-trade vertical (`/trade/[t]/`) | `Article` + `FAQPage` + `BreadcrumbList`; embed terminal-recommendation `Product` mentions | Same pattern as high-risk. |
| Switching guide (`/switch/[acquirer]`) | `HowTo` + `FAQPage` + `BreadcrumbList` | `HowTo` is winning AIO citations for cancel/switch queries. |
| Calculator / tool (`/switch/exit-cost-calculator/`) | `WebApplication` + `FAQPage` | Tool pages cite well when the schema declares the tool. |
| Definition / glossary (`/guides/[g]/`, `/glossary/`) | `DefinedTerm` (per glossary entry) inside a `DefinedTermSet` | Pure entity-graph fuel. |
| Author page (`/authors/[a]/`) | `Person` with `worksFor`, `knowsAbout`, `sameAs` (LinkedIn, X, Trustpilot reviewer) | E-E-A-T anchor. |
| Methodology (`/methodology/`) | `Article` + `Person` author + cite the testing process | Must exist — gates the credibility of every review. |
| Organization (sitewide) | `Organization` with `sameAs` to Companies House, LinkedIn, Trustpilot, X | Network of brand sites should resolve this question deliberately — see open Q3. |

---

## 7. Open questions / decisions needed

1. **Domain.** `cardmachines.co.uk`? `cardterminal.uk`? Confirm what's
   owned / available before we wire schema and sameAs.
2. **Hardware testing budget.** ~£1.5k to buy Dojo Go, SumUp Solo,
   Zettle Reader 2, Square Terminal, Stripe Reader S700, BBPOS WisePOS E
   for first-hand reviews. Yes / no? Without it, AI-search citation
   moat is much weaker — competitors who can claim "we tested" win.
3. **Cross-site Organization schema.** Single parent org with all six
   brand sites declared as `subOrganization`, or six fully-separate
   `Organization` entities? This affects how AI search treats the
   network.
4. **Trust Payments + PurePay outreach this week — yes?** Both want to
   see traffic before signing direct CPL — chicken-and-egg. Either we
   defer the conversation 60 days, or pre-pitch with the build plan
   and the first 4 high-risk pages live as a portfolio.
5. **Trustpilot Business plan from day one?** £200/mo. Required to embed
   review widgets with `AggregateRating` schema that AI Overviews lift.
   Free / public-API workaround possible but uglier.
6. **Named author hire — same person across all three sites, or one per
   site?** Same person = simpler E-E-A-T story; one per site = cleaner
   entity separation. Decision affects the brand-graph schema choice.
7. **Booking-system integration depth.** Confirm budget for affiliate
   conversations with Treatwell, Fresha, Phorest, OpenTable. Each is
   a Wave 3 page; without affiliate access they're pure citation plays.
8. **Should Tap to Pay on iPhone get its own micro-domain in the
   Fleet (e.g. `tappay.uk`)?** It's growing fast and may be cleaner as
   a satellite property — open question, default is keep on
   CardMachines for now.
