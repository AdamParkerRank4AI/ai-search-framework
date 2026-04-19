# DirectorCover — Project Plans

Research deliverable on branch `claude/research-insurance-leads-a5wLA`.

DirectorCover is the working name for a UK director-insurance publisher and broker directory built on the Rank4AI framework, designed in Phase 1 to compound into an FCA-authorised brokerage in Phase 2.

## Documents

| Doc | Purpose |
|---|---|
| [01-strategic-plan.md](./01-strategic-plan.md) | Master strategic plan. Product, brand, architecture, regulatory model, 4-register content strategy, success gates, timeline, risks. The single source of truth. |
| [02-site-build-spec.md](./02-site-build-spec.md) | What the site has to be at launch to be "perfect". Full wireframe tree, technical stack, schema, page templates, minimum content inventory, compliance, analytics, AI-search readiness. |
| [03-weekly-cadence.md](./03-weekly-cadence.md) | What we add weekly, monthly, quarterly. Rank4AI dashboard usage for trend spotting. Ecosystem distribution playbook for pushing out content. |
| [04-activequote-integration.md](./04-activequote-integration.md) | Plan for the Side 2 Layer C compare partnership with ActiveQuote. Products covered, page plan, integration template, partnership process, fallback partners, risks. |

## Reading order

1. Read `01-strategic-plan.md` first to understand the whole plan.
2. Use `02-site-build-spec.md` as the launch readiness checklist.
3. Use `03-weekly-cadence.md` as the ongoing operating rhythm once the site is live.
4. Use `04-activequote-integration.md` as the execution plan for the Side 2 comparison layer partnership.

## Status

v1.0 — captured from strategy conversation on branch `claude/research-insurance-leads-a5wLA`. Treat as a working document; update on each major decision.

## Future / Parking Lot (not now — for the 49k tiles roadmap)

Captured here so they are not lost, but explicitly out of scope for the current build:

- **Visualise the plan.** Convert the key pieces of this plan (site architecture, 3-layer commercial model, 4-register content matrix, Phase 1 → Phase 2 flow, success gates, ecosystem distribution loop) into diagrams, org charts, and Miro boards so the plan is readable at a glance rather than only as long-form markdown.
- **Link the content engine to acquisition channels.** Right now the plan treats DirectorCover as a consumer/SME-director-facing site. A later wave should explicitly map the content engine onto B2B acquisition channels — for example, offering this as a white-label service or partnership into **mid-tier UK businesses (£2–7m turnover)**, accountants, solicitors, FDs, and corporate finance firms who have the director audience but no insurance content layer.
- **Director-risk mapping tool.** Build a tool that uses Google Maps (or similar mapping / data sources) plus Companies House data to identify UK director risks, partnerships, sector concentrations, and SPV clusters — usable both as a lead-generation surface for DirectorCover and as a premium feature for the eventual brokerage.
- **Cross-link every future DirectorCover workstream back to these plans** so diagrams, tools, and channel strategies all descend from the same single source of truth rather than drifting.

None of these get built before the Phase 1 gates are hit. Keep them visible so they inform structural decisions made now (e.g. data models built during the site build should leave room for the mapping tool to plug in later without rework).
