# Portable Research Prompts

Six self-contained prompts you can paste into another Claude / GPT / Perplexity / agent terminal. Each hunts a different shape of UK search niche. Run them in parallel and bring the outputs back to this repo.

**Cover all six lenses for full coverage:**

| # | Prompt | What it hunts |
|---|---|---|
| 1 | Dormant / Resurfacing / Pivoting (generic) | Categorical opportunities across consumer + B2B |
| 2 | Digital / tech / SaaS-focused | UK SME software, AI tools, no-code, dev services, online services |
| 3 | Long-tail aggregation / matrix patterns | Niches where head term is hard but a 100×N modifier matrix is wide open |
| 4 | Event / regulation / deadline-driven | Niches with a 6–18 month recency window opening now |
| 5 | Anti-niche / competitor-traffic capture | "[Brand] alternatives", "is X worth it", "how to cancel X" |
| 6 | Hyperlocal per-postcode aggregation | Pure programmatic per UK geographic unit |

---

## Prompt 1 — Dormant / Resurfacing / Pivoting (generic)

```
You are a UK-focused niche-research analyst. Your job is to find me UK
search niches that are DORMANT, RESURFACING, or PIVOTING — places where
search demand exists but the existing content is stale, thin, or wrong,
so a fresh content site built on Astro + structured data could rank in
4–12 weeks.

DEFINITIONS

DORMANT SERP — a Google UK results page where 3+ of the following are true:
- Top 10 pages have update dates older than 2 years
- Top 10 includes Reddit / MoneySavingExpert / Mumsnet / forum threads
- Top 10 includes Yell, Yelp, FreeIndex, BT Local, or 2010-era directories
- Top 10 has thin pages (<600 words, no schema)
- No AI Overview, or AI Overview is vague and hedging
- No featured snippet or PAA, or weak PAA
- Same boilerplate template repeats across multiple top-10 results
- Top 10 has low average domain authority

RESURFACING NICHE — search demand was once high, dropped off, and is
rising again now. Triggers: new UK regulation, new trend / cultural
moment, demographic catching up, taboo lifting, or technology making an
old product viable again.

PIVOTING NICHE — the buyer's needs are changing right now because of new
compliance, new product replacement, audience shift, or old top-ranked
content being made wrong by a recent change.

WHAT I WANT BACK

Find me 15 UK niches that fit one of these three patterns. For each one,
return:

1. Niche name (one line)
2. Pattern (Dormant / Resurfacing / Pivoting / Hybrid)
3. The trigger if Resurfacing or Pivoting (regulation, trend, etc.)
4. 5–8 example UK search queries with rough monthly volume estimates
5. Why the SERP is dormant — name the signals you spotted
6. Multi-buyer lead-resale potential — name the UK buyers / affiliates
   / lead networks that would pay £15+ per qualified lead, ideally 3+
7. Programmatic potential — can it be templated by location × modifier
   × sub-type at scale?
8. Tag: Quick-Win (4–12 weeks to rank), Mid-Term (3–9 mo), or Long-Term

DISQUALIFIERS — DO NOT INCLUDE

- Property finance niches: bridging, BTL, HMO, holiday let, dev finance,
  commercial mortgages, equity release. All out.
- YMYL with hard regulatory walls (FCA-authorised broker required, MHRA
  prescription, SRA legal advice) — only include if there's a clean
  affiliate / referral path that bypasses the cert burden.
- Anything where the SERP top 10 is already dominated by 5+ updated
  authority brands — too competitive.
- Single-buyer markets where leads can only be sold to one place.
- Generic listicles like "best CRM" — only include if there's a specific
  underserved sub-niche behind it (e.g. "best CRM for UK chimney sweeps").

CONTEXT — RESEARCH WITH THESE BIASES

- UK-only audience. Use UK terminology and UK search intent.
- Date is April 2026. Use only sources and signals current to 2026.
- Lean toward niches where the in-house phone team can qualify a lead
  once and resell it to 3–5 buyers.
- Lean toward niches that pair with one of these revenue stacks:
  affiliate, lead resale, listing fees, or own white-label product.
- Bonus points for niches that surface AI Visibility Gaps — places where
  ChatGPT / Gemini / Perplexity give vague or wrong answers because the
  underlying source content is stale.
- Bonus points for trends that haven't peaked yet — rising volume on
  Google Trends UK in the past 12 months.

OUTPUT FORMAT

Return the 15 niches as a clean numbered list. Then at the end, give me
your top 3 picks with one sentence on why.
```

---

## Prompt 2 — Digital / tech / SaaS

```
You are a UK-focused niche-research analyst. Your job is to find me UK
search niches in the DIGITAL / TECH / SOFTWARE / ONLINE-SERVICES space
that are DORMANT, RESURFACING, or PIVOTING — places where search demand
exists but the existing content is stale, thin, or wrong, so a fresh
content site built on Astro + structured data could rank in 4–12 weeks.

"Digital" for this brief means:
- Software / SaaS / apps / mobile apps / web apps
- AI tools, AI agents, AI integrations, prompt-engineering, ChatGPT-for-X
- No-code / low-code platforms (Bubble, Webflow, Glide, Softr, FlutterFlow)
- Automation tools (Zapier, Make.com, n8n)
- Bespoke development services (custom CRM, internal tools, dashboards)
- Digital products (templates, courses, ebooks, info products)
- Online services (fractional execs, virtual assistants, freelancers,
  remote consultants, online tutors, online therapists, online doctors)
- Digital service comparisons / directories for UK SMEs and consumers
- Digital marketing / SEO / paid media services for UK businesses
- Cyber, GDPR, compliance services delivered digitally
- Online learning, bootcamps, career-switch courses
- Subscription products and SaaS-by-industry niches

DEFINITIONS

DORMANT SERP — a Google UK results page where 3+ of the following are true:
- Top 10 pages have update dates older than 2 years
- Top 10 includes Reddit / Hacker News / Indie Hackers / Mumsnet / forum
  threads
- Top 10 includes legacy directories: Yell, FreeIndex, Capterra (thin
  pages), G2 (thin pages), Trustpilot listings as the main result
- Top 10 has thin pages (<600 words, no schema, no comparison tables)
- No AI Overview, or AI Overview is vague, hedging, or recommends only
  US-based tools when a UK audience is searching
- No featured snippet or PAA, or weak PAA
- Same boilerplate template repeats across multiple top-10 results
- Top 10 dominated by US software brands' UK landing pages with no
  UK-specific content (no UK pricing, no UK GDPR notes, no UK case
  studies)
- Low average domain authority across the top 10

RESURFACING NICHE — digital search demand was once high, dropped off,
and is rising again. Triggers in the digital space:
- New UK regulation (UK GDPR, Online Safety Act, accessibility regs,
  Digital Markets Act, MTD ITSA, AI Act adoption)
- AI making old products viable again (AI receptionist, AI scheduling,
  AI customer service, AI bookkeeping)
- Old SaaS category being disrupted by no-code / AI alternatives
- Demographic catching up (Gen Z entering business buying, Gen X
  retiring, freelance economy hitting maturity)
- Post-Brexit UK-only buying preference rising vs offshore

PIVOTING NICHE — buyers' needs in the digital space are shifting right
now because of:
- Old SaaS being replaced (e.g. WordPress → Webflow / Framer; Mailchimp
  → Beehiiv; standalone CRMs → AI-native CRMs)
- Established categories being unbundled by AI agents (customer service,
  scheduling, content production, bookkeeping)
- Privacy / data-residency rules forcing buyers off US-hosted tools
- New compliance making existing top-ranked content wrong (AI Act, UK
  GDPR updates, Online Safety Act)
- Audience moving from generalist marketplaces (Upwork, Fiverr) to
  trusted UK-only directories

WHAT I WANT BACK

Find me 15 UK digital niches that fit one of these three patterns. For
each one, return:

1. Niche name (one line)
2. Pattern (Dormant / Resurfacing / Pivoting / Hybrid)
3. The trigger if Resurfacing or Pivoting (regulation, trend, AI
   disruption, etc.)
4. 5–8 example UK search queries with rough monthly volume estimates
5. Why the SERP is dormant — name the signals you spotted
6. Multi-buyer lead-resale / affiliate potential — name the UK and
   global SaaS / digital-service buyers, networks, or affiliate
   programmes that would pay £15+ per qualified lead, ideally 3+ per
   lead. Bonus for recurring SaaS commissions (20–40% lifetime).
7. Programmatic potential — can it be templated by industry × tool ×
   use-case × price tier × city at scale?
8. Tag: Quick-Win (4–12 weeks to rank), Mid-Term (3–9 mo), or Long-Term

DISQUALIFIERS — DO NOT INCLUDE

- Generic enterprise SaaS comparison ("best CRM 2026", "best project
  management software"). G2 / Capterra / Forrester own these. Only
  include if there is a specific underserved sub-niche behind it
  (e.g. "best CRM for UK funeral directors", "best booking software for
  UK reformer pilates studios").
- Big-ticket enterprise tooling aimed at companies with 250+ staff. Aim
  for UK SMEs with 5–250 staff and £500k–£20m turnover.
- Anything dominated by 5+ updated authority brands in the SERP top 10.
- Property-tech, mortgage-tech, BTL portfolio software, conveyancing
  software, surveyor software. Property is out.
- YMYL with hard regulatory walls (FCA-authorised, MHRA prescription,
  SRA legal advice) — only include if a clean affiliate / referral path
  bypasses the cert burden.
- Single-buyer markets (only one possible affiliate or partner).
- Anything that requires running ads on Google Ads or Meta to monetise
  (we're SEO + content + email).

CONTEXT — RESEARCH WITH THESE BIASES

- UK-only audience. Use UK terminology, UK pricing, UK GDPR / data
  residency angles, UK case studies.
- Mid-market UK buyer profile: marketing manager, ops manager, MD or
  founder of an SME, with budget for SaaS subscriptions £20–£500/month
  per seat or one-off project budgets £2k–£100k. NOT enterprise.
- The "no trust" buyer: knows they need something built or subscribed
  to, doesn't know where to start, wants UK, doesn't trust offshore /
  Upwork / Fiverr / £500 cowboys / £100k London agencies.
- Date is April 2026. Use only sources and signals current to 2026.
- Lean toward niches where one captured lead can be qualified once and
  resold or affiliate-routed to 3–5 buyers.
- Lean toward niches that pair with one of these revenue stacks:
  - Recurring SaaS affiliate (20–40% lifetime commission)
  - Digital service lead resale (fractional execs, VAs, freelancers)
  - Listing fees from vetted UK providers (£99–£499/month)
  - Concierge / matchmaking fees (10–15% of project value)
  - Own white-label digital product (template, course, mini-tool)
- Bonus points for niches that surface AI Visibility Gaps — where
  ChatGPT / Gemini / Perplexity / Claude give vague answers, recommend
  only US tools, or miss UK-specific compliance and pricing.
- Bonus points for trends that haven't peaked yet — rising volume on
  Google Trends UK in the past 12 months. Particular interest in:
  - AI agents replacing single SaaS categories
  - Tools / tools-of-tools (meta-directories, "find me a tool that does X")
  - Trust-led UK directories vs offshore freelancer marketplaces
  - No-code unbundling specific verticals
  - Post-MTD ITSA tooling waves (April 2026 onwards)
  - Industry-specific SaaS in dormant verticals
  - Digital products for the Gen X self-employed / Gen Z micro-business
    cohorts
- Bonus points for "front-door" niches — digital tools or directories
  that capture SME buyers early and feed into multiple downstream
  affiliate / lead-resale opportunities.

OUTPUT FORMAT

Return the 15 niches as a clean numbered list. For each, follow the
8-field structure exactly. Then at the end give me your top 3 picks
with one sentence on why each is the strongest commercial play. Include
a final note on any niches where you suspect existing top-10 content is
about to be invalidated by a known 2026 regulatory change or AI
disruption — those are the highest-priority swoops.
```

---

## Prompt 3 — Long-tail aggregation / matrix patterns

```
You are a UK-focused niche-research analyst. Your job is to find me UK
search niches that are LONG-TAIL AGGREGATION plays — where individual
search queries are low-volume (10–500 monthly searches each), but the
underlying STEM pattern can be templated into hundreds or thousands of
unique URLs that, stacked together, add up to enormous combined search
volume. Built on Astro + structured data + a JSON/CSV dataset, this can
ship as a programmatic site in days, with each URL capturing tiny
intent but the whole site compounding into 50k–500k+ monthly sessions.

I am specifically looking for the pattern where:

- A single "head" query is competitive and saturated.
- Behind it sits a matrix of long-tail variations (Axis A × Axis B ×
  Axis C) that incumbent sites have NOT bothered to template.
- Each variation is too small individually for big sites to chase.
- Combined, the variations represent 5,000–50,000+ monthly searches in
  the UK.
- SERPs for those long-tail variations are dominated by Reddit, niche
  forums, ageing blog posts, or thin auto-generated content — not
  authority brands.
- The buying intent on each variation is real (commercial, comparison,
  or decision-stage).
- A single Astro template + a clean dataset can produce the lot.

DEFINITIONS (carry forward from prior briefs)

DORMANT SERP — Google UK results page where 3+ of the following are
true: top 10 pages older than 2 years, top 10 includes Reddit / forums,
top 10 includes legacy directories, top 10 has thin pages (<600 words,
no schema), no AI Overview or vague AI Overview, no featured snippet or
weak PAA, same boilerplate template repeats, low average DA.

RESURFACING — once-popular topic rising again due to UK regulation,
trend, demographic, taboo lifting, or technology making it viable.

PIVOTING — buyers' needs changing now due to compliance, product
replacement, audience shift, or top-ranked content being made wrong.

LONG-TAIL AGGREGATION (the new pattern this brief is hunting for) — a
niche where the head term is hard but the underlying matrix of
combinations is easy. Examples of the pattern, NOT to be reused as
suggestions:

- "[Cooking method] [food item] [diet]" — cooking-time / temperature
  / recipe matrices.
- "Cost of owning a [pet breed]" × 80 breeds.
- "[Software] alternative for [use case]" × hundreds of combinations.
- "How to [task] in [software]" × thousands of combinations.
- "Does [food / supplement] interact with [medication]".
- "[Postcode area] [service]" hyperlocal across 1,800 UK postcode
  districts.
- "[Plant species] care guide [condition]".
- "[Tool / model number] vs [tool / model number]" pairwise.
- "[Hobby] for [skill level / age band / disability / dietary need]".
- "Is [activity] safe for [condition]".
- "Common faults [appliance brand] [model]" repair-guide matrices.

WHAT I WANT BACK

Find me 15 UK long-tail-aggregation niches that fit one of the
patterns above. For each one, return:

1. Niche name (one line)
2. Pattern type (Long-Tail Aggregation, with sub-pattern: matrix /
   pairwise / hyperlocal / how-to / care-guide / interaction-check /
   troubleshoot / vs)
3. The "stem" pattern — the templated query in plain English, e.g.
   "[cooking method] [food item] [air fryer time]"
4. The dimensions of variation — Axis A, Axis B, Axis C — with rough
   counts of items in each axis
5. Approximate total templated URLs achievable
6. Per-URL volume estimate (showing it's individually low: 10–500/mo)
7. Total combined UK monthly search volume estimate
8. 5 example queries from the matrix with rough monthly volume each
9. Why the SERP is dormant — name the signals
10. Monetisation stack — affiliate, lead resale, listing fees, white-
    label, AdSense, with realistic UK CPL or commission ranges
11. Dataset source — where the analyst would source the data to populate
    the matrix (public registers, scraping ethics permitting, ONS / VOA
    / Companies House / CQC / Ofsted / FSA / open APIs / community
    wikis / brand spec sheets)
12. Tag: Quick-Win (4–12 weeks), Mid-Term (3–9 mo), or Long-Term

DISQUALIFIERS — DO NOT INCLUDE

- Property finance niches: bridging, BTL, HMO, holiday let, dev finance,
  commercial mortgages, equity release. Out.
- YMYL with hard regulatory walls (FCA-authorised, MHRA prescription,
  SRA legal advice) — unless there's a clean affiliate path that
  bypasses the cert burden.
- Single-axis niches with no variation matrix behind them (those are
  head-term plays, not aggregation plays).
- Generic listicles: "best CRM", "best gym" — only include if there's
  a deep matrix behind a specific sub-niche.
- Anything dominated by 5+ updated authority brands in top 10 of the
  long-tail variations.
- Pure programmatic spam patterns (e.g. dictionary scrape, keyword
  permutations with no real intent). Each URL must answer a real
  question with real intent.
- Niches where the matrix has fewer than ~200 templated URLs — too
  small to justify the build.

CONTEXT — RESEARCH WITH THESE BIASES

- UK-only audience. UK terminology, UK measurements, UK pricing,
  UK postcode geography, UK regulators (CQC / Ofsted / FSA / VOA / etc.)
  as data sources where relevant.
- Date is April 2026.
- Lean toward niches where the dataset is freely available or
  scrape-cheap (open APIs, public registers, brand spec sheets,
  Wikipedia, community wikis, Reddit-mined common questions).
- Lean toward niches where each long-tail URL has commercial intent
  and at least one obvious affiliate / lead / ad cash-out per page.
- Bonus points for matrices where the data updates seasonally or
  yearly (creates a content-refresh moat).
- Bonus points for matrices where AI Overviews currently fail to
  return useful answers because no clean structured source exists.
- Bonus points for niches that pair with an existing UK content hub I
  could already be running (gym, pet, wedding, home improvement,
  cleaning trades, car / vehicle, finance, MTD ITSA, ADHD / mental
  health, side-hustle, etc.) — a long-tail aggregation site that feeds
  another site of mine is double value.
- Bonus points if the dataset can be sourced once and used to power
  multiple sites (e.g. UK breed list powers pet costs, pet supplements,
  pet insurance pages all at once).

OUTPUT FORMAT

Return the 15 niches as a clean numbered list, each with the 12-field
structure. Then at the end give me your top 3 picks with one sentence
on why each is the strongest commercial aggregation play, plus a
bottom-line estimate of combined monthly UK search volume and total
templated URL count if all 15 niches were built.

Also flag any niche where the dataset is held in a single hard-to-scrape
proprietary source (e.g. a paywalled industry database). Those are
lower priority unless we can negotiate a data partnership.
```

---

## Prompt 4 — Event / regulation / deadline-driven (recency window)

```
You are a UK-focused niche-research analyst. Your job is to find me UK
search niches where a SPECIFIC DATE TRIGGER is creating a recency
window — a regulation, deadline, scheme launch / closure, tax change,
cultural event, or market event in 2026–2027 that is causing search
demand to rise sharply while existing top-ranked content is becoming
stale, wrong, or outdated. Built on Astro + structured data, a fresh
content site can ride the recency window and capture the spike before
incumbents refresh their content.

I want triggers where the window is OPEN NOW or opens within the next
18 months. Anything older than 6 months past trigger date is closed.

DEFINITIONS

DORMANT SERP — top 10 has 3+ of: pages older than 2 years, Reddit /
forum threads ranking, legacy directories, thin pages, vague AI
Overview, no PAA, boilerplate templates, low DA.

RECENCY WINDOW — a 6–18 month period where:
- A specific dated event triggers a measurable search spike
- Existing top-ranked content is dated, incomplete, or factually wrong
  in light of the trigger
- AI Overviews are hedging or quoting outdated rules
- Buyers are confused and actively researching
- New entrants can win the SERP simply by being current and accurate

UK TRIGGERS WORTH HUNTING (categories — find specific 2026–2027
instances within each)

- UK tax deadlines (Self Assessment, MTD ITSA, Corporation Tax, VAT
  thresholds, IR35, off-payroll, Capital Gains)
- HMRC reporting changes (Schedule 23, OECD CARF, MTD waves)
- Property regulation (Renters' Rights Act May 2026, EPC C 2030,
  Awaab's Law extension to PRS, leasehold reform, HMO licensing)
- Consumer regulation (Online Safety Act enforcement, Digital Markets
  Act, AI Act adoption, accessibility regs WCAG 2.2)
- Energy / climate (Boiler Upgrade Scheme uplifts, ECO5, Great British
  Insulation Scheme, EV grant changes, smart meter targets, FIT closure)
- Pensions (auto-enrolment changes, State Pension Age changes, dashboard
  launch, pension review)
- Workplace (umbrella tax reforms April 2026, employment rights bill,
  fire-and-rehire ban, statutory sick pay 2026, day-one rights)
- Consumer finance (interest rate decisions, FCA Consumer Duty
  enforcement, savings rate ceiling/floor changes)
- Driving (FORS, DVS direct vision standard expansion, ULEZ scope,
  Clean Air Zones in new cities, MOT rule changes)
- Education (T-levels, apprenticeship levy reform, university fee
  changes)
- Cultural / event (UK general election cycle, Eurovision UK
  involvement, Commonwealth Games, royal events, school holiday
  patterns, Black Friday timing, Christmas trading rules)

WHAT I WANT BACK

Find me 15 UK niches with an OPEN OR ABOUT-TO-OPEN recency window. For
each one, return:

1. Niche name (one line)
2. Trigger date (specific calendar date or month)
3. Window status: OPEN NOW / OPENING IN [N] MONTHS / RECURRING ANNUAL
4. The trigger explained in two sentences — what changes, who it
   affects
5. Why existing top-ranked content is now wrong or stale
6. 5–8 example UK search queries with rough monthly volume estimates
   and direction of trend (rising / spiking / sustained)
7. AI Overview status — is the AIO currently giving wrong, vague, or
   outdated answers? (If yes, this is a high-priority swoop.)
8. Multi-buyer lead-resale / affiliate potential — name 3+ UK buyers,
   networks, or affiliates that would pay £15+ per qualified lead
9. Programmatic potential — can we template the content per region /
   sector / use-case so the recency window covers more than one URL?
10. Estimated time the window stays open (months)
11. Tag: Quick-Win (4–12 weeks to rank), Mid-Term (3–9 mo), or
    Long-Term

DISQUALIFIERS — DO NOT INCLUDE

- Triggers more than 18 months in the future (too far out, content
  decays before the window opens)
- Triggers more than 6 months past (window has closed; existing
  content has caught up)
- Property finance: bridging, BTL, HMO, holiday let, dev finance,
  commercial mortgages, equity release
- YMYL with hard regulatory walls (FCA-authorised, MHRA prescription,
  SRA legal advice) — only include if a clean affiliate path bypasses
  the cert burden
- Single-product triggers (e.g. one specific lender's rate change)
- Triggers that only affect 250+ staff enterprises

CONTEXT — RESEARCH WITH THESE BIASES

- UK-only audience. UK terminology, UK regulators, UK calendar.
- Date is April 2026. Anchor everything to this date.
- Lean toward triggers that recur annually (you build once, harvest
  every cycle).
- Lean toward triggers that affect UK SMEs and consumers (mid-market,
  not enterprise).
- Bonus points for triggers where the existing top 10 is visibly
  outdated (still quoting pre-trigger numbers / rules).
- Bonus points for triggers where AI Overviews are hedging or quoting
  the wrong year.
- Bonus points for triggers that overlap with multiple existing
  content hubs (a single trigger that lights up wedding + finance +
  tax + landlord audiences is gold).

OUTPUT FORMAT

Return the 15 niches as a clean numbered list with the 11-field
structure. Then at the end give me your top 3 picks with one sentence
on why each has the strongest commercial recency window. Also flag any
trigger that recurs annually (the "build once, harvest forever"
patterns) — those should jump priority.
```

---

## Prompt 5 — Anti-niche / competitor-traffic capture

```
You are a UK-focused niche-research analyst. Your job is to find me UK
search niches that capture COMPETITOR TRAFFIC — searches from buyers
who are actively trying to leave, complain about, cancel, or replace an
incumbent UK brand or service. The buyer has high commercial intent,
the SERP is usually weak (because the incumbent brand will not write
this content about themselves), and a clean independent comparison
site can swoop in and route the buyer to alternatives via multi-buyer
affiliate or lead resale.

DEFINITIONS

ANTI-NICHE — search territory consisting of one or more of:
- "[brand] alternatives" / "[brand] competitors"
- "is [brand] worth it" / "is [brand] legit" / "[brand] honest review"
- "[brand] complaints" / "[brand] problems" / "[brand] issues"
- "how to cancel [brand]" / "[brand] cancellation"
- "[brand] vs [competitor]" pairwise comparisons
- "[brand] price hike 2026" / "[brand] gone up"
- "switch from [brand]" / "leaving [brand]"
- "[product] not working" / "[service] down today"

DORMANT SERP — top 10 has 3+ of: pages older than 2 years, Reddit /
forum threads ranking high (very common in anti-niche), legacy
directories, thin affiliate clones, vague AI Overview, no PAA, low DA.

WHY ANTI-NICHE WORKS

- The incumbent brand will not host this content (it would harm them)
- Reddit dominates by default (community always discusses alternatives)
- Buyers are mid-funnel or bottom-funnel — high conversion intent
- Each anti-search can be routed to 3–10 alternative providers, each
  paying lead / affiliate fees
- Many anti-searches recur (price hikes happen yearly, scandals
  repeat, churn cycles are predictable)

WHAT I WANT BACK

Find me 15 UK anti-niches that fit this pattern. For each one, return:

1. Niche name — the incumbent or category (e.g. "Sky TV alternatives",
   "PureGym cancellation")
2. Anti-pattern type (alternatives / cancellation / complaints / scam-
   check / pairwise-vs / "is it worth it" / scandal-driven / price-hike-
   driven)
3. Why people are searching for the anti-niche right now — name the
   trigger (price hike, service issue, scandal, regulation change,
   churn season, contract renewal)
4. 5–8 example UK search queries with rough monthly volume estimates
5. Why the SERP is dormant — name the signals you spotted (incumbent
   silence, Reddit dominance, thin affiliates)
6. Multi-buyer lead-resale / affiliate stack — name 3+ UK alternative
   brands, networks, or affiliate programmes that would pay £15+ per
   qualified lead. Bonus for recurring SaaS / service commissions.
7. Programmatic potential — can we template "[brand] alternatives" /
   "[brand] vs [competitor]" / "how to cancel [brand]" across multiple
   brands in the same category?
8. Recurrence — does the search demand recur annually (contract
   renewal cycles, energy price cap rounds, gym January spikes) or is
   it one-off (scandal-driven, regulatory change)?
9. Tag: Quick-Win (4–12 weeks), Mid-Term (3–9 mo), or Long-Term

DISQUALIFIERS — DO NOT INCLUDE

- Brands too small for meaningful UK search volume (<500 monthly
  searches across the anti-pattern)
- Categories with only one viable alternative (single-buyer = no
  resale)
- YMYL with hard regulatory walls — only include if a clean affiliate
  path exists (e.g. "leaving Vitality" can route to Bupa / AXA Health
  / WPA via authorised broker, fine; "is XYZ vaccine safe" is out)
- Property finance brands (BTL lenders, mortgage brokers, etc.)
- Pure trolling / hate-content territory — keep it commercial
- Brands where the parent owns the SERP defensively (e.g. brands with
  active reputation-management agencies suppressing all anti-content)

CONTEXT — RESEARCH WITH THESE BIASES

- UK SERP only. UK incumbents. UK alternatives.
- Date is April 2026.
- Strong bonus points for incumbents that have:
  - Recently raised prices (energy suppliers, broadband, streaming,
    gym memberships, banks, insurers)
  - Recently been in the news for service issues, outages, scandals,
    or regulatory action
  - Predictable contract-renewal cycles (annual energy contracts,
    insurance renewals, mobile contracts, broadband)
  - Visible churn — declining Trustpilot scores, rising "cancel"
    search volume
- Strong bonus points for categories where the buyer routinely
  switches every 1–3 years (energy, broadband, insurance, gym,
  mortgage, mobile, streaming, banking)
- Lean toward niches where multiple alternative providers exist and
  all want leads (energy switching, broadband switching, gym
  membership, banking, insurance, SaaS).

OUTPUT FORMAT

Return the 15 anti-niches as a clean numbered list with the 9-field
structure. Then at the end give me your top 3 picks with one sentence
on why each has the strongest commercial signal. Also flag any
incumbent that's currently in the news for a price hike, scandal, or
regulatory action — those are the highest-priority swoops because the
search spike is happening now and the SERP hasn't caught up.
```

---

## Prompt 6 — Hyperlocal / per-postcode aggregation

```
You are a UK-focused niche-research analyst. Your job is to find me UK
search niches that work as PURE HYPERLOCAL programmatic sites — where
content is templated per UK geographic unit (postcode district, ward,
village, town, council area, parliamentary constituency) at scale.
Individual per-location volume is small, but the geographic matrix
gives you 1,800–95,000+ unique URLs per service, each capturing local
buying intent.

UK GEOGRAPHIC MATRIX SCALES (any axis the analyst can use)

- ~1,800 UK postcode districts (e.g. SW1, M1, BD3)
- ~3,000 UK postcode sectors (e.g. SW1A 1, M1 4)
- ~9,500 UK wards
- ~10,000 UK parishes
- ~33,000 UK postcode walking-routes (very granular, niche)
- ~650 UK parliamentary constituencies
- ~390 UK councils (county / unitary / district)
- ~1,500 UK towns and small cities (>2,000 pop)
- ~20,000+ UK villages

DEFINITIONS

DORMANT SERP — top 10 has 3+ of: ageing pages, Yell / FreeIndex / BT
Local results, single-business pages from 2014, thin council pages,
forum threads, no AI Overview or AI Overview giving generic answers.

HYPERLOCAL AGGREGATION — a niche where:
- Each per-location URL has tiny volume (10–500 monthly searches)
- The dataset is templated from public sources (Companies House, OS,
  council registers, NHS / CQC / Ofsted / FSA registers, ONS, Land
  Registry, OpenStreetMap, postcode database, UK Charity Commission)
- 500+ unique URLs are achievable from a single template + dataset
- Local buying intent is high (commercial, urgent, or comparison)
- Google Business Profile is a strong signal in the SERP, but the
  long-tail informational + comparison space is weakly covered
- A clean Astro site with structured data + map embeds + sortable
  tables outperforms incumbents

WHAT I WANT BACK

Find me 15 UK hyperlocal niches that fit this pattern. For each one,
return:

1. Niche name (one line)
2. Geographic granularity (postcode district / ward / village / town /
   council / constituency / postcode sector / radius)
3. Total templated URLs achievable (e.g. 1,800 postcode districts ×
   8 service types = 14,400 URLs)
4. Per-URL volume estimate (showing it's individually low: 10–500/mo)
5. Total combined UK monthly search volume estimate (head term +
   long-tail aggregated)
6. 5 example queries from the matrix with rough monthly volume each
7. Dataset source — where the analyst would get the data to populate
   the matrix (must be free or scrape-cheap UK public source)
8. Why the SERP is dormant — name the signals (Yell-era directories,
   thin council pages, forum dominance, etc.)
9. Multi-buyer lead-resale / affiliate stack — name 3+ UK buyers,
   networks, or affiliates that would pay £15+ per qualified local
   lead
10. Local intent type (urgent / planned / comparison / informational /
    transactional)
11. Programmatic data refresh frequency (does the dataset change
    monthly, quarterly, yearly — affects the content-refresh moat)
12. Tag: Quick-Win (4–12 weeks), Mid-Term (3–9 mo), or Long-Term

DISQUALIFIERS — DO NOT INCLUDE

- Property finance: bridging, BTL, HMO, holiday let, dev finance,
  commercial mortgages, equity release
- Niches dominated entirely by Google Business Profile (where the
  organic SERP is irrelevant because the map pack owns it). Only
  include if there's a clear comparison / informational layer above
  GBP that we can win.
- YMYL with hard regulatory walls (FCA-authorised, MHRA prescription,
  SRA legal advice) — only include if affiliate path bypasses the cert
  burden
- Services only available in major cities (need geographic variation
  across all UK regions)
- Datasets locked behind paywalls or proprietary APIs (must be public
  or scrape-cheap)
- Niches with fewer than 500 templated URLs achievable

CONTEXT — RESEARCH WITH THESE BIASES

- UK-only. UK postcodes, UK councils, UK regulators as data sources.
- Date is April 2026.
- Lean toward niches where the buyer wants a UK local provider and
  doesn't trust national directories (Yell, BT Local).
- Lean toward niches where multiple national / regional providers
  compete locally, all want leads (cleaning trades, repair services,
  pet services, tradesmen, fitness, food delivery).
- Bonus points for niches where Google Business Profile is weak or
  inconsistent — many micro-niches have huge gaps in GBP coverage.
- Bonus points for niches where the dataset can be sourced from a
  public UK register (Companies House, CQC, Ofsted, FSA, OS,
  OpenStreetMap, council planning portals, charity commission).
- Bonus points for niches where the per-location URL can be paired
  with structured-data outputs that AI Overviews would cite (lists,
  tables, schema-marked-up local-business profiles).
- Bonus points for niches where the data REFRESHES regularly — that
  becomes a recurring content-update moat that competitors can't keep
  up with.

OUTPUT FORMAT

Return the 15 hyperlocal niches as a clean numbered list with the
12-field structure. Then at the end give me your top 3 picks with one
sentence on why each is the strongest commercial play. Also estimate
the combined total templated URL count if all 15 niches were built —
the moat compounds enormously when you stack hyperlocal sites that
share the same UK geographic dataset.
```

---

## How to use these prompts

1. Pick the prompt that matches the angle you want to hunt.
2. Paste the entire fenced block (between the ``` marks) into another Claude / GPT / Perplexity / agent terminal.
3. Run it.
4. The agent returns a 15-niche list with 8–12 fields per niche.
5. Send the survivors back to this repo — they get rubric-scored against the Five-Signal Model in `niche-brief.md` and added to the master numbered index in `niche-shortlist-2026-04.md`.

### Sanity checks before trusting an output

- **Cross-check Google Trends UK manually** for any "rising volume" claim. AIs can hallucinate "this is rising" without checking.
- **Run the actual UK Google search incognito** before committing to a niche. Some AIs see cached SERPs from months ago.
- **Drop anything property-related** unless it's been explicitly approved for the build queue. Property is dropped from this plan.
- **Drop anything with FCA / MHRA / SRA hard walls** unless an affiliate path bypasses the cert burden.
