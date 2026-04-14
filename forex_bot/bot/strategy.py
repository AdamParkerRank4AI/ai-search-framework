"""Strategy framework and a sample strategy.

A Strategy takes bars one at a time and emits Signals. It does NOT
know about money, position size, or the broker; those concerns live
in the risk manager and broker modules.

The sample strategy (``EmaCrossRsiStrategy``) is intentionally simple
and transparent. It is here to exercise the pipeline, not because it
has any edge. Do not trade real money off it.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum
from typing import List, Optional

from .data import Candle
from .indicators import ATR, EMA, RSI


class Side(str, Enum):
    BUY = "BUY"
    SELL = "SELL"


@dataclass(frozen=True)
class Signal:
    """A trading signal emitted by a strategy."""

    side: Side
    price: float  # reference price (usually the close)
    stop_loss: float  # absolute price level
    take_profit: float  # absolute price level
    reason: str = ""


class Strategy:
    """Abstract base class. Override ``on_bar``."""

    name: str = "base"

    def on_bar(self, bar: Candle) -> Optional[Signal]:  # pragma: no cover
        raise NotImplementedError


@dataclass
class EmaCrossRsiStrategy(Strategy):
    """EMA crossover with RSI filter and ATR-based stops.

    Rules (long mirror short):
      * Go long when fast EMA crosses ABOVE slow EMA AND RSI > rsi_long.
      * Go short when fast EMA crosses BELOW slow EMA AND RSI < rsi_short.
      * Stop = entry -/+ atr_mult * ATR
      * Take profit = entry +/- (atr_mult * rr_ratio) * ATR

    One open signal at a time is enforced by the backtester/broker,
    not by the strategy itself.
    """

    fast_period: int = 12
    slow_period: int = 26
    rsi_period: int = 14
    atr_period: int = 14
    atr_mult: float = 2.0
    rr_ratio: float = 2.0
    rsi_long: float = 55.0
    rsi_short: float = 45.0

    name: str = "ema_cross_rsi"

    _fast: EMA = field(init=False)
    _slow: EMA = field(init=False)
    _rsi: RSI = field(init=False)
    _atr: ATR = field(init=False)
    _prev_diff: Optional[float] = field(default=None, init=False)

    def __post_init__(self) -> None:
        if self.fast_period >= self.slow_period:
            raise ValueError("fast_period must be < slow_period")
        if self.atr_mult <= 0 or self.rr_ratio <= 0:
            raise ValueError("atr_mult and rr_ratio must be positive")
        self._fast = EMA(self.fast_period)
        self._slow = EMA(self.slow_period)
        self._rsi = RSI(self.rsi_period)
        self._atr = ATR(self.atr_period)

    def on_bar(self, bar: Candle) -> Optional[Signal]:
        fast = self._fast.update(bar.close)
        slow = self._slow.update(bar.close)
        rsi = self._rsi.update(bar.close)
        atr = self._atr.update(bar.high, bar.low, bar.close)

        if fast is None or slow is None or rsi is None or atr is None:
            return None

        diff = fast - slow
        prev = self._prev_diff
        self._prev_diff = diff

        if prev is None:
            return None

        crossed_up = prev <= 0 < diff
        crossed_down = prev >= 0 > diff

        if crossed_up and rsi > self.rsi_long:
            sl = bar.close - self.atr_mult * atr
            tp = bar.close + self.atr_mult * self.rr_ratio * atr
            return Signal(
                side=Side.BUY,
                price=bar.close,
                stop_loss=sl,
                take_profit=tp,
                reason=f"EMA{self.fast_period}>EMA{self.slow_period}, RSI={rsi:.1f}",
            )
        if crossed_down and rsi < self.rsi_short:
            sl = bar.close + self.atr_mult * atr
            tp = bar.close - self.atr_mult * self.rr_ratio * atr
            return Signal(
                side=Side.SELL,
                price=bar.close,
                stop_loss=sl,
                take_profit=tp,
                reason=f"EMA{self.fast_period}<EMA{self.slow_period}, RSI={rsi:.1f}",
            )
        return None


def available_strategies() -> List[str]:
    return ["ema_cross_rsi"]


def build_strategy(name: str, **kwargs) -> Strategy:
    if name == "ema_cross_rsi":
        return EmaCrossRsiStrategy(**kwargs)
    raise ValueError(f"Unknown strategy: {name}")
