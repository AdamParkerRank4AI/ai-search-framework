# CardMachines — competitive deep-dive

Last updated: 2026-04-25
Site: CardMachines — UK card terminals, merchant accounts and payment
processing. Editorial + transactional combined. Owns terminal reviews,
switching content, vertical pages, high-risk merchant content,
booking-system integrations, Tap to Pay on iPhone.
Sister sites: BBL (loans editorial), FundBiz (loans broker / transactional).

Monetisation paths (already decided — see `docs/route-to-market.md`):
- **Awin:** Tide, SumUp, Zettle, Square
- **Direct in-house:** SumUp, Square, Zettle, Stripe, Tide, Dojo
- **Direct CPL with brokers:** Take Payments, Paymentsense, MerchantSavvy
- **High-risk direct deals:** Trust Payments, Universe Payments,
  Acquired.com — £200–500 CPLs

---

## 1. Executive summary

**Where CardMachines plays.** UK card terminals, merchant accounts and
payment processing for SMBs. A combined editorial + transactional play
that covers (a) terminal model reviews (Dojo Go, SumUp Solo, Zettle
Reader 2, Square Terminal, Stripe Reader S700, BBPOS WisePOS E), (b)
"card machine for [trade]" sector pages, (c) switching content from the
legacy acquirers (Worldpay / Barclaycard / Elavon), (d) UK high-risk
merchant accounts, and (e) Tap to Pay on iPhone — the four big content
vacuums in the UK SERP.

**Why CardMachines can dominate.** The competitor field is bifurcated
and weak in exactly the places that pay best. MerchantSavvy, Expert
Market, Mobile Transaction and money.co.uk dominate generic "best card
machine" listicles but barely cover sector landers, switching journeys,
or high-risk verticals. CardSwitcher and MerchantSwitch own the
quote-form switching funnel but have shallow editorial. BoonPay is a
small Manchester broker punching above its weight on hospitality but
nothing else. Merchant Insiders skews US. **No-one** owns UK Tap to Pay
on iPhone editorial, and UK high-risk content is a near-vacuum (most
ranking pages are US-based — QuadraPay, Tailored Pay, Chargebacks911).

**Top opportunity.** UK high-risk merchant accounts. £200–500 CPLs from
Trust Payments, Universe Payments and Acquired.com against a UK SERP
where most of the top 10 are non-UK pages. Stack high-risk on top of
switching content (Worldpay/Barclaycard exit-pain queries) and a clean
trade matrix (~16 trades × terminal recommendation), and CardMachines
captures the three highest-value query clusters in UK payments at once.
Tap to Pay on iPhone is the quick-win sweetener — fresh post-launch
market, low competition, every direct programme (SumUp, Square, Zettle,
Stripe, Tide, Revolut, Starling) ships an instant-signup affiliate.

---

## 2. Competitor table (top 10)

| # | Competitor | Content focus (one line) | Monetisation pattern | Vertical coverage | Signature page | Weakness / gap |
|---|---|---|---|---|---|---|
| 1 | **MerchantSavvy** | Editorial reviews + provider comparisons + processor "fees" deep-dives | Affiliate links + lead form to in-house brokered panel | Broad (light sector landers, mostly product-led) | `/payment-processors/elavon-review-fees/` and `/credit-card-machines-readers/` | Weak on Tap to Pay on iPhone, weak on UK high-risk, no per-trade landers |
| 2 | **Expert Market** | Listicles + provider reviews + "cheapest way" guides | Quote form (Quotezone-style lead gen) + affiliate | Broad-but-shallow (retail / hospitality / mobile) | `/uk/merchant-accounts/credit-card-machines-for-small-businesses` and Worldpay/SumUp pricing pages | Lead-form UX is heavy; sector landers are thin; reviews skim surface, no hands-on hardware testing |
| 3 | **Mobile Transaction (mobiletransaction.org)** | In-depth reviews of card readers + Tap-to-Pay coverage; rates 1–5 stars | Display ads + affiliate links | Mobile / sole-trader heavy (hairdressers, charities, market stalls) | `/card-reader-for-phones-uk/` and `/sumup-review/` | No transactional funnel; weak on traditional acquirers (Worldpay/Barclaycard/Elavon) and high-risk |
| 4 | **Compare Your Business Costs** | Quote-form comparison + provider pages | CPL with brokers + acquirer panel | Broad — utility-comparison style | `/card-payment-machines` and `/portable-card-machines` | Generic; thin editorial; no per-trade landers; no high-risk; no Tap to Pay editorial |
| 5 | **MerchantSwitch** | Switching content — "how to cancel" + "how to switch" + fees explainers | Quote form → broker callback | Switching-led not vertical-led | `/blog/how-to-cancel-worldpay-card-machine` | No hardware reviews, no per-trade content, no high-risk, no Tap to Pay |
| 6 | **CardSwitcher** | Quote-form comparison + glossary + blog | Lead gen to acquirer panel (20+ providers) | Broad / generic | Homepage compare quote tool + `/payment-processing/` | Thin editorial breadth; no Tap to Pay / high-risk depth; old-school SEO with limited AIO surface |
| 7 | **BoonPay (boonpay.uk)** | Manchester-based broker with strong hospitality / salon / beauty / healthcare blog | Direct merchant signup (in-house broker, PAX A920 Pro terminal) | Narrow — hospitality / hair & beauty / healthcare | `/blog/best-card-machine-for-a-salon-or-barber-shop-in-the-uk-2026` | Single-brand seller, not a true comparison; doesn't cover competitors fairly; no high-risk; small DR |
| 8 | **Startups.co.uk (payments)** | Editorial listicles + tested-and-rated reviews + niche guides (e.g. taxi) | Display + affiliate + sponsored | Broad with a few niche pages (taxis, retail) | `/payment-processing/best-small-business-credit-card-machines-readers/` and `/payment-processing/taxi-card-payment/` | Strong general SEO, weak on switching content + high-risk + sector matrix |
| 9 | **Take Payments (content hub)** | Long-form blog from a transactional broker — strong on "how to take payments in a [trade]" | In-house lead gen (their own acquirer panel + ISO) | Broad-and-deep — many trade-specific blog posts | `/blog/product-information/how-to-take-card-payments-in-a-hairdressers/` (and ~30 similar) | Blog format not landing-page format — wins informational SEO but converts less; no high-risk; no formal terminal-review section |
| 10 | **Merchant Insiders** | US-leaning content but heavy "Worldpay fees" / acquirer-fee guides that rank in UK SERPs | Affiliate / lead gen | Generic, US slant | `/blogs/worldpay-fees/` (the de-facto Worldpay fees guide that ranks UK) | US-coded entity; thin UK trust signals; no UK sector landers, no Tap to Pay UK, no UK high-risk |

**Add-on watchlist (clear UK rankers worth tracking):**
- **money.co.uk** — `/business/card-payment-solutions` ranks for top "best card machine" head terms; comparison-table style, broad-not-deep. Most resourced and hardest to outrank on plain head terms.
- **Merchant Machine (merchantmachine.co.uk)** — broker-content hybrid; strong on "11 Best Card Machines from £19" and provider review pages; Bionic-stable owned (similar to BusinessComparison).
- **Wise Tranxact (wetranxact.co.uk)** — comparison + ISO play with strong sector landers (tradespeople, beauty salons, retail) — closest competitor to a CardMachines-style trade matrix.
- **Independent Merchant Services (independentmerchantservices.co.uk)** — small independent ISO with rate-comparison content.
- **Teya** — direct acquirer (Saltpay rebrand) with growing blog presence.
- **Paymentsense (content)** — direct acquirer with sector-specific landers (beauty salon etc.). Counts as direct competition because they bid on the same trade keywords.
- **NPI.uk** — newer entrant ranking on "Best Card Machine UK 2026 buying guide".

---

## 3. Niche map by trade (trades × competitors)

Coverage of dedicated "card machine for [trade]" pages (i.e. either a
sector landing page or a clearly-titled blog with sector ranking
intent). `Y` = dedicated page; `~` = generic mention only / blog post
not a lander; `-` = no coverage. Wise Tranxact, Paymentsense and
Mobile Transaction are added to the matrix because they own the most
trade-specific pages — without them the gap analysis misses the real
incumbents.

| Trade | MerchantSavvy | Expert Market | Mobile Transaction | CYBC | MerchantSwitch | CardSwitcher | BoonPay | Startups.co.uk | Take Payments | Merchant Insiders | Wise Tranxact | Paymentsense | **Gap?** |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Plumber | - | - | ~ | - | - | - | - | - | ~ | - | **Y** (tradespeople) | ~ | **Wide gap** — high-intent mobile payments |
| Electrician | - | - | ~ | - | - | - | - | - | ~ | - | **Y** (tradespeople) | ~ | **Wide gap** |
| Gardener | - | - | ~ | - | - | - | - | - | ~ | - | **Y** (tradespeople) | - | **Wide gap** |
| Mobile mechanic | - | - | ~ | - | - | - | - | - | ~ | - | ~ | - | **Wide gap — clean vacuum** |
| Dog groomer | - | - | ~ | - | - | - | - | - | ~ | - | - | - | **Wide gap — clean vacuum** |
| Hairdresser (mobile) | - | ~ | **Y** | - | - | - | - | - | **Y** (blog) | - | ~ | - | Mid coverage; mobile-specific gap |
| Hairdresser (salon) | - | ~ | **Y** | - | - | - | **Y** | - | **Y** (blog) | - | **Y** (beauty salons) | **Y** | Saturated — incumbent territory |
| Barber | - | - | **Y** | - | - | - | **Y** | - | ~ | - | ~ | ~ | Mid gap — barber-specific lander wins |
| Mobile beautician | - | - | **Y** | - | - | - | - | - | ~ | - | ~ | - | Mid gap |
| Takeaway | - | - | ~ | - | - | - | **Y** | - | ~ | - | ~ | - | Mid gap — split chip-shop / kebab / pizza sub-pages still open |
| Restaurant | - | **Y** | ~ | **Y** | - | - | **Y** | - | **Y** (blog) | - | **Y** | **Y** (beauty) → no | Saturated head; sub-niches (gastropub, BYO, fine-dining) open |
| Pub | - | - | ~ | - | - | - | ~ | - | ~ | - | ~ | - | **Wide gap** |
| Cafe | - | ~ | ~ | - | - | - | ~ | - | ~ | - | ~ | - | Mid gap — clean lander wins |
| Vape shop | - | - | - | - | - | - | - | - | - | - | - | - | **Pure vacuum** — and high-risk payments tie-in |
| Off-licence | - | - | - | - | - | - | - | - | - | - | - | - | **Pure vacuum** |
| Salon (beauty/spa) | - | ~ | **Y** | - | - | - | **Y** | - | ~ | - | **Y** | **Y** | Saturated head; nail / lash / aesthetic sub-niches open |
| Market stall | - | - | **Y** | - | - | - | - | - | ~ | - | ~ | - | Mid gap |
| Taxi / private hire | - | ~ | ~ | - | - | - | - | **Y** | ~ | - | ~ | - | Mid gap |
| Charity | - | - | **Y** | - | - | - | - | - | ~ | - | ~ | - | Mid coverage |
| Tutor / driving instructor | - | - | ~ | - | - | - | - | - | ~ | - | - | - | **Wide gap** |
| Car wash / valeting | - | - | - | - | - | - | - | - | - | - | - | - | **Pure vacuum** |
| Trades (other — locksmith, chimney sweep, pest control) | - | - | - | - | - | - | - | - | ~ | - | - | - | **Wide gap** |
| Florist | - | - | - | - | - | - | - | - | ~ | - | - | - | **Wide gap** |
| Independent retail | - | **Y** | ~ | ~ | - | - | - | **Y** | ~ | - | **Y** | ~ | Saturated head |
| Pop-up / events | - | - | ~ | - | - | - | - | - | - | - | - | - | **Wide gap** |

### Headline read

- **Wise Tranxact, Paymentsense and BoonPay are the only competitors
  with real per-trade landers.** Wise Tranxact has the broadest matrix
  (tradespeople, beauty salons, restaurants, retail). Paymentsense
  owns beauty salons and restaurants direct. BoonPay punches above its
  weight on hospitality + salons. Everyone else relies on generic blog
  posts.
- **Take Payments has a sprawling blog-post network** ("how to take
  card payments in a [trade]") that ranks informational SEO but not
  transactional landing pages — CardMachines can convert on the same
  trade keywords with proper landers + matchers.
- **Pure vacuums (no UK competitor):** vape shop, off-licence, car
  wash / valeting, mobile mechanic, dog groomer. Each is a clean
  ranking play with a direct CPL or affiliate path. Vape shop also
  bridges into the high-risk merchant content vertical (vape is
  high-risk MID territory) — double-monetised.
- **Wide gaps (one weak incumbent):** plumber, electrician, gardener,
  pub, tutor / driving instructor, florist, locksmith / pest control /
  chimney sweep, pop-up / market stall events.
- **Mid gaps (saturated head, sub-niches open):** restaurant
  (sub-niches: gastropub, fine-dining, BYO, dark kitchen),
  takeaway (chip shop, kebab, pizza, fried chicken), salon (nail bar,
  lash bar, aesthetic clinic, men's grooming).
- **CardMachines wedge:** build ~25 dedicated "card machine for
  [trade]" landers in the priority order vacuum → wide gap → mid gap.
  Each lander = recommended terminal + alternatives table + sector
  feature must-haves (e.g. tip prompts for salons, 4G fallback for
  taxis, integrated EPOS for restaurants) + sector-specific FAQ +
  affiliate links to SumUp / Square / Zettle / Stripe / Tide where
  appropriate, plus a "compare quotes" CTA into Take Payments /
  Paymentsense / MerchantSavvy CPL deals.

---

## 4. Switching content opportunity (Worldpay / Barclaycard / Elavon)

### Why this matters

The three legacy acquirers — Worldpay (now FIS / GTCR-owned), Barclaycard
Merchant Services (now Worldline) and Elavon — collectively process the
majority of UK SMB card volume on **18–36 month contracts** with
**£150–£2,000 exit fees**, **90-day notice periods**, **auto-renewal**,
**equipment leases that survive cancellation**, and **PCI-compliance
charges of £5–£40/month**. Every year a large cohort of merchants reaches
contract-end / auto-renewal trigger, googles "how to cancel [acquirer]"
or "[acquirer] PCI fee" or "switch from [acquirer]", and looks for an
exit. Capturing that intent is a direct hand-off into Take Payments,
Paymentsense, MerchantSavvy, Dojo, SumUp Pro and (for high-risk) Trust
Payments — every one of them buys these leads.

### Ownership today

| Query | Top-3 owners | Strength |
|---|---|---|
| `cancel Worldpay` | MerchantSwitch (`/blog/how-to-cancel-worldpay-card-machine`), Merchant Maverick, Expert Market | MerchantSwitch wins because the URL is exact-match. Maverick is US-coded. Expert Market is generic. |
| `Worldpay PCI fee` / `Worldpay fees` | Merchant Insiders (`/blogs/worldpay-fees/` — the de-facto guide), Airwallex blog, MerchantSavvy | Merchant Insiders is the citation winner despite being US-leaning. UK-specific page is wide open. |
| `switch from Worldpay` | Merchant Maverick, MerchantSwitch, Expert Market `/end-card-machine-contract` | No clean UK transactional matcher; all are blog-style |
| `cancel Barclaycard merchant services` | MerchantSwitch (`/blog/how-to-cancel-barclaycard-merchant-services`), Barclaycard help pages (irrelevant to switching), Wise blog | MerchantSwitch owns the URL. Single page, beatable. |
| `switch from Barclaycard` | MerchantSwitch, scattered acquirer pages | Wide open |
| `cancel Elavon` / `Elavon exit fee` | Compare Your Business Costs review, Merchant Maverick, Elavon's own help pages | Pure vacuum on the cancel/switch intent — Elavon's own help pages outrank any commercial competitor |
| `Worldpay alternatives` / `Barclaycard alternatives` | Generic listicles (Expert Market, MerchantSavvy, money.co.uk) | Generic, beatable with proper comparison page |
| AI Overviews on these queries | MerchantSwitch + Merchant Insiders dominate today | Informational pages are winning the cite — switching matchers are not |

### The gap

No UK competitor runs a **diagnose-the-exit matcher**. The shape is:

> "Which acquirer are you on?" → contract-length / exit-fee / PCI-fee /
> notice-period explainer (Worldpay vs Barclaycard vs Elavon vs
> Paymentsense vs Take Payments vs takepayments) → "is it worth
> switching now or waiting?" calculator (remaining months × current
> rate vs new provider rate over remaining term) → CTA into a
> Paymentsense / Take Payments / MerchantSavvy / Dojo quote form.

MerchantSwitch has the right URL slugs. They don't have the calculator,
the alternatives matrix, or the AIO-shaped FAQ structure. Beatable.

### The 8 pages to build

1. **`/switch/`** — top-of-funnel hub: "Switching card machine providers
   in 2026 — read this first." Diagnose-by-acquirer matcher (Worldpay /
   Barclaycard / Elavon / Paymentsense / Tide / others) → exit-cost
   calculator → quote form. Primary surface: SEO + AIO.
2. **`/switch/cancel-worldpay/`** — head term `cancel Worldpay`. 18-month
   contract, £150–£500 exit fee, 90-day notice, auto-renewal trap, PCI
   fee, equipment lease persistence. Step-by-step cancel script + sample
   notice letter. Primary surface: SEO + AIO. CPL: Take Payments,
   Paymentsense, MerchantSavvy, Dojo.
3. **`/switch/worldpay-fees/`** — head term `Worldpay fees` / `Worldpay
   PCI fee`. Comprehensive fees teardown — match Merchant Insiders'
   structure but UK-coded with a named UK author + 2026 update date.
   Primary surface: AI Search (citation magnet). CPL: same panel.
4. **`/switch/cancel-barclaycard-merchant-services/`** — head term
   `cancel Barclaycard merchant services`. 3-5 year contracts (now
   Worldline), £2k exit fees, 90-day notice. Negotiation script
   (30–60% reductions are achievable). Primary surface: SEO + AIO.
5. **`/switch/cancel-elavon/`** — head term `cancel Elavon` /
   `Elavon exit fee`. 36-month contracts, £50 reconnection charge,
   equipment return process. Pure vacuum. Primary surface: SEO.
6. **`/switch/worldpay-alternatives/`** — comparison page: Worldpay vs
   Take Payments / Dojo / Paymentsense / SumUp Pro / Square / Tide.
   Rate-and-term comparison table. Primary surface: SEO + AIO. CPL:
   panel + Awin.
7. **`/switch/barclaycard-alternatives/`** — same shape, Barclaycard
   focus. Primary surface: SEO. CPL: panel.
8. **`/switch/exit-cost-calculator/`** — interactive calculator: input
   provider + monthly volume + remaining contract months → output
   exit-cost vs savings-from-switch over 12/24 months. Primary surface:
   AIO + SEO. Internal — feeds quote forms across the switch hub.

### Sizing

- "cancel Worldpay" + "switch from Worldpay" + variants ≈ 2k–4k UK
  monthly searches combined.
- "Barclaycard merchant services" cluster ≈ 1k–2k.
- "Elavon" cluster ≈ 500–1k.
- Total cluster ≈ 4k–7k UK monthly searches at top-of-funnel intent.
- Conversion model: 25% of switching searches result in a quote-form
  fill at sites that own the journey; 30% of those convert to a signed
  merchant. At £80–£150 CPL across Take Payments / Paymentsense /
  MerchantSavvy panel, conservative annual capture = **£75k–£200k/year**
  before high-risk upsell. Lower-risk than high-risk vertical because
  the buyer intent is mainstream.

---

## 5. High-risk merchant UK opportunity

### Why this is the biggest single content vacuum

CPLs are **£200–£500 per qualified merchant** (Trust Payments,
Universe Payments, Acquired.com, PurePay, We Tranxact, EpaymentSolutions,
Merchant Advice Service all buying). Approval cycles are 1–4 weeks but
sticky once landed (3-year+ relationships, processing-volume rev share).
**The UK SERP is dominated by US-coded pages** — QuadraPay, eMerchantBroker,
PayKings, Durango, Tailored Pay, Chargebacks911, Corepay, PaymentCloud,
SecureGlobalPay all rank for UK queries despite being US providers
without UK acquiring licences. The handful of UK-coded pages are thin.

### UK pages that actually exist

| URL | Owner | Coverage |
|---|---|---|
| `cardmachineproviders.co.uk/high-risk-merchant-accounts-uk/` | Card Machine Providers (small UK ISO) | Decent overview, low DR, no per-vertical depth |
| `wetranxact.co.uk/services/high-risk-merchant-accounts/` | Wise Tranxact | Best UK-coded — covers vape, supplements, forex, gaming, travel, subscription, CBD. Low DR. |
| `merchantadviceservice.co.uk/high-risk-merchant-accounts/` | Merchant Advice Service | Adult, CBD, vape, gaming verticals — lender-finder broker style |
| `epaymentsolutions.co.uk/high-risk-merchant-account/` | EpaymentSolutions | Adult, gaming, CBD — broker-style, thin content |
| `bestpaymentproviders.co.uk/cbd/` | Best Payment Providers | Single-vertical CBD page |
| `quadrapay.com/high-risk-merchant-accounts-uk/` | QuadraPay | US provider with UK page — actually ranks for UK queries |

The Trust Payments / Acquiring.com / PurePay partnership (announced 2023,
operational 2024–25) made Trust Payments the most credible UK
high-risk acquirer. They process for tobacco, CBD, nutraceuticals
direct, and feed in adult / gaming via partners. This is the named
direct-deal partner per `docs/route-to-market.md`.

### Most commercially valuable UK verticals (CPL band, named partner)

| Vertical | UK status | CPL band | Named UK partners |
|---|---|---|---|
| **CBD** (oils, edibles, topicals) | Legal but high-risk; FSA novel-foods compliance live | £250–£400 | Trust Payments / PurePay, We Tranxact, EpaymentSolutions, Axcess MS |
| **Vape / e-cig** | Legal but disposable-vape ban June 2025; reformulation churn = lots of new merchants | £250–£400 | Trust Payments, We Tranxact, Universe Payments |
| **Adult (UK-based content / toys / clubs)** | Legal but Stripe / PayPal hostile; Online Safety Act AV compliance live | £300–£500 | CCBill, Verotel, Universe Payments, EpaymentSolutions |
| **Firearms / shooting / airsoft** | Legal regulated; mainstream acquirers won't underwrite | £250–£400 | Trust Payments, Universe Payments, We Tranxact |
| **Online gambling / gaming** | UKGC-licensed only — narrow buyer pool, big tickets | £400–£500+ | Trust Payments (gaming licence), Acquired.com |
| **Travel / OTA / tour operator** | High chargeback risk; ATOL compliance | £200–£350 | Trust Payments, Acquired.com, We Tranxact |
| **Subscription / continuity / membership** | High chargeback / friendly-fraud | £200–£300 | Acquired.com, Trust Payments |
| **Nutraceuticals / supplements** | High chargeback + advertising-claims risk | £250–£400 | We Tranxact, Trust Payments, EpaymentSolutions |
| **Debt collection / debt management** | FCA-regulated; mainstream acquirers refuse | £250–£400 | Universe Payments, We Tranxact |
| **Dating / introduction services** | Reputational risk + chargebacks | £250–£350 | We Tranxact, EpaymentSolutions |
| **Crypto / FX / forex broker** | FCA-regulated for crypto; brokers need crypto-friendly acquirer | £400–£500 | Trust Payments, We Tranxact, B2BinPay-style |
| **Tobacco / cigars** | Legal regulated; mainstream-hostile | £250–£400 | Trust Payments / PurePay, We Tranxact |

### The 10 pages to build

1. **`/high-risk/`** — top-of-funnel hub: "UK high-risk merchant
   accounts in 2026 — the complete guide." Diagnose-by-vertical matcher
   (CBD / vape / adult / firearms / gambling / travel / subscription /
   nutra / debt collection / dating / crypto / tobacco) → vertical-specific
   explainer → quote form into Trust Payments / Universe Payments /
   Acquired.com / We Tranxact panel. Primary surface: AI Search +
   AIO. Direct CPL: £200–£500 across panel.
2. **`/high-risk/cbd/`** — head term `CBD merchant account UK`. FSA
   compliance, lab-report requirements, age-gate, allowed claims,
   reserve % typical, named UK acquirers. Primary surface: AI Search.
   CPL: Trust Payments, PurePay, We Tranxact (£250–£400).
3. **`/high-risk/vape/`** — head term `vape merchant account UK`.
   Disposable ban impact, age-verification, multi-pack rules, refill /
   pod processing, Online Safety Act for vape websites. Primary
   surface: AI Search. CPL: same panel (£250–£400). Cross-link to
   the `/trade/vape-shop/` lander.
4. **`/high-risk/adult/`** — head term `adult merchant account UK`.
   OnlyFans / clip-site / toys / clubs split. Online Safety Act AV
   compliance live (highest-friction AV regime in Europe). Visa /
   Mastercard adult-content rules. Named UK / EU acquirers (CCBill,
   Verotel, Universe Payments). Primary surface: AI Search. CPL:
   £300–£500.
5. **`/high-risk/firearms/`** — head term `firearms merchant account
   UK` / `gun shop card payments`. RFD compliance, Section-1 vs
   Section-2, airsoft / shotguns / shooting clubs. Pure vacuum.
   Primary surface: AI Search. CPL: £250–£400.
6. **`/high-risk/gambling/`** — head term `gambling merchant account
   UK` / `casino payment processor`. UKGC licensing prerequisite,
   credit-card ban for gambling (2020), Open Banking pay-in
   alternatives, stablecoin rails. CPL: £400–£500. Primary surface:
   AI Search.
7. **`/high-risk/travel-tour-operator/`** — head term `travel merchant
   account UK` / `tour operator payment processing`. ATOL compliance,
   chargeback windows on holiday products, airline IATA. Primary
   surface: AI Search + SEO. CPL: £200–£350.
8. **`/high-risk/subscription/`** — head term `subscription merchant
   account UK` / `recurring billing high risk`. Continuity-billing
   rules, friendly-fraud chargebacks, dunning, network tokenisation.
   Primary surface: AI Search. CPL: £200–£300. Cross-link to BBL /
   FundBiz for SaaS finance content.
9. **`/high-risk/nutraceuticals/`** — head term `supplements merchant
   account UK` / `nutraceutical payment processing`. Free-trial rules,
   ASA advertising-claims compliance, MHRA borderline products. Primary
   surface: AI Search. CPL: £250–£400.
10. **`/high-risk/debt-collection-credit-repair/`** — head term `debt
    collection merchant account UK` / `credit repair payment processing`.
    FCA permission requirements, low approval rates at mainstream banks.
    Pure vacuum. Primary surface: AI Search. CPL: £250–£400.

**Bonus tier (build when traffic justifies):** dating, crypto / FX,
tobacco / cigars, e-cig wholesale, kratom, kava, dropshipping
high-risk, MLM / network marketing — each is a clean ranking play with
the same panel.

### Sizing

- High-risk vertical search volumes are individually small (50–500
  monthly searches per head term) but concentrated commercial intent:
  the searcher is a business owner who has already been declined by a
  mainstream acquirer.
- Conservative TAM: 12 priority verticals × 500 monthly searches × 30%
  capture × 25% form-fill conversion ≈ 5,000 quote-form fills/year.
- At a 30% CPL-conversion rate (panel of 4 acquirers, only one needs to
  approve) and £300 average CPL = **£450k/year** at modest market share.
- This is the **single biggest revenue line** for CardMachines once
  built — bigger than switching, bigger than per-trade landers — because
  CPLs are 3–5× higher and competition is the lowest of the three
  themes. **It is the priority build.**

---

## 6. Tap to Pay on iPhone UK opportunity

### Why this is the cleanest quick win

Tap to Pay on iPhone launched in the UK in **July 2023** with Revolut
and Tyl by NatWest first; SumUp, Square, Stripe, Zettle, Adyen, Dojo,
myPOS, Viva Wallet and Worldline followed through 2024–25. Starling
launched in 2025. By April 2026 every major direct-affiliate partner
(SumUp, Square, Zettle, Stripe, Tide, Revolut, Starling) ships a
zero-hardware Tap-to-Pay product with **instant signup, software-only
activation, no contract**. That makes Tap to Pay the **easiest commission
path in the entire CardMachines niche**: low buyer friction, fast
conversion, and direct-programme commissions across multiple in-house
deals (£20–£40 per active reader from SumUp, flat fee from Square, etc.).

Despite the launch being three years old, the **content is overwhelmingly
US-coded or pre-launch UK**. UK SERPs surface a mix of:
- Apple's own marketing pages (no commercial intent capture)
- Mobile Transaction's `accept-contactless-payments-tap-on-phone-options`
  page (best UK content but old)
- Merchant Machine's `/tap-to-pay/` (decent but generic listicle)
- US guides (SwipeSimple, AGMS, PaymentNerds) ranking by default
- One-off news pieces from 9to5mac / MacRumors / Thurrott — pre-launch
- Provider-direct landers (apple.com, square.com, sumup.com, paypal.com)

### Who owns it today

| Query | Top-3 ranker | Strength |
|---|---|---|
| `Tap to Pay on iPhone UK` | apple.com/uk, sumup.com, mobiletransaction.org | Brand + Apple — beatable on the editorial slot |
| `how to take payments on iPhone UK` | mobiletransaction.org, gosolo.net, paypal.com | Mobile Transaction wins; gosolo is challenger |
| `best Tap to Pay app UK` | merchantmachine.co.uk, joinstored.com, mobiletransaction.org | All beatable — none has clean comparison-table format |
| `Tap to Pay vs card reader` | scattered, mostly provider-direct | **Pure vacuum** for editorial coverage |
| `Stripe Tap to Pay UK` / `Square Tap to Pay UK` / `SumUp Tap to Pay UK` (per-provider) | Provider-direct + occasional Mobile Transaction | Wide gap on per-provider editorial |
| `Tap to Pay PCI compliance UK` | paymentnerds.com (US), Apple support | UK vacuum |
| AI Overviews on these queries | Apple's own page + Mobile Transaction dominate today | Beatable — neither is structured for AIO |

### The gap

No UK content site runs a **per-provider Tap to Pay comparison + an
honest "should I use this or buy a card reader?" matcher**. Every
direct-programme partner pays an instant-signup commission. Build the
hub now while the buyer journey is still young.

### The 5 pages to build

1. **`/tap-to-pay-iphone/`** — head term `Tap to Pay on iPhone UK`.
   The editorial hub: how it works, device requirements (iPhone XS+),
   £100 contactless cap, supported providers comparison table (SumUp /
   Square / Stripe / Zettle / Tide / Revolut / Starling / Dojo / Adyen /
   myPOS / Tyl / Worldline), fees side-by-side, decision tree
   ("instant signup vs in-app vs developer-led"). Primary surface:
   SEO + AIO. Commission path: instant-signup affiliate fan-out across
   SumUp, Square, Zettle, Stripe (Awin + direct).
2. **`/tap-to-pay-iphone/vs-card-reader/`** — head term
   `Tap to Pay vs card reader`. Honest matcher — when Tap to Pay
   beats a £29 SumUp Air, when it doesn't (no chip & PIN above £100
   contactless, no tip prompt without app, battery drain, multi-staff
   workflow). Primary surface: AIO + AI Search. Commission: same panel
   + cross-link to the per-trade landers.
3. **`/tap-to-pay-iphone/sumup/`** — provider-specific lander. SumUp
   Tap to Pay setup, fees (1.69%), eligibility, business types, cap on
   transaction value, comparison vs SumUp Solo / SumUp Air. Primary
   surface: SEO. Direct: SumUp partner programme.
4. **`/tap-to-pay-iphone/square/`** — provider-specific lander. Square
   Tap to Pay setup, fees (1.75%), Square POS app interaction, refunds,
   tipping, multi-location. Primary surface: SEO. Direct: Square
   partner.
5. **`/tap-to-pay-iphone/by-trade/`** — head term cluster
   `Tap to Pay for [trade]`. Single page with trade-by-trade
   recommendations: market traders, mobile hairdressers, tutors, dog
   walkers, food trucks, delivery / pop-up, plumbers, electricians.
   Primary surface: SEO + AIO. Cross-link to per-trade landers in
   section 8. Commission: panel.

**Bonus tier (build if Tap to Pay momentum justifies):** Tap to Pay on
Android UK (different rails — Google Wallet / SoftPOS), Tap to Pay
PCI compliance UK guide, Tap to Pay limits and the £100 contactless
cap explained.

---

## 7. Terminal model reviews coverage

Coverage of dedicated single-model review pages (URL slug like
`/dojo-go-review` or equivalent). `Y` = dedicated review page; `~` =
mention inside a listicle / comparison; `-` = no coverage.

| Model | MerchantSavvy | Expert Market | Mobile Transaction | CYBC | MerchantSwitch | CardSwitcher | BoonPay | Startups.co.uk | Take Payments | Merchant Insiders | Finder | Stored | Merchant Machine | money.co.uk |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Dojo Go** | ~ | **Y** (Dojo) | **Y** | **Y** | - | - | ~ | ~ | ~ | - | **Y** | **Y** | **Y** | ~ |
| **SumUp Solo** | ~ | **Y** (SumUp) | **Y** | ~ | - | - | ~ | **Y** (SumUp) | ~ | - | - | **Y** | ~ | ~ |
| **Zettle Reader 2** | **Y** | ~ | **Y** | ~ | - | - | - | ~ | ~ | - | - | **Y** | **Y** | ~ |
| **Square Terminal** | ~ | **Y** (Square) | **Y** | ~ | - | - | - | **Y** (Square reader) | ~ | - | - | **Y** | ~ | ~ |
| **Stripe Reader S700** | - | ~ | **Y** (Stripe Terminal — covers S700) | - | - | - | - | - | ~ | - | **Y** (Stripe) | - | - | - |
| **BBPOS WisePOS E** | - | ~ (mentioned in Stripe review) | ~ | - | - | - | - | - | - | - | - | - | - | - |
| Square Reader (3rd gen) | ~ | **Y** | **Y** | ~ | - | - | - | **Y** | ~ | - | - | **Y** | ~ | ~ |
| SumUp Air | ~ | ~ | **Y** | ~ | - | - | - | ~ | ~ | - | - | **Y** | ~ | ~ |
| SumUp Solo Lite (2024) | - | - | **Y** | - | - | - | - | - | - | - | - | - | - | - |
| Tide Card Reader Plus | - | **Y** | ~ | ~ | - | - | - | ~ | ~ | - | - | - | - | ~ |
| takepaymentsplus | ~ | **Y** | - | **Y** | - | - | - | **Y** | **Y** | - | - | - | - | - |
| PAX A920 Pro | ~ | - | ~ | - | - | - | **Y** | - | - | - | - | - | - | - |
| Clover Flex | ~ | ~ | - | - | - | - | - | ~ | - | - | - | - | - | - |
| Revolut Reader | ~ | ~ | **Y** | - | - | - | - | ~ | - | - | - | ~ | - | - |
| Tyl by NatWest reader | ~ | - | ~ | - | - | - | - | - | - | - | - | - | - | - |

### Headline read

- **Mobile Transaction owns terminal-model reviews.** They have the
  deepest single-page reviews, scoring rubric (5 criteria × 5 stars),
  hands-on testing, and frequent updates. The closest competitor is
  Stored (joinstored.com) which is newer but actively investing.
- **AI Overview citation surface.** Single-model review pages are
  where AI Overviews surface citations on queries like "is the Dojo Go
  any good", "what's the difference between SumUp Solo and Air",
  "best card reader for [trade]". Mobile Transaction wins these
  citations today because the structure is clean (Pros / Cons /
  Pricing / Verdict / FAQ in question-as-H2 form).
- **BBPOS WisePOS E is a clean vacuum.** Almost no UK content
  reviews this terminal as a stand-alone product (everyone treats it
  as "Stripe Terminal" generically). It's the entry-level Stripe
  countertop reader for £179. Single-model lander wins.
- **Stripe Reader S700 is near-vacuum.** Mobile Transaction has a
  Stripe Terminal review that mentions it; Stored covers Stripe; no-one
  has a dedicated S700 lander.
- **CardMachines wedge:** build dedicated review landers for the 6
  priority models in the brief (Dojo Go, SumUp Solo, Zettle Reader 2,
  Square Terminal, Stripe Reader S700, BBPOS WisePOS E) plus 6 more
  high-value models (SumUp Air, Tide Card Reader Plus, takepaymentsplus,
  PAX A920 Pro, Square Reader 3rd gen, Revolut Reader). Each =
  1,500–2,500 words, hands-on test where possible, scoring rubric,
  comparison table vs nearest alternatives, FAQPage schema for AIO.
  Use `/reviews/[model]` URL pattern. Total = 12 review pages, all
  AI-Overview-citation candidates.

---

## 8. First 30 pages to build

Prioritised. **Pages 1–10 are the wedge** (high-risk hub + switching hub
+ Tap to Pay hub + the three highest-CPL high-risk verticals). **Pages
11–20 build out the trade matrix and review hub.** **Pages 21–30 fill
out switching long-tail, more high-risk verticals, and Tap to Pay
sub-pages.**

| # | URL slug | Target query | Primary surface | Commission path |
|---|---|---|---|---|
| 1 | `/high-risk/` | "high risk merchant account uk" | AI Search + AIO | Direct CPL: Trust Payments, Universe Payments, Acquired.com, We Tranxact (£200–£500) |
| 2 | `/high-risk/cbd/` | "cbd merchant account uk" | AI Search | Direct CPL: Trust Payments / PurePay, We Tranxact (£250–£400) |
| 3 | `/high-risk/vape/` | "vape merchant account uk" | AI Search | Direct CPL: Trust Payments, We Tranxact, Universe Payments (£250–£400) |
| 4 | `/high-risk/adult/` | "adult merchant account uk" | AI Search | Direct CPL: CCBill, Verotel, Universe Payments (£300–£500) |
| 5 | `/switch/` | "switch card machine provider uk" | SEO + AIO | Direct CPL: Take Payments, Paymentsense, MerchantSavvy, Dojo |
| 6 | `/switch/cancel-worldpay/` | "cancel worldpay" | SEO + AIO | Direct CPL: Take Payments, Paymentsense, Dojo, SumUp Pro |
| 7 | `/switch/worldpay-fees/` | "worldpay fees" / "worldpay pci fee" | AI Search + AIO | Direct CPL: Take Payments, Paymentsense, MerchantSavvy |
| 8 | `/tap-to-pay-iphone/` | "tap to pay on iphone uk" | SEO + AIO | Direct in-house: SumUp, Square, Zettle, Stripe (instant signup) |
| 9 | `/reviews/dojo-go/` | "dojo go review" | AIO + AI Search | Direct: Dojo (apply direct per route-to-market doc) |
| 10 | `/reviews/sumup-solo/` | "sumup solo review" | AIO + AI Search | Direct: SumUp partner (£20–£40 per active reader) |
| 11 | `/trade/vape-shop/` | "card machine for vape shop uk" | SEO + AIO | Direct CPL: Trust Payments (high-risk) + Awin (SumUp / Square) |
| 12 | `/trade/restaurant/` | "card machine for restaurant uk" | SEO | Awin: SumUp / Square / Zettle; Direct CPL: Take Payments, Paymentsense |
| 13 | `/trade/takeaway/` | "card machine for takeaway uk" | SEO | Awin + CPL panel |
| 14 | `/trade/cafe/` | "card machine for cafe uk" | SEO | Awin: SumUp / Square / Zettle |
| 15 | `/trade/pub/` | "card machine for pub uk" | SEO | Awin + CPL: Paymentsense, Take Payments |
| 16 | `/trade/hairdresser-salon/` | "card machine for hairdresser uk" / "card machine for salon" | SEO + AIO | Awin + CPL panel |
| 17 | `/trade/barber/` | "card machine for barber uk" | SEO | Awin: SumUp / Square (low-volume sole-trader fit) |
| 18 | `/trade/mobile-mechanic/` | "card machine for mobile mechanic uk" | SEO + AIO | Direct: SumUp, Square (mobile-fit); CPL panel |
| 19 | `/trade/dog-groomer/` | "card machine for dog groomer uk" | SEO + AIO | Direct: SumUp, Square; CPL panel |
| 20 | `/reviews/zettle-reader-2/` | "zettle reader 2 review" | AIO + AI Search | Awin: Zettle (PayPal Partner Network) |
| 21 | `/reviews/square-terminal/` | "square terminal review uk" | AIO + AI Search | Direct: Square partner |
| 22 | `/reviews/stripe-reader-s700/` | "stripe reader s700 review uk" | AIO + AI Search | Direct: Stripe Partner Ecosystem |
| 23 | `/reviews/bbpos-wisepos-e/` | "bbpos wisepos e review" / "stripe wisepos e" | AIO (clean vacuum) | Direct: Stripe |
| 24 | `/switch/cancel-barclaycard-merchant-services/` | "cancel barclaycard merchant services" | SEO + AIO | Direct CPL panel |
| 25 | `/switch/cancel-elavon/` | "cancel elavon" / "elavon exit fee" | SEO | Direct CPL panel |
| 26 | `/switch/exit-cost-calculator/` | "card machine exit fee calculator uk" | AIO + SEO | Internal — feeds quote forms |
| 27 | `/high-risk/firearms/` | "firearms merchant account uk" | AI Search | Direct CPL: Trust Payments, Universe Payments (£250–£400) |
| 28 | `/high-risk/gambling/` | "gambling merchant account uk" / "casino payment processor uk" | AI Search | Direct CPL: Trust Payments, Acquired.com (£400–£500+) |
| 29 | `/tap-to-pay-iphone/vs-card-reader/` | "tap to pay vs card reader" | AIO + AI Search | Awin + direct panel |
| 30 | `/trade/plumber-electrician/` | "card machine for plumber" / "card machine for electrician" | SEO + AIO | Direct: SumUp, Square (mobile-fit); CPL panel |

### Build sequence note

- **Weeks 1–4:** ship pages 1, 5, 8 — the three hub pages. They're the
  internal-link backbone and AI-Overview citation candidates.
- **Weeks 5–8:** ship pages 2, 3, 4 (top three high-risk verticals,
  highest CPLs) and pages 6, 7 (Worldpay switching — biggest organic
  volume).
- **Weeks 9–12:** ship pages 9, 10, 20, 21, 22 — the terminal review
  hub (AI-Overview citation factory) and pages 11–14 (priority trades
  including the vape-shop / high-risk crossover).
- **Months 4–6:** fill out the trade matrix (15–19, 30), the rest of
  switching (24, 25, 26), and the remaining high-risk verticals
  (27, 28).
- **Cross-link rule:** every trade page links to (a) the relevant
  reviewed terminal, (b) the switch hub, (c) Tap to Pay where the
  trade is mobile-fit. Every high-risk page links to the trade page
  if a trade exists (vape shop ↔ vape merchant account, takeaway ↔
  none, dating site ↔ none).

---

## 9. Multilingual / Fleet candidates

Per `docs/niche-brief.md` Fleet rules: multilingual content **defaults
to Fleet, not CardMachines**, because non-English subfolders dilute
CardMachines' English entity graph and AI-Overview citation profile.
The trade × community combos worth a Fleet microsite:

| Combo | Why it works | Fleet domain working name |
|---|---|---|
| **Polish builder / tradesperson card payments** | Polish is the largest non-English UK community. Builders, plumbers, electricians, decorators — heavy Tap to Pay / SumUp / Square fit. Polish-language Reddit + Facebook groups discuss card readers. | `terminalplatniczy.uk` or `czytnikkartuk.pl` |
| **Polish hairdresser / beauty / nail bar** | Large diaspora vertical, mobile + salon mix; SumUp / Square direct programmes pay on signup. | `salon-platnosci.uk` |
| **Bengali / Sylheti takeaway + restaurant** | UK curry-house vertical is dominated by Sylheti-speaking owners; Take Payments / Paymentsense already chase this audience offline. | `cardterminal-bangla.uk` |
| **Turkish barber + kebab takeaway** | Turkish-coded barber shops + kebab takeaways concentrated London / Birmingham / Manchester. SumUp / Square Tap to Pay fit. | `kart-makinesi.uk` |
| **Punjabi / Hindi convenience store + off-licence** | Convenience-store + off-licence vertical heavily Punjabi / Hindi. Off-licence is also a content vacuum on the brand site. | `cardmachine-punjabi.uk` |
| **Romanian car wash + valeting** | Romanian-coded vertical, heavy mobile-payments fit; pure vacuum on UK SERP. | `aparat-card.uk` |
| **Mandarin takeaway + nail bar** | Two strong Mandarin-speaking SMB verticals; nail-bar takeaway niche is essentially un-covered. | `dukapayment.uk` |

**Routing reminder:** these are **Fleet sites, not CardMachines
subfolders**. Each microsite ships with its own Trustpilot, named
author in-language, and direct-CPL relationships routed via the same
backend (Trust Payments accepts merchants regardless of marketing
language). Surface this in the chat summary if any community-vertical
brief comes in.

**Hyper-local fleet candidate (single):** `cardmachine-london.uk` for
a London-only payments microsite covering Camden / Shoreditch / Soho /
Brixton hospitality clusters — but only if the English brand
saturates first. Defer.

---

## 10. Open questions

1. **Direct-CPL contracts for high-risk acquirers.** Trust Payments,
   Universe Payments, Acquired.com all run partner programmes but
   most require traffic before sign-off. What's the minimum-traffic
   threshold for each? Can we sign on referral / soft-launch via
   PurePay (Trust Payments' high-risk introducer)? £200–£500 CPLs
   only land if the contracts close.
2. **Dojo direct programme.** Per `docs/route-to-market.md` Dojo
   should be applied to direct. Confirm: are they running an
   affiliate / partner programme right now, or is this a "call BD,
   negotiate per-lead" play? Their cold-call sales motion suggests
   they pay materially per qualified merchant.
3. **AI-Overview citation profile.** AIO is a primary surface for
   reviews + switching pages. We need named-author E-E-A-T (real UK
   payments specialist with LinkedIn + bylines), Trustpilot
   collection from day one, and consistent entity descriptions across
   the network. Who is the named author? Which partner agency runs
   review collection?
4. **Hands-on hardware testing.** Mobile Transaction wins terminal
   reviews because they hands-on test. To compete on AI Overviews we
   need hands-on photos / video for the 12 priority terminals. Budget
   ~£1.5k for hardware + 1 week of testing. Worth it given each
   review compounds into permanent AIO citations.
5. **PSR card-fees market review.** Payment Systems Regulator's
   ongoing market review of scheme + processing fees (2024–26) is a
   trigger event for switching content. When it reports, a "what the
   PSR review means for your card fees" page is a citation magnet.
   Track the publication date.
6. **Online Safety Act AV requirements.** Live in 2025 — affects
   adult merchants and certain dating / gambling operators. The
   `/high-risk/adult/` page must reflect current AV-provider list
   (Yoti, Persona, AgeVerification.com, k-ID). Review every 6 months
   as the regime tightens.
7. **Cross-link governance with sister sites.** CardMachines should
   send loan-funnel intent (e.g. "I need finance for my new card
   machine") to BBL / FundBiz; BBL/FundBiz sector landers (hospitality,
   beauty, retail, e-commerce) should link to CardMachines per-trade
   landers. Define the link pattern.
8. **Booking-system integrations content.** Skipped per scope. But
   Phorest / Treatwell / Fresha / Timely / Vagaro / OpenTable /
   ResDiary / Booksy integration pages are AI-search citation magnets
   in the salon / hospitality verticals. Pick up in a follow-up brief.
9. **Schema strategy.** Skipped per scope. FAQPage + Product +
   Review + HowTo schema will be load-bearing on the review hub and
   high-risk pages. Pick up in a follow-up.
10. **MTD April 2026 trigger event.** Making Tax Digital phase 2 is
    live — small businesses now need to keep digital records. This
    drives EPOS-integrated card-terminal demand (Xero / QuickBooks /
    Sage integrations). Worth a `/integrations/` mini-hub.
