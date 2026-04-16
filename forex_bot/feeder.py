"""OANDA live data feeder.

Polls OANDA's practice API for the latest completed candle and
appends it to a CSV file. Run this alongside ``main.py paper`` to
get a real-time (well, bar-frequency) paper trading experience on
real prices without risking any money.

Usage:
    export OANDA_API_KEY=...
    python feeder.py --instrument EUR_USD --granularity H1 --out data/live.csv

This will:
  1. If the CSV doesn't exist, backfill the last ``warmup`` bars.
  2. Then poll every ``interval`` seconds for new completed bars.
  3. Append each new bar to the CSV (one row per bar, deduped).

Run in parallel with:
    python main.py paper data/live.csv --poll 60 --tracker-out runs/live.json --dashboard-out runs/dashboard.html

Ctrl-C to stop either process. The CSV is the shared interface.
"""

from __future__ import annotations

import argparse
import csv
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

from bot.brokers.oanda import PRACTICE_HOST, OandaError, _request, _parse_candle


def _last_timestamp(path: Path) -> str | None:
    """Return the ISO timestamp of the last row in the CSV, or None if empty/missing."""
    if not path.exists():
        return None
    last = None
    with path.open() as fh:
        reader = csv.DictReader(fh)
        for row in reader:
            last = row.get("timestamp")
    return last


def _append_bars(path: Path, bars: list) -> int:
    """Append bars to CSV. Creates file + header if needed. Returns count written."""
    exists = path.exists() and path.stat().st_size > 0
    n = 0
    with path.open("a", newline="") as fh:
        writer = csv.writer(fh)
        if not exists:
            writer.writerow(["timestamp", "open", "high", "low", "close", "volume"])
        for c in bars:
            writer.writerow([c.timestamp.isoformat(), c.open, c.high, c.low, c.close, c.volume])
            n += 1
    return n


def poll_once(
    instrument: str,
    granularity: str,
    api_key: str,
    host: str,
    since: str | None,
    count: int = 10,
) -> list:
    """Fetch the latest completed candles since ``since``."""
    url = f"{host}/v3/instruments/{instrument}/candles"
    params = {
        "granularity": granularity,
        "price": "M",
        "count": count,
    }
    if since:
        params["from"] = since
    data = _request(url, api_key, params)
    candles = []
    for raw in data.get("candles", []):
        c = _parse_candle(raw)
        if c is not None:
            candles.append(c)
    return candles


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        prog="feeder",
        description="Poll OANDA for new bars and append to CSV.",
    )
    ap.add_argument("--instrument", required=True, help="e.g. EUR_USD")
    ap.add_argument("--granularity", default="H1", help="M1/M5/M15/M30/H1/H4/D")
    ap.add_argument("--out", required=True, help="CSV path to append to.")
    ap.add_argument("--interval", type=int, default=60,
                    help="Seconds between polls (default 60).")
    ap.add_argument("--warmup", type=int, default=500,
                    help="If CSV is empty, backfill this many bars first.")
    ap.add_argument("--host", default=PRACTICE_HOST)
    args = ap.parse_args(argv)

    api_key = os.environ.get("OANDA_API_KEY")
    if not api_key:
        print("Set OANDA_API_KEY env var first.", file=sys.stderr)
        return 2

    path = Path(args.out)
    path.parent.mkdir(parents=True, exist_ok=True)

    # Warmup: if CSV is empty or doesn't exist, pull historical bars.
    last_ts = _last_timestamp(path)
    if last_ts is None:
        print(f"No existing data. Backfilling {args.warmup} bars...")
        try:
            bars = poll_once(args.instrument, args.granularity, api_key,
                             args.host, since=None, count=args.warmup)
        except OandaError as e:
            print(f"OANDA error during warmup: {e}", file=sys.stderr)
            return 2
        n = _append_bars(path, bars)
        print(f"Wrote {n} warmup bars to {path}")
        if bars:
            last_ts = bars[-1].timestamp.isoformat()
    else:
        print(f"Resuming from last timestamp: {last_ts}")

    # Seen timestamps to avoid duplicates.
    seen = set()
    if last_ts:
        seen.add(last_ts)

    print(f"Polling {args.instrument} every {args.interval}s. Ctrl-C to stop.")
    try:
        while True:
            time.sleep(args.interval)
            try:
                bars = poll_once(args.instrument, args.granularity, api_key,
                                 args.host, since=last_ts, count=10)
            except OandaError as e:
                print(f"  poll error (will retry): {e}", file=sys.stderr)
                continue
            new = [b for b in bars if b.timestamp.isoformat() not in seen]
            if new:
                n = _append_bars(path, new)
                for b in new:
                    seen.add(b.timestamp.isoformat())
                    last_ts = b.timestamp.isoformat()
                print(f"  [{datetime.now(timezone.utc).strftime('%H:%M:%S')}] "
                      f"+{n} bars, last={last_ts}")
            else:
                print(f"  [{datetime.now(timezone.utc).strftime('%H:%M:%S')}] "
                      f"no new bars yet")
    except KeyboardInterrupt:
        print("\nStopped.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
