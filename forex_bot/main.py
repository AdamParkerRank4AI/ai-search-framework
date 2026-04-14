"""Command-line entry point for the forex bot.

Subcommands:
  * backtest  -- run a strategy over historical CSV data.
  * demo      -- generate synthetic data and backtest on it (no network).
  * paper     -- tail a CSV as new rows arrive and trade against them.

There is intentionally no ``live`` subcommand. To trade real money,
you must write a broker adapter yourself and edit this file to wire
it up. See the README for guidance.
"""

from __future__ import annotations

import argparse
import json
import sys
import time
from pathlib import Path

from bot.broker import PaperBroker
from bot.data import CSVDataFeed, SyntheticDataFeed, write_csv
from bot.engine import run
from bot.journal import compute_metrics, format_metrics, write_trades_csv
from bot.risk import RiskConfig
from bot.strategy import build_strategy


def _add_common(parser: argparse.ArgumentParser) -> None:
    parser.add_argument("--symbol", default="EURUSD")
    parser.add_argument("--equity", type=float, default=10_000.0)
    parser.add_argument("--risk-per-trade", type=float, default=0.01)
    parser.add_argument("--max-leverage", type=float, default=5.0)
    parser.add_argument("--spread", type=float, default=0.0001)
    parser.add_argument("--commission-per-unit", type=float, default=0.0)
    parser.add_argument("--strategy", default="ema_cross_rsi")
    parser.add_argument("--fast", type=int, default=12)
    parser.add_argument("--slow", type=int, default=26)
    parser.add_argument("--atr-mult", type=float, default=2.0)
    parser.add_argument("--rr", type=float, default=2.0)
    parser.add_argument("--trades-out", default=None,
                        help="Write closed trades to this CSV path.")


def _build(args) -> tuple:
    strategy = build_strategy(
        args.strategy,
        fast_period=args.fast,
        slow_period=args.slow,
        atr_mult=args.atr_mult,
        rr_ratio=args.rr,
    )
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


def cmd_backtest(args) -> int:
    feed = CSVDataFeed(args.csv)
    strategy, risk, broker = _build(args)
    result = run(feed, strategy, broker, risk)
    metrics = compute_metrics(result.trades, args.equity)
    print(format_metrics(metrics))
    if args.trades_out:
        write_trades_csv(args.trades_out, result.trades)
        print(f"\nWrote {len(result.trades)} trades to {args.trades_out}")
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
    result = run(bars, strategy, broker, risk)
    metrics = compute_metrics(result.trades, args.equity)
    print(format_metrics(metrics))
    if args.trades_out:
        write_trades_csv(args.trades_out, result.trades)
    return 0


def cmd_paper(args) -> int:
    """Tail a CSV file and act on new rows.

    This is the closest thing to 'live' the bot ships. It does not
    connect to any broker; it just watches a file you (or a separate
    data feeder script) append to.
    """
    path = Path(args.csv)
    if not path.exists():
        print(f"CSV does not exist: {path}", file=sys.stderr)
        return 2

    strategy, risk, broker = _build(args)
    from bot.data import _parse_ts  # noqa: WPS436 -- small helper reuse
    from bot.data import Candle

    # Replay existing history to warm up indicators.
    feed = CSVDataFeed(path)
    warmup = list(feed)
    print(f"Warmup: replaying {len(warmup)} historical bars...")
    run(warmup, strategy, broker, risk)
    print(
        f"Equity after warmup: {broker.equity(warmup[-1].close if warmup else 0):.2f}"
    )

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
            run(new_bars, strategy, broker, risk)
            last = new_bars[-1]
            eq = broker.equity(last.close)
            print(
                f"[{last.timestamp.isoformat()}] close={last.close:.5f} "
                f"equity={eq:.2f} pos={'yes' if broker.has_position() else 'no'} "
                f"trades={len(broker.trades)}"
            )
    except KeyboardInterrupt:
        print("\nStopping.")
        metrics = compute_metrics(broker.trades, args.equity)
        print(format_metrics(metrics))
        if args.trades_out:
            write_trades_csv(args.trades_out, broker.trades)
    return 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(prog="forex-bot", description="Paper-trading forex bot.")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p_bt = sub.add_parser("backtest", help="Backtest on a CSV of OHLCV bars.")
    p_bt.add_argument("csv")
    _add_common(p_bt)
    p_bt.set_defaults(func=cmd_backtest)

    p_demo = sub.add_parser("demo", help="Backtest on synthetic data.")
    p_demo.add_argument("--bars", type=int, default=2000)
    p_demo.add_argument("--seed", type=int, default=42)
    p_demo.add_argument("--volatility", type=float, default=0.0008)
    p_demo.add_argument("--drift", type=float, default=0.0)
    p_demo.add_argument("--save", default=None, help="Optional: dump bars to CSV.")
    _add_common(p_demo)
    p_demo.set_defaults(func=cmd_demo)

    p_paper = sub.add_parser("paper", help="Paper-trade by tailing a CSV.")
    p_paper.add_argument("csv")
    p_paper.add_argument("--poll", type=float, default=5.0)
    _add_common(p_paper)
    p_paper.set_defaults(func=cmd_paper)

    args = ap.parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
