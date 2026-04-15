"""OANDA v20 practice API: historical candles only.

Read-only. No order submission here. The goal is to let you pull
real historical data into the CSV format used by the rest of the
bot so walk-forward is tested on real prices, not synthetic.

Auth: set the env var ``OANDA_API_KEY`` to a practice (demo) API
token from https://www.oanda.com/demo-account/tpa/personal_token.

Usage:
    from bot.brokers.oanda import fetch_candles_to_csv
    fetch_candles_to_csv(
        instrument="EUR_USD",
        granularity="H1",
        from_iso="2022-01-01T00:00:00Z",
        to_iso="2024-01-01T00:00:00Z",
        out_path="data/EURUSD_H1.csv",
    )
"""

from __future__ import annotations

import csv
import json
import os
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable, Iterator, List, Optional

from ..data import Candle


# OANDA's practice environment host. Do NOT point this at the live
# environment without explicit code changes -- the live host returns
# different rate limits and will charge real spread.
PRACTICE_HOST = "https://api-fxpractice.oanda.com"

# The v20 candles endpoint paginates at 5000 candles per request.
_MAX_COUNT = 5000


class OandaError(RuntimeError):
    pass


def _request(url: str, api_key: str, params: dict) -> dict:
    query = urllib.parse.urlencode(params)
    full = f"{url}?{query}"
    req = urllib.request.Request(full, headers={
        "Authorization": f"Bearer {api_key}",
        "Accept-Datetime-Format": "RFC3339",
    })
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8")
    except urllib.error.HTTPError as e:
        body = e.read().decode("utf-8", errors="replace")
        raise OandaError(f"HTTP {e.code} from OANDA: {body[:500]}") from e
    except urllib.error.URLError as e:
        raise OandaError(f"Network error calling OANDA: {e}") from e
    return json.loads(body)


def _parse_candle(raw: dict) -> Optional[Candle]:
    if not raw.get("complete", False):
        # Skip incomplete (still-forming) candles.
        return None
    mid = raw.get("mid") or {}
    try:
        return Candle(
            timestamp=datetime.fromisoformat(raw["time"].replace("Z", "+00:00")),
            open=float(mid["o"]),
            high=float(mid["h"]),
            low=float(mid["l"]),
            close=float(mid["c"]),
            volume=float(raw.get("volume", 0) or 0),
        )
    except (KeyError, ValueError) as e:
        raise OandaError(f"Malformed candle: {raw} ({e})") from e


def fetch_candles(
    instrument: str,
    granularity: str,
    from_iso: str,
    to_iso: str,
    api_key: Optional[str] = None,
    host: str = PRACTICE_HOST,
    sleep_between: float = 0.2,
) -> Iterator[Candle]:
    """Yield candles from OANDA between ``from_iso`` and ``to_iso``.

    Paginates automatically. Only completed candles are yielded.
    Instrument format is OANDA's, e.g. ``EUR_USD``, ``XAU_USD``.
    Granularity: ``M1``, ``M5``, ``M15``, ``M30``, ``H1``, ``H4``, ``D``.
    """
    api_key = api_key or os.environ.get("OANDA_API_KEY")
    if not api_key:
        raise OandaError(
            "Set OANDA_API_KEY env var (a practice-account token from "
            "https://www.oanda.com/demo-account/tpa/personal_token)."
        )

    url = f"{host}/v3/instruments/{instrument}/candles"
    cursor = from_iso
    last_ts: Optional[str] = None
    while True:
        params = {
            "granularity": granularity,
            "price": "M",  # mid prices
            "from": cursor,
            "count": _MAX_COUNT,
        }
        data = _request(url, api_key, params)
        candles = data.get("candles", [])
        if not candles:
            break
        count_yielded = 0
        for raw in candles:
            if raw["time"] >= to_iso:
                return
            c = _parse_candle(raw)
            if c is None:
                continue
            if last_ts is not None and raw["time"] <= last_ts:
                continue
            last_ts = raw["time"]
            yield c
            count_yielded += 1
        if count_yielded == 0:
            break
        # Advance cursor to just after the last seen timestamp.
        last_dt = datetime.fromisoformat(last_ts.replace("Z", "+00:00"))
        cursor = (last_dt + timedelta(seconds=1)).isoformat().replace("+00:00", "Z")
        # Gentle rate limiting.
        time.sleep(sleep_between)


def fetch_candles_to_csv(
    instrument: str,
    granularity: str,
    from_iso: str,
    to_iso: str,
    out_path: str | Path,
    api_key: Optional[str] = None,
    host: str = PRACTICE_HOST,
    progress_every: int = 10_000,
) -> int:
    """Stream candles to a CSV. Returns the number of bars written."""
    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with out.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["timestamp", "open", "high", "low", "close", "volume"])
        for c in fetch_candles(instrument, granularity, from_iso, to_iso,
                               api_key=api_key, host=host):
            writer.writerow(
                [c.timestamp.isoformat(), c.open, c.high, c.low, c.close, c.volume]
            )
            n += 1
            if n % progress_every == 0:
                print(f"  fetched {n} bars... (last {c.timestamp.isoformat()})")
    return n
