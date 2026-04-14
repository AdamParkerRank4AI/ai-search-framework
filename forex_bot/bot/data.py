"""Market data loading.

Supports:
  * CSV files with columns: timestamp, open, high, low, close, volume
  * A deterministic synthetic generator (for demos / tests only)

Intentionally does NOT ship a live market-data client. If you want live
data, plug in your broker's data feed via a subclass of ``DataFeed``.
"""

from __future__ import annotations

import csv
import math
import random
from dataclasses import dataclass
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Iterable, Iterator, List, Optional


@dataclass(frozen=True)
class Candle:
    """A single OHLCV bar."""

    timestamp: datetime
    open: float
    high: float
    low: float
    close: float
    volume: float = 0.0

    def __post_init__(self) -> None:
        # Sanity check: high/low must bracket open/close.
        if self.high < max(self.open, self.close) or self.low > min(self.open, self.close):
            raise ValueError(
                f"Invalid candle at {self.timestamp}: "
                f"o={self.open} h={self.high} l={self.low} c={self.close}"
            )


class DataFeed:
    """Abstract iterable of candles."""

    def __iter__(self) -> Iterator[Candle]:  # pragma: no cover - interface only
        raise NotImplementedError


class CSVDataFeed(DataFeed):
    """Load candles from a CSV file.

    Expected columns (case-insensitive): timestamp, open, high, low, close, volume.
    Timestamps are parsed as ISO-8601. Missing volume defaults to 0.
    """

    def __init__(self, path: str | Path):
        self.path = Path(path)
        if not self.path.exists():
            raise FileNotFoundError(self.path)

    def __iter__(self) -> Iterator[Candle]:
        with self.path.open(newline="") as fh:
            reader = csv.DictReader(fh)
            if reader.fieldnames is None:
                return
            field_map = {name.lower(): name for name in reader.fieldnames}
            required = {"timestamp", "open", "high", "low", "close"}
            missing = required - set(field_map)
            if missing:
                raise ValueError(f"CSV missing columns: {sorted(missing)}")
            for row in reader:
                yield Candle(
                    timestamp=_parse_ts(row[field_map["timestamp"]]),
                    open=float(row[field_map["open"]]),
                    high=float(row[field_map["high"]]),
                    low=float(row[field_map["low"]]),
                    close=float(row[field_map["close"]]),
                    volume=float(row.get(field_map.get("volume", ""), 0) or 0),
                )


class SyntheticDataFeed(DataFeed):
    """Deterministic random-walk generator for demos and tests.

    This is NOT a market simulator. It produces plausible-looking OHLC
    data so the pipeline can be exercised end-to-end without network.
    """

    def __init__(
        self,
        n_bars: int = 1000,
        start_price: float = 1.1000,
        seed: int = 42,
        drift: float = 0.0,
        volatility: float = 0.0008,
        start: Optional[datetime] = None,
        timeframe: timedelta = timedelta(hours=1),
    ):
        if n_bars <= 0:
            raise ValueError("n_bars must be positive")
        self.n_bars = n_bars
        self.start_price = start_price
        self.seed = seed
        self.drift = drift
        self.volatility = volatility
        self.start = start or datetime(2024, 1, 1, tzinfo=timezone.utc)
        self.timeframe = timeframe

    def __iter__(self) -> Iterator[Candle]:
        rng = random.Random(self.seed)
        price = self.start_price
        ts = self.start
        for _ in range(self.n_bars):
            # Log-normal-ish step with optional drift.
            step = rng.gauss(self.drift, self.volatility)
            new_price = max(price * math.exp(step), 1e-6)
            o = price
            c = new_price
            # High/low as a fraction of intrabar range.
            wick = abs(rng.gauss(0, self.volatility)) * price
            h = max(o, c) + wick
            l = min(o, c) - wick
            yield Candle(
                timestamp=ts,
                open=round(o, 5),
                high=round(h, 5),
                low=round(l, 5),
                close=round(c, 5),
                volume=0.0,
            )
            price = new_price
            ts = ts + self.timeframe


def load_candles(feed: DataFeed) -> List[Candle]:
    """Materialize a feed into a list. Convenience for backtests."""
    return list(feed)


def _parse_ts(value: str) -> datetime:
    value = value.strip()
    # Accept both with/without timezone.
    try:
        dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
    except ValueError as e:
        raise ValueError(f"Unparseable timestamp: {value!r}") from e
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=timezone.utc)
    return dt


def write_csv(path: str | Path, candles: Iterable[Candle]) -> None:
    """Write candles to a CSV. Useful for caching a synthetic feed."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["timestamp", "open", "high", "low", "close", "volume"])
        for c in candles:
            writer.writerow(
                [c.timestamp.isoformat(), c.open, c.high, c.low, c.close, c.volume]
            )
