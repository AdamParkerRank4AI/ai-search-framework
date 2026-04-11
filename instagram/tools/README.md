# Render pipeline — compareSEO ranking → Instagram posts

One command. One JSON. A full Instagram ranking drop — two posts and a full stories sequence — rendered as ready-to-upload PNGs with matching captions and tag list. No Canva, no Figma, no CapCut for static content. You don't touch a design tool.

## The whole workflow

```
1. Paste a ranking into a JSON file         → rankings/<slug>.json
2. Run the script                           → python3 tools/render_ranking.py rankings/<slug>.json
3. Collect the output                       → output/<slug>/
4. Download PNGs to your phone, upload to Instagram, paste captions
```

That's the entire thing. Step 1 is ~5 minutes of typing/pasting. Step 2 is 10 seconds. Step 3 is a drag-and-drop. Step 4 is whatever your scheduler takes.

---

## Requirements

- Python 3.11+
- Pillow (`pip install Pillow`)

That's it. The fonts we use (DejaVu Sans, DejaVu Sans Mono, Liberation Sans) are baked into most Linux images and are also easy to install locally.

---

## The input format

Create a file in `rankings/` with the shape below. Look at `rankings/top-10-ai-seo-agencies-uk.json` as a reference.

```json
{
  "title": "Top 10 AI SEO Agencies",
  "region": "UK",
  "date": "April 2026",
  "slug": "top-10-ai-seo-agencies-uk",
  "category_hashtag": "#ukseoagency",
  "entries": [
    {
      "position": 1,
      "name": "Rise at Seven",
      "score": 94,
      "verdict": "They own entity clarity across all four AI platforms.",
      "top_signal": "Identity Clarity",
      "weak_spot": "Ecosystem",
      "handle": "riseatseven"
    }
    // ... 10 entries total
  ]
}
```

### Field rules

| Field | Required | Notes |
|---|---|---|
| `title` | yes | What goes on the cover slide. Keep to 2–4 words if possible. |
| `region` | yes | Short label ("UK", "US", "EMEA"). Shown next to the date. |
| `date` | yes | "April 2026". Shown in footer and cover. |
| `slug` | yes | URL-safe ID. Used as the output folder name. |
| `category_hashtag` | optional | One Instagram hashtag specific to the list (e.g. `#ukseoagency`). Appended to captions. |
| `entries[].position` | yes | Integer 1–10. |
| `entries[].name` | yes | Displayed uppercase. Long names wrap automatically. |
| `entries[].score` | optional | 0–100. Shown in mono under the name. |
| `entries[].verdict` | optional | One sentence, in quotes. Capped at ~3 lines. |
| `entries[].top_signal` | optional | Green chip at the bottom of the slide. |
| `entries[].weak_spot` | optional | Red chip below the green one. |
| `entries[].handle` | optional | Instagram handle without the `@`. Feeds the auto-generated tag list. |

### Adding a new ranking by pasting

When compareseo.co.uk publishes or updates a ranking, you can literally just paste the ten rows into a new JSON file. If it's easier, use a Google Sheet with the columns above, export as CSV, and paste into a new JSON — or ask Claude to transform your CSV into the JSON shape above.

---

## Running it

```bash
python3 instagram/tools/render_ranking.py instagram/rankings/top-10-ai-seo-agencies-uk.json
```

Expected output:
```
✔ Rendered Top 10 AI SEO Agencies (UK, April 2026)
  → instagram/output/top-10-ai-seo-agencies-uk
    · 7 slides   → post 1
    · 8 slides   → post 2
    · 12 frames  → stories
    · captions.md, tag-list.md
```

---

## What you get in the output folder

```
output/top-10-ai-seo-agencies-uk/
├── post-1-01.png   Cover — "TOP 10 AI SEO AGENCIES · UK · APRIL 2026"
├── post-1-02.png   #10
├── post-1-03.png   #9
├── post-1-04.png   #8
├── post-1-05.png   #7
├── post-1-06.png   #6
├── post-1-07.png   Bridge — "TOP 5 — next post"
│
├── post-2-01.png   Cover — "TOP 5"
├── post-2-02.png   #5
├── post-2-03.png   #4
├── post-2-04.png   #3
├── post-2-05.png   #2
├── post-2-06.png   #1
├── post-2-07.png   Methodology — "How we rank"
├── post-2-08.png   CTA — "Your turn — free audit"
│
├── story-01.png    Story cover
├── story-02.png    #1 story frame
├── story-03.png    #2 story frame
│    ...
├── story-11.png    #10 story frame
├── story-12.png    Story CTA
│
├── captions.md     Full captions for post 1, post 2, and stories
└── tag-list.md     Checklist of handles to follow + tag
```

All carousel slides are 1080×1350 PNG. All story frames are 1080×1920 PNG. Both are exactly Instagram's recommended sizes — no resizing needed.

---

## The posting workflow

### The day before
1. **Download the output folder** to your phone (AirDrop, Google Drive, or just SSH)
2. **Open `tag-list.md`** — follow every handle listed from the compareSEO Instagram account

### Post day 1 — positions 10 → 6
1. Open Instagram → new post → select all 7 `post-1-*.png` files in order
2. Paste the "Post 1" caption from `captions.md`
3. Tag each agency's @-handle on their position slide using Instagram's tag tool
4. Publish

### Post day 2 — positions 5 → 1
1. Same as day 1, with `post-2-*.png` and the "Post 2" caption
2. Tag @-handles on slides 2–6 (#5 through #1)
3. Publish

### Stories
1. Upload `story-01.png` → `story-12.png` as a story series, in order
2. Add a **Question** sticker to frame 1: "Guess who's #1 next month?"
3. Add a **Link** sticker to frame 12: `compareseo.co.uk/audit`
4. Add an **@mention** sticker to each position frame, matching `tag-list.md`

---

## Changing the brand system

Every colour, font size, and layout decision lives in the top of `render_ranking.py`. Edit the constants, re-run, done.

```python
BG = (11, 13, 16)          # background
TEXT = (245, 245, 242)     # primary text
ACCENT = (255, 210, 63)    # yellow — position numbers, highlights
...
```

For bigger structural changes (new slide types, different post splits), edit the `render_*` functions near the bottom of the file. Each one is self-contained and only knows about Pillow — no other dependencies.

---

## When this breaks

- **Long agency names truncate / look cramped** → shorten `name` in the JSON, or lower `f_name` size at the top of `render_entry`.
- **Verdict runs off the slide** → cap to ~100 characters. The script already truncates to 3 wrapped lines.
- **Score renders as `94.0`** → set `score` as an integer in the JSON, not a float.
- **Font missing on your machine** → install `fonts-dejavu` and `fonts-liberation` (Debian/Ubuntu) or `brew install --cask font-dejavu` (macOS).

---

## Why this file instead of Canva

You already know this — you told me you hate design tools. This pipeline is the alternative:

- **You never open a design app.** Everything is code.
- **Monthly refresh** = edit one JSON + re-run one command. ~2 minutes.
- **Any change to the brand system propagates to every slide at once** — edit a hex code, every post is rebuilt.
- **Version control.** Every ranking is a file in git. You can diff rankings month-over-month to see who moved.
- **Zero recurring cost.** No Canva Pro, no Figma subscription.

The trade-off is flexibility — a designer can do things Pillow can't (complex gradients, logos integrated into layouts, cinematic text treatments). But the point isn't to win design awards. The point is to ship 7 slides a week, every week, for a year, on brand, for free.
