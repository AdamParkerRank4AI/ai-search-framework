"""Risk management: position sizing and sanity limits.

The single most important module in this package. A winning strategy
with bad risk control loses money; a mediocre strategy with good risk
control survives long enough to learn. Do not bypass this.
"""

from __future__ import annotations

from dataclasses import dataclass

from .strategy import Side, Signal


@dataclass(frozen=True)
class RiskConfig:
    """Global risk limits.

    * ``risk_per_trade``: fraction of equity risked on a single trade
      (0.01 = 1%). This is the max you can lose if the stop is hit.
    * ``max_leverage``: hard cap on notional / equity. Retail FX often
      offers 30-500x; you almost never want more than 5-10x in a bot
      running unattended.
    * ``max_open_positions``: concurrent positions cap.
    """

    risk_per_trade: float = 0.01
    max_leverage: float = 5.0
    max_open_positions: int = 1
    min_units: float = 1.0  # broker minimum lot / unit

    def __post_init__(self) -> None:
        if not 0 < self.risk_per_trade <= 0.05:
            # Hard ceiling: 5% per trade is already aggressive.
            raise ValueError(
                "risk_per_trade must be in (0, 0.05]. "
                "If you want more than 5% per trade, edit the source and "
                "take responsibility for it."
            )
        if self.max_leverage <= 0:
            raise ValueError("max_leverage must be positive")
        if self.max_open_positions < 1:
            raise ValueError("max_open_positions must be >= 1")


def size_position(
    signal: Signal,
    equity: float,
    config: RiskConfig,
) -> float:
    """Return position size in base-currency units.

    Sizing is driven by the stop distance so that a stop-out loses
    approximately ``risk_per_trade * equity``. A leverage cap is also
    applied.
    """
    if equity <= 0:
        return 0.0

    stop_distance = abs(signal.price - signal.stop_loss)
    if stop_distance <= 0:
        return 0.0

    risk_cash = equity * config.risk_per_trade
    units_by_risk = risk_cash / stop_distance

    # Leverage cap: notional = units * price.
    units_by_leverage = (equity * config.max_leverage) / signal.price

    units = min(units_by_risk, units_by_leverage)
    if units < config.min_units:
        return 0.0
    # Sign by direction.
    return units if signal.side is Side.BUY else -units
