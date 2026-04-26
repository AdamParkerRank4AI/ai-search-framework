# Real-World Footfall as Grounding Data for AI Search Platforms

**A proposal for vetting and feedback**

**Author:** Liam, with the Rank4AI framework
**Date:** April 2026
**Length:** ~5 minute read
**Status:** Early-stage, seeking honest critique before we commit serious time or capital

---

## Executive summary

**AI search is a trust engine.** When ChatGPT, Gemini, Claude, Perplexity or Copilot decides what to recommend, what they are really doing is judging which entities are real, active, popular and credible. Today they make that judgement almost entirely from **digital signals**: web pages, online reviews, structured data, citations, social mentions. Every one of those signals can be manipulated, and the AI platforms know it. Hallucinated or gamed answers are their single biggest credibility risk.

The signal they don't have is **physical**. If a business has a real footprint — people actually walking in, spending time, coming back — that is the strongest trust signal in existence and the hardest to fake. Right now, AI platforms cannot see it. They only have access to the digital half of trust.

The next industry phase is "places" — AI-generated maps, location-aware answers, "what should I do here today" queries. But even the new map layer is being built on the same online-derived signals. The map is new, the underlying trust data is the same as before. Manipulable.

We propose to close the gap. Build a consent-based pipeline that captures real-world foot traffic, converts it into LLM-readable structured data attached to entity records, and sells the resulting feed to AI platforms as a grounding signal. The product works across the full size range — from Lakeside-class shopping centres down to single independent shops — because every business needs trust signals to be recommended, not just the big ones. Secondary value: the same data stream is exactly what retailers and venue landlords already pay for from companies like Placer.ai, except more granular and consent-clean.

We are looking for honest pushback before committing further. Specific questions at the end.

---

## Honest framing: this is a starting hypothesis, not a finished thesis

A note before the rest of this document.

This is the **start** of an idea, not a fully formed business. We don't yet know:

- Exactly what this footprint data could ultimately be used for once it exists at scale.
- Whether AI platforms will actually pay for it at the price and in the shape we're imagining.
- Whether the indoor map is the right wedge, or whether one of the alternative paths (Section 10) is better.
- Which venue category we should pilot in first.
- Whether the whole model works end-to-end at all.

What we are confident about is the underlying observation: **footprint data — who actually goes where, in physical space — is not being used by LLMs or AI search platforms today.** Their grounding signals are entirely digital. That gap is real, and someone is going to close it. We think it might as well be us, given the right combination of methodology, consent quality and indoor specificity, because no incumbent is positioned to do it cleanly. But that's a thesis, not a certainty.

Treat the rest of this proposal as a working hypothesis to scrutinise, not as a finished plan to approve. The point of sending it for vetting is to help us figure out what's wrong with it *before* we commit serious money — which is why honest "this won't work because…" feedback is far more useful than encouragement.

---

## 1. Where AI search is today — and why trust is the whole problem

AI search platforms are, fundamentally, **trust engines**. Every time ChatGPT recommends a phone shop, suggests a restaurant, or answers "what should I do in Lakeside today," it is deciding which businesses to trust enough to surface. That decision is made from a fixed pool of available signals.

Today, that pool is entirely digital:

- Web pages and content marketing.
- Online reviews (Google, Trustpilot, Yelp).
- Structured data (schema.org, Wikidata, Google Knowledge Graph).
- Citations and backlinks.
- Social media mentions and posts.

This is **digital trust** — what twenty years of SEO was built around, and what the AI platforms inherited.

The problem: every one of these signals is gameable. SEO, paid reviews, link buying, AI-generated content farms, bot networks. Anyone with budget can move the needle. The AI platforms know this and treat the resulting answers with appropriate caution — but they have no better data to draw on for most place-based questions.

**The signal they're missing is physical.** Whether real people actually walk into a place, spend time there, and come back is the strongest trust evidence in existence — and it is invisible to every LLM today. If a business has a footprint, AI platforms need that data, because it's the half of trust they can't currently see. The opportunity is to be the supplier that gives it to them.

## 2. What's coming next: AI maps

In the next 12–24 months, AI platforms are clearly moving into maps and place-aware answers. OpenAI has signalled interest in commerce and local. Google AI Overviews is increasingly map-anchored. Perplexity is investing in local search. The category is forming.

But the maps that come out of this round will still be built on **digital data**: addresses, geocodes, opening hours scraped from websites, reviews ingested from public sources. The map is new, the underlying trust signal is the same as before. Manipulable.

So the ground question is: what would a *better* signal look like?

## 3. The gap: offline truth

Real-world behaviour is the answer.

Whether 4,000 people actually walked through a venue on Saturday, how long they stayed, which shops they visited and which they skipped — this is the truth that no amount of website manipulation can fake. Footfall is offline, observed and costly to forge.

Today this data exists in fragments — held by carriers, by venue WiFi systems, by camera-based counters, by a few footfall analytics vendors (Placer.ai, Foursquare, Huq). None of it is packaged as **AI grounding data**. It is sold to retailers and landlords for marketing decisions. The AI platforms don't see it. The category is empty.

## 4. The thesis

**Convert real-world foot traffic into LLM-readable data, and sell it to AI search platforms as a grounding feed.**

Stated longer: aggregate consent-based location and presence data from many indoor venues, attach it to stable entity records (each shop, each brand, each chain), format it into the structured grounding shape AI platforms can ingest, and license the result.

For an AI platform asking "is Acme Coffee in Lakeside actually a real, popular, currently-trading place" — instead of triangulating from Google reviews and the company's website, they would also see: 4,200 unique visits last week, average dwell 12 minutes, returning-visitor rate 22%, peak Saturday afternoons. That is a fundamentally different class of evidence — the offline reality their answers currently lack.

## 5. The product

**Front of house: an indoor map.** A scan-to-open, no-app-install, browser-rendered map for venues like Lakeside, Westfield, Bluewater, large hospitals and universities. Visitor scans a QR code on entry, the map opens in their browser showing where they are and where everything in the venue is. Each pin is also a structured entity record so the venue and its tenants become more discoverable to AI platforms.

**Behind the scenes: consent-based location capture.** Every visitor who scans the map gives explicit permission for their anonymous, location-only presence data to be captured for that visit. This is the cleanest possible consent flow — visitor-initiated, single-purpose, with no carry-over to advertising or identity.

**The output: a grounding feed.** Aggregated and anonymised to a k-anonymity threshold, attached to entity IDs that resolve to Wikidata, Companies House and the Rank4AI graph. Daily-refreshed records of:

- Visit counts per shop, per venue, per brand.
- Dwell distributions and peak-hour profiles.
- Returning-visitor rates.
- Common routes and adjacency patterns (which shops are visited together).
- Change-vs-prior-period and freshness timestamps.

Sold under documented methodology with provenance disclosed per record — exactly what AI platform procurement teams now require under emerging EU AI Act sourcing rules.

## 6. Big and small — the product works at both ends of the market

A common mistake when pitching this is to make it sound like it only matters for shopping centres. It doesn't. The trust problem is the same for a single independent coffee shop in Soho as for the H&M flagship in Lakeside — both want to be recommended by ChatGPT, both currently rely on the same gameable digital signals, both would benefit from a footfall trust layer.

The product spans the size range:

- **Large venues (Lakeside, Westfield, large hospitals, airports, universities, stadiums).** Full indoor map, multi-tenant, multi-floor, full footfall analytics, premium SaaS price band. Anchors the network — high foot traffic, many entities, rich data.
- **Mid-size venues (high streets, retail parks, mid-size hospitals, secondary stations, cultural venues).** Simpler map or area directory, single-floor or small multi-floor, mid-tier SaaS. Fills the geographic and category gaps the big anchors leave.
- **Small businesses (a single café, an independent bookshop, a barber, a small restaurant).** No indoor map needed for a 50-square-metre shop. Just a QR check-in by the door, a claim-your-business flow, and the same per-visit consent capture. Free or low-cost tier. The data they contribute is smaller per location but the count of locations is enormous.

Why this matters strategically:

- **The addressable market is the whole built environment**, not just a couple of hundred large venues. There are roughly 270,000 retail premises in the UK alone before you count hospitality, healthcare and culture. The big-venue path alone is too narrow to be the whole business.
- **Small businesses are exactly who AI search currently fails worst.** A user asking ChatGPT "best independent bookshop in Bristol" gets a worse, more outdated answer than the same query for a chain — because small businesses have weaker digital signals. A footprint trust signal helps the underdog disproportionately.
- **Network effect.** Big venues anchor the data; mid and small venues fill in the long tail. The same AI platform query "where to eat near Liverpool Street" returns more reliable answers as more nearby small businesses are in the network.
- **Pricing tiers.** Free tier for independents (data contribution is the trade), mid-tier SaaS for high-street and retail-park operators, premium for flagship venues. Same product, different price points, same back-end data pipeline.
- **Sales motion.** Big venues are slow enterprise deals. Small businesses can self-serve sign up like Stripe or Square. Doing both lets us grow the network faster than either alone.

This expands the proposal in one important way: it isn't just an indoor-map company with an AI data line attached. It's a **footprint trust layer for every business with a physical premises**, scaled from solo independents up to the largest venues in the country, all feeding the same AI-grounding feed.

## 7. Why AI platforms would buy this

Five reasons:

1. **It reduces hallucination on place questions.** The single biggest credibility risk for ChatGPT and its peers when asked "where should I go" is recommending somewhere that's closed, struggling, or fake. Footfall data prevents that class of error.

2. **It's costly to fake.** Web content, reviews and citations can be manufactured. Real human feet in real venues can't be — at least not at the scale needed to game the data.

3. **It's recent.** Footfall is fresh by definition. Stale web content can't say whether a place is still trading; a footfall feed can.

4. **It cross-references their existing signals.** A business with strong online signals *plus* strong footfall is verifiably real and active. A business with only one is suspicious. The combined signal is more powerful than either alone.

5. **OpenAI has shown they will pay for grounding data.** AP, Le Monde, Reddit, Stack Overflow, FT, News Corp, Time, Vox, Condé Nast — all licensed in 2024–2025. Pattern is consistent: novel data that improves grounding gets paid for, often $1M–$60M/year depending on scale and exclusivity. Footfall fits the same pattern, in a category they don't yet have a supplier for.

## 8. Why this is better than card-transaction data

Card data (Mastercard SpendingPulse, Visa, Fable, Consumer Edge) and loyalty data are the obvious adjacent signal — and they have a structural flaw.

A family of four enters a venue, has lunch, browses three shops, buys clothes, leaves. Card data captures **one cardholder** — the parent who paid. Four humans, one signal. Loyalty data: same flaw, one Clubcard, four people. And card data only registers the visit *if* a purchase happens — browsers and non-payers are invisible.

Per-device location data inverts that:

- Four phones with the map open = four hits, not one.
- Browsing visits count even with zero spend.
- Arrival, dwell, route and departure are all captured — not just a single point-of-sale timestamp.
- Cross-tenant journeys are visible — including the shops people *didn't* buy from.

Combined with the granular pin-point data, route patterns and pattern-of-life signals from the map, this is a much richer picture than any card or loyalty feed can produce.

(Honest note: per-device data also has limits — children typically don't have phones, not every family member will have the map open, and people who don't scan are invisible to us. We document these as part of the methodology rather than hide them. AI platforms specifically prefer suppliers who disclose limitations cleanly.)

## 9. Secondary value: retailers and landlords

The same data stream we're selling to AI platforms is also what venues and retailers already pay for, today. Placer.ai is reportedly close to a $1B valuation on this market. Springboard, Huq, Sensormatic and Foursquare all sell into it.

Layered onto our base product:

- **Venue landlords** pay for the indoor map as a SaaS amenity for visitors, plus get a built-in analytics dashboard.
- **Retailer brands** (H&M, Boots, Greggs) get a free dashboard for their own stores in our network — visits, dwell, peak hours, returning rate. Many will sign up for the analytics alone.
- **Sponsored placements** inside the map become high-margin advertising at point-of-intent.

So even if the AI platform play takes longer than expected to land, the indoor map plus retailer/venue analytics is already a working, proven business model. Pointr, Mapwize, Situm have built nine-figure businesses on a more enterprise-heavy version of the same shape.

## 10. Alternative path: aggregate existing sources instead of originating

Originating data via the indoor map is the long-term moat, but it takes years to reach meaningful coverage. There is a parallel route worth considering — possibly to run *first*, possibly *instead*: aggregate signals from data sources that already exist, build an algorithm that reconciles them into a single entity-keyed feed, and sell that to AI platforms today.

The candidate sources, each capturing a different facet of "people are at this place":

- **Card transaction data** — Visa, Mastercard SpendingPulse, Fable Data, Consumer Edge, Earnest, Facteus. Tells us spend patterns by merchant and location.
- **Venue WiFi networks** — Cisco Meraki, Aruba, Purple WiFi. Tells us connected device counts per venue, in real time, where the venue is a customer.
- **Mobile phone carriers** — Vodafone Analytics, O2 Motion, EE/BT, Three. Tells us area-level flow and arrival data, by network.
- **Social check-ins and geotagged posts** — Instagram, X, TikTok, OpenTable bookings, Eventbrite ticket sales. Tells us demand and presence indirectly.
- **Public transport tap data** — TfL station tap-ins, National Rail stats. Tells us arrivals at major nodes near venues.
- **Vehicle probe and parking data** — HERE, TomTom, INRIX, RingGo, JustPark. Tells us car arrivals at retail destinations.

The pitch: rather than waiting years to originate at scale, license slices from each of these and build the **algorithm and methodology** that turns disparate signals into a single AI-grounding feed. None of the source vendors does this packaging for AI platforms today. The work is in the reconciliation, the entity linkage, and the documented methodology.

Honest trade-offs:

- **Pros:** live in months not years; no consumer product to support; multi-source blend reduces single-source dependency; gets us into AI-platform conversations with real data far sooner.
- **Cons:** thin margin per source (we're a re-packager); supplier relationships can be re-traded once they see what AI grounding is worth; less defensible than originated data; exposure to upstream suppliers' privacy and regulatory issues.

The most likely realistic shape: **Phase 1 (months 1–18) is the aggregation play** — get into the OpenAI room with bought-in stitched data and a clean methodology. **Phase 2 onwards (year 2+) is the originated map** — first-party data progressively replaces bought-in slices, margin and quality both improve, the moat compounds.

Card data deserves a particular caveat here. As covered in Section 7, card data structurally undercounts groups (one cardholder, four humans) and ignores browsers (no spend, no signal). It is one source in the blend, not a foundation. The algorithm has to weight it accordingly.

## 11. Going nicher — places where data is easier to get

The proposal so far has assumed shopping centres (Lakeside-style retail). That is a hard market: retail data is commercially sensitive, incumbents are entrenched, and venue ops teams are slow.

Other categories of place may be materially easier to acquire data for, and worth piloting first:

- **Hospitals.** Public funding, public-benefit angle, often willing to share aggregated data with researchers. Wayfinding pain is acute (lost patients arriving for appointments is a measurable problem). NHS trust partnership could open many sites under one signature.
- **Universities.** Academic-openness culture, student safety angle, high seasonal and event-driven footfall, willing to experiment.
- **Stadiums and event venues.** Already heavily instrumented (ticketing, security, turnstiles), event-driven so per-event value is easy to demonstrate.
- **Transport hubs.** TfL already publishes station-level tap data; rail and bus operators have similar feeds. Rich infrastructure, partial open-data attitude.
- **Tourist and cultural venues** — museums, galleries, heritage sites, zoos. Typically open-data leaning, publicly funded, AI-grounding queries are common ("is this museum open today, how busy").
- **Single-operator retail estates** — coffee chains, pharmacy chains, restaurant groups. One signature with a head office gets nationwide coverage rather than venue-by-venue sales.

The argument: pick the niche where data acquisition is the least friction *and* where AI grounding queries are common, prove the model end-to-end, then expand outward. Shopping centres can come later once the playbook is proven.

This needs deciding before the prototype venue is chosen. Same Section 12-style demo, easier real-world deployment.

## 12a. Note on Living Map (the company that triggered this idea)

Living Map (livingmap.com) is the UK indoor mapping company that prompted this whole line of thinking. Worth being explicit about them up front because anyone vetting this who knows the space will name them within minutes.

The basics: Bath-based, founded 2012, around 30 people, took a £2.6M Series A in 2019 led by Committed Capital and Mercia. They sell digital indoor mapping, wayfinding, asset tracking and an analytics dashboard. Delivery is web, mobile and kiosk. Their customer list spans the exact sectors this proposal targets: NHS hospitals (in partnership with VitalHub UK), Canary Wharf, St Pancras International, Star Alliance, the Met Museum, Detroit Institutes of Arts, City of Edmonton.

What they have:
- Real venue relationships in healthcare, transport, culture, retail and smart cities.
- A mature product across web, mobile and kiosk.
- An analytics dashboard that captures visitor searches and destinations.
- Published thinking on AI's impact on wayfinding (their own blog acknowledges the trend).

What they appear not to have (based on public information):
- A footfall data feed packaged for licensing to AI search platforms as a grounding signal.
- A small-business / single-shop tier alongside their enterprise venue product.
- An entity-graph linkage that connects venue pins to a published AI-search optimisation methodology.
- A QR-to-web, no-app entry model as the primary delivery surface.

Implications for this proposal:

- **We should not compete head-on with Living Map for indoor mapping deployments.** Decade-long head start, real customer base, mature product. That fight is lost on day one.
- **Partnership is the more interesting first conversation.** Layer the AI grounding data product on their installed base. They get a new revenue line, we get coverage on day one. Worth a direct call early in the validation phase.
- **Acquisition or being acquired is plausible at maturity.** A company like Living Map (or one of its larger global counterparts) is the kind of buyer that would want an AI-grounding data layer bolted onto its existing venue footprint, three to five years out.
- **The competitive read is the same conclusion as elsewhere in this doc.** Don't try to rebuild what Living Map (or Pointr, Mapwize, Situm) already do. Build the layer they don't.

This is the most important single competitive datapoint in the document. Anyone reviewing this proposal should be asked specifically whether they have insight into Living Map's strategic intentions on AI grounding, and whether they have a route to an introduction.

## 12b. Note on kiosks — an adjacent product, already happening

There is already a market for **physical interactive kiosks** in venues. Companies like 22Miles, Visix, Acquire Digital, Mvix and many smaller operators ship touchscreen wayfinding, advertising and self-service hardware into retail, hospitality, hospitals and transit. Some retail chains run their own (McDonald's order screens, supermarket self-checkout, hotel check-in stations).

Their primary purposes are wayfinding, in-venue advertising, ordering and check-in. **Not data capture for AI grounding.**

What their existence proves:

- Venues will sign deals to install branded interactive hardware in high-footfall locations.
- Visitors will engage with venue-placed screens.
- The placement model (entrance, atrium, food court) works at scale.
- Hardware operators have established relationships with venue ops teams that we don't.

What they don't currently do:

- Treat each interaction as a footfall-data-generation event.
- Link kiosk interactions to entity-level AI grounding records.
- Operate per-visitor consent flows producing licensable data feeds.

Implications for our plan:

- **Partner route, not competitor.** Existing kiosk operators are a potential channel — license our software-and-data layer to them as an upgrade, in exchange for installed-base access.
- **Hardware variant of the map.** The same scan-to-phone flow can have a kiosk equivalent for visitors who prefer touchscreen — same data model, different interface.
- **Channel into venues we couldn't otherwise reach.** Kiosk operators already have signed contracts with venues; partnering shortcuts our sales motion.

This is a parallel route worth exploring during the validation phase, not a pivot. It also suggests a useful framing for the vetting conversation: someone has already proven venues will adopt physical placement at the entrance — we are layering a new product on a delivery channel that exists.

## 13. Why now

Several conditions only aligned in the last 12–18 months:

- AI search has legitimised. Real budgets are being spent on grounding data; OpenAI's publisher deals confirm a category exists.
- Mobile-SDK footfall (the legacy way to get this data) is collapsing under Apple's App Tracking Transparency and Google's Privacy Sandbox. The FTC banned X-Mode/Outlogic in 2024. Gravy Analytics was breached in early 2025. The incumbents are weakened, not strengthened.
- Privacy regulation now creates a moat for clean-consent operators rather than just being friction. Late entrants will struggle to retrofit the consent quality that AI platforms will require.
- Indoor mapping is mature enough to ship a competent product in months, not years.
- The Rank4AI methodology already exists and gives the data product a thesis to sit inside.

Realistic first-mover window: probably 18–24 months before Foursquare, Placer or one of the AI platforms themselves notices the category and pivots into it.

## 14. What's defensible

Honest read on what's hard for someone else to copy:

- **Consent quality.** Built from day one on visitor-initiated QR scans. SDK-aggregator competitors carry years of murky consent provenance and active regulator interest.
- **Entity linkage.** Every record tied to stable IDs that resolve to Wikidata, Companies House, brand parents, the Rank4AI graph. Most footfall vendors sell "device near coordinates" and have no entity layer.
- **Indoor precision.** Most outdoor footfall products are tile- or postcode-based. Inside Lakeside, "best phone shop" needs to know which unit, not which sector.
- **Methodology bundle.** Rank4AI is published, scored, audit-anchored. The data product sits inside a thesis and a brand, not as a standalone CSV.
- **Speed.** Big incumbents are slow to pivot strategy. Small operators can define a new category faster than they can react.

We will not beat the incumbents on raw data volume early on. We can beat them on cleanliness, structure, indoor specificity, and being there first.

## 15. What we don't know yet

Honest list. These are the things the vetting reader is invited to challenge.

- **Will AI platforms actually pay for this?** Plausible but unproven. Direct conversations with grounding-team contacts at OpenAI / Anthropic / Google / Perplexity are the cheapest way to find out.
- **What's the coverage threshold for the data to be interesting?** Probably hundreds of venues, not tens. The road from venue 1 to venue 100 is real work.
- **Will visitors actually scan?** Believable for venues that promote the QR well; unproven below ~30% scan rates.
- **Could OpenAI / Google build this themselves?** They could. Our defence is being smaller, faster, neutral and multi-platform.
- **Is the market for indoor maps + venue SaaS strong enough to fund the early years?** Pointr/Mapwize numbers suggest yes; we'd need to validate per-venue economics ourselves.

## 16. What we're asking from you

If you're reading this to vet it, the most useful things you can tell us:

1. **Have you seen anyone else building this?** Stealth startups, internal teams at AI platforms, recent moves from footfall vendors? If yes — who, and how seriously.
2. **Where would you push back hardest?** Which assumption in this document is the weakest?
3. **Who should we be talking to?** Specifically: data-partnerships people at OpenAI / Anthropic / Google / Perplexity, indoor-mapping operators, venue ops contacts, AI-grounding researchers.
4. **What kills it?** What's the most likely reason this doesn't work, that we've underweighted?

The plan is to spend the next three to six months proving the prototype, validating AI-platform demand, and signing one pilot venue — total cost £30–80k including time. We won't raise serious capital until those steps are mostly green. This document is a snapshot before that work begins.

Honest critique appreciated. Sycophantic "this is great" feedback isn't useful — we'd rather hear the hardest version of why this might fail.

---

## Appendix: one-line framing for the bullet list version

> AI search is a trust engine. Today its only trust signals are digital — and digital signals can be faked. The signal it's missing is physical: who actually goes where. We're building the pipeline that converts real-world foot traffic into LLM-readable trust data, for every business with a footprint, from a single café up to Lakeside-class venues. Sold to AI platforms first, retailers and landlords second. The map is the wedge. The data is the product. The window is now.
