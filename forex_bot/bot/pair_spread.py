"""Multi-pair spread / mean-reversion strategy.

This captures the "trades between currencies" idea. The simplest
version: pick two correlated FX pairs, track the ratio (or spread)
between their prices, and bet on the spread reverting to its mean.

Example pairs that tend to be correlated:
  * EUR_USD and GBP_USD  (both vs dollar, both European)
  * AUD_USD and NZD_USD  (both commodity, both Oceania)
  * EUR_JPY and GBP_JPY  (both vs yen)

When the spread between them widens beyond a threshold, trade the
convergence: go long the cheap one, short the expensive one, exit
when the spread normalises.

This is conceptually a market-neutral strategy: you don't care if
the dollar goes up or down, only that the gap between the two pairs
narrows. That said, residual directional risk is always present.

Limitations:
  * The current bot engine runs one symbol at a time. This strategy
    operates on a SYNTHETIC spread series that you pre-compute from
    two CSVs. See ``build_spread_csv()`` below.
  * Transaction costs are doubled (you're always opening two legs).
"""

from __future__ import annotations

import csv
import math
from collections import deque
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Deque, List, Optional, Tuple

from .data import Candle, CSVDataFeed
from .indicators import SMA
from .strategy import Side, Signal, Strategy


@dataclass
class PairSpreadStrategy(Strategy):
    """Mean-reversion on the spread between two correlated pairs.

    The "spread" is pair_a.close / pair_b.close (the ratio). When
    this ratio deviates from its rolling mean by more than
    ``entry_z`` standard deviations, enter a convergence trade.
    Exit when the ratio returns within ``exit_z`` standard deviations.

    Trades are signalled on the SPREAD candle (see ``build_spread_csv``).
    The broker trades the spread as a single synthetic instrument; in
    real life you'd need to open two legs simultaneously.

    Parameters:
      * lookback: rolling window for mean + stdev of the ratio.
      * entry_z: z-score threshold to open a trade.
      * exit_z: z-score threshold to close a trade.
      * atr_period: ATR of the spread series for stop sizing.
      * atr_mult: stop distance in ATR units.
    """

    lookback: int = 60
    entry_z: float = 2.0
    exit_z: float = 0.5
    atr_period: int = 14
    atr_mult: float = 2.5

    name: str = "pair_spread"

    _buf: Deque[float] = field(default_factory=deque, init=False)
    _prev_z: Optional[float] = field(default=None, init=False)
    _in_trade: bool = field(default=False, init=False)
    _trade_side: Optional[Side] = field(default=None, init=False)

    def __post_init__(self) -> None:
        if self.lookback < 10:
            raise ValueError("lookback must be >= 10")
        if self.entry_z <= self.exit_z:
            raise ValueError("entry_z must be > exit_z")
        from .indicators import ATR
        self._atr = ATR(self.atr_period)

    def _zscore(self) -> Optional[float]:
        if len(self._buf) < self.lookback:
            return None
        mean = sum(self._buf) / len(self._buf)
        var = sum((x - mean) ** 2 for x in self._buf) / len(self._buf)
        std = math.sqrt(var)
        if std < 1e-10:
            return 0.0
        return (self._buf[-1] - mean) / std

    def on_bar(self, bar: Candle) -> Optional[Signal]:
        self._buf.append(bar.close)
        if len(self._buf) > self.lookback:
            self._buf.popleft()
        atr = self._atr.update(bar.high, bar.low, bar.close)
        z = self._zscore()
        if z is None or atr is None:
            return None

        signal: Optional[Signal] = None

        if not self._in_trade:
            # Spread is expensive (ratio above mean) -> short the spread
            # (short pair_a, long pair_b).
            if z >= self.entry_z:
                sl = bar.close + self.atr_mult * atr
                tp = bar.close - self.atr_mult * atr  # target: reversion
                signal = Signal(
                    side=Side.SELL,
                    price=bar.close,
                    stop_loss=sl,
                    take_profit=tp,
                    reason=f"spread z={z:.2f} >= {self.entry_z} (ratio high -> short spread)",
                )
                self._in_trade = True
                self._trade_side = Side.SELL
            # Spread is cheap (ratio below mean) -> long the spread.
            elif z <= -self.entry_z:
                sl = bar.close - self.atr_mult * atr
                tp = bar.close + self.atr_mult * atr
                signal = Signal(
                    side=Side.BUY,
                    price=bar.close,
                    stop_loss=sl,
                    take_profit=tp,
                    reason=f"spread z={z:.2f} <= -{self.entry_z} (ratio low -> long spread)",
                )
                self._in_trade = True
                self._trade_side = Side.BUY

        # Note: actual SL/TP exit is handled by the broker. We just
        # record the entry logic. The broker's on_bar checks SL/TP per
        # bar. When the trade closes, we reset.
        self._prev_z = z
        return signal

    def notify_trade_closed(self) -> None:
        """Called by the engine when a trade closes (SL/TP/forced)."""
        self._in_trade = False
        self._trade_side = None


# ---- Spread CSV builder ----------------------------------------------


def build_spread_csv(
    path_a: str | Path,
    path_b: str | Path,
    out_path: str | Path,
    label: str = "SPREAD",
) -> int:
    """Build a synthetic 'spread' CSV from two aligned OHLCV CSVs.

    Each bar's fields become pair_a / pair_b. Bars are matched by
    timestamp; any timestamp present in only one file is skipped.

    The output CSV can be fed to ``backtest`` or ``walkforward``
    just like a regular single-pair CSV.

    Returns the number of bars written.
    """
    bars_a = {c.timestamp: c for c in CSVDataFeed(path_a)}
    bars_b = {c.timestamp: c for c in CSVDataFeed(path_b)}
    common = sorted(set(bars_a) & set(bars_b))
    if not common:
        raise ValueError("No overlapping timestamps between the two CSVs.")

    out = Path(out_path)
    out.parent.mkdir(parents=True, exist_ok=True)
    n = 0
    with out.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["timestamp", "open", "high", "low", "close", "volume"])
        for ts in common:
            a = bars_a[ts]
            b = bars_b[ts]
            if b.open == 0 or b.high == 0 or b.low == 0 or b.close == 0:
                continue
            # Ratio: pair_a / pair_b.
            o = a.open / b.open
            h = max(a.high / b.low, a.open / b.open, a.close / b.close)
            l = min(a.low / b.high, a.open / b.open, a.close / b.close)
            c = a.close / b.close
            # Ensure OHLC consistency.
            h = max(h, o, c)
            l = min(l, o, c)
            writer.writerow([ts.isoformat(), round(o, 8), round(h, 8),
                             round(l, 8), round(c, 8), 0])
            n += 1
    return n
