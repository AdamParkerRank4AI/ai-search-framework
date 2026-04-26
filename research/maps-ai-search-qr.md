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
