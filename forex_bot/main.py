"""Command-line entry point for the forex bot.

Subcommands:
  * backtest    -- run a strategy over historical CSV data.
  * demo        -- generate synthetic data and backtest on it (no network).
  * paper       -- tail a CSV as new rows arrive and trade against them.
  * walkforward -- run walk-forward validation over calendar months.
  * dashboard   -- regenerate the HTML dashboard from a saved tracker.

There is intentionally no ``live`` subcommand. To trade real money,
you must write a broker adapter yourself and edit this file to wire
it up. See the README for guidance.
"""

from __future__ import annotations

import argparse
import sys
import time
from pathlib import Path

from bot.broker import PaperBroker
from bot.daily_guard import DailyGuard, DailyGuardConfig, default_fx_sessions
from bot.dashboard import write_dashboard
from bot.data import CSVDataFeed, SyntheticDataFeed, write_csv
from bot.engine import run
from bot.journal import compute_metrics, format_metrics, write_trades_csv
from bot.risk import RiskConfig
from bot.strategy import build_strategy
from bot.tracker import Tracker
from bot.walkforward import (
    WalkForwardReport,
    make_month_windows,
    run_walk_forward,
)


# ---- common argument helpers ----------------------------------------


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--symbol", default="EURUSD")
    parser.add_argument("--equity", type=float, default=10_000.0)
    parser.add_argument("--risk-per-trade", type=float, default=0.01)
    parser.add_argument("--max-leverage", type=float, default=5.0)
    parser.add_argument("--spread", type=float, default=0.0001)
    parser.add_argument("--commission-per-unit", type=float, default=0.0)
    parser.add_argument("--strategy", default="ema_cross_rsi")
    parser.add_argument("--fast", type=int, default=12,
                        help="ema_cross_rsi only")
    parser.add_argument("--slow", type=int, default=26,
                        help="ema_cross_rsi only")
    parser.add_argument("--entry-period", type=int, default=20,
                        help="donchian_breakout only")
    parser.add_argument("--atr-mult", type=float, default=2.0)
    parser.add_argument("--rr", type=float, default=2.0)
    parser.add_argument("--trades-out", default=None,
                        help="Write closed trades to this CSV path.")


def _add_guard(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--daily-loss-cap", type=float, default=None,
                        help="Daily loss cap as a fraction of SoD equity (e.g. 0.02 for 2%%).")
    parser.add_argument("--daily-profit-target", type=float, default=None,
                        help="Daily profit target as a fraction of SoD equity (e.g. 0.01 for 1%%).")
    parser.add_argument("--sessions", default=None,
                        help="'default' for London+NY, or 'all' for 24/5.")


def _add_tracking(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--tracker-out", default=None,
                        help="Persist tracker state to this JSON path.")
    parser.add_argument("--dashboard-out", default=None,
                        help="Write an HTML dashboard to this path.")
    parser.add_argument("--tracker-label", default="default")


# ---- construction helpers -------------------------------------------


def _build_strategy(args):
    return build_strategy(
        args.strategy,
        fast_period=args.fast,
        slow_period=args.slow,
        entry_period=args.entry_period,
        atr_mult=args.atr_mult,
        rr_ratio=args.rr,
    )


def _build(args) -> tuple:
    strategy = _build_strategy(args)
    risk = RiskConfig(
        risk_per_trade=args.risk_per_trade,
        max_leverage=args.max_leverage,
    )
    broker = PaperBroker(
        symbol=args.symbol,
        starting_equity=args.equity,
        spread=args.spread,
        commission_per_unit=args.commission_per_unit,
    )
    return strategy, risk, broker


def _build_guard(args):
    if args.daily_loss_cap is None and args.daily_profit_target is None and args.sessions is None:
        return None
    sessions = []
    if args.sessions == "default" or args.sessions is None:
        sessions = default_fx_sessions()
    elif args.sessions == "all":
        sessions = []
    cfg = DailyGuardConfig(
        daily_loss_cap_pct=args.daily_loss_cap or 0.02,
        daily_profit_target_pct=args.daily_profit_target or 0.01,
        sessions=sessions,
    )
    return DailyGuard(cfg)


def _maybe_tracker(args) -> Tracker | None:
    if not (args.tracker_out or args.dashboard_out):
        return None
    return Tracker(label=args.tracker_label, starting_equity=args.equity)


def _emit_outputs(args, tracker, guard, trades) -> None:
    if args.trades_out:
        write_trades_csv(args.trades_out, trades)
        print(f"Wrote {len(trades)} trades to {args.trades_out}")
    if tracker is not None and args.tracker_out:
        tracker.save(args.tracker_out)
        print(f"Wrote tracker state to {args.tracker_out}")
    if tracker is not None and args.dashboard_out:
        hit_rates = guard.daily_hit_rates() if guard else None
        write_dashboard(args.dashboard_out, tracker, daily_hit_rates=hit_rates,
                        title=f"forex_bot: {args.tracker_label}")
        print(f"Wrote dashboard to {args.dashboard_out}")


# ---- subcommands -----------------------------------------------------


def cmd_backtest(args) -> int:
    feed = CSVDataFeed(args.csv)
    strategy, risk, broker = _build(args)
    guard = _build_guard(args)
    tracker = _maybe_tracker(args)
    result = run(feed, strategy, broker, risk, guard=guard, tracker=tracker)
    metrics = compute_metrics(result.trades, args.equity)
    print(format_metrics(metrics))
    if guard:
        print("\nDaily guard:", guard.daily_hit_rates())
    _emit_outputs(args, tracker, guard, result.trades)
    return 0


def cmd_demo(args) -> int:
    feed = SyntheticDataFeed(
        n_bars=args.bars,
        seed=args.seed,
        volatility=args.volatility,
        drift=args.drift,
    )
    bars = list(feed)
    if args.save:
        write_csv(args.save, bars)
        print(f"Saved {len(bars)} synthetic bars to {args.save}")
    strategy, risk, broker = _build(args)
    guard = _build_guard(args)
    tracker = _maybe_tracker(args)
    result = run(bars, strategy, broker, risk, guard=guard, tracker=tracker)
    metrics = compute_metrics(result.trades, args.equity)
    print(format_metrics(metrics))
    if guard:
        print("\nDaily guard:", guard.daily_hit_rates())
    _emit_outputs(args, tracker, guard, result.trades)
    return 0


def cmd_paper(args) -> int:
    path = Path(args.csv)
    if not path.exists():
        print(f"CSV does not exist: {path}", file=sys.stderr)
        return 2

    strategy, risk, broker = _build(args)
    guard = _build_guard(args)
    tracker = _maybe_tracker(args)

    warmup = list(CSVDataFeed(path))
    print(f"Warmup: replaying {len(warmup)} historical bars...")
    run(warmup, strategy, broker, risk, guard=guard, tracker=tracker)
    if warmup:
        print(f"Equity after warmup: {broker.equity(warmup[-1].close):.2f}")

    last_count = len(warmup)
    print(f"Tailing {path} (Ctrl-C to stop). poll={args.poll}s")
    try:
        while True:
            time.sleep(args.poll)
            bars = list(CSVDataFeed(path))
            if len(bars) <= last_count:
                continue
            new_bars = bars[last_count:]
            last_count = len(bars)
            run(new_bars, strategy, broker, risk, guard=guard, tracker=tracker)
            last = new_bars[-1]
            eq = broker.equity(last.close)
            print(
                f"[{last.timestamp.isoformat()}] close={last.close:.5f} "
                f"equity={eq:.2f} pos={'yes' if broker.has_position() else 'no'} "
                f"trades={len(broker.trades)}"
            )
            # Persist tracker on each tick so a crash doesn't lose history.
            if tracker and args.tracker_out:
                tracker.save(args.tracker_out)
            if tracker and args.dashboard_out:
                hit_rates = guard.daily_hit_rates() if guard else None
                write_dashboard(args.dashboard_out, tracker,
                                daily_hit_rates=hit_rates,
                                title=f"forex_bot: {args.tracker_label}")
    except KeyboardInterrupt:
        print("\nStopping.")
        metrics = compute_metrics(broker.trades, args.equity)
        print(format_metrics(metrics))
        _emit_outputs(args, tracker, guard, broker.trades)
    return 0


def cmd_walkforward(args) -> int:
    feed = CSVDataFeed(args.csv)
    bars = list(feed)
    if not bars:
        print("No bars in CSV.", file=sys.stderr)
        return 2
    windows = make_month_windows(bars)
    print(f"Running walk-forward over {len(windows)} monthly windows...")

    risk = RiskConfig(
        risk_per_trade=args.risk_per_trade,
        max_leverage=args.max_leverage,
    )
    report = run_walk_forward(
        bars=bars,
        windows=windows,
        strategy_factory=lambda: _build_strategy(args),
        risk=risk,
        symbol=args.symbol,
        starting_equity=args.equity,
        spread=args.spread,
        commission_per_unit=args.commission_per_unit,
    )
    s = report.summary()
    print("\nWalk-forward summary:")
    for k, v in s.items():
        print(f"  {k}: {v}")

    if args.report_out:
        import json as _json
        Path(args.report_out).parent.mkdir(parents=True, exist_ok=True)
        Path(args.report_out).write_text(_json.dumps(report.to_dict(), indent=2))
        print(f"\nWrote report to {args.report_out}")

    if args.dashboard_out:
        # Generate a dashboard from a dummy tracker plus the WF report.
        tracker = Tracker(label=args.tracker_label, starting_equity=args.equity)
        write_dashboard(args.dashboard_out, tracker, walk_forward=report,
                        title=f"walkforward: {args.tracker_label}")
        print(f"Wrote dashboard to {args.dashboard_out}")
    return 0


def cmd_fetch(args) -> int:
    """Pull real historical candles from OANDA's practice API into a CSV."""
    from bot.brokers.oanda import OandaError, fetch_candles_to_csv
    try:
        n = fetch_candles_to_csv(
            instrument=args.instrument,
            granularity=args.granularity,
            from_iso=args.frm,
            to_iso=args.to,
            out_path=args.out,
        )
    except OandaError as e:
        print(f"OANDA error: {e}", file=sys.stderr)
        return 2
    print(f"Wrote {n} bars to {args.out}")
    return 0


def cmd_dashboard(args) -> int:
    tracker = Tracker.load(args.tracker)
    report = None
    if args.walkforward:
        import json as _json
        data = _json.loads(Path(args.walkforward).read_text())
        report = WalkForwardReport()
        # Reconstruct window results from JSON for rendering.
        from bot.walkforward import WindowResult
        from datetime import datetime as _dt
        for w in data.get("windows", []):
            report.windows.append(WindowResult(
                label=w["label"],
                start=_dt.fromisoformat(w["start"]),
                end=_dt.fromisoformat(w["end"]),
                starting_equity=w["starting_equity"],
                final_equity=w["final_equity"],
                n_trades=w["n_trades"],
                win_rate=w["win_rate"],
                pnl=w["pnl"],
                max_drawdown=w["max_drawdown"],
            ))
    path = write_dashboard(args.out, tracker, walk_forward=report,
                           title=args.title or f"forex_bot: {tracker.label}")
    print(f"Wrote dashboard to {path}")
    return 0


# ---- arg parser ------------------------------------------------------


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="forex-bot", description="Paper-trading forex bot.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_bt = sub.add_parser("backtest", help="Backtest on a CSV of OHLCV bars.")
    p_bt.add_argument("csv")
    _add_common(p_bt); _add_guard(p_bt); _add_tracking(p_bt)
    p_bt.set_defaults(func=cmd_backtest)

    p_demo = sub.add_parser("demo", help="Backtest on synthetic data.")
    p_demo.add_argument("--bars", type=int, default=2000)
    p_demo.add_argument("--seed", type=int, default=42)
    p_demo.add_argument("--volatility", type=float, default=0.0008)
    p_demo.add_argument("--drift", type=float, default=0.0)
    p_demo.add_argument("--save", default=None, help="Optional: dump bars to CSV.")
    _add_common(p_demo); _add_guard(p_demo); _add_tracking(p_demo)
    p_demo.set_defaults(func=cmd_demo)

    p_paper = sub.add_parser("paper", help="Paper-trade by tailing a CSV.")
    p_paper.add_argument("csv")
    p_paper.add_argument("--poll", type=float, default=5.0)
    _add_common(p_paper); _add_guard(p_paper); _add_tracking(p_paper)
    p_paper.set_defaults(func=cmd_paper)

    p_wf = sub.add_parser("walkforward",
                          help="Walk-forward validation over calendar-month windows.")
    p_wf.add_argument("csv")
    p_wf.add_argument("--report-out", default=None,
                      help="Write walk-forward report JSON here.")
    p_wf.add_argument("--dashboard-out", default=None,
                      help="Write an HTML dashboard here.")
    p_wf.add_argument("--tracker-label", default="walkforward")
    _add_common(p_wf)
    p_wf.set_defaults(func=cmd_walkforward)

    p_fetch = sub.add_parser("fetch",
                             help="Fetch historical candles from OANDA practice API into CSV.")
    p_fetch.add_argument("--instrument", required=True,
                         help="OANDA format, e.g. EUR_USD, XAU_USD, GBP_USD.")
    p_fetch.add_argument("--granularity", default="H1",
                         help="M1/M5/M15/M30/H1/H4/D (default H1).")
    p_fetch.add_argument("--from", dest="frm", required=True,
                         help="ISO-8601, e.g. 2023-01-01T00:00:00Z.")
    p_fetch.add_argument("--to", required=True,
                         help="ISO-8601, e.g. 2025-01-01T00:00:00Z.")
    p_fetch.add_argument("--out", required=True, help="Output CSV path.")
    p_fetch.set_defaults(func=cmd_fetch)

    p_dash = sub.add_parser("dashboard",
                            help="Render an HTML dashboard from a saved tracker.")
    p_dash.add_argument("tracker", help="Path to tracker JSON.")
    p_dash.add_argument("--out", required=True, help="HTML output path.")
    p_dash.add_argument("--walkforward", default=None,
                        help="Optional path to a walk-forward report JSON.")
    p_dash.add_argument("--title", default=None)
    p_dash.set_defaults(func=cmd_dashboard)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
