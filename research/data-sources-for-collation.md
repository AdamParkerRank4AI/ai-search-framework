# Data sources for collating an area, to build a working map and feed

A scratchpad of every accessible data source we could blend to build a working "show one area, real numbers, real day" prototype, plus links and notes on access. Use this as the working list when actually trying to assemble a test for a specific area like Lakeside or a single high street.

Updated: April 2026.

---

## 1. Map base layer (the canvas)

These give us the visual map of the area to render against. Free or near-free.

- **OpenStreetMap (OSM).** Fully open, community-edited, includes some indoor data via Simple Indoor Tagging schema. Pull via Overpass API or download regional extracts. Lakeside's outdoor footprint and parts of its interior are already mapped.
- **Mapbox.** Free tier covers 50,000 map loads per month. Polished tiles, vector data, full SDK ecosystem. Probably the right choice for the prototype because of the developer tooling.
- **Apple MapKit JS.** Free for Apple developers, browser-renderable.
- **Google Maps Platform.** Generous free tier ($200/month credit), tightest rate limits to monitor.
- **Ordnance Survey (UK).** OS Maps API has free tier for non-commercial use. Higher quality for UK-specific deployments.

---

## 2. Outdoor presence and footfall data (people in the area)

The bulk of what we'd licence or scrape for a one-area test.

### Mobile carrier flow data
Coarse spatial precision (50m to 1km) but real coverage of every phone on that network. Sold aggregated only.

- **Vodafone Analytics.** UK ~20% of subscribers. Mobility insights, footfall, origin-destination, dwell, demographic estimates.
- **O2 Motion (Telefonica Tech).** UK ~25%. Same shape.
- **BT/EE mobility insights.** UK ~25%. Less heavily marketed but exists via BT's enterprise data team.
- **Three UK.** UK ~12%. Smaller mobility offering.

To approximate national coverage you'd need at least three of these. Each one alone covers roughly a quarter to a third of phones.

### Mapbox Movement
- **What it is.** Aggregated mobile device density, activity and movement, drawn from 700M+ MAUs across 45,000 apps with the Mapbox SDK embedded. 20B+ daily live location updates. 100m tile resolution and admin boundary aggregation.
- **Access.** Paid licence via Mapbox sales contact, no self-serve. https://www.mapbox.com/movement-data
- **Strategic note.** Mapbox is partnered with OpenAI (Mapbox maps are now in ChatGPT search, since Nov 2024). They have the closest thing to ready-made AI-grounding-data raw material. They haven't packaged it for that use case yet. This is both an opportunity (partner) and a threat (they could pivot first).

### Other mobility / footfall vendors
- **Placer.ai.** US-focused but has UK data. Sample-based, sold to retail planners. https://www.placer.ai
- **Foursquare Movement APIs.** POI-anchored visit data. Paid. Sample-based.
- **Huq Industries.** UK and EU, council and planner focus. https://huq.io
- **Springboard.** UK retail footfall, mostly venue-camera based. https://www.spring-board.info
- **Mytraffic.** France/UK retail mobility analytics.
- **Quadrant.** Anonymised mobile location panels, hundreds of millions of devices, tens of billions of monthly events. https://www.quadrant.io
- **Geolytix.** UK retail intelligence, includes mobility layers.
- **CACI.** UK location data products including mobility.
- **Blis.** UK-founded (2004, now part of T-Ads), operates in 40+ markets. Strictly a programmatic advertising DSP rather than a raw-data broker — they use location plus behavioural and lifestyle signals to target ads for brands like Unilever, Samsung, McDonald's, HSBC. "Privacy-first location-powered" positioning post-cookies, and recently launched Blis AI for audience planning. Not a likely AI-grounding competitor (different business model, ad-targeting commoditises if data is licensed out) but plausible as a data partner or eventual buyer of an AI-grounding business. https://blis.com

### SDK aggregator brokers (use with caution)
Sample is shrinking under ATT/Privacy Sandbox, regulatory exposure rising.
- **SafeGraph, Veraset, Cuebiq.** US-leaning.
- **Outlogic** (formerly X-Mode). FTC-banned in 2024 from selling sensitive data — avoid.
- **Gravy Analytics.** Major breach early 2025 — avoid.
- **Tamoco, Adsquare, Near, Kochava.** Various, all in the same regulatory uncertainty.

### Vehicle / car probe data (for arrivals to venues)
- **HERE Technologies.** Probe data + traffic API.
- **TomTom.** Traffic Stats and Move products.
- **INRIX.** Traffic and movement intelligence.
- **StreetLight Data** (now part of Jacobs). Origin-destination from probes.

### Real-time tracking SDKs (your own users only)
- **Radar.** Geofencing and location SDK for first-party apps. https://radar.com
- **Unwired Labs.** Cellular/WiFi positioning API for your own devices. https://unwiredlabs.com

These don't give us "who is in this area" — they let us track our own users. Useful if we build a panel or our own consumer app, not as a third-party data source.

---

## 3. Indoor / venue-specific signals

When we want to know about a specific venue rather than a general area.

- **Venue WiFi analytics.** Cisco Meraki, Aruba (HPE), Ruckus, Extreme Networks, Purple WiFi, Cloud4Wi, Tanaza. APIs available where the venue is a customer. Real, complete, ground-truth for that venue.
- **Camera / CV vendors.** Hoxton Analytics, V-Count, RetailNext, Sensormatic/ShopperTrak, Brickstream. Out of scope per the location-only decision but listed for completeness.
- **Bluetooth beacon networks.** Estimote, Kontakt.io, Eddystone-deployed networks if a venue has one.

---

## 4. Public / open / free signals (start here for a prototype)

Free things you can pull right now for a one-area test, no contract required.

- **Google "Popular Times".** Free, public, sample-based, no official API. Scrape via the unofficial `populartimes` Python library for specific POI busyness curves.
- **TfL Open Data Portal.** Free. Station entry/exit counts, bus passenger numbers, road traffic. https://tfl.gov.uk/info-for/open-data-users/
- **National Rail / ORR data portal.** Free. Station footfall by year. https://www.orr.gov.uk/statistics/published-stats/station-usage-estimates
- **ONS mobility data.** Some open mobility datasets, especially Covid-era leftovers.
- **DfT (Department for Transport).** Road traffic counts, public transport stats. Open.
- **Local council open data portals.** Westminster, Manchester, Leeds and others have published carrier-derived footfall in pilot programmes. Worth a search per target area.
- **Geolytix Retail Points.** Free UK retail location dataset (for entity matching, not movement).
- **Companies House.** Free entity data for the businesses themselves.
- **Wikidata.** Free entity data with stable IDs that map to real places.

---

## 5. Booking / event / commerce signals (presence by intent)

Signals that tell us "people are going to / interested in this place" without being raw location data.

- **OpenTable / Resy / Quandoo / Bookatable.** Restaurant booking demand.
- **Eventbrite / Ticketmaster / Skiddle / Fatsoma.** Event ticket sales and demand.
- **Instagram / TikTok / X / Threads geotagged posts.** Social check-ins. Various API access tiers.
- **Foursquare Places.** Free tier of the POI graph plus paid Movement APIs.
- **Yelp / Trustpilot / Google reviews.** Review timestamps as activity proxies.
- **RingGo / JustPark / ParkMobile.** Parking app demand near venues.
- **Just Eat / Deliveroo / Uber Eats.** Open-restaurant signals.

---

## 6. IP-based geolocation (low-precision, fast, cheap)

Useful for online-side context, not for physical footfall.

- **MaxMind GeoIP.** Standard, paid.
- **IP2Location, IPinfo, Gigasheet.** Various.
- **Cloudflare/Vercel/AWS edge data.** Often built into infrastructure free.

Not useful for "who is at Lakeside today" — useful for "where are this venue's website visitors coming from" as a soft demand signal.

---

## What you can buy how

| Pattern | Examples | Speed to access | Cost |
|---------|----------|-----------------|------|
| Free open data | TfL, ONS, Popular Times, OSM, Companies House | Same day | £0 |
| Demo / sample report | Vodafone Analytics, O2 Motion, EE | 1-2 weeks via sales | £0 to low £k |
| Data marketplace one-off | Snowflake, AWS Data Exchange, Datarade | Days to a week | £1k-£5k/month limited scope |
| Annual data licence | Mapbox Movement, Placer, Huq, carrier full | 6-12 weeks procurement | £20k-£100k+ per year |
| API usage-based | Foursquare, HERE, TomTom, Radar | Same day signup | Per-call pricing |
| Re-packaged dashboard | Mytraffic, CACI, Locomizer, BlueDot | Days for trial | £10k-£50k/year |

---

## Suggested collation plan for a one-area test

For a working "show real footfall in one area for one day" demo without committing serious budget:

1. **Pick the area.** Lakeside, a single London tube station catchment, a specific high street.
2. **Pull the free stuff first.** OSM map base, TfL data for nearest station, National Rail, Google Popular Times for every POI in the area. Free. Half a day of work.
3. **Email three carriers** (Vodafone, O2, EE/BT) asking for a sample report on the area for one Saturday. They're used to these requests; expect 1-2 week turnaround. Free if they like the use case, low £k otherwise.
4. **Sign up for Mapbox developer free tier** to render the map and start a Mapbox Movement sales conversation in parallel. They might give a sample tile for the area.
5. **Pull POI data** from Foursquare free tier and Companies House to populate entity records.
6. **Layer everything onto the Mapbox-rendered map** with simple visual encoding (heatmap for tile density, pin for each POI with linked entity record and Popular Times curve).
7. **Take screenshots, package as the demo asset** for the OpenAI / Anthropic / venue conversations.

Total elapsed time: 2-4 weeks. Total cost: £0 to low £k depending on which carrier samples you pay for.

That's a working test of the whole concept on a single real area, before you commit to building the full indoor map or signing any data licences.

---

## Strategic notes worth remembering

**Mapbox is the most uncomfortable competitor.** They have Mapbox Movement (the raw material), an existing OpenAI partnership for the rendering layer, and the engineering capacity to add entity-linking. If they decide to enter the AI-grounding-feed category, they leapfrog us in months. The right move is probably to engage them as a potential partner rather than a competitor early on.

**Quadrant, Placer, Foursquare are all "data exists, packaging missing" players.** Same conclusion as Mapbox — they have the data, they don't sell it as AI grounding. Each is a potential supplier, partner or eventual buyer.

**Carriers are the cleanest path for "real data, fast" testing** in the UK because their products are sold to UK retail planners already, the contracting is established, and the sample-vs-modelled story is straightforward. Mapbox's product is more polished but slower to procure for a non-strategic customer.

**Free public data is enough for the first prototype.** Nothing in step 2 of the collation plan above costs anything. You can have a credible demo before any budget is committed. Use that to validate AI-platform demand before paying for premium feeds.

---

## Market context: what The Markup investigation showed and what's happened since

The Markup published "There's a Multibillion-Dollar Market for Your Phone's Location Data" in September 2021. Useful baseline read but the picture has shifted materially since.

**What the article documented (2021 baseline):**
- Estimated $12 billion market for phone location data.
- 47 companies identified across collectors, aggregators, marketplaces and intelligence firms.
- Major named players: Advan Research, Complementics, Adsquare, Cuebiq, Near, Mobilewalla, X-Mode.
- Scale claims: Near "1.6B people across 44 countries," Mobilewalla "1.9B+ devices, 50B signals daily," X-Mode "25%+ of adult US population monthly."
- Customers: retail, private equity, advertising, government.
- Key critique: users had no meaningful awareness that location data shared with one app was being syndicated through dozens of brokers.

**What has happened to that market since:**
- **April 2021.** Apple App Tracking Transparency rolled out. Most users opted out of cross-app tracking. iOS sample volumes in SDK panels dropped 70-90%.
- **December 2023.** Near Intelligence (Chapter 11 bankruptcy nine months after going public via SPAC). Assets sold to lender Blue Torch in early 2024. FTC ordered deletion of sensitive data.
- **January 2024.** FTC banned X-Mode/Outlogic from selling sensitive location data.
- **Late 2024.** Mobilewalla settled with the FTC for unauthorised collection and sale of location data.
- **2024.** FCC fined US carriers (AT&T, T-Mobile, Verizon, Sprint) approximately $200 million collectively for sharing customer location data without consent.
- **January 2025.** Gravy Analytics suffered a major data breach that leaked their full supply chain, exposed which apps were SDK partners, and triggered widespread enterprise-buyer caution.
- **Ongoing.** Google Privacy Sandbox progressively tightening Android-side data collection.

**Implication for our project:** The 2021 incumbents are materially weaker. Probably 30-50% of those 47 companies are bankrupt, banned, settled, breached, or quietly winding down. Buyers (especially enterprise and government) are increasingly cautious about the category's regulatory exposure. The market is still big but in transition, and AI platforms specifically need data sources that can be defended in front of regulators. Clean-consent operators starting fresh are well-positioned.

The bad news read of the same data: this is a politically and legally sensitive market with active regulator interest. Anything we build needs to be visibly distinct from the SDK-broker model in its consent architecture. "Looks like Outlogic but cleaner" is not enough. Has to be a different model.

---

## Commercial models for buying location data

Useful framing borrowed from a recent prompt response. There are several different things you can mean by "buy location data" and they have different shapes, prices and uses.

**1. Annual data licence for bulk datasets.** What you buy when you want a feed to power analytics or grounding products at scale. Examples: Mapbox Movement, Placer, Foursquare Movement, Quadrant, carrier full extracts, Huq. Procurement: 6-12 weeks, signed contracts, NDAs, £20k-£100k+ per year. This is what we'd buy for a production AI grounding feed.

**2. Usage-based API access.** What you embed in your own app to track your own users with permission. Examples: Radar (geofencing/location SDK), Unwired Labs (cellular/WiFi positioning), Mapbox APIs (geocoding, routing, search). Per-call or per-MAU pricing, sign up online, integrate in days. This is what we'd embed in the indoor map app.

**3. POI / map / traffic APIs.** Standard map service stack. Mapbox, Google Maps Platform, Apple MapKit, HERE, TomTom, Foursquare Places. Tells you *where* places are and what's there. Doesn't tell you who's there. Built into anything that renders a map.

**4. Real-time tracking SDKs.** Radar, Mapbox Vision, geofencing platforms. For tracking *your* users on *your* app. Not third-party data sources.

**5. GeoIP enrichment.** MaxMind, IP2Location, IPinfo, Gigasheet. IP address to rough location. Useful for online analytics, useless for footfall. Country-level is reliable, anything finer is approximate.

**6. Data marketplace one-off purchases.** Snowflake Data Marketplace, AWS Data Exchange, Datarade. Closer to self-serve. Limited geographic scope, monthly subscriptions £1k-£5k. Faster procurement than direct vendor licensing.

The two we'd most likely use in different phases of this project: **#1 for the AI-grounding feed production data, #2 to power our own consumer/venue app.** These are completely different commercial worlds despite both being called "buying location data."

---

## Sources / further reading

- The Markup, "There's a Multibillion-Dollar Market for Your Phone's Location Data" (September 2021): https://themarkup.org/privacy/2021/09/30/theres-a-multibillion-dollar-market-for-your-phones-location-data
- The Markup, "What Happens to Your Sensitive Data When a Data Broker Goes Bankrupt?" (February 2024): https://themarkup.org/privacy/2024/02/23/what-happens-to-your-sensitive-data-when-a-data-broker-goes-bankrupt
- FTC X-Mode/Outlogic ban announcement (January 2024).
- Bloomberg, "Data Firm Near Intelligence Files for Bankruptcy Months After Going Public Via SPAC" (December 2023).
- FCC fines on US carriers for selling location data (2024).
- Mapbox Movement product page: https://www.mapbox.com/movement-data
- Mapbox / OpenAI ChatGPT search integration announcement (November 2024).
