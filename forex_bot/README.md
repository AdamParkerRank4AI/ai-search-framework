# forex_bot

A small, transparent, **paper-trading-first** forex bot. Written to be
read, understood, and modified — not to be a black box.

## Read this first

- Retail FX/CFD is a zero-to-negative-sum game for most participants.
  Broker disclosures routinely show 70–85% of accounts lose money.
- Automating a strategy does not give it an edge. It just lets a bad
  strategy lose money faster and more reliably.
- Screenshots of huge monthly P/L on social media are overwhelmingly
  either cherry-picked, demo-account, or fabricated. Do not use them
  as a target.
- This bot ships with **no live broker adapter**. It runs on
  historical CSVs or synthetic data. Getting it to trade real money
  requires you to write broker integration code yourself. That is on
  purpose.

## What's in the box

```
forex_bot/
├── bot/
│   ├── data.py              # CSV + synthetic candle feeds (no network)
│   ├── indicators.py        # SMA, EMA, RSI, ATR (streaming)
│   ├── strategy.py          # EMA-cross + RSI and Donchian breakout
│   ├── risk.py              # Position sizing, hard risk caps
│   ├── daily_guard.py       # Daily loss cap + profit target + sessions
│   ├── broker.py            # Paper broker: entries, SL/TP, fills, trades
│   ├── brokers/oanda.py     # OANDA v20 historical-data fetcher (read-only)
│   ├── journal.py           # End-of-run metrics and CSV export
│   ├── engine.py            # Bar-by-bar event loop
│   ├── tracker.py           # Persistent equity/trade log for 2-year tracking
│   ├── walkforward.py       # Month-by-month walk-forward validator
│   └── dashboard.py         # Self-contained HTML dashboard (inline SVG)
├── tests/                   # 37 pytest tests
├── main.py                  # CLI: backtest|demo|paper|walkforward|fetch|dashboard
├── PLAYBOOK.md              # Operational plan with checkpoints
└── README.md
```

**Start here:** read `PLAYBOOK.md` before anything else. The code is
scaffolding; the playbook is the thing that keeps you honest.

## Install

```bash
# From the forex_bot/ directory:
python -m pip install pytest  # for tests only; the bot itself has no deps
python -m pytest tests/ -q
```

No numpy, no pandas, no broker SDK. Pure standard library.

## Usage

### 1. Synthetic demo (no data needed)

```bash
python main.py demo --bars 2000 --seed 5 --volatility 0.002
```

This generates a deterministic random walk, runs the sample strategy
on it, and prints metrics. If the bot returns a positive PnL on this,
that is noise, not skill — synthetic data has no edge to find.

### 2. Pull real data from OANDA

Open a free OANDA practice account, then generate a personal API
token. `export OANDA_API_KEY=...` and:

```bash
python main.py fetch --instrument EUR_USD --granularity H1 \
    --from 2023-01-01T00:00:00Z --to 2025-01-01T00:00:00Z \
    --out data/EURUSD_H1.csv
```

Pure stdlib — uses `urllib`, no `requests` or OANDA SDK dependency.
Only hits the practice host (`api-fxpractice.oanda.com`); edit the
source explicitly if you ever want to switch to live.

### 3. Backtest on your own CSV

CSV format (header row required, case-insensitive columns):

```
timestamp,open,high,low,close,volume
2024-01-01T00:00:00Z,1.10234,1.10250,1.10210,1.10245,0
...
```

```bash
python main.py backtest path/to/EURUSD_1h.csv \
    --symbol EURUSD \
    --equity 10000 \
    --risk-per-trade 0.01 \
    --max-leverage 5 \
    --spread 0.0001 \
    --trades-out trades.csv
```

### 4. Walk-forward validation (do this before trusting anything)

Tests the strategy month-by-month with no parameter tuning between
windows. Prints a summary: what fraction of months were positive,
mean/stdev of monthly returns, worst month.

```bash
python main.py walkforward path/to/EURUSD_1h.csv \
    --equity 100 \
    --report-out reports/wf.json \
    --dashboard-out reports/wf.html
```

Useful numbers to look at:
- `pct_positive_windows`: if this is near 50% and the mean is small,
  you have a coin flip, not a strategy.
- `return_over_stdev`: rough signal-to-noise ratio across months.
  Below ~0.3 is noise. Above ~1.0 is notable and probably overfit.
- `worst_return_pct`: assume you will live through this repeatedly.

### 5. Paper trade a live-ish feed

The `paper` subcommand tails a CSV file. A separate process (yours)
is expected to append new rows to that CSV as real bars close — e.g.
a small script that polls your broker's API every N seconds and
writes the latest bar.

```bash
python main.py paper live_feed.csv --poll 5
```

On startup the bot replays the existing rows to warm up the
indicators, then polls for new rows. Ctrl-C prints final metrics.

Enable persistent tracking + an auto-refreshing dashboard:

```bash
python main.py paper live_feed.csv \
    --poll 60 \
    --equity 100 \
    --daily-loss-cap 0.02 \
    --daily-profit-target 0.01 \
    --sessions default \
    --tracker-out  runs/live.json \
    --dashboard-out runs/dashboard.html \
    --tracker-label "eurusd-live-001"
```

`tracker.json` is append-only and survives restarts. The dashboard
is rewritten on each tick, so you can tail it in a browser.

### 6. Regenerate a dashboard from a saved tracker

```bash
python main.py dashboard runs/live.json \
    --out runs/dashboard.html \
    --walkforward reports/wf.json \
    --title "My bot -- year 1"
```

## Strategy

The shipped strategy (`ema_cross_rsi`) is deliberately simple so you
can read it in one sitting:

- Long when fast EMA crosses above slow EMA **and** RSI > 55.
- Short when fast EMA crosses below slow EMA **and** RSI < 45.
- Stop = entry ± `atr_mult × ATR`.
- Take profit at `rr_ratio × stop_distance`.
- One open position at a time.
- Position size such that a stop-out costs ~`risk_per_trade × equity`.

It is a baseline, not a recommendation. It exists to exercise the
plumbing. Replace it with your own `Strategy` subclass by implementing
`on_bar(bar) -> Optional[Signal]`.

## Risk defaults (and hard limits)

`bot/risk.py` enforces these:

| Setting              | Default | Hard cap                          |
|----------------------|---------|-----------------------------------|
| `risk_per_trade`     | 1%      | Raises `ValueError` above 5%.     |
| `max_leverage`       | 5x      | Configurable, but start low.      |
| `max_open_positions` | 1       | Enforced by the broker.           |

`bot/daily_guard.py` adds a day-level layer:

| Setting                   | Default | Hard cap                                  |
|---------------------------|---------|-------------------------------------------|
| `daily_loss_cap_pct`      | 2%      | Raises `ValueError` above 10%.            |
| `daily_profit_target_pct` | 1%      | Raises `ValueError` above 10%.            |
| `sessions`                | London + NY opens | Any, or empty for 24/5.         |

When the loss cap is hit, the bot closes any open position and refuses
new signals until the next UTC day. Same for the profit target: take
the win, go for a walk. Default FX sessions are London open
(07:00-11:00 UTC) and NY open (12:30-16:00 UTC).

## About "grow £100 by x% per day"

A common ask. The math (compounding daily from £100):

| Daily gain | After 1 year | After 2 years |
|------------|--------------|---------------|
| 1%/day     | £3,778       | £142,700      |
| 2%/day     | £137,000     | £188 million  |
| 5%/day     | £13 million  | £1.8 trillion |

This is not an edge anyone has, retail or institutional. Renaissance
Technologies' Medallion (the best hedge fund ever recorded) averages
~0.2%/day net, and it is closed to outside money because its capacity
is limited.

The bot therefore does not ship with a "grow x% per day" setting.
What it ships with instead is: daily loss cap, daily profit target,
and a dashboard that shows you honestly what fraction of days you
actually hit the target on your data. Run a year of walk-forward
and look at the `% target days` tile. If it's 8% on good data,
that's what "grow my account each day" really means in practice.

## Going live (what you would have to do)

1. Open a **demo** account with a regulated broker. Many offer REST
   or FIX APIs (e.g. OANDA v20, Interactive Brokers, IG, MT5 Python
   bridge). Stay on the demo account for months, not days.
2. Write a subclass of `PaperBroker` that overrides `submit`, `on_bar`,
   `equity`, `has_position`, `force_close_all` so each method talks to
   the real broker API instead of in-memory state. Match the semantics
   (e.g. next-bar execution, stop orders placed at submit time).
3. Write a data feeder that pushes the broker's real-time bars into
   the engine (or into the tailed CSV if you want to keep using the
   `paper` command).
4. Paper trade with the real broker for at least 3 months and compare
   to the backtest. If the live paper results diverge materially from
   the backtest, your backtest is lying to you (look-ahead bias,
   survivorship, optimistic fills, spread assumed too low, etc.).
5. Only after that — and with risk caps tightened, not loosened —
   would consider trickling **small** real money through it.

Steps 1–4 are the job. Step 5 is a footnote.

## What this bot will NOT do

- Double your account in a month. Anything advertising that is
  selling a course or a lead, not a system.
- Replace judgement about **whether** to trade at all. Most people who
  run this honestly for a quarter conclude they'd rather index.
- Recover from a strategy that has no edge. Garbage in, garbage out,
  at full CPU speed.

## License

Same as the parent repository.
