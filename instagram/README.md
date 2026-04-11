# compareSEO → Instagram: Ranking Tables Redesign

This folder turns the compareSEO ranking tables (Top AI SEO Agencies UK, Top GEO Agencies US, UK AI Search Specialist Landscape, etc.) into an Instagram-native content system.

The core idea: the rankings already exist on the site as web tables. Web tables do not go viral on Instagram. We keep the **data** and the **methodology** — the trust — and we rebuild the **format** for feed, reels, carousels and stories.

One compareSEO ranking = 7 Instagram posts. Publish them all in the same week, then refresh monthly when the ranking updates.

---

## Files in this folder

| File | What it contains |
|------|------------------|
| `post-formats.md` | The 7 Instagram formats one ranking expands into, with visual specs |
| `design-system.md` | Colours, type, grids, safe zones — the locked visual system so every post looks like the same brand |
| `caption-templates.md` | Fill-in-the-blanks captions and hooks for every format |
| `example-top10-ai-seo-agencies-uk.md` | A worked example using the "Top AI SEO Agencies UK" ranking slot-by-slot |
| `monthly-refresh-playbook.md` | What to post every time a ranking updates — the "who moved" cycle |
| `figma-spec.md` | Frame sizes, exports, naming convention for the designer/template builder |

---

## The principle: one ranking = one week of content

Every time compareSEO publishes or updates a ranking, we ship this exact set in the same week:

| Day | Format | Purpose |
|-----|--------|---------|
| Mon | **Cover reel** — "Top 10 AI SEO Agencies UK 2026 (ranked)" | Awareness, saves |
| Tue | **10-slide carousel** — one slide per agency | Deep dive, saves, profile visits |
| Wed | **Countdown reel** — #10 → #1, 3 seconds each | Reach, re-watches |
| Thu | **Criteria carousel** — "How we actually rank them" | Authority, methodology |
| Fri | **#1 spotlight reel** — why the top entry won | Controversy, shares |
| Sat | **Movers carousel** — who went up, who dropped | Recurring hook |
| Sun | **Stories quiz** — "Guess the #1" with swipe-up to the full list | DMs, link clicks |

One ranking, seven posts, one full feed week. Scales to every category compareSEO covers: UK agencies, US agencies, GEO specialists, AI tools, platform-specific rankings, industry landscapes.

**Standing rule: follow and tag every ranked account.** Before the first post of any ranking week goes live, the compareSEO IG account follows every agency / tool on the ranking page. Every post then tags them in the asset itself (not just the caption). See the full rule in `monthly-refresh-playbook.md` under the T-7 section.

---

## Why redesigning the tables matters more than making new content

Right now the rankings live as web pages. The problem:

1. **Web tables don't travel.** A screenshot of an HTML table looks cheap on Instagram and kills reach because the text is unreadable on mobile without pinch-zoom.
2. **No hierarchy on feed.** The #1 spot and the #10 spot get equal visual weight in a web table. On Instagram the #1 entry needs to be the entire screen.
3. **No story.** A table shows the final state. Instagram audiences want to know *why* — criteria, scoring, movement, the upset at #3. Each of those is a separate post.
4. **No format variation.** Instagram punishes accounts that post the same thing twice. A single ranking must output cover reels, carousels, countdowns, spotlights, and stories — all from the same source data.

The redesign is not "put the table in a nicer graphic." It's "break the table into 7 formats, each optimised for what Instagram actually rewards."

---

## Locked visual system (the non-negotiable)

Every post uses the same:

- **Aspect ratios:** 1080x1920 for reels + stories, 1080x1350 for feed carousels
- **Safe zone:** 160px top, 280px bottom (nothing important in the UI-overlap zones)
- **Palette:** 2 brand colours + 1 accent (see `design-system.md`)
- **Type:** 1 display face for titles, 1 mono for scores, 1 sans for body
- **Badge:** a circular "compareSEO Rank" badge with position number — this is the one element every post shares, the brand mnemonic
- **Footer bar:** `compareseo.co.uk · updated Apr 2026 · by Rank4AI`

Consistency compounds. Every post has to be instantly recognisable as a compareSEO post in the feed scroll.

---

## What I need from you to finish this

The templates are ready to fill. To turn them into finished posts I need one of:

1. **A link I can access** to one live ranking page (the rank4ai.co.uk pages return only tracking scripts to me — the tables are rendered client-side). A JSON export, PDF, or a plain-text paste of the ranking works equally well.
2. **Brand assets:** hex codes for the compareSEO palette, logo, font names (or a Figma file URL I can reference).
3. **Decision on #1 focus:** which ranking do we launch with — "Top AI SEO Agencies UK" or "UK AI Search Specialist Landscape 2026"?

Drop any of the above in the chat and I'll slot the real data into `example-top10-ai-seo-agencies-uk.md` and produce a finished specification a designer can build in Figma in an afternoon.
