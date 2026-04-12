#!/usr/bin/env python3
"""
Render a compareSEO ranking JSON into Instagram-ready PNG slides,
stories, captions and a tag list.

Usage:
    python3 tools/render_ranking.py rankings/top-10-ai-seo-agencies-uk.json

Output is written to instagram/output/[slug]/ and contains:
    post-1-[NN]-[slide].png   Post 1 — cover + positions 10..6 + bridge
    post-2-[NN]-[slide].png   Post 2 — cover + positions 5..1 + CTA
    story-[NN]-[slide].png    Story frames (9:16), one per position
    captions.md               Ready-to-paste captions for each post
    tag-list.md               Placeholder tag list (fill handles as you verify)

Depends only on Pillow.
"""

from __future__ import annotations

import json
import os
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable

from PIL import Image, ImageDraw, ImageFont

# ---------------------------------------------------------------------------
# Brand system — match instagram/design-system.md
# ---------------------------------------------------------------------------

BG = (11, 13, 16)          # --cs-bg        near-black
SURFACE = (20, 24, 29)     # --cs-surface
TEXT = (245, 245, 242)     # --cs-text      off-white
MUTED = (138, 143, 150)    # --cs-muted
ACCENT = (255, 210, 63)    # --cs-accent    yellow
GOOD = (62, 224, 137)      # --cs-good
BAD = (255, 92, 92)        # --cs-bad

POST_SIZE = (1080, 1350)   # 4:5 feed carousel
STORY_SIZE = (1080, 1920)  # 9:16 reel / story

# Font paths (these exist on the Linux container)
FONT_DISPLAY = "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf"
FONT_SANS = "/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf"
FONT_SANS_BOLD = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
FONT_MONO = "/usr/share/fonts/truetype/dejavu/DejaVuSansMono-Bold.ttf"


# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------

@dataclass
class Entry:
    position: int
    name: str
    score: int | None = None
    verdict: str = ""
    top_signal: str = ""
    weak_spot: str = ""
    handle: str = ""  # optional IG handle for tagging


@dataclass
class Ranking:
    title: str
    region: str
    date: str
    slug: str
    entries: list[Entry]
    category_hashtag: str = "#aiseo"
    chip_top_label: str = "TOP"    # customisable: "TOP" for agencies, "ROLE" for people
    chip_bottom_label: str = "WEAK"  # customisable: "WEAK" for agencies, "FIND" for people

    @classmethod
    def from_json(cls, path: Path) -> "Ranking":
        data = json.loads(path.read_text())
        entries = [Entry(**e) for e in data["entries"]]
        return cls(
            title=data["title"],
            region=data.get("region", ""),
            date=data["date"],
            slug=data["slug"],
            entries=entries,
            category_hashtag=data.get("category_hashtag", "#aiseo"),
            chip_top_label=data.get("chip_top_label", "TOP"),
            chip_bottom_label=data.get("chip_bottom_label", "WEAK"),
        )


# ---------------------------------------------------------------------------
# Text drawing helpers
# ---------------------------------------------------------------------------

def font(path: str, size: int) -> ImageFont.FreeTypeFont:
    return ImageFont.truetype(path, size)


def text_size(draw: ImageDraw.ImageDraw, s: str, f: ImageFont.FreeTypeFont) -> tuple[int, int]:
    bbox = draw.textbbox((0, 0), s, font=f)
    return bbox[2] - bbox[0], bbox[3] - bbox[1]


def draw_centered(draw, s, f, y, color, canvas_w):
    w, _ = text_size(draw, s, f)
    draw.text(((canvas_w - w) / 2, y), s, font=f, fill=color)


def wrap_text(s: str, f: ImageFont.FreeTypeFont, max_width: int, draw: ImageDraw.ImageDraw) -> list[str]:
    """Very simple greedy word-wrap."""
    words = s.split()
    lines: list[str] = []
    current: list[str] = []
    for word in words:
        trial = " ".join(current + [word])
        w, _ = text_size(draw, trial, f)
        if w <= max_width or not current:
            current.append(word)
        else:
            lines.append(" ".join(current))
            current = [word]
    if current:
        lines.append(" ".join(current))
    return lines


def draw_footer(draw, canvas_w, canvas_h, date: str):
    """The footer bar that appears on every slide."""
    f = font(FONT_MONO, 24)
    line = f"compareseo.co.uk  ·  {date}  ·  by Rank4AI"
    w, h = text_size(draw, line, f)
    draw.text(((canvas_w - w) / 2, canvas_h - 60), line, font=f, fill=MUTED)


def draw_badge(draw, canvas_w, canvas_h, position: int):
    """The compareSEO RANK badge — circular, bottom-right."""
    size = 220
    x = canvas_w - size - 80
    y = canvas_h - size - 100
    draw.ellipse((x, y, x + size, y + size), outline=ACCENT, width=4)

    f_small = font(FONT_MONO, 22)
    f_pos = font(FONT_MONO, 54)

    label = "compareSEO"
    w, _ = text_size(draw, label, f_small)
    draw.text((x + (size - w) / 2, y + 40), label, font=f_small, fill=TEXT)

    rank_label = "RANK"
    w, _ = text_size(draw, rank_label, f_small)
    draw.text((x + (size - w) / 2, y + 72), rank_label, font=f_small, fill=MUTED)

    pos_text = f"#{position:02d}"
    w, _ = text_size(draw, pos_text, f_pos)
    draw.text((x + (size - w) / 2, y + 110), pos_text, font=f_pos, fill=ACCENT)


# ---------------------------------------------------------------------------
# Slide renderers
# ---------------------------------------------------------------------------

def render_cover(ranking: Ranking, subtitle: str, swipe_hint: str, size: tuple[int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size, BG)
    draw = ImageDraw.Draw(img)

    # Title stack
    f_label = font(FONT_MONO, 36)
    f_title = font(FONT_DISPLAY, 128 if w == 1080 and h == 1350 else 120)
    f_sub = font(FONT_MONO, 40)

    # "TOP 10" label
    label = subtitle.upper()
    draw_centered(draw, label, f_label, h * 0.22, ACCENT, w)

    # Main title (wrapped to fit)
    title_lines = wrap_text(ranking.title.upper(), f_title, w - 160, draw)
    y = h * 0.28
    for line in title_lines:
        draw_centered(draw, line, f_title, y, TEXT, w)
        y += f_title.size * 1.08

    # Region + date
    stamp = f"{ranking.region.upper()}  ·  {ranking.date.upper()}"
    draw_centered(draw, stamp, f_sub, y + 40, MUTED, w)

    # Swipe hint at the bottom
    f_swipe = font(FONT_SANS_BOLD, 44)
    draw_centered(draw, swipe_hint, f_swipe, h - 200, ACCENT, w)

    draw_footer(draw, w, h, ranking.date)
    return img


def render_entry(ranking: Ranking, entry: Entry, size: tuple[int, int],
                  chip_top: str = "TOP", chip_bottom: str = "WEAK") -> Image.Image:
    """One slide = one ranked entry. Number is the biggest element."""
    w, h = size
    img = Image.new("RGB", size, BG)
    draw = ImageDraw.Draw(img)

    # Huge position number — the hero visual
    pos_text = f"#{entry.position:02d}"
    pos_size = 480 if h == 1350 else 520
    f_pos = font(FONT_DISPLAY, pos_size)
    pw, ph = text_size(draw, pos_text, f_pos)
    draw.text(((w - pw) / 2, 60 if h == 1350 else 120), pos_text, font=f_pos, fill=ACCENT)

    # Agency name (wrapped)
    f_name = font(FONT_DISPLAY, 80 if h == 1350 else 96)
    name_lines = wrap_text(entry.name.upper(), f_name, w - 160, draw)
    y = 560 if h == 1350 else 740
    for line in name_lines:
        draw_centered(draw, line, f_name, y, TEXT, w)
        y += f_name.size * 1.08

    # Score
    if entry.score is not None:
        f_score = font(FONT_MONO, 56)
        score_text = f"{entry.score} / 100"
        draw_centered(draw, score_text, f_score, y + 30, ACCENT, w)
        y += 120

    # Verdict (wrapped, italicised via quotes)
    if entry.verdict:
        f_verdict = font(FONT_SANS, 44)
        verdict_lines = wrap_text(f'"{entry.verdict}"', f_verdict, w - 200, draw)
        for line in verdict_lines[:3]:  # cap at 3 lines
            draw_centered(draw, line, f_verdict, y, TEXT, w)
            y += f_verdict.size * 1.3

    # Signal chips
    if entry.top_signal or entry.weak_spot:
        f_chip = font(FONT_MONO, 26)
        chip_y = h - 220
        if entry.top_signal:
            draw.text((80, chip_y), f"{chip_top}  {entry.top_signal.upper()}", font=f_chip, fill=GOOD)
        if entry.weak_spot:
            draw.text((80, chip_y + 36), f"{chip_bottom} {entry.weak_spot.upper()}", font=f_chip, fill=MUTED)

    draw_footer(draw, w, h, ranking.date)
    return img


def render_bridge(ranking: Ranking, size: tuple[int, int]) -> Image.Image:
    """The 'swipe for the top 5' bridge slide between post 1 and post 2."""
    w, h = size
    img = Image.new("RGB", size, BG)
    draw = ImageDraw.Draw(img)

    f_huge = font(FONT_DISPLAY, 200)
    draw_centered(draw, "TOP 5", f_huge, h * 0.18, ACCENT, w)

    f_body = font(FONT_SANS_BOLD, 56)
    lines = ["NEXT POST:", "The top five", "will surprise you."]
    y = h * 0.42
    for line in lines:
        draw_centered(draw, line, f_body, y, TEXT, w)
        y += 80

    f_cta = font(FONT_MONO, 36)
    draw_centered(draw, "follow @compareaiseo for the drop →", f_cta, h - 220, MUTED, w)

    draw_footer(draw, w, h, ranking.date)
    return img


def render_cta(ranking: Ranking, size: tuple[int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size, BG)
    draw = ImageDraw.Draw(img)

    f_title = font(FONT_DISPLAY, 100)
    draw_centered(draw, "YOUR TURN.", f_title, h * 0.15, ACCENT, w)

    f_body = font(FONT_SANS_BOLD, 54)
    body = [
        "Want to see your own",
        "AI visibility score?",
        "",
        "Free audit,",
        "2 minutes,",
        "all four AI platforms.",
    ]
    y = h * 0.32
    for line in body:
        if line:
            draw_centered(draw, line, f_body, y, TEXT, w)
        y += 70

    f_link = font(FONT_MONO, 44)
    draw_centered(draw, "→ compareseo.co.uk", f_link, h - 260, ACCENT, w)
    draw_centered(draw, "link in bio", f_link, h - 200, MUTED, w)

    draw_footer(draw, w, h, ranking.date)
    return img


def render_methodology(ranking: Ranking, size: tuple[int, int]) -> Image.Image:
    w, h = size
    img = Image.new("RGB", size, BG)
    draw = ImageDraw.Draw(img)

    f_title = font(FONT_DISPLAY, 88)
    draw_centered(draw, "HOW WE RANK", f_title, h * 0.1, ACCENT, w)

    f_body = font(FONT_SANS, 40)
    lines = [
        "5 signal layers.",
        "17 audit sections.",
        "0 paid placements.",
        "",
        "01  Identity Clarity",
        "02  Subject Authority",
        "03  Meaning Architecture",
        "04  Ecosystem Validation",
        "05  Signal Consistency",
    ]
    y = h * 0.28
    for line in lines:
        if line:
            draw_centered(draw, line, f_body, y, TEXT if "0" in line[:2] else MUTED, w)
        y += 70

    f_meta = font(FONT_MONO, 32)
    draw_centered(draw, "full methodology → rank4ai.co.uk/methodology", f_meta, h - 220, MUTED, w)

    draw_footer(draw, w, h, ranking.date)
    return img


# ---------------------------------------------------------------------------
# Captions (ready to paste)
# ---------------------------------------------------------------------------

CAPTION_SIGNATURE = """\
──
compareSEO · independent rankings by Rank4AI
compareseo.co.uk"""

HASHTAG_SET = (
    "#aisearch #aiseo #llmseo #generativesearch #aeo "
    "#seotips #marketingstrategy #chatgpt #perplexity #founder"
)


def caption_post_1(r: Ranking) -> str:
    return f"""\
We ranked the {r.title.lower()} in the {r.region} right now. The #1 spot wasn't who we expected.

This is post 1 of 2 — positions 10 through 6.
The top 5 drops tomorrow. Save this so you don't miss it.

Independent ranking. No paid spots. Scored on AI Visibility, Citation Frequency and Signal Consistency across ChatGPT, Claude, Gemini and Perplexity.

→ Swipe for positions 10 to 6
→ Tomorrow: the top 5

{CAPTION_SIGNATURE}

{HASHTAG_SET} {r.category_hashtag}
"""


def caption_post_2(r: Ranking) -> str:
    return f"""\
The top 5. This is the post you've been waiting for.

Positions 5 → 1 on our independent {r.title} ranking ({r.region}, {r.date}).

If you missed yesterday's post, positions 10 → 6 are there.
If you want your own AI visibility score — free audit, link in bio.

→ Swipe for the top 5
→ Slide 7 is the methodology

{CAPTION_SIGNATURE}

{HASHTAG_SET} {r.category_hashtag}
"""


def caption_story() -> str:
    return """\
Stories sequence — use each PNG as one story frame, in order.
Add the Instagram "Link" sticker to frame 1 and the "Question" sticker
to the final frame ("Guess who's #1 next month?").

Every ranked account should be tagged via the @mention sticker
on their position frame — see tag-list.md.
"""


# ---------------------------------------------------------------------------
# Tag list
# ---------------------------------------------------------------------------

def tag_list(r: Ranking) -> str:
    out = [
        f"# Tag list — {r.title} ({r.region}, {r.date})",
        "",
        "Before posting:",
        "1. Follow each account from the compareSEO Instagram.",
        "2. Add an @mention sticker to each account's position slide.",
        "3. If no handle is set below, search Instagram manually and fill it in.",
        "",
        "| Pos | Agency | Handle | Followed? | Tagged? |",
        "|----:|--------|--------|:---------:|:-------:|",
    ]
    for e in r.entries:
        handle = f"@{e.handle}" if e.handle else "_(find me)_"
        out.append(f"| {e.position} | {e.name} | {handle} | [ ] | [ ] |")
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------

def render_all(r: Ranking, out_dir: Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    # Sort entries by position and split
    ordered = sorted(r.entries, key=lambda e: e.position)
    top_5 = [e for e in ordered if e.position <= 5]
    bottom_5 = [e for e in ordered if 6 <= e.position <= 10]

    # --- POST 1 — positions 10 → 6 (plus cover + bridge) ---
    post_1: list[Image.Image] = []
    post_1.append(render_cover(r, "TOP 10", "swipe for positions 10 → 6 →", POST_SIZE))
    for e in sorted(bottom_5, key=lambda e: -e.position):  # 10, 9, 8, 7, 6
        post_1.append(render_entry(r, e, POST_SIZE, r.chip_top_label, r.chip_bottom_label))
    post_1.append(render_bridge(r, POST_SIZE))

    for i, img in enumerate(post_1, start=1):
        img.save(out_dir / f"post-1-{i:02d}.png")

    # --- POST 2 — positions 5 → 1 (plus cover, methodology, CTA) ---
    post_2: list[Image.Image] = []
    post_2.append(render_cover(r, "TOP 5", "swipe for the top five →", POST_SIZE))
    for e in sorted(top_5, key=lambda e: -e.position):  # 5, 4, 3, 2, 1
        post_2.append(render_entry(r, e, POST_SIZE, r.chip_top_label, r.chip_bottom_label))
    post_2.append(render_methodology(r, POST_SIZE))
    post_2.append(render_cta(r, POST_SIZE))

    for i, img in enumerate(post_2, start=1):
        img.save(out_dir / f"post-2-{i:02d}.png")

    # --- STORIES — cover + one frame per entry + CTA ---
    stories: list[Image.Image] = []
    stories.append(render_cover(r, "TOP 10", "tap to see the full ranking →", STORY_SIZE))
    for e in ordered:
        stories.append(render_entry(r, e, STORY_SIZE, r.chip_top_label, r.chip_bottom_label))
    stories.append(render_cta(r, STORY_SIZE))

    for i, img in enumerate(stories, start=1):
        img.save(out_dir / f"story-{i:02d}.png")

    # --- CAPTIONS ---
    (out_dir / "captions.md").write_text(
        "# Captions — copy and paste into Instagram scheduler\n\n"
        "## Post 1 (positions 10 → 6)\n\n"
        f"{caption_post_1(r)}\n\n"
        "## Post 2 (positions 5 → 1)\n\n"
        f"{caption_post_2(r)}\n\n"
        "## Stories\n\n"
        f"{caption_story()}"
    )

    # --- TAG LIST ---
    (out_dir / "tag-list.md").write_text(tag_list(r))

    # --- SUMMARY ---
    print(f"\n✔ Rendered {r.title} ({r.region}, {r.date})")
    print(f"  → {out_dir}")
    print(f"    · {len(post_1)} slides   → post 1")
    print(f"    · {len(post_2)} slides   → post 2")
    print(f"    · {len(stories)} frames  → stories")
    print(f"    · captions.md, tag-list.md")


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        print("Usage: python3 tools/render_ranking.py rankings/<your-ranking>.json", file=sys.stderr)
        return 1

    ranking_path = Path(argv[1]).resolve()
    if not ranking_path.exists():
        print(f"Ranking file not found: {ranking_path}", file=sys.stderr)
        return 1

    r = Ranking.from_json(ranking_path)

    # Write to instagram/output/<slug>/ relative to the ranking file's parent-parent
    repo_instagram = ranking_path.parent.parent
    out_dir = repo_instagram / "output" / r.slug

    render_all(r, out_dir)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
