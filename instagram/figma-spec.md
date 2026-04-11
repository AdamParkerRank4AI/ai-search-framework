# Figma spec — compareSEO Instagram templates

A single Figma file. Every post in the system maps to one frame in this file. Hand this spec to a designer and they can build the master file in an afternoon.

---

## File structure

```
compareSEO-IG-system.fig
│
├── 00 · Foundations
│   ├── Colours (local styles: cs-bg, cs-surface, cs-text, cs-muted, cs-accent, cs-good, cs-bad)
│   ├── Type (local styles: Display/XL, Display/L, Mono/XL, Mono/L, Body/M, Body/S, Footer)
│   ├── Grid (9:16 and 4:5 layout grids saved as shared styles)
│   └── Components (compareSEO badge, footer bar, #-number block, score block, signal chip)
│
├── 01 · Cover reel (9:16)        ← Format 1
│   ├── Frame A (0.0–1.5s)
│   ├── Frame B (1.5–4.0s, animated)
│   ├── Frame C (3 & 2 blurred)
│   └── Frame D (outro)
│
├── 02 · Carousel (4:5)           ← Format 2
│   ├── Slide 01 — Cover
│   ├── Slide 02 — #10
│   ├── Slide 03 — #9
│   ├── Slide 04 — #8
│   ├── Slide 05 — #7
│   ├── Slide 06 — #6
│   ├── Slide 07 — #5
│   ├── Slide 08 — #4
│   ├── Slide 09 — #3
│   ├── Slide 10 — #2
│   ├── Slide 11 — #1  (inverted)
│   ├── Slide 12 — Methodology
│   └── Slide 13 — CTA
│
├── 03 · Countdown reel (9:16)    ← Format 3
│   ├── Card 10
│   ├── Card 9
│   ├── ...
│   └── Card 1
│
├── 04 · Criteria carousel (4:5)  ← Format 4
│   ├── Slide 1 — Cover
│   ├── Slide 2 — 5 signals
│   ├── Slide 3 — Signal 01
│   ├── Slide 4 — Signal 02
│   ├── Slide 5 — Signal 03
│   ├── Slide 6 — Signal 04
│   ├── Slide 7 — Signal 05
│   └── Slide 8 — CTA
│
├── 05 · #1 spotlight (9:16)      ← Format 5
│   └── Static end-card + lower-thirds (video edited outside Figma)
│
├── 06 · Movers (4:5)              ← Format 6
│   ├── Slide 1 — Cover
│   ├── Slide 2 — Riser
│   ├── Slide 3 — Dropper
│   ├── Slide 4 — New
│   ├── Slide 5 — Out
│   └── Slide 6 — CTA
│
└── 07 · Stories (9:16)           ← Format 7
    ├── Frame 1 — Question
    ├── Frame 2 — Poll
    ├── Frame 3 — Quiz
    ├── Frame 4 — Countdown
    └── Frame 5 — Link
```

---

## Components to build first

Build these five components before touching any frames. Every frame in the system reuses them.

### 1. `cs/badge`
- Variants: `position=01 … 10`, `state=default | invert`
- Properties: `position` (text), `invert` (boolean)
- Size: 280×280 (9:16) or 220×220 (4:5) — two sizes, one per canvas

### 2. `cs/score-block`
- Displays `[score] / 100` in mono
- Variants: `size=L | XL`, `tone=default | good | bad`

### 3. `cs/signal-chip`
- Small label for "Top signal: X" and "Weak spot: Y"
- Variants: `tone=positive | negative`

### 4. `cs/footer-bar`
- Horizontal bar at the bottom of every slide/frame
- Content: `compareseo.co.uk · updated [MMM YYYY] · by Rank4AI`
- Auto-layout: full width, 80 px tall

### 5. `cs/position-number`
- The huge position number that dominates every ranking frame
- Variants: `size=reel | carousel`
- Text property: `n`

---

## Shared text styles

| Style | Typeface | Weight | Size (reel) | Size (carousel) | Line-height |
|-------|----------|--------|-------------|-----------------|-------------|
| Display/XL | Söhne Breit | 85 Bold | 720 | 520 | 1.0 |
| Display/L | Söhne Breit | 85 Bold | 140 | 120 | 1.05 |
| Agency/XL | Inter | 600 SemiBold | 96 | 88 | 1.1 |
| Mono/XL | JetBrains Mono | 500 Medium | 72 | 64 | 1.0 |
| Body/M | Inter | 400 Regular | 56 | 48 | 1.3 |
| Footer | JetBrains Mono | 500 Medium | 32 | 28 | 1.4 |

---

## Layout grids

### 9:16 (reels / stories)
- Columns: 4
- Gutter: 48 px
- Margin: 120 px
- Safe top: 240 px
- Safe bottom: 340 px

### 4:5 (feed carousels)
- Columns: 6
- Gutter: 40 px
- Margin: 80 px
- Safe top/bottom: 80 px each

Save each as a Figma layout grid style and apply to every frame.

---

## Export pipeline

1. Every frame is placed in a top-level page matching its format.
2. Every frame is named exactly as the filename spec:
   `cs-[format]-[ranking-slug]-[slide]-[YYYY-MM]`
3. Batch export: PNG at 1x for carousels, MP4 via After Effects/CapCut import for reels.
4. Export destination: `/compareSEO-IG/YYYY-MM/[ranking-slug]/`

---

## Hand-off checklist for the designer

- [ ] Create the file and the 8 pages above
- [ ] Build the 5 components first
- [ ] Build the 4 colour styles and 7 text styles
- [ ] Build Format 1 (cover reel) end to end — this is the most complex, surfacing issues early
- [ ] Build Format 2 (carousel) — all 13 slides with components swapped to live data
- [ ] Duplicate the file, rename to `compareSEO-IG-2026-04.fig` — this becomes the working file for April's ranking
- [ ] Every future month: duplicate the working file, update the data, export

---

## Time budget (first build)

| Step | Hours |
|------|-------|
| Component library | 3 |
| Format 1 cover reel | 1.5 |
| Format 2 carousel | 3 |
| Format 3 countdown | 2 |
| Format 4 criteria carousel | 2 |
| Format 5 spotlight end-card | 0.5 |
| Format 6 movers carousel | 1.5 |
| Format 7 stories | 1 |
| **Total** | **~14.5 hours** |

Every monthly refresh after month 1: **~3 hours** of design work to swap data into templates.
