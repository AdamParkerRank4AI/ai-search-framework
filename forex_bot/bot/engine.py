"""Event loop that ties strategy, risk, and broker together.

Used by both the backtester and the live/paper runner. Everything
runs bar-by-bar so there's no distinction between "simulated" and
"live" logic above this layer -- the only difference is where the
bars come from.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Callable, Iterable, List, Optional

from .broker import PaperBroker, Trade
from .data import Candle
from .risk import RiskConfig, size_position
from .strategy import Signal, Strategy


@dataclass
class EngineResult:
    trades: List[Trade]
    broker: PaperBroker


def run(
    bars: Iterable[Candle],
    strategy: Strategy,
    broker: PaperBroker,
    risk: RiskConfig,
    on_signal: Optional[Callable[[Candle, Signal], None]] = None,
    on_trade: Optional[Callable[[Trade], None]] = None,
) -> EngineResult:
    """Consume bars in order and run the pipeline.

    Order of operations per bar (this order avoids look-ahead):
      1. Broker processes the current bar for SL/TP against open positions.
      2. Strategy sees the bar and may emit a Signal.
      3. If a signal was emitted AND no position is open, it is queued
         for entry on the NEXT bar's open.
    """
    pending: Optional[Signal] = None

    for bar in bars:
        # 1. Fill pending entry at this bar's open (next-bar execution).
        if pending is not None and not broker.has_position():
            equity = broker.equity(bar.open)
            units = size_position(pending, equity, risk)
            if units != 0:
                broker.submit(pending, units, bar)
        pending = None

        # 2. Process SL/TP against this bar's range.
        closed = broker.on_bar(bar)
        if on_trade:
            for t in closed:
                on_trade(t)

        # 3. Let strategy see the bar; emit possible next-bar signal.
        sig = strategy.on_bar(bar)
        if sig is not None and not broker.has_position():
            if on_signal:
                on_signal(bar, sig)
            pending = sig

    return EngineResult(trades=list(broker.trades), broker=broker)
