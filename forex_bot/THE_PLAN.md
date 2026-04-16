# The Plan — In Plain English

## What we are building

A computer program that watches currency prices (like EUR/USD, GBP/USD,
gold) and decides when to buy and sell — without you having to sit at a
screen. It runs on your computer (or a cheap server), watches the market,
and makes trades automatically based on rules you can see and understand.

It is NOT a magic money printer. It is a tool. Like any tool, it works
if used properly and breaks things if used badly.

---

## Why "between currencies" works (and what that actually means)

You mentioned you used to have a bot that traded between currencies.
That approach has a name: **pair trading** or **spread trading**.

Here is the idea in plain English:

Imagine two mates, Dave and Steve, who always walk to the pub together.
Sometimes Dave walks a bit ahead, sometimes Steve does, but they always
end up roughly side by side because they're going to the same place.

EUR/USD and GBP/USD are Dave and Steve. They move in the same general
direction most of the time (because both are "European currency vs the
US dollar"). When one gets too far ahead of the other, you bet that
the gap will close:

- If EUR/USD has gone up a lot more than GBP/USD → sell EUR/USD, buy
  GBP/USD. Wait for the gap to close. Collect the difference.
- If GBP/USD has gone up a lot more than EUR/USD → sell GBP/USD, buy
  EUR/USD. Same thing.

You don't care if the dollar goes up or down. You only care that the
GAP between the two narrows. This is what makes it "lower risk" than
betting on one currency going in one direction — you're hedged.

**The catch:** sometimes Dave and Steve stop being mates. The
correlation breaks. Brexit was a good example — GBP went its own way
and the gap didn't close. When that happens, you lose. The strategy
has a stop-loss for this, but it's the main risk.

---

## The three strategies we've built (pick one or test all three)

### 1. EMA Crossover + RSI ("trend follower")

**What it does:** watches two moving averages of the price (a fast one
and a slow one). When the fast one crosses above the slow one and
momentum is strong → buy. When it crosses below → sell.

**In pub terms:** you're watching whether the crowd is moving toward
the bar or away from it, and joining whichever direction the crowd is
going.

**Strength:** catches big moves.
**Weakness:** gets chopped up in sideways markets, lots of small losses.

### 2. Donchian Breakout ("channel breakout")

**What it does:** tracks the highest high and lowest low over the last
20 bars. When price breaks above the high → buy. When it breaks below
the low → sell.

**In pub terms:** you're waiting for someone to shout. If the pub
suddenly gets louder than it's been all night, you join the
excitement. If it goes dead quiet, you leave.

**Strength:** catches explosive moves, historically the basis of the
famous "Turtle Traders" in the 1980s.
**Weakness:** lots of false breakouts, low win rate (you lose often
but win big when you win).

### 3. Pair Spread ("trades between currencies")

**What it does:** tracks the ratio between two correlated pairs (e.g.
EUR/USD ÷ GBP/USD). When the ratio deviates too far from its average
→ trade the convergence.

**In pub terms:** Dave and Steve. Bet they'll walk together again.

**Strength:** market-neutral (doesn't care about overall direction),
historically more consistent.
**Weakness:** when the correlation breaks, you're wrong on BOTH sides
at once.

---

## How the bot protects you (the safety net)

These are hard rules coded into the bot. They cannot be overridden
without editing the source code. That is deliberate.

| Rule | What it does |
|------|-------------|
| **1% risk per trade** | Each trade risks at most 1% of your account. If you have £100, the maximum you can lose on one trade is £1. |
| **Stop-loss on every trade** | Every single trade has a price where it automatically closes at a loss. No "hoping it comes back." |
| **Take-profit on every trade** | Every trade has a price where it automatically takes the win. No "let me hold for more." |
| **Daily loss cap (2%)** | If the bot loses 2% of your account in one day, it shuts down until tomorrow. |
| **Daily profit target (1%)** | If the bot makes 1% in one day, it banks it and stops. |
| **Trading hours only** | Only opens new trades during London (7am–11am) and New York (12:30pm–4pm) market hours. These are when spreads are tightest and liquidity is best. |
| **Single position** | One trade open at a time. No stacking. |
| **Max leverage 5x** | Even though brokers offer 30–500x, the bot caps at 5x. Higher leverage = bigger swings = blown account. |

---

## The three phases

### Phase 1: Backtest (no money, no account needed)

**What happens:** we download 2 years of real historical prices from
OANDA (free) and run the bot on them as if it had been trading live.
The bot doesn't know the future — it sees each bar one at a time,
just like it would in real life.

**What you learn:** does this strategy actually make money on real
data, or is it a coin flip? The walk-forward validator tests each
month independently so you can't accidentally cheat by optimising
for the past.

**Time needed:** one afternoon to set up and run.
**Money needed:** £0.

**Go/no-go checkpoint:** if the strategy isn't profitable on at
least 55% of months, with a mean monthly return above +0.5%, stop.
Try a different strategy or pair. Do not proceed to Phase 2.

### Phase 2: Paper trade on live prices (no real money)

**What happens:** the bot connects to OANDA's practice (demo) API.
Real prices, real spreads, real market conditions — but fake money.
A feeder script polls OANDA every 60 seconds and writes new price
bars to a file. The bot reads that file and trades against it.

A dashboard (HTML file you open in your browser) updates on every
tick. It shows your equity curve, win rate, monthly returns, and
how many days hit the daily target vs the daily loss cap.

**What you learn:** does the strategy still work when it's running
live, not on historical data? Slippage, spread widening during news,
gaps — all the things backtests don't capture.

**Time needed:** run it for 6-12 months. Check the dashboard once
a week (30 minutes). Monthly review (1 hour).
**Money needed:** still £0.

**Go/no-go checkpoints:**
- Month 6: total return positive AND within 25% of backtest results.
  Max drawdown < 15%. At least 20 trades recorded.
- Month 12: 55%+ positive months. Return/stdev ratio ≥ 0.3. You can
  explain every drawdown > 3%.

If either checkpoint fails, restart from Phase 1 with different
parameters or a different strategy. Do not put real money in.

### Phase 3: Real money, tiny

**What happens:** you open a live OANDA account and deposit exactly
what you're prepared to lose completely. £100. Not more. You write
a broker adapter (I'll help) that sends real orders.

Start at HALF the risk from paper trading. If paper was 1% per
trade, live starts at 0.5% per trade.

**What you learn:** real execution. Real emotions. Real slippage.

**Scaling rule:** after 2 consecutive profitable months at a given
risk level, you may increase risk by 0.25%. So 0.5% → 0.75% →
1.0%. Never above 2%.

**Red lines (non-negotiable):**
- Drawdown hits 15% → everything stops. Back to paper for 30 days.
- 3 consecutive losing months → stop. Review everything.
- You start overriding the bot manually → you've broken the system.
  Stop until you trust the system again.
- Withdraw 50% of profits each month. The rest compounds.

---

## What success actually looks like (honestly)

After a full year of live trading with £100:

| Scenario | Annual return | Year-end balance | Monthly avg |
|----------|-------------|-----------------|-------------|
| **Great** | 15-20% | £115-120 | +£1.25-1.67 |
| **Good** | 8-12% | £108-112 | +£0.67-1.00 |
| **Mediocre** | 0-5% | £100-105 | +£0-0.42 |
| **Bad** | -10 to -15% | £85-90 | -£0.83-1.25 |
| **Blown** | -100% | £0 | don't do this |

The "great" scenario on £100 is £20 profit in a year. That is not
life-changing money. The POINT of year one is to prove the system
works with real money, not to get rich. If year one works, year two
you deposit more. If year one doesn't work, you lost £100, not
£5,000.

At £1,000 with a proven 15% edge, you're looking at £150/year.
At £10,000, £1,500/year. It only becomes meaningful at scale, and
you only scale after proof.

---

## What's already built

| Component | Status | What it does |
|-----------|--------|-------------|
| Price data loader | Done | Reads CSV files of price bars |
| Synthetic data generator | Done | Fake price data for testing without network |
| OANDA data fetcher | Done | Pulls real historical prices (free demo API) |
| Live feeder | Done | Polls OANDA in real time, writes to CSV |
| Indicators (SMA, EMA, RSI, ATR) | Done | The maths the strategies use |
| Strategy 1: EMA crossover | Done | Trend-following strategy |
| Strategy 2: Donchian breakout | Done | Channel-breakout strategy |
| Strategy 3: Pair spread | Done | Trades-between-currencies strategy |
| Risk manager | Done | 1% per trade, leverage cap, position sizing |
| Daily guard | Done | Daily loss cap + profit target + session hours |
| Paper broker | Done | Simulated trading (fills, SL/TP, spread costs) |
| Backtester | Done | Run a strategy on historical data |
| Walk-forward validator | Done | Test month-by-month, no cheating |
| Equity tracker | Done | Logs every tick to JSON, survives restarts |
| HTML dashboard | Done | Equity curve, monthly returns, trade log |
| CLI (command line) | Done | Single entry point for all commands |
| 44 automated tests | Done | Proves the code works correctly |
| PLAYBOOK.md | Done | Operational plan with dated checkpoints |

| Component | Status | What it does |
|-----------|--------|-------------|
| Live OANDA broker adapter | NOT built | Places real orders (Phase 3 only) |
| Multi-pair simultaneous feeds | NOT built | Run spread strategy on live pairs |
| Telegram/email alerts | NOT built | Notify you when trades happen |

The "not built" items are Phase 3 features. We build them only when
the dashboard says the system works on paper.

---

## What you need to do right now

1. **Get an OANDA practice account.** Free. No money. No ID. Takes 5
   minutes. This gives you an API key to pull real price data.

2. **Tell me which pairs interest you.** EUR/USD + GBP/USD is the
   classic starter for pair spread. If you want gold, that's XAU/USD
   (single-pair strategies only, pair spread doesn't apply as well).

3. **Tell me if you can keep a machine running.** The feeder + bot
   for Phase 2 need to run during market hours. A laptop is fine for
   testing. A £5/month VPS or a Raspberry Pi is ideal for longer runs.

Once you've got the OANDA key, we pull the data and run the first
backtest. That's when you see real numbers on your three dashboards
and decide which strategy (if any) passes the first checkpoint.
