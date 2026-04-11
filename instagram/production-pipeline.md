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

**Fallback stack (if no Figma skills available):** do every static post in **Canva Pro**. You lose some pixel control but the templates exist.

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
