"""Rolling indicators used by strategies.

Streaming-friendly: each indicator accepts one value at a time via
``update()`` and reports ``ready`` when it has enough history. This
matches the live-trading model where you see bars one at a time.
"""

from __future__ import annotations

from collections import deque
from dataclasses import dataclass, field
from typing import Deque, Optional


@dataclass
class SMA:
    """Simple moving average."""

    period: int
    _buf: Deque[float] = field(default_factory=deque)
    _sum: float = 0.0

    def __post_init__(self) -> None:
        if self.period <= 0:
            raise ValueError("period must be positive")

    @property
    def ready(self) -> bool:
        return len(self._buf) >= self.period

    @property
    def value(self) -> Optional[float]:
        return self._sum / self.period if self.ready else None

    def update(self, x: float) -> Optional[float]:
        self._buf.append(x)
        self._sum += x
        if len(self._buf) > self.period:
            self._sum -= self._buf.popleft()
        return self.value


@dataclass
class EMA:
    """Exponential moving average using the classic alpha = 2/(N+1)."""

    period: int
    _value: Optional[float] = None
    _n: int = 0

    def __post_init__(self) -> None:
        if self.period <= 0:
            raise ValueError("period must be positive")
        self._alpha = 2 / (self.period + 1)

    @property
    def ready(self) -> bool:
        return self._n >= self.period

    @property
    def value(self) -> Optional[float]:
        return self._value if self.ready else None

    def update(self, x: float) -> Optional[float]:
        self._n += 1
        if self._value is None:
            self._value = x
        else:
            self._value = self._alpha * x + (1 - self._alpha) * self._value
        return self.value


@dataclass
class ATR:
    """Average True Range (Wilder smoothing). Needs high/low/close."""

    period: int
    _prev_close: Optional[float] = None
    _value: Optional[float] = None
    _n: int = 0

    def __post_init__(self) -> None:
        if self.period <= 0:
            raise ValueError("period must be positive")

    @property
    def ready(self) -> bool:
        return self._n >= self.period

    @property
    def value(self) -> Optional[float]:
        return self._value if self.ready else None

    def update(self, high: float, low: float, close: float) -> Optional[float]:
        if self._prev_close is None:
            tr = high - low
        else:
            tr = max(
                high - low,
                abs(high - self._prev_close),
                abs(low - self._prev_close),
            )
        self._prev_close = close
        self._n += 1
        if self._value is None:
            self._value = tr
        else:
            # Wilder smoothing.
            self._value = (self._value * (self.period - 1) + tr) / self.period
        return self.value


@dataclass
class RSI:
    """Relative Strength Index (Wilder)."""

    period: int = 14
    _prev: Optional[float] = None
    _avg_gain: float = 0.0
    _avg_loss: float = 0.0
    _n: int = 0

    def __post_init__(self) -> None:
        if self.period <= 1:
            raise ValueError("period must be > 1")

    @property
    def ready(self) -> bool:
        return self._n > self.period

    @property
    def value(self) -> Optional[float]:
        if not self.ready:
            return None
        if self._avg_loss == 0:
            return 100.0
        rs = self._avg_gain / self._avg_loss
        return 100 - (100 / (1 + rs))

    def update(self, close: float) -> Optional[float]:
        if self._prev is None:
            self._prev = close
            self._n += 1
            return None
        change = close - self._prev
        gain = max(change, 0.0)
        loss = max(-change, 0.0)
        self._n += 1
        if self._n <= self.period + 1:
            # Seed with simple average over the first ``period`` changes.
            self._avg_gain += gain / self.period
            self._avg_loss += loss / self.period
        else:
            self._avg_gain = (self._avg_gain * (self.period - 1) + gain) / self.period
            self._avg_loss = (self._avg_loss * (self.period - 1) + loss) / self.period
        self._prev = close
        return self.value
