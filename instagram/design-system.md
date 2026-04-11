# compareSEO Instagram Design System

The locked visual system for every ranking post. Nothing in here is up for debate post-to-post — consistency is the point. If a post doesn't look like it was built from this system, it doesn't ship.

> **Note:** Hex codes and typefaces below are placeholders. Replace with the finalised compareSEO palette before production. Any replacement is a one-time global find-and-replace.

---

## 1. Canvas and safe zones

| Surface | Size (px) | Ratio | Safe-zone top | Safe-zone bottom | Safe-zone left/right |
|---------|-----------|-------|---------------|------------------|----------------------|
| Reel / Story | 1080 × 1920 | 9:16 | 240 | 340 | 80 |
| Feed carousel | 1080 × 1350 | 4:5 | 80 | 80 | 80 |
| Feed single | 1080 × 1350 | 4:5 | 80 | 80 | 80 |
| Profile cover (highlight) | 1080 × 1920 | 9:16 | centre-circle 400px |

Anything critical — the position number, the score, the brand badge — must sit inside the safe zone. The bottom of a reel is covered by the username/caption/CTA overlay on some devices.

---

## 2. Colour palette

### Core (placeholders — replace with brand colours)

| Token | Hex | Use |
|-------|-----|-----|
| `--cs-bg` | `#0B0D10` | Background of every post. Near-black. |
| `--cs-surface` | `#14181D` | Card surfaces, slide backgrounds in multi-panel layouts. |
| `--cs-text` | `#F5F5F2` | Primary text. Off-white, never pure white. |
| `--cs-muted` | `#8A8F96` | Secondary labels, footers, timestamps. |
| `--cs-accent` | `#FFD23F` | Position numbers, #1 badge, the one pop colour. |
| `--cs-good` | `#3EE089` | "Riser" arrows on movers posts. |
| `--cs-bad` | `#FF5C5C` | "Dropper" arrows on movers posts. |

### Usage rules

- **Background is always near-black.** Instagram's feed is mostly white and light-mode. A dark feed post is a pattern interrupt.
- **One accent colour per post.** Yellow lives on the position number and nothing else.
- **Never gradient the background.** Flat colour only. Gradients read as low-effort stock templates.

---

## 3. Typography

Three typefaces max. Any more kills consistency.

| Role | Typeface (placeholder) | Weight | Use |
|------|------------------------|--------|-----|
| Display | `Söhne Breit` or `Neue Haas Grotesk Display` | 85 Bold | Position numbers, cover titles |
| Mono | `JetBrains Mono` or `IBM Plex Mono` | 500 Medium | Scores, methodology numbers, footer |
| Body | `Inter` or `Söhne` | 400 Regular / 600 SemiBold | Agency names, verdicts, captions |

### Type scale (reels / 1080 × 1920)

| Element | Size (px) | Line-height |
|---------|-----------|-------------|
| Position number (huge) | 720 | 1.0 |
| Cover title | 140 | 1.05 |
| Agency name | 96 | 1.1 |
| Verdict quote | 56 | 1.3 |
| Score | 72 (mono) | 1.0 |
| Footer / attribution | 32 | 1.4 |

### Type scale (carousel / 1080 × 1350)

| Element | Size (px) | Line-height |
|---------|-----------|-------------|
| Position number | 520 | 1.0 |
| Cover title | 120 | 1.05 |
| Agency name | 88 | 1.1 |
| Verdict quote | 48 | 1.3 |
| Score | 64 (mono) | 1.0 |
| Footer | 28 | 1.4 |

**Rule:** the position number is always the biggest thing on the slide. Always. This is the single visual device that makes compareSEO instantly recognisable in a feed.

---

## 4. The compareSEO ranking badge

This is the one asset every post shares. Think of it as the brand mnemonic.

```
   ╭─────────────╮
   │   compare   │
   │     SEO     │
   │  ─────────  │
   │    RANK     │
   │     #07     │     ← position number, mono, yellow
   ╰─────────────╯
```

**Specs:**
- 280 × 280 px circle on 9:16
- 220 × 220 px circle on 4:5
- Bottom-right of every slide unless the slide *is* the position (covers, spotlight reels)
- Always over solid background, never over imagery
- Never rotate, recolour or restyle

---

## 5. Grids and spacing

- **Base unit:** 8px. Every spacing value is a multiple of 8.
- **Column grid:** 6 columns, 40px gutter, 80px side margin (carousel). 4 columns, 48px gutter, 120px side margin (reel).
- **Vertical rhythm:** 80px between stacked text blocks. 40px inside grouped blocks.

---

## 6. Motion rules (reels only)

- **Cuts, not transitions.** Hard cuts between cards. No fades, no slides, no "whoosh" unless there's a matching SFX on the beat.
- **0.3s minimum hold** on any readable text. Faster and it's unreadable; slower and retention drops.
- **One animation per frame.** Either the number counts, or the text slides, or the badge pops — never more than one at once.
- **No stock motion graphics.** No particles, no "AI brain" 3D renders, no glitch effects. Flat, confident, text-first.

---

## 7. Sound rules (reels only)

- **Sound-off first.** Design every reel to work fully with the sound muted. Burn captions in — never rely on IG auto-captions.
- **One music bed per month.** Use the same trending audio across every reel in a month so the account builds auditory recognition too. Switch the first week of each month.
- **Voiceover optional.** Founder-led reels (Format 5) always have voiceover. Data reels (Formats 1 and 3) never do — let the numbers speak.

---

## 8. Photography and imagery

- **Zero stock photography.** Not ever. No handshakes, no laptops, no "AI brain" renders. This is a data brand.
- **Screen recordings only.** Live ChatGPT / Claude / Perplexity queries, Search Console screens, Rank4AI audit dashboards. All real.
- **Founder portrait** (Adam) — one approved headshot, black background, used only on Format 5 spotlight reels.

---

## 9. Do-not-do list

- ❌ Don't put the full ranking table in a single slide. Break it up.
- ❌ Don't use emojis in the position number area. Yellow mono number, full stop.
- ❌ Don't ship a post without the ranking badge.
- ❌ Don't use more than one accent colour.
- ❌ Don't use more than three typefaces.
- ❌ Don't put anything important in the bottom 280 px of a reel.
- ❌ Don't use light-mode backgrounds. Feed differentiation depends on dark.
- ❌ Don't rotate, skew or 3D the position number. It's always flat and centred.
- ❌ Don't use the Rank4AI logo and compareSEO badge together. Pick one per post — the audience needs to learn one brand at a time.

---

## 10. File naming and export

All Figma exports follow:

```
cs-[format]-[ranking-slug]-[slide]-[yyyy-mm].png

cs-cover-top10-ai-agencies-uk-01-2026-04.png
cs-carousel-top10-ai-agencies-uk-07-2026-04.png
cs-countdown-top10-ai-agencies-uk-2026-04.mp4
cs-spotlight-top10-ai-agencies-uk-2026-04.mp4
cs-movers-top10-ai-agencies-uk-03-2026-04.png
```

- Carousels export as PNG, not JPG. Text is crisper.
- Reels export at H.264, 1080 × 1920, 30 fps, 10 Mbps.
- All files dumped into `/compareSEO-IG/YYYY-MM/[ranking-slug]/` in the shared drive before scheduling.
