# UK Gym & Fitness Hub — Master Project Plan

**Domain:** `findagym.co.uk` (or `.com`)
**Status:** Master plan — April 2026
**One-line vision:** A UK-wide gym & fitness comparison site that wins by capturing the things buyers actually want to know — when each gym is quiet, who goes there, what the equipment is really like — that no incumbent reviews. Multi-buyer affiliate + listing fees + lead resale + cross-sell into the existing card-terminals / asset-finance fleet.

Pilot scope is locked separately in `docs/site-builds/gym-colchester-pilot-v0.md` (Colchester, 35 URLs, v0.1).

---

## 1. Two ideas, not one

### Asset A — The Under-Served Review Engine (the real IP)

A structured dataset and rendering engine that captures, for every UK gym:
- Demographic profile (gender / age / skill split)
- Popular times (Google Maps Popular Times feed)
- Equipment audit (counts, ceilings, condition)
- Class roster + named instructors
- Best for / Underrated for / Worst for honest assessments
- Pricing + contract terms

Once built, this engine renders every kind of comparison page (best gyms in [town], cheapest, 24h, women's, by goal, by specialism, brand reviews, vs pages, under-served angles like "quietest gym for [town]"). It's the chassis. Town-by-town expansion is just adding rows to the dataset.

### Asset B — `findagym.co.uk` (the consumer site)

The first surface that consumes the Engine. Pilot launches in Colchester, scales nationally.

**Strategic implication:** the Under-Served Review Engine is what makes this site uncopyable. AI Overviews can't write these reviews because the source data doesn't exist publicly in structured form. Generic UK gym sites don't bother because it's expensive to capture. Once we've done it for 200 UK towns, displacing us requires the same investment — and by then we own the SERP.

---

## 2. The market

UK Health & Fitness Market Report 2026:
- **12.2 million UK gym members (record)**
- **18% of over-16s** are members (record penetration)
- Sector growing fast post-pandemic
- Major chains:
  - **PureGym** — 362 sites, 1.9m+ members (UK's largest)
  - **The Gym Group** — 240+ sites
  - **Anytime Fitness** — 175+ sites
  - **JD Gyms** — 95+ sites
  - **énergie Fitness** — ~100 sites
  - **David Lloyd** — ~100 premium sites
  - **Nuffield Health** — ~100 sites (medical / corporate angle)
  - **Virgin Active** — ~40 premium sites
  - **Bannatyne** — ~70 sites
  - **Gymbox / Third Space / Equinox** — premium London-led
  - **Better (GLL)** — council leisure, ~270 sites
- Pricing variance is huge: Leicester / Manchester / Birmingham £15–20/mo, Oxford / York / Brighton / Bath £30–50+/mo (2026)

That regional pricing variance is programmatic gold.

---

## 3. The SERP today (why it's dormant)

For "PureGym vs The Gym Group", "best gym [city]", and most modifier searches, the top 10 is dominated by:
- Wikipedia
- Indeed (employer reviews — wrong intent)
- The Student Room (forum thread)
- TikTok / YouTube videos (not text-content competitors)
- Which? (paywalled)
- Solix (small comparison page)
- One niche attempt: askgympal.co.uk — thin, no scale
- Big chain location pages (own brand only)

**No authoritative UK gym comparison/directory exists.** Hussle is a *gym-pass aggregator* (different model). Per-town comparison space is wide open. Per-modifier ("best gym for early mornings", "least intimidating gym in [town]") space is wider open still. Nobody captures equipment audits or demographic profiles. **That's the gap.**

---

## 4. The differentiator (this is the whole strategy)

Generic gym-ranking content tells you which is cheapest. We tell you what buyers actually want to know:

- **When is each gym quiet vs busy?**
- **Who actually goes there?** (M/F/other split, age bands, beginner-to-advanced ratio, atmosphere)
- **What's the equipment really like?** (count, ceiling, condition, broken bits)
- **Which classes are good?** (instructor names, popularity)
- **What's it underrated for?** (the surprising win nobody mentions)
- **What's it bad at?** (we don't soften this)

This is content AI Overviews can't write. Reddit has it scattered. Existing UK gym review sites don't have this depth. Capturing it once per gym, structuring it cleanly, refreshing seasonally — **that's the moat.**

The full page-template that renders this on every gym page is locked in `gym-colchester-pilot-v0.md` §5.

---

## 5. The modifier matrix (the SERP playbook at full UK scale)

Each axis is a content cluster. The same gym dataset renders pages across every axis.

### 5.1 Tier / cost (8 variants per town)
budget · cheap · affordable · mid-range · luxury · premium · "under £20/mo" · "no contract"

### 5.2 Hours / access (5 variants per town)
24-hour · 24/7 · early-bird (5–7am open) · late-opening (after 22:00) · weekend access

### 5.3 Brand reviews (15+ variants per town, where the brand has a branch)
PureGym · The Gym Group · Anytime Fitness · JD Gyms · énergie · Snap Fitness · Gymbox · Third Space · Equinox · Nuffield Health · David Lloyd · Virgin Active · Bannatyne · Total Fitness · Everlast · Better (GLL council)

### 5.4 Brand × modifier pairwise comparisons (~30 strongest UK-wide)
"PureGym vs The Gym Group" · "PureGym vs Anytime Fitness" · "Gym Group vs JD Gyms" · "Anytime Fitness vs PureGym 24/7" · "David Lloyd vs Nuffield" · etc.

### 5.5 Specialism / boutique (12+ variants per town)
CrossFit · Hyrox-prep · F45 · Barry's · Orangetheory · reformer pilates · hot yoga · climbing · bouldering · calisthenics · Olympic lifting · powerlifting · bodybuilding · MMA · boxing · jiu-jitsu · swimming pool gym · spin studio

### 5.6 Audience (8 variants per town)
women's-only · ladies-only · men's · students · over 50s · post-natal · accessible · LGBT-friendly · neurodivergent-friendly · beginners

### 5.7 Goal (10+ variants per town)
weight loss · muscle gain · marathon prep · Hyrox prep · post-injury · postnatal · fitness over 40 / 50 · fat-burning · powerlifting · bodybuilding · functional / movement

### 5.8 Under-served angle (5+ variants per town — the differentiator pages)
quietest · least intimidating · best classes · best equipped · most progress-friendly · friendliest beginner gym · best for serious lifters · best showers · best parking

### 5.9 Comparison hub-pages (UK-wide, not town-level)
"PureGym review 2026" · "The Gym Group review 2026" · "Anytime Fitness review UK 2026" · "Best gym chains UK 2026" · "Gym chain comparison UK 2026"

---

## 6. Programmatic scale (full UK)

| Layer | Calculation | URLs |
|---|---|---|
| Tier × town | 8 modifiers × 250 towns | 2,000 |
| Hours × town | 5 × 250 | 1,250 |
| Brand × town (where present) | avg 6 brands × 250 towns | 1,500 |
| Brand × modifier pairwise | 30 strong × 100 town context | 3,000 |
| Specialism × town | 12 × 250 | 3,000 |
| Audience × town | 8 × 250 | 2,000 |
| Goal × town | 10 × 250 | 2,500 |
| Under-served angle × town | 5 × 250 | 1,250 |
| Per-brand UK reviews | 16 brands | 16 |
| Town hub pages | 250 | 250 |
| Site-level pages | 10 | 10 |
| **Total at full scale** | | **~16,776 pages** |

(Pilot scope is 35 pages — see `gym-colchester-pilot-v0.md`.)

---

## 7. The data model

Every page on the site is rendered from one shared dataset. The full JSON schema per gym is in `gym-colchester-pilot-v0.md` §6.1. Summarised here:

### 7.1 Identity layer
gym_id, name, brand, tier, address, postcode, lat, lng, phone, website

### 7.2 Hours + pricing layer
24/7 flag, daily hours, monthly price, joining fee, contract terms

### 7.3 Demographic profile layer (the moat)
gender split estimate · age bands · beginner / intermediate / advanced split · intimidation factor 1–5 · music volume · atmosphere notes

### 7.4 Popular Times layer
24-hour-by-7-day numeric matrix sourced from Google Maps Popular Times (refresh quarterly)

### 7.5 Equipment audit layer
cardio counts by type · dumbbell ceiling kg · barbell count · squat rack count · deadlift platform count · power cage count · cable stations · functional zone size · pool / sauna / steam · broken-or-worn notes

### 7.6 Class roster layer
list of class names with instructor names where known + day / time / popularity

### 7.7 Honest review layer
best_for (3–5) · underrated_for (1–2) · worst_for (2–3) · honest_pros · honest_cons

### 7.8 External review aggregation layer
review_count_google · review_avg_google · review_count_trustpilot · review_avg_trustpilot

### 7.9 Refresh metadata
last_data_refresh · last_visit_date

---

## 8. Data sources

### 8.1 Free / open

| Source | What we extract | Refresh |
|---|---|---|
| Brand websites | locations, hours, prices, contracts, classes | Quarterly |
| Google Maps Place API + Popular Times | name, address, lat/lng, popular times, photos, hours | Quarterly |
| Trustpilot | review count + average per gym | Monthly |
| Google Reviews | review count + average + atmosphere quote mining | Monthly |
| Companies House SIC 93.13 (fitness facilities) | UK independent gym register | Quarterly |
| REPS / CIMSPA | UK personal trainer register (Phase 2 PT directory) | Monthly |
| ONS Postcode Directory | town / region / lat-lng | Quarterly (shared with Geo Engine) |

### 8.2 Manual visits (the actual moat)

For each town, the top 6 gyms get a real visit:
- Peak slot (Mon 18:00) and off-peak (Sat 09:00)
- Capture equipment audit, demographic read, "underrated for" angle
- ~2 hours per visit, 12 visits per town = 24 hours' work
- Cost ~£200 per town if outsourced (student / fitness-savvy freelancer)

Across 250 UK towns, that's £50,000 of fieldwork over the lifetime of the build — but it's also the moat. Competitors won't do it. AI Overviews can't fake it. **It's what makes the site uncopyable.**

### 8.3 User-submitted reviews (post-launch)

Once the first 6 towns are live, add a structured review form on every gym page:
- "When did you last visit?"
- "How busy was it on a scale of 1–5?"
- "Estimate the gender split"
- "What's the gym best for in your view?"
- "What's it worst for?"
- "Free-text comment"

User submissions get moderated, then merged into the dataset. Compounding moat.

---

## 9. Monetisation

### 9.1 Affiliate (primary, immediate)

| Partner | Network | CPL / commission | Where it appears |
|---|---|---|---|
| The Gym Group | Awin | ~£8/signup | Brand review, cheap, 24-hour, day pass |
| PureGym | direct | ~£10/signup | Brand review, cheap, 24-hour, audience |
| Anytime Fitness | direct | ~£15/signup | Brand review, 24-hour |
| JD Gyms | Awin | ~£8/signup | Brand review |
| Hussle (gym pass) | direct | ~£10–20/signup | Day pass, no-contract, hub, every gym page |
| ClassPass | Impact | ~£20–40 first conversion | Boutique, reformer pilates, classes |
| MyProtein | Awin | 8% commission | Sidebar all pages |
| Bulk | Awin | 8% commission | Sidebar |
| Holland & Barrett | Awin | 4% commission | Sidebar |
| Gymshark | direct | ~6% | Sidebar |
| Garmin / Whoop / Oura | Awin | £20–60/sale | Sidebar fitness pages |
| Apple Fitness+ | Apple | varies | Sidebar |
| Mirafit / JLL Fitness / Bowflex | Awin | 4–8% | Home gym, equipment pages |
| Origym (PT cert) | direct | £100–500/lead | PT directory page (Phase 2) |
| Train Fitness (PT cert) | direct | £100–500/lead | PT directory (Phase 2) |

### 9.2 Listing fees (high-margin, recurring, requires ranking proof)

| Tier | Price | What they get |
|---|---|---|
| Independent gym featured listing | £99–£499/year | Premium card position in town hub, claim profile, edit equipment / hours / classes |
| Boutique studio listing | £49–£199/month | Specialism page premium placement, photo gallery, direct booking link |
| PT directory listing (Phase 2) | £15–£40/month | Profile page, lead form |

Pitched to local businesses Week 4+ once we have ranking data to show.

### 9.3 Lead resale (for boutique studios + Phase 2 PT)

Gym membership leads tend to convert better via affiliate than lead resale. Boutique studios and PTs without strong affiliate programmes are the lead-resale target — £10–25 per converted booking lead.

### 9.4 Display ads (volume play)

Mediavine or Raptive eligibility starts at 50k monthly sessions (Mediavine) or lower (Raptive). RPM in fitness category is high (£15–30 in 2026). Ads go below the fold only. Never above the at-a-glance card.

### 9.5 Cross-sell into the existing fleet (Phase 2)

Once ranking is established, gym operators (audiences for `/for-gyms/` page) become pitchable for:
- **Card terminals + EPOS** (membership desk + retail counter)
- **Asset finance** for equipment (every cardio machine £2–10k)
- **Business loans** for fit-out / expansion
- **Invoice finance** for B2B corporate-package contracts

Mapped in `docs/fleet-finance-plays.md` §5.

---

## 10. Tech stack

| Layer | Choice | Why |
|---|---|---|
| Static site generator | **Astro** | Programmatic at scale, near-zero JS, perfect for content + structured data |
| Hosting | **Cloudflare Pages** | Free, fast global edge, generous build minutes |
| Domain registrar | Namecheap / Cloudflare | £10/yr |
| Form capture | **Tally** (free tier) | Webhook to Sheet + email, two forms (gym enquiry + class enquiry) |
| Lead routing | **Zapier** / **Make** | Webhook fan-out to SMS / email |
| Database (Phase 2) | **Cloudflare D1** | SQLite at the edge for user-submitted reviews |
| Maps | OpenStreetMap (Leaflet) | No API key, no per-load cost |
| Popular Times scraping | Cron job + headless browser | Quarterly refresh |
| Analytics | **Plausible** | GDPR-friendly default |
| CMS for honest-review overrides | Markdown files + YAML frontmatter | Version-controlled, no CMS needed |

Repo structure: see `gym-colchester-pilot-v0.md` §7.

---

## 11. Build sequence (post-pilot)

### Month 1 — Colchester pilot (35 URLs, locked in pilot doc)

### Month 2 — First expansion (5 more towns)
Towns to add: **Chelmsford, Ipswich, Cambridge, Romford, Southend** (Eastern England cluster — same data scrape pattern as Colchester, builds regional authority)
Total URLs after Month 2: ~210

### Month 3 — Wave 2 (10 more towns, regional authority broadens)
Add: Norwich, Peterborough, Luton, Watford, St Albans, Reading, Slough, Oxford, Milton Keynes, Northampton
Total URLs after Month 3: ~570

### Month 4 — Wave 3 (London + South-East core)
Add: 30 London postcodes / boroughs as quasi-towns, plus Brighton, Crawley, Maidstone, Tunbridge Wells, Guildford (already pilot), Camberley (already pilot), Aldershot (already pilot — sister of FindATradey)
Total URLs after Month 4: ~1,500

### Month 5 — Wave 4 (Midlands + North)
Birmingham, Manchester, Leeds, Sheffield, Liverpool, Newcastle, Nottingham, Leicester, Coventry, Stoke, Derby, Wolverhampton, Bradford, Hull, York, Lancaster
Total URLs after Month 5: ~3,500

### Month 6+ — Wave 5 (Scotland + Wales + remaining)
Edinburgh, Glasgow, Aberdeen, Dundee, Cardiff, Swansea, Newport, plus remaining UK towns
Total URLs after Month 9: ~10,000+

### Month 12+ — Full scale
~250 towns × full modifier matrix = ~16,000+ URLs.

---

## 12. Refresh cadence (the moat in motion)

| Layer | Refresh | Trigger |
|---|---|---|
| Brand pricing | Quarterly | Cron pulling brand websites |
| Brand new locations | Monthly | Cron + Companies House SIC 93.13 |
| Popular Times | Quarterly | Cron + headless scrape |
| Trustpilot / Google review counts | Monthly | Cron |
| Equipment audits | Annual | Manual revisit |
| Demographic profiles | Annual | Manual revisit |
| Class rosters | Quarterly | Brand sites + manual |
| Atmosphere / "Underrated for" | When changed | User submissions + manual |
| Page rebuild | Triggered by data change | Cloudflare Pages cron |

---

## 13. Success criteria (full master plan, Year 1)

| Metric | Month 6 | Month 12 |
|---|---|---|
| Total URLs live | ~3,500 | ~16,000 |
| Pages indexed | ≥ 95% | ≥ 95% |
| Pages ranked top 10 | ≥ 25% | ≥ 35% |
| Monthly affiliate revenue | ≥ £2k | ≥ £15k |
| Monthly listing-fee revenue | ≥ £1k | ≥ £8k |
| Monthly lead-resale revenue | ≥ £500 | ≥ £4k |
| Monthly display-ad revenue (post-50k sessions) | ≥ £500 | ≥ £6k |
| Monthly sessions | ≥ 50k | ≥ 250k |
| Total monthly revenue target | ≥ £4k | ≥ £33k |

---

## 14. Risks + mitigations

| Risk | Mitigation |
|---|---|
| Brand-owned location pages outrank our brand reviews | We win on modifier intent ("PureGym Manchester quiet hours" not "PureGym Manchester"); brand SERP is conceded |
| Map pack dominance for "best gym near me" | We rank on long-tail modifier queries that map pack doesn't fight for ("least intimidating gym Colchester") |
| Manual visits don't scale economically | Visits only for top 6 gyms per town; rest filled from public data + reviews mining; user submissions compound the dataset over time |
| Affiliate networks pull approval if reviews are too critical | Diversify affiliate stack (16 partners); local listings + display ads grow as fallback; lose-one-affiliate is survivable |
| Helpful Content update treats programmatic as spam | Each gym page is 70%+ unique data (demographic profile + equipment audit + visit observations); ratio of structured data to template is high |
| Google Maps Popular Times scraping breaks | Manual observation overlays remain; user submissions become primary signal over time |
| Independent gyms refuse paid listings | Affiliate + display + lead resale carry revenue; listings are a bonus tier, not the foundation |

---

## 15. The strategic insight

`findagym.co.uk` is a £30k–£500k/year revenue site at full scale. The Under-Served Review Engine that powers it is the asset. Once built, the engine renders:
- gym hub at full UK scale
- equipment-finance comparison hub (cross-sell into Asset Finance fleet)
- supplements / wearables / apparel content arms
- could power adjacent fitness directories (yoga studios, dance studios, climbing walls) with light template variation

Don't build `findagym.co.uk` thinking it's the goal. Build it thinking it's the demonstration that the moat works in fitness — then ask which other dormant UK service-review category gets the same treatment.

---

## 16. Cross-references

- `docs/site-builds/gym-colchester-pilot-v0.md` — locked pilot v0.1 (35 URLs, Colchester only)
- `docs/niche-shortlist-2026-04.md` #75 — UK Gym & Fitness Hub master entry
- `docs/location-plays.md` §2.2 — full modifier matrix and full UK ambition (this doc supersedes that summary)
- `docs/fleet-finance-plays.md` §3 — Card Terminals + Asset Finance cross-sell into gym operator audience
- `docs/site-builds/findatradey.md` — sister hyperlocal project, shares the Geo Engine chassis
