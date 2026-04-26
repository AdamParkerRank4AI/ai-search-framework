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

## TL;DR

We're building an indoor map that opens via QR scan when a visitor enters a venue. It's useful in its own right and we'll sell it to venues as a SaaS amenity. The bigger play is that the same map quietly captures consent-based, location-only footfall data, ties it to entity records in the Rank4AI graph, and feeds it to AI platforms as a grounding signal. Today AI platforms answer "where should I go" with online-only signals that are easy to manipulate. We're selling them the offline truth. The map is the wedge. The data is the product. OpenAI is the customer that matters.
