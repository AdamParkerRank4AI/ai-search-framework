# URL Crawl Priority Analysis

**Date:** 22 March 2026
**Based on:** Google Search Console indexed URL data as of March 2026

---

## Critical Issue: www vs non-www Duplicate Indexing

Several pages are indexed under both `rank4ai.co.uk` and `www.rank4ai.co.uk`, splitting crawl equity and creating signal inconsistency (undermines Signal 05: Signal Consistency).

| Page Path | Versions Indexed |
|---|---|
| /ai-search/ai-visibility-agency | Both www and non-www (Feb 23) |
| /blog/what-does-ranking-mean-in-ai-search | Both www and non-www (Feb 22) |
| /blog/why-does-my-business-not-show-up-in-claude | Both www and non-www (Feb 20) |
| /blog/does-page-structure-affect-ai-answers | www (Feb 25), non-www (Feb 20) |

**Action:** Ensure canonical tags point to one version. Fix server-side redirects so only the preferred domain is indexed.

---

## Indexing Priority Tiers

### Tier 1 — Request Immediately (Core Commercial Pages)

High-value service and conversion pages. Maps to Signal 01 (Identity Clarity) and Signal 02 (Subject Authority).

| URL | Last Crawled | Reason |
|---|---|---|
| /ai-seo | Feb 21 | Core service page, most stale |
| /ai-seo/ai-seo-audit | Feb 28 | Direct conversion page |
| /ai-visibility-consultancy | Mar 2 | Primary service page |
| /ai-platform-visibility | Mar 2 | Key differentiator page |
| /ai-search/ai-visibility-agency | Feb 23 | Commercial landing page |
| /ai-seo-agency-uk/london | Feb 28 | Location service page |

### Tier 2 — Request This Week (Framework and Authority Content)

Establishes Subject Authority (Signal 02) and builds the topical cluster.

| URL | Last Crawled | Reason |
|---|---|---|
| /complete-guide-to-ai-search-visibility | Feb 28 | Pillar content |
| /ecosystem | Feb 28 | Core framework concept |
| /guides | Feb 28 | Content hub page |
| /ai-seo/technical/examples-outcomes-signals | Feb 22 | Technical depth |
| /ai-search-platform-differences | Mar 2 | Differentiating content |

### Tier 3 — Request Next (Strategic Blog Content)

Blog posts addressing high-intent AI search questions (Signal 02: Full Prompt Spectrum Coverage).

| URL | Last Crawled | Reason |
|---|---|---|
| /blog/can-you-rank-in-chatgpt | Unknown | Possibly not fully crawled |
| /blog/why-is-ai-not-mentioning-my-business-name | Feb 20 | High-intent question |
| /blog/does-ai-prioritise-businesses-with-more-online-presence | Feb 22 | High-intent question |
| /blog/can-ai-recommend-small-businesses-over-large-chains | Feb 23 | High-intent question |
| /blog/can-ai-recommendations-be-trusted-for-services | Feb 24 | Trust-building content |

### Tier 4 — Lower Priority (Recently Crawled)

These pages were crawled in early March and are less urgent.

- /ai-search/perplexity-ranking-services (Mar 2)
- /ai-search/claude-ranking-agency (Mar 2)
- /ai-search/ecosystem-validation (Mar 2)
- /ai-marketing-growth/* pages (Mar 2–6)
- /ai-search-questions/* pages (Mar 3–4)

---

## Pages to Check: Possibly Not Indexed

Based on site structure, verify whether these important pages are indexed at all:

- **/methodology** — Referenced in framework, critical for trust
- **/about** or **/team** — Identity Clarity signal
- **/contact** — Basic commercial page
- **/case-studies** — Evidence over Assertion (Signal 02)
- **/ai-seo-agency-uk** (parent page) — Only /london and /leeds variants appear
- **/pricing** or **/services** — If they exist

---

## Summary

| Priority | Action | Count |
|---|---|---|
| Fix now | Resolve www/non-www canonicalization | 4+ duplicates |
| Tier 1 | Request indexing for core service pages | 6 URLs |
| Tier 2 | Request indexing for authority/framework pages | 5 URLs |
| Tier 3 | Request indexing for strategic blog posts | 5 URLs |
| Check | Verify these pages are discoverable | 5+ pages |

**Logic:** Service pages first (conversion), then authority pages (topical cluster for AI platforms), then blog posts (prompt spectrum coverage). Fix duplicate indexing in parallel — it actively dilutes signals.
