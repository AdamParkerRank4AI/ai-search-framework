# Operational playbook

A concrete plan for taking this from zero to a paper-verified system.
Follow the checkpoints. Do not skip them.

The rule behind the rules: **no real money moves until the dashboard
says yes, twice, on two different independent test windows**.

---

## Week 0 — Setup (half a day total)

- [ ] Clone the repo. `cd forex_bot && python -m pytest tests/ -q` — 37 tests must pass.
- [ ] Open an **OANDA practice (demo) account**. Takes 5 minutes, no ID.
- [ ] Generate an API token at `oanda.com/demo-account/tpa/personal_token`.
- [ ] `export OANDA_API_KEY=...` in your shell rc file.
- [ ] Decide one pair to focus on. Suggestion: start with `EUR_USD` because spreads are tight and data is clean. Gold (`XAU_USD`) is more volatile and more expensive to trade — come back to it later.

---

## Week 1 — Pull real data & run the baseline

```bash
# Two years of hourly EURUSD:
python main.py fetch --instrument EUR_USD --granularity H1 \
    --from 2023-01-01T00:00:00Z --to 2025-01-01T00:00:00Z \
    --out data/EURUSD_H1.csv
```

Then run walk-forward on both strategies:

```bash
python main.py walkforward data/EURUSD_H1.csv \
    --equity 100 --strategy ema_cross_rsi \
    --report-out reports/wf_ema.json \
    --dashboard-out reports/wf_ema.html

python main.py walkforward data/EURUSD_H1.csv \
    --equity 100 --strategy donchian_breakout --entry-period 20 \
    --report-out reports/wf_donchian.json \
    --dashboard-out reports/wf_donchian.html
```

**Checkpoint 1 — after week 1.** Look at the dashboards. For each strategy, check:

| Metric                  | Go            | No go                |
|-------------------------|---------------|----------------------|
| % positive months       | ≥ 55%         | ≤ 50%                |
| return / stdev          | ≥ 0.3         | < 0.2                |
| worst month             | ≥ -8%         | < -15%               |
| mean monthly return     | ≥ +0.5%       | ≤ 0% after fees      |

If **neither strategy passes**, that is information. Do not jam it through to the next step. Either:
- try the other pair (`XAU_USD`, `GBP_USD`), or
- try a different granularity (H4 tends to be less noisy than H1), or
- accept that the two baseline strategies don't have an edge on current data, and pause. This is the most common outcome.

---

## Weeks 2-3 — Tuning without cheating

Two knobs per strategy are acceptable to tune:
- EMA: `--fast` and `--slow`.
- Donchian: `--entry-period`.

**Do not** test dozens of combinations and pick the best — that is overfitting. The rule: try at most 3 settings per strategy. Record each result. Then lock the parameters.

If you cannot find parameters that pass **Checkpoint 1** in 3 attempts, the strategy does not work on this pair. Move on.

---

## Month 2-13 — Forward tracking (live demo paper trading)

This is the 12-month honest run. Cannot be shortcut.

Plug OANDA's practice account into a simple data-feeder script (~50 lines; ask me for one once you've picked your broker and confirmed API access). Point `main.py paper` at the CSV the feeder writes to. Tracker + dashboard update on every tick.

```bash
python main.py paper data/live_feed.csv --poll 60 \
    --equity 100 --strategy <the one you picked> \
    --daily-loss-cap 0.02 --daily-profit-target 0.01 \
    --sessions default \
    --tracker-out runs/live.json \
    --dashboard-out runs/dashboard.html \
    --tracker-label "eurusd-m2-m13"
```

### Running schedule

FX market runs 24/5 from Sunday 22:00 UTC to Friday 22:00 UTC. The bot runs whenever the feeder is running. The `--sessions default` flag restricts **entries** to London + NY opens (07:00-11:00 UTC and 12:30-16:00 UTC) because those are the liquid hours; the bot will still manage open positions outside those windows.

Practical setup:
- Run the feeder + bot on a cheap always-on machine (a £5/month VPS, a Raspberry Pi at home, or a small cloud VM). Laptop on the kitchen counter is fine for the demo phase.
- Keep the machine on UTC time. Do not worry about BST/GMT.

### Weekly ritual (every Sunday, 30 minutes)

- [ ] Open the dashboard. Screenshot the summary tiles.
- [ ] Export that week's tracker JSON to a dated backup folder.
- [ ] Sanity check: does the equity curve on live data still look like the one from the walk-forward, or has it diverged? **Divergence is the biggest warning sign.**
- [ ] If drawdown has exceeded the worst month in your walk-forward, stop the bot. Investigate before restarting.

### Monthly ritual (every 1st of the month, 1 hour)

- [ ] Re-run the walk-forward on data that now includes the most recent month.
- [ ] Compare the new walk-forward summary to last month's. Metric drift is normal; cliff drops are not.
- [ ] Update a simple spreadsheet: month / return / drawdown / trades / win rate. 12 rows after a year.

### Checkpoint 2 — month 6

- [ ] Live paper dashboard's `Total return` is positive **and** within 25% of the walk-forward expectation.
- [ ] Max drawdown < 15%.
- [ ] Tracker has recorded at least 20 trades.

If not, restart. Do not advance to month 7 with a broken system.

### Checkpoint 3 — month 12

- [ ] 12 full months recorded.
- [ ] Dashboard's `% positive months` ≥ 55%.
- [ ] Return / stdev ≥ 0.3 on the monthly return series.
- [ ] No single day's loss exceeded the daily cap (i.e. the cap did its job).
- [ ] You can explain every drawdown > 3% in writing.

---

## Month 13+ — Real money, tiny

Only if all three checkpoints cleared.

1. Fund the OANDA **live** account with exactly the amount you are fully willing to lose. For most people that's £100-500, not £5,000.
2. Write the live broker adapter (a subclass of `PaperBroker` that calls OANDA's order endpoints). This is deliberately left as work for you: it forces you to read OANDA's order-rejection rules, partial fills, margin calls, etc. before your money touches them.
3. Start at **half** your paper risk. If paper was 1% per trade, live starts at 0.5%.
4. First week: run for 7 days, then stop and compare real fills to what the paper bot would have recorded. Slippage + spread will always be worse than paper. Quantify the gap.
5. If the gap is within 25% of paper performance, continue at half size for another month.
6. Only after 2 months of live matching paper do you size up to the 1% paper risk.

### Red-line rules that apply from live day 1

- **Max drawdown 15%**: if live equity drops 15% from peak, everything stops, period. No revenge trading. No "one more attempt." You review, you fix, you paper-trade again for a month before restarting.
- **No manual overrides**: the entire point is to remove discretion. The day you start "helping" the bot is the day it stops being a system.
- **No increasing risk per trade without 3 consecutive profitable months** at the current risk level.
- **Withdraw 50% of every month's profit**. Bot money that stays in the bot becomes emotional. Move half out to a separate account you don't touch.

---

## Signs it's time to stop

- 3 consecutive losing months on real money.
- Drawdown > 15%.
- Live results diverge by > 25% from paper for a full month.
- You start changing rules mid-month to make results look better.
- You cannot reconstruct, from the tracker alone, why any individual trade was taken.

If any of these happen: pause, switch back to paper for at least 30 days. Diagnose in writing. Resume only after the paper run proves the fix.

---

## What success actually looks like

A boring log that shows:
- ~50-80 trades per year on H1 data (one pair, one strategy).
- Annual return in the high single digits to low-teens percentage.
- Max drawdown ≤ 15%.
- Monthly return distribution wider than you'd like, but with a mean clearly > 0.

This is not a fast track to wealth. It is a **skill** that, if built honestly, might earn you 10-15% a year net on small capital. At £100 starting equity, year 1 is £10-15. The learning is worth more than the money for the first two years.

If that's not what you're here for, go back to Option A from the earlier conversation — index ETF on autopilot. Zero shame in that.
