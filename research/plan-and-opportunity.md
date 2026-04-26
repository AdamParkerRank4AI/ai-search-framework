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

## 8. The AI search side specifically: who else is there, and can we compete?

The earlier competitor section covered indoor mapping (Pointr, Mapwize, MazeMap, etc.). That's only half the picture. There's a second, faster-moving competitor set on the AI-search side that needs its own honest read.

### Who else is in AI search

**Monitoring / GEO (Generative Engine Optimisation) tools.** A wave of well-funded startups launched in 2024–2025 to track how brands appear in AI answers:

- **Profound** — raised significant funding in 2024, monitors brand mentions across ChatGPT, Perplexity, Gemini, Claude. Reports inclusion rate, sentiment, citation sources.
- **AthenaHQ** — GEO platform with agency tooling.
- **Otterly.AI** — AI search visibility tracking, smaller, European.
- **Peec AI** — generative engine optimisation suite.
- **Goodie AI, Daydream, Scrunch AI, Evertune** — newer entrants, similar shape.
- **Brandlight, Brandwatch** — broader social/brand monitoring expanding into AI.

**Structured-data and schema tools.**
- **Schema App, Yoast, RankMath** — implementation help for the schema layer of AI optimisation.
- **WordLift** — knowledge-graph tooling for content sites.

**Established SEO platforms moving in.**
- **SEMrush, Ahrefs, Moz, BrightEdge, Conductor, HubSpot** — all adding AI search visibility modules to existing platforms with millions of users.

**The AI platforms themselves.**
- OpenAI is rumoured to be building merchant tools, Perplexity has merchant programs, Google has its full Search Console + Merchant Center stack already aimed at AI Overviews.

### What makes Rank4AI different

Honest read, point by point:

- **Methodology, not just monitoring.** Most competitors are dashboards — they tell you *what's happening* in AI answers. Rank4AI is a defined Five Signal Model and an audit — it tells you *what to do about it*. Closer to a McKinsey-style framework than a SaaS dashboard.
- **Audit produces a score, not just a feed of mentions.** AI Visibility Score (weighted) and Structural Reference Score (unweighted) are concrete deliverables. Most monitoring tools can't tell you whether you're "doing well" — only how often you appear.
- **Five-signal coverage.** Identity Clarity, Subject Authority, Meaning Architecture, Ecosystem Validation, Signal Consistency — most competitors only cover one or two layers (usually mentions and structured data).
- **Bundled with a methodology a human can defend.** Founder-led, methodology-led, framework-published. Easier to sell to a CMO who needs to justify the spend than a dashboard subscription is.

### What makes the map + footfall genuinely uncatchable

This is the part that the AI-search monitoring tools structurally cannot do:

- They can monitor what AI platforms say. They cannot give the AI platforms new data to say better things with.
- They have no offline footprint, no physical-world data, no consent-based collection mechanism.
- Adding it later would require them to build a consumer product, sign venue deals, and stand up a privacy-first data pipeline — a multi-year detour from their core business.
- Meanwhile, we'd already be the documented source of "real-world grounding for AI search." First-mover position in a category that doesn't exist yet.

### Can we actually compete?

Three honest answers depending on which slice we're talking about.

- **Pure AI-search monitoring (the Profound / Otterly / AthenaHQ slice).** Probably not, head-on. Profound alone has more funding than Rank4AI is likely to raise this year, and the SEO incumbents (SEMrush, Ahrefs) have distribution we can't match. Don't try to out-monitor the monitors.
- **Methodology + audit (the McKinsey-of-AI-search slice).** Yes. This is Rank4AI's existing edge. Smaller market by user count but much higher per-customer revenue, and the framework is already published.
- **Real-world grounding signal for AI platforms (the new slice).** Yes, and probably uncontested for at least 18–24 months. Nobody in the AI-search competitor set is positioned to build this; nobody in the indoor-mapping competitor set has the AI-search expertise to package it. We sit in the only chair where both halves are possible.

The summary: don't compete with Profound on dashboards. Compete with no-one on the part nobody else can do — the offline grounding feed.

---

## 9. The "skip the map, just do the data" alternative

Worth thinking through properly because it's a legitimate strategic question.

### What the alternative would look like

Drop the consumer-facing indoor map entirely. Run a pure data business: aggregate location/footfall data from many places, attach it to Rank4AI entity records, sell the feed to OpenAI and other AI platforms. Closer in shape to Placer.ai, SafeGraph or Huq — but pivoted toward AI grounding instead of retail analytics.

### Where the data would come from without the map

This is the entire question. Options:

1. **Buy SDK location data from existing aggregators.** Outlogic, Cuebiq, Gravy Analytics, Veraset. Margin-thin, no moat, fully dependent on suppliers who themselves sit on shrinking data sources thanks to ATT and Privacy Sandbox.
2. **License from mobile carriers.** Telefonica Tech, Vodafone Analytics, EE/BT. Rich and reliable but expensive, slow to procure, and most of these vendors have their own competing data products.
3. **Resell from Placer or SafeGraph.** They sell wholesale; we'd repackage with entity linkage and AI-grounding framing. Hard to defend the margin once they notice the use case and pivot themselves.
4. **Build our own data-collection SDK and embed it in third-party apps.** This is exactly what Outlogic / X-Mode did. The same regulatory and platform headwinds that hammered them would hit us — and we'd be a year late to a shrinking pool.
5. **Buy carrier-derived datasets from intermediaries.** Smaller versions of #2.

None of these give us a defensible position. We become a data broker with a thin reseller margin and no unique signal.

### What we lose by dropping the map

- **Consent.** The map gives us an explicit, visitor-initiated permission moment. Without it, every other data source has murkier consent provenance — exactly the thing AI platforms want clean for grounding.
- **Differentiation.** Without the map, our raw data is the same as Placer's. With the map, we have something nobody else has — first-party scan-anchored presence data tied to a specific entity.
- **Entity linkage.** The map gives us per-polygon entity IDs that map to specific stores in specific venues. Bought-in SDK data is much fuzzier — "device near 51.5074, 0.1278" vs. "device inside the H&M unit at Lakeside floor 1 between 14:32 and 14:51."
- **A second revenue line.** Venue SaaS pays bills while the AI deal is being built. Without it we're spending years burning cash to reach data scale.
- **A consumer-facing reason to exist.** Pure data brokers have no public face, no story, no PR upside. The map gives the project a story.
- **Privacy moat.** Buying second-hand SDK data inherits its consent baggage. Originating data through a clean consent flow is a defensible posture; reselling someone else's pings is not.

### What we gain by dropping the map

- **Faster to data volume.** Buying / licensing existing data could give us national coverage in months, not years.
- **No consumer product to build, support, document, debug.**
- **No venue sales motion.** Selling to landlords is hard; selling to data buyers is a smaller, more concentrated market.
- **Smaller team needed early.**
- **Could start AI-platform conversations earlier** because we'd have data scale on day one.

### Honest verdict

The map is not the product, but it's also not optional. Without it we're a data broker reseller in a margin-compressed market with no moat against the existing incumbents. With it we have:
- Differentiated, first-party data nobody else can replicate without building their own consumer wedge.
- A clean consent story that AI platforms specifically need.
- Entity linkage that turns raw pings into structured grounding records.
- A revenue line that funds the long road to AI-platform deals.

### A sensible hybrid

Worth considering: do both, in sequence.

- **Phase 0 (now):** start a small bought-in / licensed footfall pilot — a few hundred POIs, carrier data or wholesale SDK data — purely to demo the concept to AI platforms. Cheap research, no commitment.
- **Phase 1 (months 1–12):** run the AI-platform conversations *and* the map pilot in parallel. The bought-in data tests whether AI platforms even want this category; the map builds the differentiated long-term asset.
- **Phase 2 (year 2+):** as map coverage grows, gradually replace bought-in data with our own first-party feed. Margin and quality both improve. Bought-in data becomes the supplement, not the foundation.

This way we don't bet everything on the map taking off before we know AI platforms care. We also don't bet everything on a commodity data-broker model that has no defensible position. The map is the long-term moat; the early bought-in pilot is what gets us in the OpenAI room within months instead of years.

**Recommendation:** keep the map as the strategic spine. Add a small bought-in data pilot to accelerate the AI-platform conversation. Do not pivot to pure data-broker — that's a worse business than the one we're already designing.

---

## 10. The footfall data landscape: who handles it today and can we see it?

Direct answer first: **no, there is no single place to see all footfall traffic.** The market is fragmented across tens of companies, each holding their own slice with their own methodology, coverage and customer base. There is no master "show me every phone in this geofence right now" service. There are vendors who can give you a *modelled estimate* of how many people were in a defined area over a defined time window, but each estimate is built from a sample and extrapolated.

This fragmentation matters because it is the gap our wedge is built on.

### Who actually holds location/footfall data

Grouped by where the data originates.

**Mobile OS providers (the giants).**
- **Apple.** Holds iPhone location via Find My, Maps and system services. Does not sell raw or aggregated data. Internal use only.
- **Google.** Holds Android + Google Maps + Search location. Uses it internally (Maps "popular times", Traffic). Sells limited aggregated mobility insights via Google Maps Platform; does not sell raw pings.
- **Microsoft, Meta, Amazon.** Hold smaller slices via their apps. Don't sell raw.

These three sit on the largest datasets by far but are not buyable. They are competitors-in-waiting more than suppliers.

**Mobile carriers (UK).**
- **EE / BT.** Mobility insights products via BT for retail and planning.
- **Vodafone.** Vodafone Analytics — anonymised cellular-derived flow data, sold for retail, transport, planning.
- **O2 / Virgin Media O2.** O2 Motion — same shape, was a Telefonica Tech product.
- **Three UK.** Smaller mobility insights offering.

Carriers see *every phone connected to their network* aggregated to cell-tower level (~100m–1km accuracy outdoors, worse indoors). Coverage is huge but spatial precision is low. Buyable but expensive and slow to procure.

**Mobile SDK location aggregators (the controversial layer).**
This is the sector that grew up by paying to embed location-collecting SDKs inside random apps (weather, flashlight, games) and selling the aggregated pings.

- **SafeGraph** (US-focused, large POI dataset).
- **Veraset** (US, supplies many of the analytics players).
- **Foursquare** (Pilgrim SDK + huge POI graph; also licenses).
- **Cuebiq** (Italy/US).
- **Outlogic** (formerly X-Mode — banned by US FTC in 2024 from selling sensitive location data).
- **Gravy Analytics** (US — suffered a major data breach in January 2025 that exposed the underlying brittleness of the whole sector).
- **Tamoco, Predicio, Adsquare, Near Intelligence, Kochava, Onfido.**

This whole layer is structurally weakened. ATT (Apple's App Tracking Transparency) cratered iOS data volumes in 2021. Google's Privacy Sandbox is doing the same to Android. The FTC action against X-Mode/Outlogic and the Gravy breach have made buyers nervous and regulators active. Coverage is shrinking, prices are wobbling. **We do not want to inherit this baggage.**

**Footfall analytics products (built on the layers above).**
- **Placer.ai** — US-focused, retail and real-estate analytics, builds on SDK data plus its own panel. The category leader by visibility.
- **Huq Industries** — UK and European, council/planner-focused.
- **Springboard** — UK retail footfall, mostly venue-camera based.
- **Sensormatic Solutions / ShopperTrak, V-Count, RetailNext, Brickstream, Hoxton Analytics** — camera-based venue counters.
- **Geoblink, PiinPoint, Mytraffic** — regional location-intel platforms.

These are the buyable products — what someone like a retail planner or a landlord pays for today. Most of them sell to humans for business decisions. **None of them are packaged as AI grounding data.**

**Venue WiFi analytics.**
- **Cisco Meraki, Aruba (HPE), Ruckus, Extreme Networks** — venue-side WiFi access points that already produce analytics.
- **Purple WiFi, Cloud4Wi, Tanaza** — guest-WiFi platforms with analytics.

This data sits inside each venue and is owned by the venue / their network operator. Buyable but only one venue at a time.

**Camera / CV vendors.** Already listed under footfall analytics. Out of scope for our project.

**Connected car / vehicle data.** Otonomo (merged), Wejo (troubled), Geotab. Useful for venue-arrival signal, not in-venue movement.

**Card / open-banking transactions.** Out of scope per the location-only decision but listed for completeness: Mastercard SpendingPulse, Visa, Fable Data, Consumer Edge, Earnest, Facteus.

**Data marketplaces (where the above gets resold).**
- **Snowflake Data Marketplace, AWS Data Exchange, Databricks Marketplace, Datarade, Dawex.** Browseable catalogues of datasets including footfall feeds. Convenient for procurement; doesn't change who originally collected the data.

### Is it one place or hundreds?

Hundreds, by count. **No single source sees the whole market**, and the market itself is split between:

- A few giant non-sellers (Apple, Google).
- A handful of carriers per country (sells nationally).
- Tens of SDK aggregators (declining, exposed).
- A few dozen camera/WiFi/POS vendors operating venue-by-venue.
- Tens of analytics-product re-packagers.

The closest things to "one view of UK footfall" are:
- A single major UK carrier dataset (Vodafone or O2) — broad but coarse, single country.
- Placer.ai or Foursquare for retail POIs — broad but sample-based, not a complete count.
- Google's internal data — best in class, not for sale.

There is no consolidated "see all phones in this area" service. There is no national footfall registry. Anyone telling you they have one is either a carrier (single network only), an SDK aggregator (sample, weakened) or a POI analytics player (sample plus modelling).

### Could we, for a given geo area, see how many phones were there?

Yes — but with material caveats. Concretely, today, for a defined geofence and a defined time window, you can:

- **Buy a Placer.ai tile.** Get a modelled visit count, dwell distribution, day-part split, demographic estimate, true visit vs. drive-by separation. Subscriptions start in the low thousands per month for serious use; per-tile / per-report buying is also available.
- **Buy a carrier extract.** Vodafone Analytics or O2 Motion for the area, get cell-tower-derived counts. Coarser spatial precision but full network coverage.
- **Subscribe to Foursquare's Places / Movement APIs.** Per-call pricing. POI-anchored.
- **Buy an SDK extract from Veraset / SafeGraph / Outlogic.** Raw or aggregated, declining quality, regulatory risk.
- **Look at Google "Popular Times".** Free, public, no API, only for known POIs.
- **Tap into venue WiFi analytics if the venue is a customer of Meraki / Aruba / Purple.** Only that venue.

What none of these will give you is the actual ground truth. Every count is:
- A sample of the people who happened to be using whatever data source the vendor draws on (an SDK app, a network, a particular phone OS).
- Extrapolated to a population estimate using a vendor-specific model.
- Often unreliable below a coverage threshold (rural areas, indoor spaces, niche venues).

For a flagship test: if we wanted to know how many people were in a specific Lakeside store at 2pm last Saturday, the most accurate answer today comes from Lakeside's own venue-side WiFi or camera data, not from any of the third-party sellers. That's part of why our project's first-party map data is differentiated — once it exists at scale, it's higher quality than the bought-in alternatives because it's actually inside the venue with consent.

### What this means for our plan

- **The supply chain is fragmented and weakened.** No incumbent is in a position to dominate. Good news for a new entrant.
- **Bought-in data is good enough for early demos.** A Placer or Huq tile lets us show OpenAI what an AI-grounding feed could look like, months before our own map network reaches scale. This is the hybrid pilot from Section 9.
- **Bought-in data is not good enough as a foundation.** Sample-based, modelled, regulatorily fragile, indistinguishable from what every other reseller could buy. Doesn't justify a margin and doesn't last.
- **Our first-party map data is structurally better** for the specific use case (indoor, entity-anchored, consent-based). Worse coverage early, better quality always.
- **A mixed pipeline wins.** First-party map data where we have it; carrier or analytics-vendor data filling gaps elsewhere; clear documentation of which slice is which when we sell to AI platforms. AI buyers will respect "this is our consented first-party data; this is licensed carrier data; here's the methodology" much more than "trust us, we have a number."
- **Watch for marketplace consolidation.** If Snowflake or AWS Data Exchange becomes the de-facto place AI platforms shop for grounding data, being listed there matters more than direct sales. Worth tracking.

So: hundreds of handlers, no master view, every count is a model. Our edge is producing the cleanest slice — first-party, indoor, entity-linked, consent-based — and being the first to package it as AI grounding rather than retail analytics.

---

## 11. Map APIs as a data source: what's actually exposed?

Reasonable instinct — if Google, Mapbox and Apple all have huge map products, surely there's an API somewhere that lets us pull "who is in this area, by route, by time"?

**Short answer: no, not really.** Map APIs are excellent for *enrichment* (where places are, what they're called, how to get there) and for *vehicle traffic* (cars on roads), but they are deliberately not exposing pedestrian footfall, in-venue presence or "how many people are here right now." The companies that have that data either keep it internal (Apple, Google) or sell it through separate, paid mobility data products that look more like the footfall vendors in Section 10 than like a normal map API.

Going through them properly.

### Google Maps Platform

What you *can* pull via documented APIs:
- **Places API** — search POIs, get name/address/type/opening hours/photos/reviews.
- **Geocoding / Reverse Geocoding** — address ↔ coordinates.
- **Routes / Directions API** — turn-by-turn routes with traffic-aware ETAs.
- **Distance Matrix** — travel times between many origin/destination pairs (driving, walking, cycling, transit).
- **Roads API** — snap-to-road, speed limits.
- **Maps JavaScript API + Traffic Layer** — visual traffic overlay only, no underlying numbers.
- **Geolocation API** — estimate device location from WiFi/cell signals.

What you *cannot* pull:
- Raw or aggregated user pings.
- "How many people are at this POI right now" — Google Maps shows this in its "Popular times" UI but does not expose it via a stable, supported API. Unofficial scrapers exist (the `populartimes` Python library) and Google periodically clamps down on them. Treat this as unsupported and unreliable.
- Historical pedestrian flow.
- In-venue presence.

The traffic-layer data is real but represents *vehicle* movement on roads, derived from Google Maps app users in cars and partner sources. It tells you nothing about footfall to or inside a shop.

### Mapbox

What you can pull:
- **Vector tiles, geocoding, search, directions, isochrones, matrix, snap-to-roads** — same shape as Google.
- **Mapbox Boundaries, Mapbox Streets POI dataset** — POI enrichment.

What about movement data:
- **Mapbox Movement** *was* a paid product giving daily aggregated mobility data tiles from their SDK panel + partners. It has been repositioned over time and is no longer a flagship product. Not currently a reliable foundation.

### Apple Maps / MapKit

- POI search, geocoding, directions, basic embeds, indoor maps for accredited venues.
- **No movement data, no footfall, no traffic API.** Apple does not sell this category.

### OpenStreetMap

- Map data and tiles, fully open, community-edited.
- **No movement, footfall or traffic data** at the OSM project level. There are community projects (e.g. OpenTraffic) but no production API to depend on.

### HERE Technologies

This is where it gets more interesting. HERE is not just a map provider — it sells a real mobility data line.

- **HERE Traffic API** — real-time and historical traffic flow on roads.
- **HERE Probe Data** — anonymised vehicle probe pings (from HERE's automotive partnerships), buyable for transport planning, traffic engineering, real-estate analytics.
- **HERE Mobility / fleet products.**

Caveat: this is **vehicle-derived**, not pedestrian. Useful for "how many cars arrived at the Lakeside car parks today" — useless for "how many people walked past Boots on the upper level."

### TomTom

- **TomTom Traffic API** — same shape as HERE.
- **TomTom Traffic Stats / TomTom Move** — historical traffic patterns from probe data.
- Vehicle-only, same caveat as HERE.

### Foursquare

Worth singling out because Foursquare is half-map, half-mobility-vendor.

- **Places API** — POI data, with the strongest historical footprint of any non-Google POI graph.
- **Movement SDK / Pilgrim SDK / Movement APIs** — paid products that give aggregated visit and dwell data per POI, sourced from their own SDK panel embedded in third-party apps. This is closest to "an API that gives you footfall by location" — but it's the same SDK-aggregator model that's been weakened by ATT.

### Specialist mobility data APIs (not map APIs but adjacent)

For completeness, paid APIs that *do* serve mobility-style queries:

- **INRIX** — traffic and movement intelligence, mostly automotive but with some pedestrian products.
- **StreetLight Data** (now part of Jacobs) — origin-destination analysis from probe data.
- **Wejo** (troubled), **Otonomo / Urgently**, **Geotab** — connected vehicle data.
- **Placer.ai, Foursquare Movement, Huq, Mytraffic** — already covered in Section 10. Some have API access, all charge for it.

### Useful summary table

| Provider | Map API | Pedestrian footfall via API | Vehicle traffic via API | Buyable mobility extracts |
|----------|---------|----------------------------|-------------------------|---------------------------|
| Google Maps Platform | Yes | No (Popular Times not officially exposed) | Visual layer only | No |
| Mapbox | Yes | Limited (Movement repositioned) | No | Limited |
| Apple MapKit | Yes | No | No | No |
| OpenStreetMap | Yes (open) | No | No | No |
| HERE | Yes | No | Yes | Yes (vehicle probe) |
| TomTom | Yes | No | Yes | Yes (vehicle probe) |
| Foursquare | Yes | Yes (paid Movement APIs) | No | Yes |
| INRIX / StreetLight / TomTom Move | No (not maps per se) | Some pedestrian | Yes | Yes |
| Placer / Huq / Mytraffic | No | Yes (paid analytics) | No | Yes |

### What this means for our plan

- **Map APIs are inputs, not footfall sources.** We will use Google Places / Mapbox / OSM for things like POI seeding, geocoding, address validation, basemap tiles, route rendering. None of these will give us footfall.
- **The closest "map API that gives you footfall" is Foursquare Movement.** Same caveats as Placer in Section 10 — sample-based, SDK-derived, regulatorily fragile, paid.
- **Vehicle probe APIs (HERE / TomTom / INRIX) are useful for venue arrival data** — counting cars into Lakeside's car parks, for example — but not for in-venue presence.
- **Google's "Popular Times" is the most tantalising free signal** but is not on a stable API surface. Don't build on it; it's fine for one-off benchmarking only.
- **Confirms the strategic shape.** The reason map APIs don't expose this data is that the companies who *have* it (Apple, Google) deliberately do not sell it, and the companies that try to sell it (Foursquare, the SDK brokers) are running on declining sample quality. There is no off-the-shelf source we can wire up to and resell. The data has to be either licensed from a few credible vendors (carriers, Placer, Huq) or *originated* — which is what the indoor map does.

Restated: map APIs tell you *where* a place is and *how to get to it.* They don't tell you *who's there.* Anyone selling "who's there" is either a footfall vendor (Section 10) or running on the same sample-based stack with the same regulatory exposure. Our wedge — first-party, consent-based, entity-linked indoor data — is the cleanest answer to a question that the existing supply chain genuinely cannot answer well.

---

## 12. Yes, you can build a prototype today — here's how

Section 11 said "off-the-shelf footfall via API doesn't really exist." That's true at the *industrial* level — you can't wire up to one paid API and get clean, complete, real-time footfall. But for a **single-venue demo** that shows the concept layered on a Lakeside map, there's a perfectly realistic build path using free or low-cost data plus a small amount of code.

The goal of the prototype is not perfect data. The goal is a **demoable artefact** — something you can show OpenAI / Anthropic / a venue / an investor and say "this is what an AI grounding feed looks like, layered on a real venue, today." That artefact unlocks every conversation that comes after.

### What the prototype would actually be

A web page that:
1. Renders a map of Lakeside (or any chosen venue).
2. Shows every shop as a polygon with the shop's name.
3. Colours each polygon by how busy it is right now (and at any point in the day).
4. Lets you scrub a time slider to watch busyness move through the centre across the day.
5. Optionally: shows simulated routes (fake or one-person-real) walking through shops, to demonstrate the route data shape.
6. Pin notes per shop pulling Rank4AI entity data (opening hours, category, AI-search summary).

That's the demo. Build time: realistic for a single competent developer in **2–4 weeks**.

### The data sources you can actually use, free or near-free

**For the map and shop polygons:**
- **OpenStreetMap.** Lakeside is already partially mapped on OSM — you can pull the existing data via the Overpass API and render it via Leaflet or Mapbox GL JS. Free.
- **Mapbox free tier.** 50,000 map loads/month free. More than enough for a demo.
- For shops not yet mapped on OSM: trace the floor plan once from a published Lakeside directory PDF into GeoJSON. Hand-trace, a couple of days of work for one venue.

**For real footfall numbers (sample, not perfect):**
- **Google "Popular Times" via the unofficial `populartimes` Python library.** For every named POI inside Lakeside (each shop has its own Google Places ID), this returns the typical-busyness graph Google shows in Maps — by day of week, by hour. Free, brittle, unsupported, but it works for a one-off demo.
- **Google Maps "Live" busyness.** Sometimes available alongside typical busyness — when present, it gives current-vs-typical. Same library can pick this up.
- **Free trials / demos from Placer.ai, Foursquare, Huq.** All three offer demo tiles or limited free POI lookups. Worth requesting for the flagship venue.
- **OpenStreetMap-derived POIs.** OSM has a shop=* tag with names, opening hours and categories — useful for enrichment when Google data is patchy.

**For route and dwell shape (one-person real, then fake the scaling):**
- **Walk Lakeside yourself with the demo on your phone.** Build a tiny PWA with `navigator.geolocation.watchPosition()` that records your trail every few seconds. Walk through 10 shops, sit in the food court, leave. Record. That gives you one real route through the venue.
- **Replay your own track on the map.** Animate the dot moving through the polygons. Then duplicate it 1,000× with random jitter to show what 1,000 routes through the venue would look like. Honest in the demo: "this is one real walk plus simulated peers."

**For the AI search side of the demo:**
- Use the Rank4AI entity record format you already have in the methodology. For each shop, write a short structured entity description (name, category, parent brand, sub-categories, exclusion statements). Render it on the pin click panel.
- Optional: paste those descriptions into ChatGPT alongside a query like "best phone shop in Lakeside" and screenshot the answer with vs. without. That's the basic version of the side-by-side eval that pitches the AI-grounding case.

### A concrete build plan, week by week

**Week 1 — Map skeleton.**
- Pull Lakeside from OpenStreetMap via Overpass.
- Render via Mapbox GL JS in a single HTML page.
- Trace any missing shop polygons by hand from the Lakeside directory.
- Each polygon carries `{shop_id, name, category, brand_parent}`.

**Week 2 — Footfall layer.**
- Run `populartimes` against every shop's Google Places ID.
- Store the resulting busyness curves in a small JSON file (no backend needed for a demo).
- Colour each polygon by the current hour's busyness, with a time slider to scrub the day.
- Add a venue-wide heatmap layer that aggregates the per-shop curves.

**Week 3 — Route demo.**
- Build a tiny PWA that records your phone's geolocation as you walk through the venue.
- Save the trail as GeoJSON.
- Replay it on the demo map as an animated dot, snapping to the nearest polygon to call out "entered Boots at 14:32, dwelled 7 minutes, moved to Costa."
- Generate 100 simulated peer routes with jitter to show what "real busy day" looks like.

**Week 4 — AI grounding panel.**
- For each shop, prepare a Rank4AI-style entity record.
- On pin click, show the entity record alongside the busyness curve.
- Build the side-by-side ChatGPT eval: take 10 prompts ("best coffee in Lakeside", "where can I get a kid's birthday gift"), record baseline answers, then re-prompt with the entity records + busyness data injected as context, record the better answers.
- Capture screenshots — that's your OpenAI deck.

End of week 4: a demo that shows a Lakeside map, with real (sampled) busyness layered on every shop, with at least one real recorded route through the venue, with Rank4AI entity records on each pin, and a screenshot pack showing how injecting this data improves ChatGPT's answers about shopping at Lakeside.

That demo is enough to walk into:
- A Lakeside / Westfield / Bluewater meeting and say "this could be your venue."
- An OpenAI / Anthropic data-partnerships meeting and say "this is what a grounding feed could look like."
- An investor meeting and say "here's the thing, here's the wedge, here's the visible product."

### Honest limits of the prototype

- Google Popular Times is sample-based, modelled, not consent-based. Fine for a demo, **not the data we'd ship to AI platforms in production.** Production data has to come from our own consent-based map (the eventual real product).
- Scraping Google's Popular Times is unsupported. They could block it tomorrow. Fine for a demo, can't be a foundation.
- One person's route is anecdotal, not a dataset.
- The map of Lakeside hand-traced from a directory PDF is approximate — fine for demo polygons, not for legal-grade venue records.

These caveats are features in the demo conversation, not bugs: "this is the shape of the product, with sampled bought-in data; the real version uses our own first-party indoor map data which is cleaner, consented and ours to license."

### What this prototype is *not*

- It is not the indoor-map product (Product A from Section 3). The indoor-map product is what visitors at the venue actually use.
- It is not the AI grounding feed (Product B from Section 3). The grounding feed is the consented, multi-venue, properly aggregated data product.
- It is a **demo artefact** that shows both products in miniature, on a venue you don't yet have a contract with, using public data sources as stand-ins.

It's the cheapest, fastest piece of evidence that the whole plan is real. Build this before you raise money. Build this before you sign a venue. Build this before you talk to OpenAI. Everything else gets easier once it exists.

---

## 13. Reality check: is there any way to see "actual" data?

Worth answering this head-on because it's the question that matters most for the credibility of the whole plan.

**Short answer: no — and structurally, no.** There is no public, buyable, accessible source of *actual* individual-level "this many real people are at Lakeside right now and here are the shops they visited." It does not exist commercially, and it cannot exist legally without consent. Every footfall product, map API, carrier dataset and analytics tool on the market today is a **sample extrapolated to an estimate**. None of them are ground truth.

This sounds disappointing until you realise it's also true of every competitor and every potential incumbent. **Nobody has actual data. The whole market is models on top of samples.**

### Who comes closest to "actual" — and why we still can't get it

**Apple.** Sees every iPhone's location continuously via the OS, Find My, Maps and system services. Closest thing on Earth to actual UK pedestrian footfall. **Does not sell, does not license, does not expose via API.** Apple's brand is built on not being a data seller. This will not change.

**Google.** Sees every Android phone, plus every Google Maps user on iOS, plus Search, plus Pay, plus Photos location metadata. Even larger dataset than Apple. Uses it internally (Maps "popular times", Traffic, Mobility Reports during Covid). **Does not sell raw data**, sells some aggregated insights via Google Maps Platform / Movement Insights, but never ground-truth "who is here."

**Mobile carriers (Vodafone, O2, EE, Three).** A carrier really does see every one of *its* customers' phones, in real time, via cell-tower handshakes. No sampling for that network. **But:**
- Aggregated only when sold (legal requirement under GDPR / PECR — they cannot sell individual location data).
- Coarse spatial precision (cell-tower level, ~100m–1km, much worse indoors).
- Each carrier sees ~20–30% of the UK population. Not the whole picture.
- Pricing is enterprise-tier and procurement is slow.

**Venue-side WiFi and cameras.** A shopping centre's own WiFi access points see every connected guest device. The cameras see every visitor. This is real, complete, ground-truth data **for that one venue**. It is not aggregated, not standardised, not licensable across venues without per-venue commercial deals. The venue owns it.

**Mobile SDK aggregators (Outlogic, Veraset, Gravy, etc.).** Used to be the closest thing to a "you can buy individual-level pings" product. **Collapsing.** The FTC banned X-Mode/Outlogic in 2024 from selling sensitive data. Gravy was breached in January 2025 and exposed the brittleness of the whole sector. Apple ATT and Google Privacy Sandbox are throttling the underlying data supply year on year. The "buy real-ish individual location data" route is closing.

### Why "actual" can't legally exist as a public product

Privacy law sets a floor. Under GDPR (Article 5), the UK Data Protection Act 2018, the ePrivacy Directive and PECR, you cannot publish, sell or expose individual-level location data without explicit informed consent from each person whose data it is. Even "anonymised" individual-level data has been repeatedly shown to be re-identifiable (the New York Times' anonymised taxi-trip dataset, Strava's global heatmap revealing US military bases, AOL's anonymised search logs). Regulators know this. The legal floor for what is sellable is **aggregation to a k-anonymity threshold** — and that, by definition, is not "actual" individual data.

So there is no legal path to a product that says "here is exactly which people went where in Lakeside today." Even if such a product existed, anyone buying it would be buying a regulatory time bomb.

### What you can actually see, today

The closest things to "actual" data that are legally available:

- **Aggregated carrier flows for an area.** Real for every phone on that network in that area, but k-anonymised and cell-tower-coarse. Useful for "how many distinct devices entered the Lakeside boundary on Saturday" — not "which shops they visited."
- **Venue-side WiFi or camera counts** if you have a deal with the venue. Real for that venue, not aggregable across venues without contracts.
- **Sample-based footfall vendor estimates** (Placer, Foursquare Movement, Huq). Modelled. They will tell you "estimated 4,200 visits" but the underlying sample is a few hundred.
- **Google Popular Times.** Free, sampled, modelled, unsupported via API. Best free public signal for typical busyness.
- **Your own first-party data once you build it** (the indoor map). Real for the people who scan and consent. Sample of "everyone who entered the venue" but a clean, documented one.

That last point is the whole point of the project. We don't promise actual ground truth — that doesn't exist on the market and can't legally exist as a global product. **We promise the cleanest available sample, with the best consent provenance, mapped to entities AI platforms can use.** That's a different product, but it's an honest product, and it's the one OpenAI can actually buy without legal risk.

### The right framing for venue and AI-platform conversations

When asked "how many people will you see":
- Don't claim actual / ground truth — you'll lose credibility immediately.
- Do say: "every visitor who scans the map gives us their explicit consent and a precise indoor position. That's a documented sample of *N* per venue per day, with consent provenance, polygon-level entity linkage, and dwell data. No competing footfall product can offer the same combination of consent and precision."
- For the rest of the visitors who don't scan, name the corroborating sources clearly: WiFi counts at the venue, carrier-aggregated arrivals, camera counts where available. Document each.
- Position the feed sold to AI platforms as "consented, entity-linked, multi-venue presence sample with documented coverage and methodology" — not as a population census.

That positioning is defensible. The "we have ground truth on everyone" positioning isn't, and would attract the wrong kind of buyer and the wrong kind of regulator.

### So is there a way to see actual data?

For one venue, with the venue's permission, via their own WiFi and cameras: yes, with paperwork. They already have it.

For the public market, via an API or a paid data product: no, and there shouldn't be. Every alternative is a sample dressed up as a number.

For our project: the *play* isn't to find a magical source of actual data. It's to build the cleanest sample anyone is selling, document its methodology better than anyone has, and be the first to package it for AI platforms specifically. That's the win available, and it's still a very large business if executed.

---

## 14. So where is the actual business?

Fair pushback. If we can't get ground truth — and nobody else can either — what's the business actually made of? Here's the honest layered answer.

The mistake earlier in this doc was making it sound like *AI data licensing* is the whole business. It is one leg of four, and the least certain. The real business is the stack. Each layer makes sense on its own; the layers above it are upside.

### Layer 1: Rank4AI methodology and audit (revenue today)

This already exists. Documented framework, defined audit, two scoring outputs (AI Visibility Score, Structural Reference Score), established methodology page, founder-led delivery. It runs whether the maps project happens or not.

- **Customer:** any business that wants to be cited and recommended by AI platforms.
- **Pricing shape:** per-audit fee plus retainer for ongoing optimisation, like a specialist SEO agency.
- **Market reality:** the GEO/AI-search agency market is *forming now*. Profound, AthenaHQ, Otterly are proof there are buyers. Rank4AI's edge is methodology + audit, not just monitoring.
- **Certainty:** highest. Works today.

### Layer 2: Indoor map SaaS to venues (year 1–2)

Sell the indoor map to venue landlords as a low-friction, scan-to-web amenity. They pay an annual SaaS fee per venue.

- **Customer:** Lakeside, Westfield, Bluewater, smaller shopping centres, hospitals, universities, museums, stadiums, transit hubs.
- **Pricing shape:** £10k–£100k per venue per year depending on size, plus setup. Indoor-mapping incumbents (Pointr, Mapwize, MazeMap) prove this market exists and is paying. Hospital and airport contracts can run higher.
- **Why we win deals:** scan-to-web with no app install, inclusive design out of the box, bundled AI search visibility for tenants, half the price of a Pointr enterprise SDK deployment.
- **Certainty:** high. The category exists and is paying. We compete on positioning and packaging, not invention.

This layer alone is a business. Pointr is reportedly worth several hundred million on this model. Mapwize was acquired by Engie. We don't need the AI angle to make this layer pay.

### Layer 3: Inside-venue revenue (year 2–3)

Once the map is live, layered revenue stacks on top.

- **Tenant claim and analytics dashboard.** £50–£500/month per tenant for visit analytics, peak hours, dwell, returning rate (location-only, sample-honest). Standard SaaS upsell.
- **Sponsored pins / category takeovers / route-end suggestions.** High-margin advertising inventory at point of intent (visitor is in the venue and looking). Like in-airport advertising but trackable.
- **Brand-level deals with chains** (H&M, Boots, Greggs) for consolidated dashboards across every store in our network.

- **Pricing shape:** per-tenant SaaS plus ad spend. Ad CPMs at point-of-intent are premium.
- **Certainty:** medium-high. Pattern is well-established (Google's whole business is this shape, just outdoors).

### Layer 4: AI platform data licensing (year 3+, the dream)

The big bet. Aggregated, anonymised, entity-linked location feed sold to OpenAI, Anthropic, Google, Perplexity as grounding data.

- **Customer:** AI platforms.
- **Pricing shape:** £500k–£5M per platform per year if it works, based on OpenAI's known publisher-deal precedents.
- **Certainty:** speculative. Demand unproven, coverage threshold unclear, competitor reaction unpredictable.

This layer is the upside, not the foundation. If it works, the company is enormous. If it doesn't, the company is still a real SaaS business off layers 1–3.

### What "the business" actually looks like in revenue terms

Year 1: ~100% from Layer 1 (Rank4AI services). Revenue is methodology and audit work.

Year 2: Layer 2 starts (first paid venue). Revenue mix maybe 60/40 services/SaaS.

Year 3: Layers 1, 2, 3 all live. Revenue mix maybe 30/40/30 services/SaaS/ads. First AI-platform conversations happening but no signed deal yet.

Year 4–5: First AI-platform contract if the bet pays off. Layer 4 becomes the largest line. Mix might be 10/20/15/55 services/SaaS/ads/data.

Year 5+: Either Layer 4 dominates (data company outcome) or it doesn't and we have a healthy multi-line SaaS business with a methodology arm.

### Why we'd still beat the existing footfall players to AI platforms

Honest answer: this is the question that decides the upside.

**Why Placer / Foursquare Movement / Huq might beat us:**
- They have years of data already.
- They have national coverage.
- They have data-team headcount.
- They could pivot to "AI grounding" framing in a quarter if they decided to.

**Why we still have a real shot:**
- **Consent quality.** Their data sits on SDK panels with murky provenance. The FTC just spent 2024 hammering exactly this category. Ours is built on visitor-initiated QR scans with a clean consent flow. AI platform procurement teams care about this — defensible data sourcing is now a regulatory line, not a marketing nicety.
- **Entity linkage.** Our data is anchored to per-polygon entity IDs that resolve to Wikidata, Companies House, brand parents and the Rank4AI graph. Their data is "device near coordinates." Linking the latter to the structured entities AI platforms use is real engineering work they haven't done.
- **Indoor precision.** They are mostly outdoor or tile-based. AI grounding for "best phone shop in Lakeside" needs to know which unit, not just which postcode.
- **Bundle with methodology.** Rank4AI gives us a ready story for *why* this dataset exists, what its quality properties are, and how it slots into a five-signal model. They sell a feed; we sell a feed inside a thesis.
- **Speed.** They are big, public-ish, slow. We can define the category and make the first OpenAI deal before they've had the strategy meeting.

We will not beat them on volume. We can beat them on cleanliness, structure, and being there first.

### What if Layer 4 never happens?

Stress-test the plan with that assumption.

- Layers 1–3 still work.
- Layer 1 alone is a £1–5M/year services business at modest scale.
- Layer 2 at 50 venues × £30k average is £1.5M/year recurring.
- Layer 3 at the same scale could match or exceed Layer 2.
- Combined, that's a £5–15M/year SaaS-plus-services business with growth ahead and the Rank4AI brand attached.

Smaller than the dream, but real, profitable, and worth building on its own merits. Layer 4 is the call option, not the entire bet.

### So where is the business, in one sentence

The business is a **methodology-and-audit services line** with an **indoor-map SaaS attached**, with **tenant analytics and advertising layered on top**, plus a **call option on selling consent-based footfall data to AI platforms** if the category turns out to exist. Three of those four are well-understood. The fourth is the upside.

We don't need to find ground truth in the data to make the business work. We need the cleanest sample, the best entity linkage, the inclusive-design wedge, the AI-search positioning, and disciplined execution across four revenue lines that reinforce each other.

---

## 15. Just on the AI search data play — if you can't openly access or buy it, what do you do?

Stripped right back. Forget the layered business for this section. The question is just: for the location-data-to-AI-platforms play specifically, if there is no API to call and no ground-truth dataset to buy, what are the practical paths to actually having data to sell?

Five real paths. They are not mutually exclusive — most realistic plans combine them.

### Path A: Originate the data yourself

Build something that gives users an active reason to consent to location capture, and the data is yours.

The indoor map is the shape we picked. Other shapes that originate location data:
- A loyalty / deals app for a city or venue cluster.
- A parking app (RingGo, JustPark are exactly this).
- A transport companion app (live train info, last-mile).
- A scan-to-pay or scan-to-claim retail app.
- A tourism / discovery app for a city.

Pros: data is yours, consent is explicit, no supplier dependency, defensible moat once at scale.
Cons: years of consumer-product work before you have meaningful coverage. Cold-start problem — empty maps get no scans.

This is the long road. The map is our specific bet on it because it bundles cleanly with the AI-search thesis (each pin is also an entity).

### Path B: License what is buyable and add the value AI platforms specifically need

You can't buy ground truth. You can buy *samples and aggregates*, today, from:
- UK mobile carriers (Vodafone Analytics, O2 Motion, EE/BT, Three) — broad but coarse and expensive.
- Footfall analytics products (Placer.ai, Foursquare Movement, Huq, Mytraffic, Springboard) — sample-based but buyable.
- Vehicle probe data (HERE, TomTom, INRIX) — for arrival flows.
- Marketplace catalogues (Snowflake Data Marketplace, AWS Data Exchange, Datarade) — easier procurement.

Buying raw and reselling has no moat. The value-add that makes this a real product is:
- **Entity linkage.** Every record tied to stable Rank4AI / Wikidata / Companies House IDs. The buyers (AI platforms) need entity-anchored data, not "device near coordinates."
- **AI-grounding format.** Records shaped exactly as a grounding feed expects (entity ID, freshness timestamp, k-anonymity attestation, change-vs-prior-period, dwell distribution).
- **Blending across sources.** A pipeline that takes carrier flows + Placer estimates + venue WiFi where available, reconciles them, documents coverage and method per record.
- **Documentation.** A public methodology paper — provenance, consent, k-anonymity threshold, accuracy bounds, refresh cadence. This is procurement-defensible.

Pros: you can be selling something to AI platforms within months instead of years.
Cons: thin margin if you don't add real engineering value; supplier dependency; if the suppliers themselves pivot to AI-grounding, you compete with your own raw-data partners.

### Path C: Partner or co-build with someone who already has the data

Faster than originating, more defensible than reselling. Possible shapes:
- **Carrier white-label.** Approach Vodafone or O2 with the AI-grounding pitch. They have data, you have the buyer relationship and entity-linking expertise. Revenue share. They're not in the AI-grounding business and probably aren't going to enter it.
- **Venue chain deal.** Sign a master agreement with one shopping-centre operator (URW, Hammerson, Landsec, Intu's successors) that gives you access to their venue WiFi analytics across all their UK properties — twenty-plus venues from a single signature.
- **Loyalty / payments partner.** A retailer-loyalty operator (Nectar/Sainsbury's, Tesco) sees presence and spend across thousands of stores. Co-build a location-only product feed scoped narrowly enough to survive contracting.
- **Acquire a small player.** Huq, Mytraffic, or a regional footfall vendor for low-eight-figures could leapfrog years of organic build.

Pros: data scale on day one, defensible relationships, faster to revenue.
Cons: partnerships are slow to close; acquisitions need capital; partners can re-trade the deal once they realise what AI grounding is worth.

### Path D: Build a paid panel

Old school, still works. Pay users to install an app and contribute consented location data — like Nielsen for TV, or YouGov for opinion.

- Recruit a representative panel (10–50k UK residents to start).
- Pay them — £5–10 per month or accumulated points.
- App captures consented location with full transparency.
- Build entity-aggregated reports.

Pros: explicit consent, defensible methodology, exactly what AI platforms can buy without legal heartburn, fully your data.
Cons: panel acquisition is expensive (£50–200 per recruited active panellist), takes a year minimum to reach useful coverage, panel skews demographic and needs ongoing weighting.

### Path E: Use accessible web-derived signals as a starting product

This is the most underrated path. There are public or semi-public "presence at place" signals that nobody is bothering to package into AI grounding feeds:

- **Geotagged social posts.** Instagram, TikTok, X, Threads — when people post from a place, they leave a presence signal. APIs and partner programmes vary; some scrapeable, some only via paid tier.
- **Public booking platforms.** OpenTable, Resy, Quandoo, Bookatable — collectively show restaurant demand at every covered venue.
- **Event ticket sales.** Eventbrite, Ticketmaster, Skiddle, Fatsoma — dated demand signals for venues that host events.
- **Public transport tap data.** TfL has aggregated station-level tap data via open APIs. Other UK transit operators publish similar. Tells you arrivals at major nodes near venues.
- **Parking app data.** RingGo, JustPark, ParkMobile. APIs vary; aggregated parking demand tells you arrivals at retail destinations.
- **Retail open-hours and staffing signals.** Indeed job listings, Glassdoor reviews, Google reviews timestamps — proxies for store activity.
- **Reservation cancellations, queue widgets, click-and-collect availability.** Public-facing UI signals on retailer websites that reveal demand.

None of these is "footfall." Together, blended and entity-linked, they're a credible demand-and-presence signal for AI platforms — and they're already accessible. This is essentially a clever scraping-and-modelling product, lower-quality than first-party data but available *now*.

Pros: can be live in months, no consumer product needed, no panel cost, no carrier procurement.
Cons: legal terms vary by source (some scraping is ToS-violating), data is noisy and indirect, can be turned off by source platforms.

### Path F (do this one first): Validate demand before building any data

The cheapest answer to "what do I do" is: don't build data infrastructure until you've confirmed AI platforms want it.

- Five conversations with data-partnership / grounding-team contacts at OpenAI, Anthropic, Google AI, Perplexity, Microsoft.
- Use the prototype from Section 12 as the demo asset.
- Ask: "if a feed like this existed, would you license it? What would it need to look like? What coverage would matter? What's the legal bar for sourcing?"
- Total cost: a few weeks of effort and a Lakeside-style demo.

If they say yes (in any form): you have leverage to license carrier data (Path B), close venue partnerships (Path C), or fund a panel (Path D), because you have a buyer.

If they say no: you've saved years and can pivot back to layers 1–3 of the business (Section 14) without having spent on a data infrastructure that nobody wanted.

This is the cheapest, highest-information move available, and it doesn't require any actual data to do. It just requires the demo from Section 12 plus the right introductions.

### The realistic combined plan

Don't pick one path. Combine in stages.

- **Months 0–3:** Path F (demand validation) plus the Section 12 prototype. No data infrastructure yet.
- **Months 3–9:** assuming demand validates, Path E (web-derived signals) to ship something licensable now, plus Path B (license a Placer/Huq tile or Vodafone extract for the flagship region) to enrich it.
- **Months 6–18:** Path A in parallel — the indoor map at the pilot venue starts producing first-party data, slowly replacing the bought-in slices.
- **Year 2+:** Path C (carrier or venue-chain partnerships) for scale, possibly Path D (panel) for representative demographics.
- **Year 3+:** by now we have a blended pipeline — first-party map data + web-derived signals + licensed carrier data + panel weighting — sold under our methodology and brand, with documented provenance per record.

So the answer to "if I can't openly access or buy ground-truth data, what do I do" is: **validate demand first, then ship a blended sample-based feed using web-derived signals plus what you can license, then progressively replace the bought-in slices with first-party consent-based data as the map grows.**

The data product is never ground truth. It's the cleanest documented sample, with multiple sources blended, sold to a category that didn't exist before. That's the actual play.

---

## 16. Building the prototype: how to actually capture the data

You want a prototype where, when people use the map, you can see where they go. Here is the minimum-viable path that works in a browser without a native app, without BLE beacons, and without solving indoor positioning from scratch.

The headline insight: **don't try to track raw GPS through the venue.** Indoor GPS in browsers is unreliable (50–100m off, or stuck on the last outdoor fix). Instead, capture **explicit interaction events** — QR scan locations, pin taps, navigation requests, "I'm here" confirmations — and infer movement from those. That gives you a clean event log of where people actually engaged, without fighting the limits of browser geolocation.

### The data capture model

Every map session is an anonymous chain of events:

| Event | Captured when | What it tells you |
|-------|---------------|-------------------|
| `session_start` | QR scanned, map opens | Venue, anchor pin, time, anonymous session ID |
| `pin_view` | User taps a pin to see its info | They're interested in this shop |
| `route_request` | User taps "directions to" a pin | They intend to physically visit this shop |
| `route_arrive` | Optional confirm-arrival button at destination | They got there |
| `qr_rescan` | User scans another QR inside the venue | Real "you are here" anchor at a known location |
| `geo_ping` | Background `watchPosition()` callback | Lat/lng with accuracy — useful outdoors and at venue boundaries, fuzzy indoors |
| `dwell_threshold` | User stays on the same pin/area for >N seconds | Implied presence at that location |
| `session_end` | User closes the tab or 30 min idle | Visit duration |

Each event carries: `{event_type, session_id, venue_id, polygon_id?, lat?, lng?, accuracy?, timestamp}`. No personal identifiers. Session ID is a per-visit UUID generated client-side, not tied to a user account.

That event stream is enough to derive:
- Visit count per shop (from `pin_view` + `route_request` + `qr_rescan` near the polygon).
- Dwell estimates per area (from `dwell_threshold` and `qr_rescan` deltas).
- Routes through the venue (sequence of `qr_rescan` and `route_request` events).
- Conversion funnel (which `pin_view` events became `route_request` then `route_arrive`).

You don't need GPS-precise indoor tracking to get useful data. You just need to capture intent.

### The simplest tech stack that works

Whole prototype in ~1–2 weeks for one developer:

- **Frontend:** plain HTML/JS or Next.js. Render the map with **Mapbox GL JS** (free tier covers prototype). Floor plan as GeoJSON polygons.
- **Geolocation:** browser `navigator.geolocation.watchPosition()` — yes it's fuzzy indoors, capture it anyway as a secondary signal.
- **QR codes:** static URLs of the form `https://yourapp/v/lakeside?pin=p042`. Generate via `qrcode` library or any free QR generator. Print as physical signage.
- **Event capture:** **PostHog** (self-host or cloud, has a generous free tier and is privacy-friendly), or roll your own with a single `POST /event` endpoint. PostHog gives you out-of-the-box session recording, funnels, retention.
- **Backend:** **Supabase** (managed Postgres + auto-generated APIs + auth, free tier sufficient) or **Neon** + a small Node.js server. One database, three tables: `sessions`, `events`, `polygons`.
- **Hosting:** **Vercel** for the frontend (free tier), **Supabase** for the backend (free tier).
- **Dashboard:** PostHog's built-in dashboards cover most of what you need. For custom views, a tiny Next.js admin page that queries Supabase directly.

Total monthly cost for the prototype: £0–£20. No infrastructure expertise needed.

### Schema sketch

```
sessions(
  id uuid primary key,
  venue_id text,
  started_at timestamptz,
  ended_at timestamptz,
  consent_version text,
  user_agent text  -- coarse only, no fingerprinting
)

events(
  id bigserial primary key,
  session_id uuid references sessions,
  event_type text,
  polygon_id text,
  lat double precision,
  lng double precision,
  accuracy_m double precision,
  timestamp timestamptz
)

polygons(
  id text primary key,
  venue_id text,
  name text,
  category text,
  brand_parent text,
  rank4ai_entity_id text,
  geom geometry(polygon, 4326)
)
```

That's the entire data model. PostGIS extension (free, included in Supabase) lets you do `ST_Contains(geom, ST_Point(lng, lat))` to figure out which polygon a ping fell inside.

### The consent flow (legal floor, do not skip)

Before any event is captured:

1. First-scan banner: "This map captures your anonymous location and interactions to power wayfinding and improve venue analytics. No personal data is collected. [Continue] [Privacy notice] [Decline]."
2. If decline: map still works, but no events stored.
3. Privacy notice page links to: data controller, what's captured, retention period (30 days for raw events, indefinite for aggregates), opt-out instructions, ICO complaint link.
4. Cookie/consent banner only if you're using cookies — for a stateless session UUID stored in localStorage, you may avoid the cookie banner but still need PECR-compliant consent.
5. Set `consent_version` per session so you can prove what consent text was active at capture time.

For a UK prototype with no special-category data and aggregated reporting, this is enough. For production, get a lawyer to review.

### What the dashboard would show

Once events are flowing, the prototype dashboard could render:

- **Live visitor counter** per venue (active sessions in the last 5 minutes).
- **Heatmap** of pin views across the floor plan — hottest shops, coldest corridors.
- **Top routes** — most common sequences of pin interactions (Boots → Costa → Argos).
- **Funnel**: pin views → route requests → route arrivals.
- **Per-shop card**: visits today, dwell estimate, returning vs new, hour-by-hour curve.
- **Time slider**: scrub through the day to see how busyness moves.

PostHog can render most of these for you straight from the event stream. Custom polygon overlays and heatmap need a small bit of Mapbox layering.

### Honest limits of this prototype

- **Indoor positioning is fuzzy.** You'll see "user is somewhere within ~30m of this shop" not "user is in this shop." That's why we lean on intent events (pin taps, route requests, QR rescans) instead of GPS pings.
- **Coverage depends on scan rate.** If only 10% of visitors scan, you have 10% of the population to model from. This is the same sample-vs-ground-truth issue as every other footfall product.
- **No multi-visit identity.** Without an account/login, you can't tell if the same person came twice. That's a feature for privacy and a limit for repeat-visitor analysis. You can use a longer-lived localStorage UUID with consent, but it complicates the privacy story.
- **iOS Safari quirks.** Background geolocation is restricted. The map only captures `geo_ping` events while the tab is in the foreground.
- **Data quality improves with QR density.** Five QRs per venue gives sparse anchors; 20+ gives much richer route data.

These are not problems for a demo. They are problems if you tried to ship this as the production grounding feed for OpenAI. The production version replaces fuzzy GPS with a denser BLE beacon network or a native app, increases scan rates with venue partnerships, and runs at much larger scale.

### Recommended first build, in order

1. **Spin up Supabase and Vercel projects.** 30 minutes.
2. **Pick one venue** and trace its floor plan to GeoJSON. A simple shopping mall: a day's work in QGIS or a vector editor. Lakeside: probably 2–3 days.
3. **Build the map page.** Render polygons, label them, click to show a side panel. Couple of days.
4. **Wire up events.** PostHog SDK or a `POST /event` endpoint. Half a day.
5. **Generate QR codes** for entry plus 5–10 anchor points around the venue. An hour.
6. **Print and stick up the QRs**, or just simulate on a phone for the demo.
7. **Walk the venue yourself** — scan, tap pins, request routes — and watch your event stream populate.
8. **Build the dashboard** in PostHog or a small Next.js page. Day or two.

End of week 2: you have a real, working capture-and-display prototype. One venue, one developer, near-zero infrastructure cost. Sample of one (yourself) initially, but the architecture scales identically to a thousand visitors.

That's the prototype. Once it works for you walking through Lakeside alone, the next step is getting *one other person* to do the same — proves the multi-session aggregation. Then a friendly venue partner to point real visitors at it. Each step is small and de-risks the next.

---

## 17. "But phones track location all the time — surely we can use that?"

You're right that phones track. The answer to "where are people" is sitting on every iPhone and Android device in the country. The misunderstanding earlier in the doc was about who can *access* that data, not whether it exists. Let's pin this down clearly because it's the most common confusion in this whole space.

### What every phone knows about itself

Every modern phone continuously builds its own location picture from:
- **GPS** — outdoor positioning to ~5–10m.
- **WiFi triangulation** — indoor and outdoor, often more accurate than GPS in dense areas.
- **Bluetooth scanning** — proximity to nearby devices and known beacons.
- **Cell-tower handshakes** — coarse but always on.
- **Motion sensors** — accelerometer, gyroscope, magnetometer for dead-reckoning when GPS drops.
- **Connection history** — known networks (home, work, café WiFi).

Apple and Google both stitch these into a continuous location history that lives on the device and (if the user allows) syncs to iCloud / Google Account. Look at iPhone Settings → Privacy & Security → Location Services → System Services → Significant Locations. That history exists. Same on Android via Google Maps Timeline.

So yes — the data exists. **The phone knows. The OS knows. iCloud or Google Account knows.**

### Who can actually see that data

This is where it gets specific. Five parties can each see a piece of it, and only a piece:

1. **The user themselves.** Full location history visible in their phone's settings.
2. **Apple (for iPhones) and Google (for Androids).** The OS makers. They have the most complete picture. **They do not sell or expose it via any API.** This is a regulatory and brand-strategic decision — Apple's whole brand is built on not being a data seller, and Google has been forced into more privacy posture by GDPR and class actions.
3. **The mobile carrier** (Vodafone, O2, EE, Three). They see the cell-tower handshakes for every phone on their network. Real-time, complete for that network, but coarse spatially. They will only sell *aggregated* extracts (legal requirement under GDPR/PECR).
4. **Apps the user has installed and granted location permission to.** Each app sees only its own users, and on iOS only while the app is in use unless the user explicitly allows "Always."
5. **Find-My / Family-tracking apps** the user has opted in to (Apple Find My, Google Find My Device, Life360, etc.). Same model — explicit per-user consent, visible only to authorised contacts.

That is the entire universe of who can see phone-tracked location data. There is no sixth party that can "tap into the network of all phones." There is no API that exposes it. There is no broker who legally sells it.

### Why "we can't just access it"

Three reasons, all hard:

- **Apple and Google won't sell it.** Even if you offered them billions, the brand and regulatory cost of selling individual-level location data is too high. They use it internally and stop there.
- **Privacy law forbids public access to individual-level location data without consent.** GDPR Article 5, ePrivacy, PECR. Even if a route to access existed, selling or buying it would expose every party in the chain to regulator action. The FTC's 2024 ban on Outlogic for selling sensitive location data is exactly this principle in enforcement form.
- **Phone OS sandboxing prevents one app from seeing another app's data.** A weather app can't see where the maps app saw you. A retail app can't see what the parking app captured. Each app is its own silo by design — that's a privacy guarantee, not a missing feature.

So the data exists, but it's locked behind three doors that cannot be picked: the OS owner's commercial decision, the law, and the device's own sandbox.

### What this means for us — the only path that works

Because we cannot tap into existing phone tracking, the only way to get location data of our own is the same way every other app gets it: **build an app, ask the user for permission, and capture from there.**

That is exactly what the indoor map does. It is one of the apps in category 4 above. When a visitor scans the QR and opens the map:
- The map asks for location permission (browser prompt).
- If granted, we receive the same `lat/lng` stream the OS provides to any consenting app.
- We capture it for that session, attach it to the venue context, and store it.
- That data is ours to aggregate and license.

The map *is* a phone-tracking mechanism — just one that the user has explicitly turned on for our specific app. There is no shortcut around this. Every successful location-data product (Strava, Google Maps, Find My Friends, Snap Map, Life360, every retailer app with a "find your nearest store" feature) works exactly this way: it is an app the user installed and granted location permission to.

### The concrete reframe

- **Wrong question:** "How do I tap into the location data that phones already collect?" There is no answer. That door doesn't open for third parties.
- **Right question:** "How do I become one of the apps the user has granted location permission to, with the cleanest possible reason for them to grant it?" The map is our answer. A loyalty app, a parking app, or a transport app would be other shapes of the same answer.

The reason we are building the map is *exactly* because phones track. The map is how we get on the consented-app side of that tracking. We don't access existing tracking — we participate in it, with our own users, with our own consent flow.

### Quick comparison: how every successful location data product solved this

| Product | How they got the data | Why users opted in |
|---------|-----------------------|--------------------|
| Google Maps | Built the maps app | Free maps and navigation |
| Apple Maps | Built into iOS | Comes with the phone |
| Strava | Built the fitness app | Athlete tracking and social |
| Snapchat / Snap Map | Built into Snap | Social sharing |
| Life360 | Built family-locator app | Family safety |
| Foursquare | Built the check-in app, then SDKs | Social discovery |
| Placer.ai | Buys SDK data from many third-party apps | Each underlying app gave its own users a reason |
| Vodafone Analytics | Network-level (carrier) | Existed by virtue of being a carrier |
| **Our map** | Built the indoor map app | Wayfinding inside a venue |

Every one of these is "build an app users want, get permission, aggregate the result." There is no other way that exists. The map is our specific entry into the same model, with the AI-grounding twist downstream.

So yes — phones track. That's exactly why the play works. The map is how we participate in that tracking, with users who have opted in, in a way that is licensable to AI platforms because the consent provenance is clean.

---

## TL;DR

We're building an indoor map that opens via QR scan when a visitor enters a venue. It's useful in its own right and we'll sell it to venues as a SaaS amenity. The bigger play is that the same map quietly captures consent-based, location-only footfall data, ties it to entity records in the Rank4AI graph, and feeds it to AI platforms as a grounding signal. Today AI platforms answer "where should I go" with online-only signals that are easy to manipulate. We're selling them the offline truth. The map is the wedge. The data is the product. OpenAI is the customer that matters.
