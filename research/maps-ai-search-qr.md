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

---

## Inclusive design: families, mobility, age, neurodiversity

Wayfinding is hardest for the people who need it most. Most existing indoor maps treat "accessibility" as a synonym for "step-free routing" and stop there. There is a real product opportunity in going much further.

**Families with buggies / pushchairs.** Lifts (not stairs or escalators), wide aisles, baby-changing facilities, breastfeeding rooms, family toilets, kids' play zones, microwaves for warming food. A "family mode" route filter that prefers buggy-friendly paths and surfaces these facilities on the map.

**Young children.** Big-tap targets, cartoon-style icons for shops kids care about (toy shops, sweet shops, soft play), a "where's the toilet" panic button that's one tap from the home view, lost-child reunification flow (scan the QR on a wristband or sign and it shows the venue's lost-child meeting point and notifies guest services).

**Older visitors.** Larger default font, higher-contrast theme, simpler language, fewer clicks to get to the basics (toilet, exit, café, lift). Seating-along-route filter ("rest every 50m"). Slow-walk routing that prefers shorter, easier paths over the absolute shortest.

**Mobility / disability.** Step-free routing as a hard requirement, not a toggle hidden in settings. Accessible toilets (Changing Places where available), Blue Badge parking, wheelchair hire locations, hearing-loop-equipped tills, BSL-supported counters. Honest path information — "this lift is out of service today" — sourced from venue ops in real time.

**Sensory / autism / ADHD / cognitive load.** This is the most under-served group and the easiest one to differentiate on:

- **Quiet hours / quiet zones** — surface the venue's sensory-friendly hours and show low-stimulation routes (avoiding atria with loud music, busy food courts, escalators).
- **Predictability** — show what to expect at each step ("you will go through automatic doors, then turn right past a fountain"). For autistic visitors especially, predictability reduces anxiety.
- **Sensory map layer** — toggle that overlays noise, light, smell and crowd levels per zone, sourced from venue data + footfall + audio sensors where available.
- **Reduced clutter mode** — a stripped-down map UI with one route, one big arrow, no ads, no popups. ADHD-friendly default.
- **Predictable language** — short sentences, no metaphors, no jargon. Important for autistic readers and for non-native English speakers (overlap with internationalisation).
- **Communication cards / visual schedules** — pre-built "I am going to Lakeside today" social stories that families can print or load before the visit.
- **Calm rooms / sensory rooms** — surface where they are; many large venues now have them but nobody knows.
- **Crowd avoidance routing** — combine footfall data with route choice so a visitor can ask for the *quietest* path, not the shortest.

This isn't just inclusive design as ethics (though that matters). It's a real commercial wedge:

- Roughly 1 in 7 people are neurodivergent. Families with autistic or ADHD members frequently *avoid* large venues because they're overwhelming. A venue that solves this gets a measurable footfall uplift.
- Charities and advocacy groups (National Autistic Society, Mencap, Scope, Mumsnet) are powerful distribution and validation channels.
- Several UK shopping centres already run "quiet hours" but don't promote them well; the map becomes the canonical place these are surfaced.
- Maps to AI search: structured data about *who a venue serves well* feeds into the Rank4AI entity graph and changes which queries the venue gets recommended for ("autism-friendly shopping centre near Essex").

This deserves its own working group with input from disabled and neurodivergent users, not just an internal opinion about what they need.

---

## What is actually new here?

Honest question, honest answer.

**Indoor mapping itself is not new.** Mapwize, Pointr, MazeMap, Situm, Inpixon, Esri ArcGIS Indoors and Apple's Indoor Maps Program have been doing some version of this for years. Most enterprise venues that wanted indoor maps already have them. So what's different?

The defensible novelty is not the map. It's the stack the map sits inside:

1. **AI search linkage.** No competitor in the indoor-mapping space is connecting venue and tenant entities into an AI-search optimisation framework. The map isn't the product — it's a structured data feed for the Rank4AI graph. Each pin is also a Rank4AI entity, with consistent identity language across the venue, the tenant's site, and external listings. That makes it cite-able by AI platforms in a way pure indoor maps aren't.

2. **QR-to-web, no app install.** The incumbents mostly ship SDKs that get embedded inside the venue's own native app, or they ship their own app. Both add friction. Scan-a-QR-and-it-just-works is a real UX gap — and meaningfully cheaper for venues that don't want to maintain a native app.

3. **Footfall as a ground-truth signal for AI platforms.** Placer.ai, Springboard and Huq sell footfall to retailers and landlords. None of them sell it as **AI grounding data** to OpenAI, Anthropic, Google or Perplexity. That's the long-game wedge and it only exists because we're sitting at the intersection of indoor data + AI search expertise.

4. **Inclusive design as a first-class product line, not a checkbox.** Sensory-friendly routing, neurodivergence-aware UX, family-mode, age-aware defaults. Most indoor map vendors do step-free and stop. There's a clear, under-served audience here.

5. **Privacy-first by construction.** Most footfall vendors are dragging legacy MAC-tracking baggage. Starting fresh with consent-based capture, k-anonymity and a public privacy stance is a moat both for selling to AI platforms (who need defensible data sources) and for venue trust.

6. **Bundled with a methodology, not sold as a tool.** Rank4AI is already a framework with an audit and a strategic narrative. The map plugs into that as one more signal layer (Ecosystem Validation + Signal Consistency, mostly). We're not selling a map; we're selling AI visibility, and the map happens to be the most defensible signal in the stack.

What this means in practice:
- Don't compete head-on with Pointr/Mapwize for "best indoor map." That fight is lost on day one — they have years of head start, deep enterprise relationships, and better positioning tech.
- Compete on the slice they don't cover: scan-to-web access, AI search linkage, neurodivergent-friendly UX, and footfall productised as AI training/grounding data.
- Pitch to venues as: "you get a low-friction indoor map *plus* your tenants become more visible in ChatGPT, Gemini and Perplexity."
- Pitch to AI platforms (later, much later) as: "ground-truth, consent-based, real-world activity data for the venues and businesses your users ask about."

What we should *not* pretend is new:
- The map itself.
- Indoor wayfinding as a category.
- Footfall analytics as a category.
- Sensory-friendly hours as a venue concept (lots of venues already have them — they just don't surface them well).

Honest summary: this is a re-bundling of well-understood components into a new product wedge — the AI-search angle and the inclusive-design angle are the two genuine differentiators; everything else is execution.

---

## Competitor gap analysis: what they have that we don't

Splitting this two ways, because the project is really two products stacked on top of each other.

### A. Entry point: the indoor map / wayfinding product

Reference set: Mapwize (Engie), Pointr, MazeMap, Situm, Inpixon, Esri ArcGIS Indoors, Apple Indoor Maps Program, Google Maps Indoor.

What they have that we don't:

- **Real "blue dot" indoor positioning.** Mature stacks using BLE beacons, UWB, magnetic-fingerprinting and visual positioning. Pointr's flagship is sub-metre indoor location. We start from QR-anchored "you are here" which is materially weaker.
- **Multi-floor routing engines.** Years of work on pathfinding through lifts, escalators, stairs, secured doors, with accessible variants. Non-trivial to replicate.
- **CAD / BIM ingestion pipelines.** Tooling to import architectural drawings, stitch floors, generate vector tiles automatically. We'd be hand-tracing floors initially.
- **Native SDKs for iOS and Android.** Venues that already have a native app embed their SDK rather than send users to a web page.
- **Enterprise sales motion.** Already inside airports, hospitals, universities, large retail. Multi-year contracts, procurement relationships, reference customers.
- **Compliance certifications.** SOC 2, ISO 27001, HIPAA-readiness. Required for hospital and government procurement; takes 12–18 months to earn from scratch.
- **3D / extruded floor visualisations and AR Live View.** Pointr and Esri both ship AR overlays. Visual polish that wins demos.
- **Asset tracking adjacencies.** Hospitals track equipment, warehouses track inventory using the same beacon network. Big deal-expansion lever we don't have.
- **Apple Indoor Maps Program and Google Indoor accreditation.** Direct relationships with the platform owners.
- **Localisation out of the box.** Multi-language UX, RTL support, regional formats.
- **Network-deployment services.** They send engineers to install and calibrate beacon networks. We'd need a partner.
- **Years of operational data.** Crash reports, edge cases, accessibility refinements they've already learned.

What we have that they mostly don't:

- Scan-a-QR-to-web access without an app install.
- Inclusive design as a product line, not a setting.
- The Rank4AI entity linkage on every pin.
- A clean privacy posture (no legacy MAC-tracking baggage).

Honest take: **on pure indoor mapping we are years behind**. The right move is not to compete head-on. The right move is to be "good enough" on the map and win on what sits behind it.

### B. AI search side

This is where it gets interesting, and where the real product lives.

Two distinct things are bundled in "AI search" and they need to be separated:

#### B1. Per-venue / per-tenant AI visibility (today)

The Rank4AI framework already does this for businesses generally — make each entity (venue, shop, service) clearly described, structurally consistent and externally validated so AI platforms recommend it confidently.

What competitors offer:
- **Conventional SEO agencies** — still optimising for blue links, mostly weak on AI search.
- **Emerging AI search / GEO (Generative Engine Optimisation) agencies** — Profound, Otterly, AthenaHQ, Peec AI, Goodie AI. They focus on monitoring brand mentions in LLM answers and reverse-engineering which signals drive inclusion.
- **Schema / structured-data tools** — Schema App, Yoast.

What they don't offer:
- A physical-space data pipeline feeding the entity graph (this is where the indoor map plugs in).
- A footfall-derived authority signal.
- A consolidated five-signal model with a measurable audit (Rank4AI's existing edge).

#### B2. Sub-project: aggregated real-world data sold to AI platforms (the long game)

This is the question you asked directly. **Yes — that is the play, and the framing is right.**

**The thesis, stated plainly:**

AI platforms today ground their answers about places, businesses and entities almost entirely on **online signals**:
- Web content (pages, blog posts, news).
- Reviews (Google, Yelp, Trustpilot).
- Structured data (schema.org, Wikidata, Google Knowledge Graph).
- Citations and backlinks.
- Social media activity.

Every one of these signals is **manipulable at scale** — that's why SEO and reputation management exist as industries. AI platforms know this, and are actively hunting for harder-to-fake grounding sources because hallucinated or manipulated answers are their single biggest credibility risk.

**Real-world behaviour** — actual humans physically going to a place, spending time there, coming back — is the truth signal that no amount of online manipulation can fake. Footfall is offline, observed, costly to forge.

The play, in one sentence: **aggregate footfall and dwell-time data from many indoor venues, attach it to Rank4AI entity records, and license the resulting feed to AI platforms as a grounding signal — so that "what places to recommend" decisions stop being purely online-traffic-based and start incorporating offline reality.**

Concretely, an AI platform asking "is Acme Coffee in Lakeside actually a real, popular, currently-trading place" today triangulates from Google reviews, the company's website, and maybe a news mention. With our feed they'd also know: 4,200 unique visits last week, average dwell 12 minutes, returning-visitor rate 22%. That is a fundamentally different class of evidence.

**Who already plays in this space — and the gap:**

- **Placer.ai** — large US-focused footfall dataset, sold to retailers, landlords, real-estate analysts. **Not packaged for AI grounding.**
- **SafeGraph** — POI metadata + foot traffic, mostly US, sold to data scientists and advertisers. **Not packaged for AI grounding.**
- **Springboard** — UK retail footfall, sold to landlords and councils for trend reports. **Not packaged for AI grounding.**
- **Huq** — location intelligence in UK/EU, sold to councils, planners, brands. **Not packaged for AI grounding.**
- **Cuebiq, Outlogic (formerly X-Mode)** — historical SDK-based footfall, regulatory pressure mounting, sold mostly to ad-tech and finance. **Not packaged for AI grounding.**
- **Google, Apple, Meta** — have their own footfall data via their OS/apps, use it internally. **Don't sell it.**

The white space is genuinely empty: nobody is selling footfall as **structured grounding data for LLMs**, formatted to slot into an entity graph, with a clean consent story, sold under contracts that AI platforms can defend in regulatory hearings.

**Why us, why now:**

- We're already operating in the AI search world via Rank4AI — we understand what AI platforms need as grounding input, not just as marketing analytics.
- The indoor-map product gives us a legitimate, consent-based collection mechanism — visitors actively open the map, so capture is opted-in by design.
- Aggregation across many venue types (retail, hospitality, transit, healthcare, education) gives entity coverage no single-vertical incumbent has.
- Privacy-first construction lets us sell to AI platforms who increasingly need defensible data sourcing.

**The map, viewed this way, is not the product — it's the data-collection wedge.** Same playbook as Waze (gave away navigation, sold the traffic data) or Foursquare (gave away check-ins, sold the venue data). The user-facing app is the collection layer; the licensable dataset is the business.

**What we need to figure out before betting on this:**

1. **Demand validation.** Do AI platforms actually want to buy real-world grounding data, or do they assume their own users' implicit signals (clicks, follow-ups, satisfaction ratings) are enough? This needs direct conversations with people inside OpenAI / Anthropic / Google / Perplexity grounding teams. Cheap to investigate.
2. **Coverage threshold.** How many venues / how much of the UK and EU do we need before the dataset is interesting? Probably hundreds of venues, not tens. Long road.
3. **Pricing model.** Per-query? Per-entity-record? Annual licence? Revenue share with venues?
4. **Exclusivity vs. universal.** Selling to one AI platform exclusively gets a higher price but caps the ceiling. Selling to all of them commoditises faster but maximises spread. Probably non-exclusive with tiered access.
5. **Privacy posture.** Has to be aggregated, anonymised, k-anonymous from day one. Any individual-level data sales kill the product.
6. **Regulatory tailwinds and headwinds.** Incoming EU AI Act provisions on data sourcing actually help us — they push AI platforms toward documented, consent-based grounding data. ePrivacy and PECR push us toward stricter consent collection.

**Probable shape of the product offered to AI platforms:**

- A bulk feed (probably daily / weekly) keyed on stable entity IDs that map to Wikidata / Google KG / company registries.
- Each record contains: aggregated visit count, dwell distribution, returning-visitor rate, peak-hour profile, neighbour-entity co-visit pattern, change-vs-previous-period, freshness timestamp.
- A live API for grounding-time lookups against specific entities.
- A documented consent and privacy model attached to the contract.
- An attestation that data is k-anonymous above a published threshold.

That feed becomes a **structured truth layer for AI search** — directly answering your question. Yes, the play is to take footfall from many places and migrate it into the AI search world, which today is mostly online-only, to give those platforms the offline reality their answers currently lack.

**The summary of summaries:** Pointr et al. sell wayfinding to venues. Placer et al. sell footfall to retailers. Nobody sells offline reality as a grounding signal to AI platforms. That's the wedge. The map is how we earn the right to collect the data. The data is the actual product.

---

## Data source comparison: why per-device beats per-transaction

Worth thinking about how our footfall data compares to other "real-world signals" already on the market — particularly card-transaction data, which a few firms already sell.

### Existing real-world data sources

- **Card transaction data.** Mastercard SpendingPulse, Visa Spend Analytics, Fable Data, Consumer Edge, Facteus, Earnest. Aggregated card-spend feeds sold to retailers, hedge funds and economists.
- **Open banking data.** Plaid, TrueLayer, Tink — transaction-level data with the consumer's consent.
- **Loyalty schemes.** Tesco Clubcard, Nectar, John Lewis, Pret Club. Per-customer purchasing history within a single retailer.
- **Mobile-SDK footfall.** Placer, SafeGraph, Cuebiq, Outlogic — passive location pings from SDKs embedded in third-party apps.
- **WiFi probe analytics.** Cisco Meraki, Aruba, Purple — venue-side counting of nearby devices.
- **CCTV / computer vision.** Hoxton Analytics, V-Count, RetailNext — head-counting from cameras.

### The party-size problem

Card transaction data has a structural under-counting problem that's exactly what you spotted:

- A family of four walks into Lakeside, has lunch, buys clothes for the kids, leaves. Card data sees **one cardholder** (probably the parent who paid). Spend is counted, but the *humans-in-venue* count is one.
- Loyalty schemes have the same flaw — one Clubcard, four people.
- Even worse: card data only registers the visit *if* a purchase happened. A family that browses and leaves is invisible to card-based footfall entirely.

This is the gap. Card data measures *spending*. Footfall measures *presence*. AI platforms answering "is this place actually busy / loved / used by real people" need presence, not just spend.

### How per-device footfall fixes this

If each member of a family has the map open on their own phone, that's four presence signals, not one. Specifically:

- **Better party-size reality.** Four phones in a venue at the same time, moving on the same path, with similar dwell, is detectable as a *group* — and counted as four humans, not one cardholder.
- **Browsing visits count.** Presence is recorded whether or not anyone spends a penny. That captures the long pre-purchase journey AI platforms care about ("is this place worth visiting" not just "did someone buy something").
- **Visit duration is real.** Card data gives a single timestamp at point of sale. Phone presence gives arrival, dwell, route, departure. Far richer.
- **Cross-tenant journeys are visible.** Card data per merchant is siloed. Phone-based data sees the whole route through the venue, including the shops people *didn't* buy from.

### Caveats — and why the dataset still has to be careful

Per-device isn't perfect either. We need to be honest about its limits when pitching it as a grounding signal:

- **Not everyone has the app open.** A family of four might have one phone with the map open and three without. Coverage is partial unless the venue strongly nudges scans (signage at the entrance, free WiFi gated through the map, loyalty perks for using it).
- **Children often don't have phones.** Under-12s are largely invisible to phone-based capture. Family-targeted venues will under-count for this reason.
- **One person carrying multiple devices.** A single visitor with a phone + tablet + smartwatch could be counted as three. MAC randomisation and per-device IDs make de-duplication non-trivial.
- **Selection bias.** People who scan the map skew younger, more digitally engaged, more curious. The data needs weighting before it's a fair sample of "everyone who visited."
- **Occasional vs frequent visitors.** A regular who never opens the map looks identical to a no-show. Hardware-side capture (WiFi probes, CCTV) catches these; app-side capture misses them.

### The right architecture: blend the sources

The cleanest grounding signal isn't pure phone-based or pure card-based — it's blended:

- **Phone-based map presence** for granular per-person dwell and route data, and to count the children/non-payers card data misses.
- **WiFi-probe or CCTV counts** as a venue-wide ground-truth check on totals, regardless of app adoption.
- **Aggregated card-spend** as a separate signal that says "of the people who came, how much did they spend" — useful for tenant-level economics.
- **Loyalty data** where venues will share it, for repeat-visitor patterns.

Each source corrects the others' blind spots. AI platforms don't want a single noisy feed; they want a documented, multi-source signal with known coverage characteristics. That's the product.

**Implication for the pitch to venues:** the more visitors using the map, the better *every* signal becomes — and the more valuable the venue's slice of the AI-grounding dataset. That gives venues a direct incentive to drive scan rates (signage, WiFi gating, loyalty integration) rather than treat the map as a passive amenity.

**Implication for the pitch to AI platforms:** "we have *N* venues, *X* million presences per month, blended with WiFi/CCTV ground truth and reconciled against card-spend totals where available." That sentence is harder to refuse than "we have phone pings."

You're right that a family of four with four maps open is four hits, and right that card data wouldn't catch that. The real win is that no single existing data source catches it — and a blended pipeline does.

---

## Location, geo, and digital footprints: collection and entity matching

The earlier sections framed the *why*. This section is the *how*: what data we can actually capture, how we tie it to a specific physical place, how we sell that to OpenAI, and how we bring retailers along.

### Sources of location and digital-footprint data

Ordered roughly from easiest-to-collect to hardest:

- **Map-app presence.** Every time a visitor opens the venue map, we know the venue, the device, and (with permission) the indoor position. Strongest source we own outright.
- **GPS / coarse phone location.** Standard browser/native API, accurate to ~5–10m outdoors, mostly useless indoors. Good for arrival/departure detection at the venue boundary.
- **BLE beacon proximity.** Sub-metre indoor positioning when our beacons are deployed and the visitor's phone has Bluetooth on. Works without internet, fast, cheap, mature.
- **WiFi access-point triangulation.** When a phone is connected to the venue WiFi, the access points already know where it is. Cisco Meraki, Aruba and Purple expose this via API. Cost: needs a deal with the venue's network owner.
- **WiFi probe requests (passive scanning of nearby phones).** Historically used to count devices regardless of app or association. Largely killed by MAC randomisation on iOS/Android — modern probe data is noisy and counts shadows. Don't build on this.
- **Cell-tower / carrier data.** Telefonica Tech, Vodafone Analytics, EE/BT sell aggregated mobility derived from the cellular network. Coarse (100m–1km), but covers everyone with a phone, no app needed. Buy, don't build.
- **IP geolocation.** Useful for "what region is this user in" online, useless for "which shop are they in." Edge case only.
- **Mobile advertising IDs (IDFA / GAID).** Apple's App Tracking Transparency (ATT) and Google's Privacy Sandbox have killed this for new entrants. Don't build on this either.
- **Connected car data.** Otonomo, Wejo, Geotab — carpark arrival times by vehicle, useful for venue-arrival signal but not in-venue movement.
- **Camera-derived counts.** Hoxton Analytics, V-Count, RetailNext, Brickstream — venue-side counters, often already deployed at the entrance.
- **Card and open-banking transactions.** Covered above. Joins to time and merchant, not to in-venue movement.
- **Loyalty / receipt data.** Tesco Clubcard, Pret Club, retailer apps. Per-customer purchase history, retailer-by-retailer.
- **Wider digital footprints (search and review).** Google Trends per locality, Maps reviews, TripAdvisor mentions, social posts geotagged or text-tagged with the venue. All scrapable to varying degrees, all noisy. Useful as supplementary signal.

The defensible mix for our project: **map presence + BLE beacons + venue WiFi analytics + camera counts at entrances + carrier data for venue-level arrivals**. Each layer covers a blind spot in the others.

### Matching captured data to a specific place

The collection above gives us "device X was here at time T." To make that valuable we need to attach it to a real entity (the H&M at Lakeside, not just "somewhere in Essex"). Three layers:

1. **Polygon per unit.** From the indoor map we already have a GeoJSON polygon for every shop, facility and corridor. A position fix that falls inside the polygon = a presence in that unit.
2. **Entity link per polygon.** Each polygon carries a stable `entity_id` that resolves to:
   - The local trading entity (the specific H&M store at Lakeside).
   - The brand parent (H&M Hennes & Mauritz UK Ltd).
   - The global brand (H&M, Wikidata Q188326).
   - The Rank4AI entity record with all five-signal attributes attached.
3. **External cross-references.** Each entity record links out to Companies House, Wikidata, Google Knowledge Graph, the brand's own URL. This is what makes the data joinable for a buyer like OpenAI — they don't have to trust our IDs, they can pivot through theirs.

With all three in place, a query like "how many people were in H&M Lakeside between 2pm and 3pm last Saturday" becomes a straightforward count of distinct devices observed inside that polygon during that window, deduplicated, weighted for app-adoption coverage, and rolled up to the entity.

The same pipeline supports brand-level aggregation: "across our network, how many people visited any H&M last week, average dwell, peak day." That's the product OpenAI cares about — not single-store, but the whole brand footprint.

### Selling it to OpenAI (and the rest)

OpenAI has already shown they will pay for real-world data when it improves grounding: AP, Le Monde, Reddit, Stack Overflow, Financial Times, News Corp, Axel Springer, Time, Vox, Condé Nast — all signed in 2024–2025. The pattern is consistent: **content or data that reduces hallucination and improves answer quality on questions ChatGPT users actually ask**.

Why this fits that pattern:
- Place / shopping / "where should I" queries are a high-volume ChatGPT use case.
- Today the model grounds those answers on web content alone, which is stale, manipulable and silent on whether a place is actually busy or trading.
- Our feed gives a *recency* signal and a *real-people-actually-go-there* signal that no web page contains.
- Same product also serves Google AI Overviews, Gemini, Anthropic Claude, Perplexity, Copilot, Mistral, Meta AI. Don't sell exclusively unless the price is genuinely once-in-a-decade.

Sales motion to OpenAI specifically:
- **Entry route:** OpenAI Data Partnerships team (publicly listed contact). Anthropic has the same. Google has internal teams. Perplexity is the smallest and might move fastest.
- **Pitch in one sentence:** "You ground place and recommendation answers on stale web content. We give you weekly, consent-based, k-anonymous real-world presence data on UK and EU venues, mapped to entities you already use."
- **Demo asset:** a side-by-side eval. Take 100 ChatGPT prompts about UK retail destinations. Show baseline answers. Show answers when our feed is injected as context. Measure factuality, recency, recommendation accuracy. If the lift is meaningful, the deal sells itself; if it isn't, we don't have a product.
- **Commercial shapes that map to existing OpenAI deals:**
  - Bulk feed licence: annual, tiered by entity coverage (e.g. £500k–£5M/year depending on scale and exclusivity).
  - API access: per-query pricing for grounding-time lookup.
  - Hybrid: bulk for training-style use plus API for live grounding.
- **Term length:** OpenAI's data deals tend to be 2–5 years. Shorter is better for us until we know what the data is worth.
- **Delivery format:** standardised JSON feed keyed by stable entity IDs, with documented schemas. Probably the same shape as a knowledge-graph delta. They will not accept bespoke formats at any scale.

Things they'll push back on:
- **Provenance.** Where did each data point come from, who consented, under what legal basis. Need a public privacy paper before the conversation starts.
- **Coverage.** "How many UK venues, what fraction of UK retail footfall do you see, what's the lag." If the answer is "12 venues" the deal stalls. Below a coverage threshold this is a research project, not a product.
- **Bias and representativeness.** Skews to digitally-engaged visitors. Need to disclose and ideally weight against ground-truth (camera/WiFi totals).
- **Refresh cadence.** Daily is the right target. Weekly is acceptable. Monthly is too slow for grounding.
- **Exclusivity.** They will ask. The right answer is "not exclusive, but you get first-look on new entity types and the lowest-latency feed."

Things in our favour:
- The Rank4AI brand and existing methodology give us a credible story for *why* this dataset exists in the form it does, rather than being a re-skin of a bought-in feed.
- Our consent story (visitors actively scan a QR to open the map) is materially cleaner than the legacy mobile-SDK industry's.
- The framing — "ground-truth offline reality for AI search" — is a category that doesn't exist yet, which means we name it.

### Getting buy-in from retailers, in stages

Retailers are not the buyers — AI platforms are. But retailers have to consent, contribute or at least not block the data flow that makes the product. The plan to bring them along is staged.

**Stage 1: Landlords first, retailers passive.** The first deals are with venue owners (Lakeside, Westfield, Bluewater, large hospitals, airports). The landlord pays for the indoor map. Retailers inside benefit by default — their pin appears on the map, their entity record gets surfaced. We capture footfall as a side effect of the map operating. No retailer signature required at this stage because the data we capture is venue-aggregate and tenant-aggregate, not retailer-specific.

**Stage 2: Retailer claim-and-enrich.** Like Google Business Profile claiming. The H&M store manager (or H&M head office) claims their pin, gets a free dashboard showing their store's visits, dwell, peak hours, returning-visitor rate. Hook: "you can already see this data for your own store, free." Many retailers will sign up just for the analytics — that's the wedge.

**Stage 3: Brand-level deals.** Once enough individual stores in a chain are using the dashboard, approach the head office (H&M UK, Boots, Greggs, JD Sports). Pitch:
- A consolidated dashboard across every UK store in our network.
- Better AI search visibility — their stores get cited more often in ChatGPT/Gemini answers when our signal feeds the platforms.
- Crowd-aware advertising — push offers when their stores are quiet, don't compete with peak-hour traffic.
- Sponsored placements within the indoor maps.
- Optional: brand-level enrichment (richer entity descriptions, evidence of stocked categories) feeds back into the AI-search side.

**Stage 4: Consortium model.** Once 50+ retailers are in, formalise it as a consortium dataset — like NielsenIQ for retail. Members contribute (consent to aggregation) and consume (analytics + AI visibility). Members get more value from being in than out. That tips the market.

**What retailers will rightly worry about:**
- Their competitors seeing their numbers. Mitigation: aggregation thresholds, k-anonymity, no individual-store data exposed to other retailers.
- Their data being used against them in landlord rent negotiations. Mitigation: contractual firewalls between landlord-side and retailer-side products.
- Loyalty and CRM data leaking. Mitigation: never ingest this without an explicit per-deal data agreement, and never re-export.
- Customer trust. Mitigation: they need to be able to point to our public privacy posture and feel comfortable putting their brand alongside it.

**Carrots in priority order:**
1. Free analytics dashboard for their own stores.
2. Better AI search visibility (this is genuinely valuable and growing in importance).
3. Crowd-aware ad inventory at favourable rates for participants.
4. Anonymised competitive benchmarks ("you are in the top 25% of fashion retailers for dwell time in this venue").
5. Co-marketing on inclusive design (autism-friendly hours, family-mode) — many retailers want to lead here but lack the platform.

**Sticks, used carefully:**
- Once enough of a category is in, late entrants are visibly missing from AI answers. That's a real cost we don't have to manufacture.
- We never go straight to "your competitor is using us" pressure tactics with retailers we're trying to bring along — that breaks trust faster than it closes deals.

### So is the real customer OpenAI?

Probably yes, in revenue terms — and you're right to sense that.

- Venues and retailers are the *operational* customers. They pay for the map, contribute the data, get tactical value from analytics.
- AI platforms are the *strategic* customer. They pay for the aggregated, mapped-to-entity, refreshed feed and that's the contract that scales.
- A reasonable revenue split, three years out, might look like: 60–70% from AI-platform data licensing, 20–30% from venue SaaS, 10% from advertising.
- Day one is the inverse — close to 100% from venue SaaS, because the AI deal needs coverage to exist before it can be sold.

Build for the venue customer. Build the data architecture for the AI customer. Don't pretend either is optional.
