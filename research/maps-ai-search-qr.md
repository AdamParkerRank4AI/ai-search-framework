# Research: Indoor Maps + AI Search + QR Code Notes

**Status:** Early-stage research / brainstorm
**Owner:** Liam (project lead)
**Captured:** 2026-04-26

---

## Concept

An indoor wayfinding map that activates when a visitor enters a building and shows them where things are inside. Think Lakeside shopping centre as the reference experience: a large, multi-tenant venue where visitors need to locate shops, facilities, exits and amenities quickly.

The map is the surface layer. Underneath it links to the Rank4AI AI search framework so that the entities shown on the map (shops, services, points of interest) are also discoverable, described and recommendable through AI platforms — not just visible on a static floor plan.

QR codes act as the entry point and the annotation layer: a visitor scans a code on arrival (or at a specific location inside the venue) and is dropped into the relevant view of the map, with notes attached to specific pins or zones.

---

## Reference experience: Lakeside

- Large indoor shopping centre with multiple floors and zones.
- Visitors typically need: "where is X shop", "where is the nearest toilet", "how do I get to car park C".
- Existing solutions are usually static directories or kiosk touchscreens.
- Opportunity: phone-first, scan-to-open, AI-aware.

---

## Candidate tech stack

### Mapping
- **OpenStreetMap (OSM)** — open data, includes indoor mapping via the [Simple Indoor Tagging](https://wiki.openstreetmap.org/wiki/Simple_Indoor_Tagging) schema (`indoor=room`, `level=*`, etc.). Good for venues that are already mapped or that we map ourselves.
- **Mapbox** — commercial tiles + SDKs (Mapbox GL JS for web, native SDKs for mobile). Strong styling, vector tiles, good indoor map support via custom tilesets or Mapbox Studio.

Trade-off: OSM is free and open but indoor data quality varies wildly by venue. Mapbox gives polish and tooling but introduces per-load pricing at scale. A reasonable path is to **author the indoor floor plan once** (SVG or GeoJSON), then render via either OSM/Leaflet or Mapbox depending on cost/feature needs.

### Schematics (floor plans)
- "Scampateics" — assumed to mean **schematics**: the underlying floor-plan drawings that define rooms, corridors, units and POIs.
- Sources: venue's existing CAD/architectural drawings, traced manually in tools like JOSM or Mapbox Studio, or vectorised from PDF directories.
- Output format: GeoJSON per floor, with each feature carrying an `id` that links into the AI search entity graph.

### QR codes
- One QR per location/pin (e.g. at each shop entrance, lift, info point).
- Scan resolves to a deep link: `/venue/{venueId}/map?pin={pinId}` — opens the map centred on that pin with the note panel open.
- QRs can also carry a "you are here" calibration role for indoor positioning.

### AI search linkage
Each map entity (shop, service, room) is also a Rank4AI entity:
- Has an `Organisation` / `Place` schema record.
- Carries the same identity language across the venue directory, the entity's own site, and external listings (Signal 04: Ecosystem Validation).
- Notes attached to a pin become RAG-ready passages (Signal 03: Meaning Architecture) — primary answer in first 150 words, full entity name, no anaphora.

Result: a visitor who asks an AI platform "what's the best coffee in Lakeside" can be confidently recommended a tenant, *and* the same pin on the in-venue map carries the same description.

---

## Open questions

1. **Hosting model** — single multi-tenant platform, or per-venue deployment?
2. **Indoor positioning** — do we need real-time "blue dot" location (BLE beacons, UWB, Wi-Fi RTT), or is QR-anchored "you are here" enough for v1?
3. **Note authoring** — who writes the notes attached to each pin? Venue staff, tenants themselves, or auto-generated from the tenant's own AI-search-optimised content?
4. **Offline behaviour** — venues with poor mobile signal need cached tiles and notes.
5. **Accessibility** — step-free routing, audio cues, contrast for visually impaired visitors.
6. **Data ownership** — who owns the floor plan data once digitised? Venue or platform?

---

## Possible v1 scope (for later discussion, not decided)

- One pilot venue.
- Static floor plan (GeoJSON), no real-time positioning.
- QR codes at ~10 anchor points.
- Web app only, no native install.
- Map renders via Mapbox GL JS (faster to ship) with OSM as the data substrate.
- Each pin links to a note + a Rank4AI entity record.

---

## Next research steps

- Audit Lakeside's existing digital wayfinding (app, kiosk, signage) for gaps.
- Survey OSM indoor coverage of 3–5 candidate UK shopping centres.
- Prototype a single-floor GeoJSON + Mapbox render to test feel.
- Sketch the QR → deep-link → note flow on paper before any code.
- Define the schema for a "map entity" so it round-trips cleanly between the map view and the AI search framework.

---

## Distribution: Google Maps integration

Can the indoor map be added directly to Google Maps so visitors get it through a surface they already use?

- Google has a programme called **Google Maps Indoor Maps** where venue owners can submit floor plans (historically via the Google Maps Floor Plan tool, now folded into the Geo Data Upload / Business Profile flows). Approved plans show inside Google Maps when a user is at the venue.
- Submission requirements: proof of ownership/authorisation, accurate floor plans (often as georeferenced images or DWG), and ongoing accuracy.
- Trade-off: Google distribution is huge but we lose control of the experience — no QR-driven note panel, no advertising surface, no footfall capture, and pin metadata is reduced to whatever Google's schema allows.
- Likely answer: **dual-publish** — submit the basic floor plan to Google Maps for discoverability, but keep the rich experience (notes, AI search links, ads, analytics) on our own scan-to-open web app.

Open question: does Google Maps Indoor still accept new submissions for shopping centres, or is it now restricted to airports/transit/large venues? Needs verification.

---

## Sign-up: "WiFi at a pub" model for venues

The venue onboarding flow should feel as low-friction as setting up free pub WiFi:

- Venue manager scans a QR or visits a short URL.
- Enters venue name, address, contact, uploads a floor plan (or selects from existing OSM data).
- System auto-generates: venue page, base map, a starter set of QR codes (PDF download, ready to print and stick up).
- Tenants inside the venue can then claim their own pin (like claiming a Google Business Profile) and edit their note.

Parallels to draw on: Cloud4Wi, Purple WiFi, The Cloud — they all solved frictionless venue onboarding for guest WiFi. Same playbook works here.

Pricing model questions: free for the venue and monetised through tenant upgrades + ads, or per-venue SaaS fee, or both?

---

## Advertising on the map

The map is high-intent surface — the user is *in the venue*, looking for somewhere to go. That's premium ad inventory.

Possible ad formats:
- **Sponsored pins** — a tenant pays to have their pin highlighted, animated, or pinned to the top of search results inside the venue.
- **Route-end suggestions** — when a user routes to a destination, show a sponsored "on the way" pin (e.g. coffee shop on the route to John Lewis).
- **Category takeovers** — search "coffee" inside Lakeside and the top result is sponsored.
- **Dwell-triggered offers** — if a user lingers near a pin (see footfall section), surface a time-limited offer from that tenant or a competitor.
- **Seasonal / event banners** — venue-wide promotions surfaced on map open.

Guardrails: ads must be clearly labelled, must not block wayfinding, and must respect accessibility. Misleading sponsored routing would erode trust fast.

---

## Location settings: auto-enable on sign-up?

When a visitor first opens the map (via QR scan), can we auto-enable location so the "you are here" dot works without them having to dig through phone settings?

- **Browser reality:** location permission must be granted by the user — there's no programmatic auto-enable. iOS Safari and Android Chrome both require an explicit prompt per origin.
- **What we can do:** trigger the prompt at the right moment (immediately after QR scan, with a one-line explanation of why), and remember the grant for the session.
- **PWA install:** if the user adds the venue to their home screen, the location grant persists more reliably across visits.
- **Native app:** would allow background location and richer permission UX, but adds install friction — probably not v1.

Open question: do we even need device location if the QR itself anchors "you are here"? For a single-floor visit, maybe not. For multi-floor routing it becomes more valuable.

---

## Connectivity: no WiFi or 4G

Shopping centres and large indoor venues frequently have dead zones. The experience must degrade gracefully.

- **Cached tiles:** Mapbox GL JS supports offline tile packages; OSM tiles can be pre-bundled for the venue.
- **Service worker:** the web app caches the venue's map, pins, notes and routing graph on first load so subsequent navigation works offline.
- **QR payload:** the QR can encode a minimal "you are here" + venue ID so the app boots even with zero network if the bundle is already cached.
- **Venue WiFi handoff:** if the venue offers free WiFi, the QR landing page can prompt to join it (deep link to WiFi config on iOS/Android where supported).
- **Hardware fallback:** for venues that want guaranteed coverage, low-power BLE beacons at key points can broadcast a venue ID + zone ID even with no internet, and the cached app reads them.

Acceptance criterion: a visitor with a recently-cached app should be able to find a shop and route to a toilet with their phone in airplane mode.

---

## Footfall data (future)

Once the map is on enough phones inside a venue, the network of devices itself becomes a sensor.

Possible signals:
- **App-side presence:** any phone with the map open reports anonymised position to a venue-level heatmap. Aggregated, that's live footfall per corridor / per pin / per hour.
- **Bluetooth scanning of nearby devices:** phones can scan for nearby BLE/MAC signals to estimate density. **Heavy caveats:**
  - iOS does not allow apps to read raw Bluetooth MAC addresses of nearby devices (privacy lockdown since iOS 13+).
  - Android is more permissive but still requires location permission and is moving toward stricter controls.
  - MAC randomisation on modern phones makes unique-device counting unreliable.
  - This crosses a privacy/legal line (GDPR, PECR in the UK) that needs proper legal review before any scanning is built.
- **WiFi probe analytics via venue infrastructure:** the venue's existing WiFi access points can already produce footfall heatmaps (Cisco Meraki, Aruba, Purple do this). We integrate rather than rebuild — the venue sells/shares the data, our app overlays it.
- **Computer vision:** existing CCTV + analytics (e.g. Hoxton Analytics, V-Count) for entry counts and dwell. Same integration story.

Output products:
- Live "how busy is it" badge on each pin (like Google's "popular times" but real-time).
- Heatmap layer for venue managers (private dashboard).
- Anonymised, aggregated footfall data as a **sellable dataset** to retailers, landlords, planners.

---

## Footfall as a truth signal for AI search

This is the most interesting long-term thread.

AI platforms already weight signals like reviews, citations and external mentions when deciding whether to recommend a business. **Real-world behaviour** — actual humans physically going to a place and spending time there — is a far stronger truth signal than any of those, because it is much harder to fake.

Hypothesis: aggregated, anonymised footfall + dwell time data, attached to entities in the Rank4AI graph, becomes a premium ground-truth dataset that AI platforms (OpenAI, Anthropic, Google, Perplexity) would pay to ingest.

Why it's defensible:
- **Costly to fake.** Backlinks and reviews can be manufactured at scale; footfall in physical space cannot.
- **Cross-references existing signals.** A business with strong AI-search signals *and* strong footfall is verifiably real and active.
- **Recency.** Footfall is inherently fresh — answers the "is this place still open / still good" question that stale web content cannot.
- **Maps to the Five Signal Model.** Slots cleanly into Signal 04 (Ecosystem Validation) and Signal 05 (Signal Consistency) as a continuously refreshed external truth source.

Productisation path (years out, not now):
1. Build the map + venue network (this project).
2. Build the footfall capture stack (privacy-compliant from day one).
3. Aggregate to entity level — every venue and every tenant inside it gets a verifiable activity signal.
4. License the dataset to AI platforms as a "real-world verification feed" for their grounding/RAG layers.
5. Position Rank4AI as the layer that connects AI search recommendations to actual physical reality.

Risks to flag now:
- **Privacy and consent.** Any footfall product has to be privacy-first by construction or it's both illegal and brand-damaging. Aggregation thresholds, k-anonymity, no individual tracking ever.
- **Regulatory.** GDPR, PECR, ePrivacy, and likely incoming AI-data-source regulation. Build for the strictest case.
- **Data exclusivity.** If the same footfall data is available to all AI platforms, it's commoditised. Exclusivity, recency or richer entity linkage is what makes it sellable.

This is the long game. The map is the trojan horse; the footfall-to-AI-truth-signal pipeline is the actual product.

---

## Feasibility scorecard

A rough read on each idea covered above. Ratings: **Likely** (achievable with normal engineering), **Possible** (achievable but with real constraints or partner dependency), **Hard** (technical or legal blockers that need real work to clear), **Speculative** (long-horizon, depends on many other things landing first).

| Idea | Rating | Why |
|------|--------|-----|
| Indoor map rendered from a floor plan (Mapbox or Leaflet/OSM) | Likely | Off-the-shelf libraries, well-trodden path. Hardest part is getting the floor-plan data, not the rendering. |
| QR scan opens map at a specific pin | Likely | A static URL with query params solves it. No new tech needed. |
| Pin notes linked to Rank4AI entity records | Likely | Just a schema mapping plus a CMS for tenants. Adds value cheaply. |
| Google Maps indoor publishing | Possible | Programme exists but Google has tightened submissions; may now be invitation-only or restricted to large transit/retail venues. Worth applying for the flagship pilot venue but don't depend on it. |
| Pub-WiFi-style venue sign-up | Likely | Standard SaaS onboarding. The hard part is sales, not engineering. |
| Tenant self-claim of pins | Likely | Mirrors Google Business Profile claim flow. Email-domain or document verification handles it. |
| Sponsored pins / category takeovers | Likely | Standard ad-server logic. Inventory only becomes valuable once we have venue traffic. |
| Route-end / dwell-triggered offers | Possible | Needs reliable indoor positioning and consent. Without good "blue dot" the targeting is too coarse. |
| Auto-enable location on sign-up | Hard (in browser) | Browsers explicitly block programmatic geolocation. The realistic version is "prompt at the right moment with a clear reason." A native app would change this. |
| Cached / offline map experience | Likely | Service workers + Mapbox offline tiles + a small bundle. Standard PWA work. |
| BLE beacons as no-signal fallback | Possible | Hardware cost per venue and ongoing maintenance, but the tech is mature (Eddystone, iBeacon). Worth it for venues with persistent dead zones. |
| App-side anonymous presence heatmap | Possible | Requires enough installed base in-venue to be statistically meaningful. Sparse early data will mislead. |
| Bluetooth scanning of *other people's* phones | Hard | iOS blocks the raw API; Android is tightening; MAC randomisation undermines accuracy; GDPR/PECR exposure is significant. **Probably should not pursue** in this form — venue WiFi analytics or CCTV partnerships are the legal path to the same data. |
| WiFi-analytics integration (Meraki/Aruba/Purple) | Likely | These vendors already expose APIs. Integration work, not invention. |
| CCTV / computer vision footfall integration | Possible | Requires venue to have a vendor in place and to share data. Commercial deal, not a tech blocker. |
| "How busy is it now" pin badge | Possible | Trivial once any one of the footfall sources is wired up. |
| Footfall dataset sold to retailers/landlords | Possible | Existing market (Springboard, Huq, Placer.ai). We'd need either better data, better entity linkage, or a niche they don't cover. |
| Footfall as ground-truth signal sold to AI platforms | Speculative | Conceptually strong and on-thesis for Rank4AI, but depends on (a) a network large enough to matter, (b) a clean privacy story, (c) AI platforms being willing buyers of third-party grounding data. Worth designing for from day one; not worth promising for years. |

---

## Other angles worth thinking about

Things not yet covered in this doc that probably need at least a pass.

**Competitive landscape.** Existing players in indoor mapping include Mapwize (acquired by Engie), Pointr, MazeMap, Situm, Inpixon, Esri ArcGIS Indoors, and Apple's Indoor Maps Program. None of them, to our knowledge, lead with the AI-search-truth-signal angle — that's the wedge. Need a proper teardown of two or three of them before we commit to the build.

**Routing and pathfinding.** Wayfinding inside a building isn't just "show a pin," it's "guide me there from where I am." That means a routing graph (nodes = decision points, edges = walkable segments) per floor, multi-floor traversal via lifts/escalators/stairs, and accessibility-aware variants (step-free, sensory-friendly). Non-trivial data work and the thing that makes the product actually useful versus a static directory.

**Indoor positioning options beyond GPS.** GPS doesn't work indoors. Options to consider: BLE beacons (cheap, mature), UWB (very accurate, expensive, narrow device support), geomagnetic fingerprinting (IndoorAtlas), visual positioning via phone camera (Google's VPS, ARCore Geospatial API, Apple ARKit), audio cues. Likely a hybrid stack with QR-anchored "you are here" as the always-available fallback.

**AR overlay.** Google Maps Live View has shifted user expectations — point your phone down a corridor and see arrows on the floor. Very compelling demo, very hard to ship reliably indoors without VPS. Probably a v3+ feature, but worth knowing the tech stack early so we don't paint ourselves into a corner.

**Venue types beyond shopping centres.** The same product applies to airports, hospitals, universities, museums, conference centres, stadiums, theme parks, large hotels, train stations, exhibition halls. Hospitals are a particularly painful wayfinding problem with real human cost — often cited as the *highest-value* indoor wayfinding market because patients arriving stressed and lost is a measurable problem. Worth ranking these by pain, willingness to pay, and footfall quality for the AI-signal play.

**Emergency and safety use case.** Floor plans + pin metadata + real-time presence is one short step from "fire evacuation routing" or "show staff where a missing child was last scanned." Strong PR story, regulatory complexity, and meaningful product responsibility (if we route someone wrong in a fire we own that). Worth a separate think.

**Accessibility as a first-class feature, not a bolt-on.** Step-free routing, screen-reader-compatible map UI, audio descriptions of routes for visually impaired visitors, sensory-friendly hours (lighting, noise), Changing Places toilet listings. UK Equality Act and EU Accessibility Act 2025 both apply. Building this in from v1 costs little; retrofitting it costs a lot.

**Internationalisation.** Lakeside has international visitors. Venues like Westfield, airports and museums even more so. Notes, search, voice prompts and pin metadata need language coverage. Translation cost is real — auto-translation plus tenant overrides is probably the right pattern.

**Personalisation and return visitors.** A returning visitor could see their last destination, their favourites, "shops new since you last visited." Builds stickiness and improves the footfall signal over time.

**Loyalty and gamification.** "Visit five participating shops, get a discount" mechanics drive footfall (good for tenants, good for our data quality). Stamp-card style. Same plumbing also supports treasure hunts, child-friendly venue events, etc.

**API / SDK for tenants and developers.** Once entity records exist, third parties (the tenants' own websites, third-party apps) might want to embed "find us in Lakeside" widgets or programmatically read footfall. An API turns the platform into ecosystem rather than a closed app.

**Data quality and maintenance.** Floor plans go stale fast — shops move, units get refitted, signage changes. Need a process (and probably a paid role at the venue) for keeping the map current. This is what kills most indoor mapping deployments.

**Liability and insurance.** Wayfinding errors in normal use are embarrassing; in emergencies they're dangerous. Need clear T&Cs, appropriate insurance, and probably explicit "this is wayfinding guidance, not safety-critical instruction" disclaimers around emergency routing.

**Branding and white-label.** Does Lakeside want a "Lakeside Map" experience or a generic third-party one? Likely the former. Means the platform has to support per-venue theming (logo, colours, voice, even URL like `map.lakeside.co.uk`) without forking the codebase.

**Data partnerships.** OpenStreetMap is a community — contributing back the indoor data we capture both improves the global map and creates a defensible "we are the largest contributor of indoor OSM data" position. Mapbox, Apple Maps (Indoor Maps Program) and Google Maps all also accept floor-plan submissions. Where we publish what is a strategic choice, not a technical one.

**Privacy posture as marketing.** If the bigger thesis is footfall-as-truth-signal, then being visibly the *most privacy-respecting* operator in the space is a moat. Public-facing privacy white paper, k-anonymity guarantees, opt-out flows and ICO engagement from day one. This is cheap to do and expensive to retrofit.

**Scale economics.** Going from 1 venue to 100 changes everything: floor-plan onboarding pipeline, support, ad sales, data infrastructure. The architecture needs to be multi-tenant from the first line of code, even if commercially we're selling one venue at a time.
