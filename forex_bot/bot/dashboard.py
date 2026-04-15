"""Static HTML dashboard generator.

Produces a single self-contained HTML file that reads nothing at
runtime and uses no JavaScript frameworks. All charts are inline SVG.

The dashboard is intended to be re-generated after each tracking
session (or nightly in paper mode). Point a browser at the file.
"""

from __future__ import annotations

import html
from datetime import date, datetime
from pathlib import Path
from typing import Iterable, List, Optional, Sequence, Tuple

from .tracker import Tracker
from .walkforward import WalkForwardReport


# ---- SVG primitives (stdlib only) ------------------------------------


def _line_chart(
    points: Sequence[Tuple[float, float]],
    width: int = 800,
    height: int = 240,
    *,
    title: str = "",
    y_label: str = "",
    baseline: Optional[float] = None,
) -> str:
    if not points:
        return f'<svg viewBox="0 0 {width} {height}"></svg>'
    pad = 40
    xs = [p[0] for p in points]
    ys = [p[1] for p in points]
    xmin, xmax = min(xs), max(xs)
    ymin, ymax = min(ys), max(ys)
    if baseline is not None:
        ymin = min(ymin, baseline)
        ymax = max(ymax, baseline)
    if xmax == xmin:
        xmax = xmin + 1
    if ymax == ymin:
        ymax = ymin + 1

    def sx(v: float) -> float:
        return pad + (v - xmin) / (xmax - xmin) * (width - 2 * pad)

    def sy(v: float) -> float:
        return height - pad - (v - ymin) / (ymax - ymin) * (height - 2 * pad)

    d = " ".join(
        f"{'M' if i == 0 else 'L'} {sx(x):.2f} {sy(y):.2f}"
        for i, (x, y) in enumerate(points)
    )

    baseline_line = ""
    if baseline is not None:
        by = sy(baseline)
        baseline_line = (
            f'<line x1="{pad}" y1="{by:.2f}" x2="{width - pad}" y2="{by:.2f}" '
            f'stroke="#888" stroke-dasharray="4 4" stroke-width="1"/>'
        )

    return f"""<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="{width}" height="{height}" fill="#0f1115"/>
  <text x="{pad}" y="20" fill="#ddd" font-size="14" font-family="monospace">{html.escape(title)}</text>
  <text x="8" y="{height / 2:.2f}" fill="#888" font-size="10"
        font-family="monospace" transform="rotate(-90 8 {height / 2:.2f})">{html.escape(y_label)}</text>
  {baseline_line}
  <path d="{d}" fill="none" stroke="#4ade80" stroke-width="1.5"/>
  <text x="{pad}" y="{height - 8}" fill="#666" font-size="10" font-family="monospace">
    {html.escape(str(ymin)[:10])} .. {html.escape(str(ymax)[:10])}
  </text>
</svg>"""


def _bar_chart(
    bars: Sequence[Tuple[str, float]],
    width: int = 800,
    height: int = 220,
    *,
    title: str = "",
) -> str:
    if not bars:
        return f'<svg viewBox="0 0 {width} {height}"></svg>'
    pad = 40
    values = [v for _, v in bars]
    vmax = max(values)
    vmin = min(values)
    if vmax == vmin:
        vmax = vmin + 1
    # Always include zero baseline.
    top = max(vmax, 0.0)
    bot = min(vmin, 0.0)
    if top == bot:
        top = bot + 1

    bar_w = (width - 2 * pad) / len(bars)

    def sy(v: float) -> float:
        return height - pad - (v - bot) / (top - bot) * (height - 2 * pad)

    y0 = sy(0.0)
    rects = []
    for i, (label, v) in enumerate(bars):
        x = pad + i * bar_w
        y = sy(v) if v >= 0 else y0
        h = abs(sy(v) - y0)
        color = "#4ade80" if v >= 0 else "#f87171"
        rects.append(
            f'<rect x="{x:.2f}" y="{y:.2f}" width="{bar_w * 0.8:.2f}" '
            f'height="{h:.2f}" fill="{color}"><title>{html.escape(label)}: {v:.4f}</title></rect>'
        )

    first_label = html.escape(bars[0][0])
    last_label = html.escape(bars[-1][0])

    return f"""<svg viewBox="0 0 {width} {height}" xmlns="http://www.w3.org/2000/svg">
  <rect x="0" y="0" width="{width}" height="{height}" fill="#0f1115"/>
  <text x="{pad}" y="20" fill="#ddd" font-size="14" font-family="monospace">{html.escape(title)}</text>
  <line x1="{pad}" y1="{y0:.2f}" x2="{width - pad}" y2="{y0:.2f}" stroke="#444" stroke-width="1"/>
  {''.join(rects)}
  <text x="{pad}" y="{height - 8}" fill="#666" font-size="10" font-family="monospace">{first_label}</text>
  <text x="{width - pad}" y="{height - 8}" fill="#666" font-size="10"
        font-family="monospace" text-anchor="end">{last_label}</text>
</svg>"""


# ---- page assembly ---------------------------------------------------


CSS = """
* { box-sizing: border-box; }
body { margin: 0; background: #0a0c10; color: #e4e4e7; font-family: -apple-system, Segoe UI, monospace; }
.container { max-width: 1100px; margin: 0 auto; padding: 24px; }
h1 { margin: 0 0 4px 0; font-size: 22px; }
.sub { color: #888; font-size: 13px; margin-bottom: 20px; }
.grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 12px; margin-bottom: 24px; }
.card { background: #15181f; border: 1px solid #23262e; border-radius: 6px; padding: 14px; }
.card .label { color: #888; font-size: 11px; text-transform: uppercase; letter-spacing: 0.5px; }
.card .value { font-size: 20px; font-weight: 600; margin-top: 4px; }
.good { color: #4ade80; }
.bad { color: #f87171; }
.neutral { color: #e4e4e7; }
.chart { background: #15181f; border: 1px solid #23262e; border-radius: 6px; padding: 12px; margin-bottom: 16px; }
table { width: 100%; border-collapse: collapse; font-size: 12px; background: #15181f; border-radius: 6px; overflow: hidden; }
th, td { padding: 8px 10px; text-align: left; border-bottom: 1px solid #23262e; }
th { background: #1b1e26; color: #aaa; font-weight: 500; }
tr:last-child td { border-bottom: none; }
.warning { background: #2a1a12; border: 1px solid #5a3020; color: #f5b082; padding: 14px; border-radius: 6px; margin-bottom: 24px; font-size: 13px; line-height: 1.5; }
"""


def _card(label: str, value: str, cls: str = "neutral") -> str:
    return (
        f'<div class="card"><div class="label">{html.escape(label)}</div>'
        f'<div class="value {cls}">{html.escape(value)}</div></div>'
    )


def _pct(x: float) -> str:
    return f"{x:+.2f}%"


def _money(x: float) -> str:
    return f"{x:,.2f}"


def _trades_table(trades, limit: int = 30) -> str:
    if not trades:
        return '<div class="card" style="grid-column: span 4;">No trades recorded yet.</div>'
    rows = []
    recent = trades[-limit:][::-1]
    for t in recent:
        cls = "good" if t.pnl >= 0 else "bad"
        rows.append(
            "<tr>"
            f"<td>{html.escape(t.exit_time[:19])}</td>"
            f"<td>{html.escape(t.symbol)}</td>"
            f"<td>{html.escape(t.side)}</td>"
            f"<td>{t.units:.2f}</td>"
            f"<td>{t.entry_price:.5f}</td>"
            f"<td>{t.exit_price:.5f}</td>"
            f"<td class='{cls}'>{t.pnl:+.2f}</td>"
            f"<td>{html.escape(t.exit_reason)}</td>"
            "</tr>"
        )
    return (
        "<table><thead><tr>"
        "<th>Exit time (UTC)</th><th>Symbol</th><th>Side</th>"
        "<th>Units</th><th>Entry</th><th>Exit</th><th>PnL</th><th>Reason</th>"
        "</tr></thead><tbody>"
        + "".join(rows)
        + "</tbody></table>"
    )


def _wf_table(report: WalkForwardReport) -> str:
    if not report.windows:
        return ""
    rows = []
    for w in report.windows:
        cls = "good" if w.return_pct >= 0 else "bad"
        rows.append(
            "<tr>"
            f"<td>{html.escape(w.label)}</td>"
            f"<td>{w.n_trades}</td>"
            f"<td>{w.win_rate * 100:.1f}%</td>"
            f"<td class='{cls}'>{w.return_pct:+.2f}%</td>"
            f"<td>{w.max_drawdown:,.2f}</td>"
            "</tr>"
        )
    s = report.summary()
    mean_cls = "good" if s.get("mean_return_pct", 0) >= 0 else "bad"
    summary_row = (
        f"<tr style='background:#1b1e26;font-weight:600'>"
        f"<td>mean / stdev</td><td>-</td><td>-</td>"
        f"<td class='{mean_cls}'>{s['mean_return_pct']:+.2f}% &#177; {s['stdev_return_pct']:.2f}%</td>"
        f"<td>-</td></tr>"
    )
    return (
        "<table><thead><tr>"
        "<th>Window</th><th>Trades</th><th>Win rate</th>"
        "<th>Return</th><th>Max DD</th>"
        "</tr></thead><tbody>"
        + "".join(rows)
        + summary_row
        + "</tbody></table>"
    )


def render(
    tracker: Tracker,
    *,
    walk_forward: Optional[WalkForwardReport] = None,
    daily_hit_rates: Optional[dict] = None,
    title: str = "forex_bot dashboard",
) -> str:
    s = tracker.summary()
    total_cls = "good" if s["total_return_pct"] >= 0 else "bad"
    dd_cls = "bad" if s["max_drawdown_pct"] > 0 else "neutral"

    # Equity curve points using timestamps as numeric x (seconds epoch).
    eq_points: List[Tuple[float, float]] = [
        (snap.timestamp.timestamp(), snap.equity) for snap in tracker.snapshots
    ]

    # Monthly returns bars.
    monthlies = [(m, r * 100) for m, r in tracker.monthly_returns()]

    pf = s["profit_factor"]
    pf_str = f"{pf:.2f}" if pf is not None else "inf"

    # Tracking progress toward the 2-year minimum.
    days = s["tracking_days"]
    target_days = 730  # 2 years
    progress_pct = min(days / target_days * 100, 100)

    warning = """
<div class="warning">
  <b>Read this before trusting anything on this page.</b><br>
  A backtest or short paper run is not evidence of a live edge. This
  dashboard exists so you can commit to a 2-year honest tracking
  period <i>before</i> funding real money. Metrics here should be
  viewed as a rolling log, not a forecast. Past performance is not
  predictive of future results. Most retail forex accounts lose
  money.
</div>
"""

    cards = [
        _card("Label", tracker.label),
        _card("Tracking days", f"{days} / {target_days}"),
        _card("Starting equity", _money(s["starting_equity"])),
        _card("Final equity", _money(s["final_equity"])),
        _card("Total return", _pct(s["total_return_pct"]), total_cls),
        _card("Max drawdown", _pct(s["max_drawdown_pct"]), dd_cls),
        _card("Trades", str(s["n_trades"])),
        _card("Win rate", f"{s['win_rate_pct']:.1f}%"),
        _card("Profit factor", pf_str),
        _card("Progress to 2y", f"{progress_pct:.1f}%"),
    ]

    if daily_hit_rates:
        cards.append(_card("Days trading", str(daily_hit_rates.get("days", 0))))
        cards.append(_card("Target days",
                           f"{daily_hit_rates.get('target_pct', 0):.1f}%", "good"))
        cards.append(_card("Loss-cap days",
                           f"{daily_hit_rates.get('loss_cap_pct', 0):.1f}%", "bad"))

    equity_chart = _line_chart(
        eq_points, title="Equity curve", y_label="equity",
        baseline=tracker.starting_equity,
    )
    monthly_chart = _bar_chart(monthlies, title="Monthly return (%)")

    wf_section = ""
    if walk_forward and walk_forward.windows:
        wf_section = (
            "<h2 style='font-size:16px;margin:24px 0 8px 0'>Walk-forward results</h2>"
            '<div class="chart">' + _wf_table(walk_forward) + "</div>"
        )

    generated = datetime.utcnow().strftime("%Y-%m-%d %H:%M UTC")

    return f"""<!doctype html>
<html><head>
<meta charset="utf-8">
<title>{html.escape(title)}</title>
<style>{CSS}</style>
</head><body>
<div class="container">
  <h1>{html.escape(title)}</h1>
  <div class="sub">Generated {generated} &middot; tracker &quot;{html.escape(tracker.label)}&quot;</div>

  {warning}

  <div class="grid">
    {''.join(cards)}
  </div>

  <div class="chart">{equity_chart}</div>
  <div class="chart">{monthly_chart}</div>

  {wf_section}

  <h2 style="font-size:16px;margin:24px 0 8px 0">Recent trades</h2>
  <div class="chart" style="padding:0">{_trades_table(tracker.trades)}</div>
</div>
</body></html>"""


def write_dashboard(
    path: str | Path,
    tracker: Tracker,
    *,
    walk_forward: Optional[WalkForwardReport] = None,
    daily_hit_rates: Optional[dict] = None,
    title: str = "forex_bot dashboard",
) -> Path:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        render(tracker, walk_forward=walk_forward,
               daily_hit_rates=daily_hit_rates, title=title),
        encoding="utf-8",
    )
    return path
