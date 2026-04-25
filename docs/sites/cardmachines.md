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

TBD — sized separately as the biggest single content vacuum. UK pages
that exist, most commercially valuable verticals, the 8–10 pages to
build.

---

## 6. Tap to Pay on iPhone UK opportunity

TBD — fresh post-Apple-launch UK market, current owners (mostly US /
pre-launch content), the 5 pages to build.

---

## 7. Terminal model reviews coverage

TBD — table of models (Dojo Go, SumUp Solo, Zettle Reader 2, Square
Terminal, Stripe Reader S700, BBPOS WisePOS E) by competitors. AI
Overview citation magnets.

---

## 8. First 30 pages to build

TBD — prioritised. For each: URL slug, target query, primary surface
(SEO / AIO / AI Search), commission path.

---

## 9. Multilingual / Fleet candidates

TBD — short — which trade × community combos route to Fleet rather
than CardMachines.

---

## 10. Open questions

TBD.
