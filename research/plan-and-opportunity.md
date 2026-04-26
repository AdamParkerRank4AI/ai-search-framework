# Plan and Opportunity: Indoor Maps + AI Search + Footfall Grounding

**Project lead:** Liam
**Sponsor framework:** Rank4AI
**Status:** Research / pre-build
**Document date:** 2026-04-26
**Companion doc:** `research/maps-ai-search-qr.md` (the working notes this summary is drawn from)

---

## 1. The concept in one paragraph

A scan-to-open indoor map for large venues (shopping centres like Lakeside first, then airports, hospitals, universities, museums, stadiums). Visitor scans a QR code on entry; the map opens in their browser, no app install, showing where they are and where everything inside the venue is. Each pin links to a structured Rank4AI entity record so the venue and its tenants become more discoverable to AI platforms (ChatGPT, Gemini, Claude, Perplexity, Copilot). The map's quiet second job is to capture **consent-based, location-only footfall data**, aggregate it across many venues, attach it to entities in the Rank4AI graph, and license the resulting feed to AI platforms as a real-world grounding signal — the offline truth that today's web-only signals can't provide.

The map is the entry point. The data is the product.

---

## 2. The questions we worked through

Captured in order so the thinking is reproducible:

1. **What is the project?** — An indoor map that opens when you enter a building and shows you where things are. Reference experience: Lakeside shopping centre.
2. **Tech stack?** — OpenStreetMap and Mapbox as candidate map layers. Schematics (floor plans) as the underlying data source. QR codes as the scan-to-open trigger and pin-annotation entry point.
3. **Can we add it to Google Maps?** — Yes via the Google Indoor Maps programme, but submissions have tightened. Apply for the flagship venue, but dual-publish so we keep control of the rich experience.
4. **How do venues sign up?** — Pub-WiFi-style frictionless onboarding. Venue manager submits floor plan, system auto-generates the venue page, base map and a starter pack of printable QR codes. Tenants then claim their own pins.
5. **Can we put advertising on it?** — Yes. Sponsored pins, route-end suggestions, category takeovers, dwell-triggered offers, seasonal banners. Premium inventory because the user is already in the venue.
6. **Can location auto-enable on sign-up?** — No, browsers block programmatic geolocation. Best we can do is prompt at the right moment with a clear reason. PWA install helps persistence. QR anchors "you are here" without needing GPS.
7. **What if there's no WiFi or 4G?** — Cached tiles, service worker, offline-first PWA. QR can encode minimal "you are here" state. Optional BLE beacons for venues with persistent dead zones.
8. **Footfall data — can my phone see other phones in the venue?** — Not reliably. iOS blocks the API, Android is tightening, MAC randomisation makes counting unreliable, GDPR/PECR exposure is real. The legitimate route is venue-side WiFi analytics or app-side opted-in presence — not scanning other people's phones.
9. **Footfall as a signal of truth for AI search — can we sell to OpenAI?** — Yes, this is the real opportunity. AI platforms ground on online signals only today; footfall is offline truth that's hard to fake.
10. **Family of four — only one would be tracked via card data?** — Correct, and this is a structural advantage of per-device map presence. Four phones = four hits, captures browsers and non-payers, sees the whole route not just the till.
11. **What do competitors offer that we don't?** — On the entry-point side: blue-dot positioning, multi-floor routing, native SDKs, enterprise sales relationships, compliance certifications, 3D/AR overlays — we are years behind on pure mapping. On the AI-search side: nobody is selling footfall as AI grounding data. That is the empty white space.
12. **Is the play to migrate footfall from many places into the AI search world, since AI today only sees online traffic?** — Yes. That is the play, stated plainly.
13. **Scope decision: location only?** — Confirmed. No CCTV, no loyalty, no card transactions, no ad IDs, no probe scanning. Pure consent-based location capture is the cleanest sellable story.

---

## 3. The plan

Two products, stacked. The first earns the right to build the second.

### Product A: the indoor map (the entry point)

**What it is:** a scan-to-open, no-app-install, browser-rendered indoor map for a venue. Floor plan, search, pin notes, basic routing, "you are here" anchored by QR.

**Stack (candidate):**
- Map render: Mapbox GL JS for polish and tooling, or Leaflet + OSM for cost. Probably Mapbox for the pilot, OSM as the data substrate.
- Floor plans: GeoJSON per floor, hand-traced from venue CAD/PDF for pilot, automated ingestion later.
- QR codes: deep links of the form `/v/{venueId}?pin={pinId}`. Generated and printed by the platform, deployed by the venue.
- App: Progressive Web App (PWA), offline-capable via service worker.
- Backend: multi-tenant from line one (one venue today, hundreds tomorrow).

**v1 scope:**
- One pilot venue.
- Static floor plan, no real-time positioning.
- ~10 anchor QR points.
- Web-only, no native install.
- Each pin links to a tenant note + a Rank4AI entity record.
- Inclusive design baked in: family mode, sensory-friendly mode, step-free routing, large-text mode.

**v2+ adds:**
- Multi-floor routing through lifts/escalators.
- Optional BLE beacon network for blue-dot positioning where venues want it.
- Tenant self-claim (Google Business Profile-style) for editing pins.
- Sponsored pin inventory.
- Crowd-aware routing once footfall data is flowing.

### Product B: the AI grounding feed (the actual product)

**What it is:** a daily/weekly feed of aggregated, anonymised, k-anonymous **location-only** presence data per venue and per tenant entity, mapped to stable entity IDs that join to Wikidata, Companies House and Google Knowledge Graph. Sold to AI platforms (OpenAI first, then Anthropic, Google, Perplexity, others) as a grounding signal for place- and recommendation-based answers.

**Data sources (location only, by design):**
- Map presence (visitor opens the map → consent + position).
- BLE beacons where deployed.
- Venue WiFi analytics via Cisco Meraki / Aruba / Purple APIs.
- Carrier cellular data (Telefonica Tech, Vodafone Analytics, EE/BT) for venue-level arrivals.

**Explicitly out of scope:** CCTV, loyalty, card transactions, mobile ad IDs, WiFi probe scanning of unassociated devices. The location-only constraint is also the marketing — a clean, defensible, consent-based dataset is what AI platforms can actually buy.

**Entity matching:**
- Per-unit polygon from the indoor map.
- Stable entity ID per polygon, linked to local store, brand parent, global brand, Rank4AI entity record.
- External cross-references to Wikidata / Companies House / Google KG so buyers can pivot through their own IDs.

**Output records (what we actually sell):** entity-keyed records with aggregated visit count, dwell distribution, returning-visitor rate, peak-hour profile, neighbour-entity co-visit pattern, change-vs-previous-period, freshness timestamp, k-anonymity attestation.

### Stage gates

| Stage | Trigger | What we build / sell |
|-------|---------|----------------------|
| 0 | Now | Research, pilot venue conversation, prototype map. |
| 1 | Pilot venue signed | Map live in one venue. SaaS revenue from venue. Data capture starts. |
| 2 | 3–5 venues live | Tenant self-claim live. Sponsored pins. Free analytics dashboard for tenants (location-only). |
| 3 | 20–50 venues live | Brand-level deals (H&M, Boots, Greggs head-office contracts). Coverage threshold for first AI-platform conversations. |
| 4 | 100+ venues, multi-vertical coverage | Live data feed + API for AI platforms. First OpenAI / Anthropic / Perplexity contract. |
| 5 | Established AI-platform revenue | Consortium model with retailers. International expansion. Possibly own positioning hardware. |

---

## 4. The opportunity

### The thesis

AI platforms today ground their answers about places, businesses and entities almost entirely on **online signals** — web pages, reviews, structured data, citations, social media. Every one of these signals is manipulable, and the AI platforms know it. Hallucinated or manipulated answers are their single biggest credibility risk.

**Real-world behaviour** — people physically going to a place, dwelling, returning — is the truth signal that no online manipulation can fake. Footfall is offline, observed, costly to forge.

The play, in one sentence: **aggregate consent-based location/footfall data from many indoor venues, attach it to Rank4AI entity records, and license the resulting feed to AI platforms as a grounding signal — so that "what places to recommend" decisions stop being purely online-traffic-based and start incorporating offline reality.**

### Who pays, in order of strategic importance

1. **AI platforms (OpenAI, Anthropic, Google, Perplexity, Microsoft, Mistral, Meta).** Strategic customer. Bulk feed and/or API-grounding licence. The whole long-term P&L hinges here.
2. **Venue landlords (Lakeside, Westfield, Bluewater, airports, hospitals, universities).** Operational customer and data-collection partner. Pay for the indoor map as SaaS.
3. **Retailer brands (H&M, Boots, Greggs, JD Sports, etc.).** Pay for analytics dashboards on their own stores plus AI search visibility services.
4. **Tenants inside venues.** Pay for sponsored pin placements, claim-and-enrich upgrades, dwell-triggered ad inventory.
5. **Adjacent dataset buyers (planners, councils, researchers).** Aggregated dataset has secondary value — but not the focus, and we won't let it muddy the AI-grounding pitch.

### Probable revenue mix (3 years out)

- ~60–70% AI-platform data licensing.
- ~20–30% venue and brand SaaS.
- ~10% advertising.

Day one is the inverse — close to 100% from venue SaaS, because the AI deal needs coverage to exist before it can be sold. Build for venues, architect for AI platforms.

### Deal-shape precedents

OpenAI's known data-partner deals in 2024–2025 (AP, Le Monde, Reddit, FT, News Corp, Axel Springer, Time, Vox, Condé Nast, Stack Overflow) sit roughly in the $1M–$60M/year range depending on scale and exclusivity. We are not a publisher, but the pattern is the same: novel data that improves grounding and reduces hallucination, sold under multi-year contracts. The product is closer to Reddit's deal in shape (a feed, refreshed continuously) than AP's (an archive with rights).

Realistic early target: a £500k–£5M/year bulk-feed licence per major AI platform once coverage is meaningful. Non-exclusive by default. Higher numbers come later as coverage and demonstrated grounding lift increase.

### Why now

- AI platforms are actively looking for harder-to-fake grounding sources.
- EU AI Act provisions on documented data sourcing push AI platforms toward consent-based, attributable feeds.
- Indoor mapping is mature enough that "good enough" maps can be shipped quickly.
- Mobile-SDK footfall (the Placer/SafeGraph/Outlogic generation) is being squeezed by ATT and Privacy Sandbox — the incumbents are weakened, not strengthened.
- The Rank4AI brand and methodology already exist; this project plugs into a five-signal model that's already designed for AI-search assessment.

### Why us

- We sit at the intersection of AI search expertise (Rank4AI methodology) and a clean new collection mechanism (the map with explicit consent).
- We can pitch venues credibly (we're not selling them an enterprise indoor-map megaproject — we're giving them a free amenity that also makes their tenants more visible in ChatGPT).
- We can pitch AI platforms credibly later (we have a documented, consent-based dataset designed from day one for grounding use, not retro-fitted from ad-tech).
- The inclusive-design angle (autism-friendly routing, family mode, sensory map) is a marketing differentiator that no competitor leads with.

---

## 5. The honest read: what's new vs what isn't

**Not new:**
- Indoor mapping. Mapwize, Pointr, MazeMap, Situm, Inpixon, Esri ArcGIS Indoors and Apple's Indoor Maps Program have years of head start.
- Footfall analytics as a category. Placer, SafeGraph, Springboard, Huq, Cuebiq, Outlogic.
- Sensory-friendly venue hours. Many shopping centres already run them; they're just not surfaced well.

**Genuinely new:**
- Connecting venue and tenant entities into an AI-search optimisation framework (Rank4AI). No competitor does this.
- Scan-to-web access without an app install. Most incumbents ship SDKs that get embedded in venue native apps.
- Footfall packaged as **AI grounding data sold to LLM platforms**, not as marketing analytics sold to retailers. Empty white space.
- Inclusive design as a first-class product line (autism, ADHD, sensory, family) rather than a step-free routing checkbox.
- Privacy-first construction with no legacy MAC-tracking baggage.
- Bundled with the Rank4AI methodology — selling AI visibility, not a map.

**Implication:** don't fight Pointr/Mapwize on "best indoor map." That fight is lost on day one. Compete on the slice they don't cover.

---

## 6. Risks and dependencies

In rough priority order.

- **Demand from AI platforms is unproven.** Need direct conversations with OpenAI/Anthropic/Google/Perplexity grounding teams to validate that this is a real category they'd pay for. Cheap to investigate, expensive to be wrong about.
- **Coverage threshold.** Below ~100 venues the AI-grounding product is research, not a product. Long road from venue 1 to venue 100.
- **Privacy and regulatory.** GDPR, PECR, ePrivacy, EU AI Act. Build privacy-first or it's both illegal and brand-damaging.
- **Indoor positioning is hard.** QR-anchored "you are here" is fine for v1; real blue-dot is years of work or a partner deal.
- **Floor plan data quality and maintenance.** This is what kills most indoor-mapping deployments. Need a clear ownership model per venue.
- **Competitor reaction.** Once this is visibly working, Mapwize/Pointr could pivot into AI-grounding. Our defence is the Rank4AI bundle and speed.
- **AI platforms could build it themselves.** Google certainly could. Apple already has the indoor data. Mitigation: be small, fast, neutral, multi-platform.
- **Retailer trust.** One leak, one news story about a retailer's footfall being exposed to a competitor, and the project loses its data-collection partners. Privacy-by-construction matters here too.
- **Liability and safety.** Wayfinding errors in normal use are embarrassing; in emergencies they're dangerous. Clear T&Cs and insurance from day one.

---

## 7. Next steps

In rough order, none committed.

1. **Validate AI-platform demand.** Three to five conversations with data-partnership contacts at OpenAI, Anthropic, Google AI, Perplexity. Goal: signal whether "consent-based location grounding feed" is a category they'd buy at scale.
2. **Pilot venue conversation.** Identify and approach one flagship venue (Lakeside is the working example, but a slightly smaller venue might move faster). Goal: a no-cost pilot in exchange for a future revenue share.
3. **Map prototype.** Single floor of the pilot venue, GeoJSON, Mapbox GL JS render, ten QR codes, working pin notes. Three to four weeks of build to get something demoable.
4. **Privacy framework.** Public-facing privacy paper, k-anonymity threshold definition, consent flow design. Needs to exist before any data flows.
5. **Entity schema.** Define how a "map entity" maps to a Rank4AI entity record and to Wikidata / Companies House / Google KG. The schema is the data product.
6. **Inclusive-design working group.** Bring in disabled and neurodivergent users (or partner with the National Autistic Society / Mencap / Scope) to inform v1 design rather than retrofit.
7. **Competitor teardown.** Two or three of Pointr / Mapwize / MazeMap properly understood — pricing, sales motion, weaknesses — before committing to a build path.

---

## TL;DR

We're building an indoor map that opens via QR scan when a visitor enters a venue. It's useful in its own right and we'll sell it to venues as a SaaS amenity. The bigger play is that the same map quietly captures consent-based, location-only footfall data, ties it to entity records in the Rank4AI graph, and feeds it to AI platforms as a grounding signal. Today AI platforms answer "where should I go" with online-only signals that are easy to manipulate. We're selling them the offline truth. The map is the wedge. The data is the product. OpenAI is the customer that matters.
