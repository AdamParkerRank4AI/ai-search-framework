# Production pipeline — how we actually make the visuals

The design system (in `design-system.md` and `figma-spec.md`) says *what* every frame should look like. This file says *how* we produce them, what tool we use for what, and where assets come from.

Locked decisions at the top. Everything else in the file supports them.

---

## The tool stack (locked)

| Format | Tool | Why |
|--------|------|-----|
| Foundations + master Figma file | **Figma** (free tier is enough) | Components, text styles, multi-player, reusable monthly |
| 13-slide carousel (Format 2) | **Figma** | Template + data swap each month |
| Criteria carousel (Format 4) | **Figma** | Evergreen, build once, re-export with date stamp |
| Movers carousel (Format 6) | **Figma** | Template + monthly data swap |
| Stories quiz (Format 7) | **Figma** or **Canva** | One-off, either works |
| Cover reel (Format 1) | **CapCut (desktop)** | Free, fast text animation, built-in trending audio |
| Countdown reel (Format 3) | **CapCut (desktop)** | 10 identical cards chain fast, audio beat sync |
| #1 Spotlight reel (Format 5) | **CapCut + Loom** | Loom for AI screen recordings, CapCut to stitch with Adam's talking-head |

**Fallback stack (if no Figma skills available):** do every static post in **Canva Pro** using the **Bulk Create** workflow (see dedicated section below). Honestly, for a non-designer running a ranking account, this is probably *better* than Figma — it's purpose-built for "one template, N rows of data, N slides out".

**Over-budget stack (don't reach for this yet):** After Effects for motion graphics, Premiere Pro for reels. Unnecessary until the account proves format/fit at 10k followers.

---

## The hero rule (never break)

> **The position number is the biggest thing on every frame.**

Not the agency logo. Not the name. Not the score. The number. Reasoning is in `design-system.md` section 3 — it's the mnemonic that makes compareSEO posts recognisable in a muted-sound scroll. No exceptions, no creative-director second-guessing.

---

## Where assets come from

### Agency / tool logos
Clearbit Logo API — free, no auth:
```
https://logo.clearbit.com/[domain.com]
```
Example: `https://logo.clearbit.com/riseatseven.com` returns a PNG.

Fallback: screenshot the agency's own site header, crop in Figma. Never use Google Images results — licensing risk.

### AI platform screen recordings (ChatGPT / Claude / Perplexity / Gemini)
- **macOS:** built-in screen recorder (Shift-Cmd-5) or Loom
- **Windows:** Loom or ShareX
- **Mobile:** native screen record, but crop to desktop-style aspect on import

What to record:
- The exact query typed out
- The AI's full answer streaming
- A highlight/zoom on the cited agency name in the response

These clips are gold for the spotlight reel. Keep them 5–10 seconds each, no longer.

### Founder footage (Adam)
- iPhone 15/16 front camera, 4K 30fps
- Natural window light, not overhead
- Batch-shoot once a week — 6–8 minutes raw = 4–5 reels
- Frame: chest-up, headroom at the top for text overlays, background clean/neutral
- Wear the same jacket across a week's reels so they look like a set, not one-offs

### Music / audio
- **CapCut "Trending on Instagram" tab** — refresh monthly, trending sounds have a ~30-day shelf life
- Rule: same music bed across every reel in a single month so the account builds auditory recognition
- Avoid copyrighted tracks outside the in-app library — Instagram can mute them on business accounts
- No music on the countdown reel — let the tick/whoosh SFX carry it

### Icons
- Lucide (`lucide.dev`) or Heroicons — both free, minimal, MIT licensed
- Do not use Flaticon — looks dated in 2026

---

## Canva Bulk Create workflow (the no-designer path)

This is the easiest way in existence to turn a ranking table into 10 consistent Instagram slides. Canva Pro only (£10/mo). Read this once and you can run the whole ranking in under an hour.

### The principle

You design **one** master slide with placeholder text boxes. Canva reads a CSV where each row = one output slide. It auto-generates one slide per row by swapping in the data from that row. 10 rows → 10 perfect slides, identical layout, zero manual work.

### Step 1 — Build the master slide (once, ~45 minutes)

1. New design → Instagram Post (1080 × 1350)
2. Set the background to near-black (`#0B0D10`)
3. Add these text boxes, exactly as shown with the placeholder text:

| Text box | Placeholder value | Size | Position |
|----------|-------------------|------|----------|
| Position number | `#01` | Huge (520 px) | Centre, top 60% |
| Agency name | `AGENCY NAME` | Large (88 px) | Below number |
| Score | `00 / 100` | Medium mono (64 px) | Below name |
| Verdict | `"One-line verdict."` | Small (48 px) | Below score |
| Top signal | `Top signal: SIGNAL` | Chip (32 px) | Bottom-left |
| Weak spot | `Weak spot: WEAKNESS` | Chip (32 px) | Bottom-left |

4. Drop the static compareSEO badge in the bottom-right corner
5. Drop the footer bar at the bottom: `compareseo.co.uk · [MONTH] 2026 · by Rank4AI`

Save this design. This is your master. You never touch it again unless the brand system changes.

### Step 2 — Build the CSV (once per ranking, ~15 minutes)

Create a Google Sheet with these exact column headers — the header text is what Canva matches against:

```
position,agency_name,score,verdict,top_signal,weak_spot
1,[Agency 1],94,"They own entity clarity across all four platforms.",Identity Clarity,Ecosystem
2,[Agency 2],89,"Best technical meaning architecture in the UK.",Meaning Architecture,Subject Authority
3,[Agency 3],87,"A huge ecosystem moat no-one can touch.",Ecosystem Validation,Identity Clarity
4,[Agency 4],82,"Consistent signal strength over 12 months.",Signal Consistency,Meaning Architecture
5,[Agency 5],79,"Deep subject authority on one core topic.",Subject Authority,Ecosystem
6,[Agency 6],76,"Clean architecture, thin ecosystem.",Meaning Architecture,Ecosystem
7,[Agency 7],74,"Strong authority, weak identity signals.",Subject Authority,Identity Clarity
8,[Agency 8],71,"Good ecosystem, inconsistent messaging.",Ecosystem Validation,Signal Consistency
9,[Agency 9],68,"Underrated on identity, needs architecture work.",Identity Clarity,Meaning Architecture
10,[Agency 10],65,"Entry-level on the list, lots to build.",Signal Consistency,Subject Authority
```

Export as CSV. (A Google Sheet "File → Download → CSV" does it in one click.)

### Step 3 — Bulk Create (once per ranking, ~5 minutes)

1. In the Canva master design, open the **Apps** menu → **Bulk Create**
2. Click **Upload data** → pick your CSV
3. Click **Auto-connect fields** — Canva reads the column names and links each column to the matching text box automatically. If auto-connect misses one, drag the field name from the sidebar onto the right text box manually.
4. Click **Continue** → **Generate pages**
5. Canva creates 10 new pages in the design, each with a different row's data filled in

Your 10 ranking slides now exist. Review them, fix any truncated verdicts, and export.

### Step 4 — Add the 3 bookend slides (once per ranking, ~10 minutes)

Bulk Create only handles the 10 data slides. You still need:
- **Slide 1** (cover) — "TOP 10 AI SEO AGENCIES UK · 2026 · ← swipe"
- **Slide 12** (methodology) — the 5 signals, weighted
- **Slide 13** (CTA) — "Free audit → link in bio"

Build these once, save them as a separate "cover + outro" design, and duplicate it every month.

### Step 5 — Export and assemble (5 minutes)

1. Export all 13 slides as PNG at 1x
2. Rename files per the convention in `figma-spec.md`: `cs-carousel-[slug]-[NN]-2026-04.png`
3. Drag into Later / Metricool in the correct order
4. Paste caption from `caption-templates.md`
5. Schedule

### Total time

| Run | Time |
|-----|------|
| Month 1 (build master + first CSV + first ranking) | ~75 min |
| Month 2 onwards (swap CSV, re-run Bulk Create) | ~20 min |

That's faster than opening Figma.

### When Bulk Create breaks

- **Long verdicts truncate.** Cap verdicts at 60 characters. Test a row with the longest verdict before running all 10.
- **Auto-connect misses a field.** Drag it manually. Happens when the header name has a typo vs the text box name.
- **Score field appears as "94.0".** Format the CSV column as text in Google Sheets before exporting, or add a `score_display` column with the exact string you want.
- **You change the master slide.** Re-run Bulk Create — old slides will regenerate with the new layout. This is why the master is sacred.

---

## First-week production plan (one-off, ~12 hrs)

| Day | Hours | What |
|-----|-------|------|
| 1 | 4 | Build Figma master from `figma-spec.md` — foundations, 5 components, full Format 2 carousel end-to-end |
| 2 | 2 | Fill the 10 agency rows — names, scores, verdicts, top/weak signals. Pull logos from Clearbit. Record 3 AI query screen recordings. Batch-shoot 6 min of Adam talking-head. |
| 3 | 2 | Produce the 13-slide carousel in Figma — duplicate master, swap data, export PNGs |
| 4 | 3 | Produce 3 reels in CapCut — cover (9s), countdown (30s), spotlight (30s) |
| 5 | 1 | 5 story frames + schedule the whole week in Later/Metricool with captions from `caption-templates.md` |

**Total: 12 hours for week 1.**

## Monthly refresh (from month 2 onwards, ~4 hrs)

| Step | Minutes | Tool |
|------|---------|------|
| Duplicate last month's Figma file, rename | 5 | Figma |
| Swap 10 rows of data + logos | 45 | Figma |
| Export carousel PNGs | 5 | Figma |
| Re-record Adam talking-head (if new spotlight) | 30 | iPhone |
| Re-cut 3 reels in CapCut using existing project templates | 90 | CapCut |
| 5 new story frames | 20 | Figma/Canva |
| Schedule the week | 30 | Later/Metricool |
| **Total** | **~225 min / ~4 hrs** | |

The whole point of locking the system now is that the marginal cost of each month after month 1 is four hours, not forty.

---

## Hiring option (if you want to skip DIY)

Day-one Figma master build is the only job worth outsourcing on a one-off basis. Everything else is too tied to fast turnarounds to hand off unless you have a retainer designer.

- **Budget:** £400–600 for a UK freelance Figma designer to build the master from `figma-spec.md` in ~14 hours
- **Where:** People Per Hour, Dribbble, or DM a junior from an agency you respect
- **Brief:** hand them `design-system.md` + `figma-spec.md` + a Figma link, nothing else
- **Deliverable:** one `.fig` file with all components, text styles, and Format 2 built slide-by-slide
- **After that:** you (or a VA) can run monthly refreshes yourself in 4 hours

Retainer option later: once the account is past 10k followers and posting more than one ranking per month, a part-time designer @ £800–1200/mo is worth it. Not before.

---

## Pre-publish checklist (every post)

Before anything goes into the scheduler:

- [ ] Position number is the biggest element on the frame
- [ ] compareSEO badge present
- [ ] Footer bar present with correct month/year
- [ ] Dark background (never light)
- [ ] Safe zone respected — nothing important in bottom 280px of reels
- [ ] Captions burned in on reels (don't rely on IG auto-captions)
- [ ] Agency tags applied in the asset itself, not just the caption
- [ ] Filename follows `cs-[format]-[slug]-[slide]-[YYYY-MM]` spec
- [ ] Exported at spec quality (PNG 1x for carousel, H.264 10Mbps for reel)
