"""Broker abstractions.

``PaperBroker`` is a fully in-memory simulator used by both the
backtester and the "paper" live mode. It handles:

  * Market entries at the next bar's open (no look-ahead)
  * Intrabar stop-loss / take-profit (conservative: if the bar range
    touches SL, assume SL is hit first even if TP is also touched)
  * Optional per-trade spread and commission

There is no live broker adapter in this file on purpose. If you want
to go live, implement a subclass with the same interface and wire it
up yourself. See ``live_broker_example.txt`` notes in the README.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime
from typing import List, Optional

from .data import Candle
from .strategy import Side, Signal


@dataclass
class Position:
    symbol: str
    side: Side
    units: float  # signed: positive = long, negative = short
    entry_price: float
    entry_time: datetime
    stop_loss: float
    take_profit: float

    def unrealized_pnl(self, price: float) -> float:
        return (price - self.entry_price) * self.units


@dataclass
class Fill:
    timestamp: datetime
    symbol: str
    side: Side
    units: float
    price: float
    reason: str  # "entry", "stop", "take_profit", "close"


@dataclass
class Trade:
    """A completed round-trip trade (entry + exit)."""

    symbol: str
    side: Side
    units: float
    entry_time: datetime
    entry_price: float
    exit_time: datetime
    exit_price: float
    pnl: float
    exit_reason: str

    @property
    def r_multiple(self) -> Optional[float]:
        return None  # filled in by the engine if it has the stop distance


@dataclass
class PaperBroker:
    """In-memory broker. One open position at a time per symbol."""

    symbol: str
    starting_equity: float = 10_000.0
    spread: float = 0.0001  # price units (e.g. 1 pip on EURUSD)
    commission_per_unit: float = 0.0  # charged on each fill
    cash: float = field(init=False)
    positions: List[Position] = field(default_factory=list, init=False)
    fills: List[Fill] = field(default_factory=list, init=False)
    trades: List[Trade] = field(default_factory=list, init=False)

    def __post_init__(self) -> None:
        self.cash = self.starting_equity

    # ---- state -----------------------------------------------------

    def equity(self, mark_price: float) -> float:
        unreal = sum(p.unrealized_pnl(mark_price) for p in self.positions)
        return self.cash + unreal

    def has_position(self) -> bool:
        return bool(self.positions)

    # ---- actions ---------------------------------------------------

    def submit(self, signal: Signal, units: float, at_bar: Candle) -> Optional[Position]:
        """Open a position at the CURRENT bar's open, plus spread.

        The caller is responsible for sizing. We apply half-spread on
        each side so a round-trip pays the full spread.
        """
        if units == 0:
            return None
        if self.has_position():
            return None  # enforce single-position policy

        half_spread = self.spread / 2.0
        if signal.side is Side.BUY:
            fill_price = at_bar.open + half_spread
        else:
            fill_price = at_bar.open - half_spread

        # Commission charged up front.
        self.cash -= self.commission_per_unit * abs(units)

        pos = Position(
            symbol=self.symbol,
            side=signal.side,
            units=units,
            entry_price=fill_price,
            entry_time=at_bar.timestamp,
            stop_loss=signal.stop_loss,
            take_profit=signal.take_profit,
        )
        self.positions.append(pos)
        self.fills.append(
            Fill(at_bar.timestamp, self.symbol, signal.side, units, fill_price, "entry")
        )
        return pos

    def on_bar(self, bar: Candle) -> List[Trade]:
        """Check SL/TP against the bar range. Returns trades closed."""
        closed: List[Trade] = []
        still_open: List[Position] = []
        for pos in self.positions:
            exit_price: Optional[float] = None
            reason = ""
            if pos.side is Side.BUY:
                # Long: stop below, tp above. Assume SL hit first if both.
                if bar.low <= pos.stop_loss:
                    exit_price = pos.stop_loss
                    reason = "stop"
                elif bar.high >= pos.take_profit:
                    exit_price = pos.take_profit
                    reason = "take_profit"
            else:
                if bar.high >= pos.stop_loss:
                    exit_price = pos.stop_loss
                    reason = "stop"
                elif bar.low <= pos.take_profit:
                    exit_price = pos.take_profit
                    reason = "take_profit"

            if exit_price is not None:
                closed.append(self._close(pos, bar.timestamp, exit_price, reason))
            else:
                still_open.append(pos)
        self.positions = still_open
        return closed

    def force_close_all(self, bar: Candle) -> List[Trade]:
        """Close any remaining positions at the bar close. Used at end of backtest."""
        closed: List[Trade] = []
        for pos in self.positions:
            closed.append(self._close(pos, bar.timestamp, bar.close, "close"))
        self.positions = []
        return closed

    # ---- internals -------------------------------------------------

    def _close(
        self,
        pos: Position,
        timestamp: datetime,
        price: float,
        reason: str,
    ) -> Trade:
        half_spread = self.spread / 2.0
        # Exit sign flips.
        if pos.side is Side.BUY:
            fill_price = price - half_spread
            exit_side = Side.SELL
        else:
            fill_price = price + half_spread
            exit_side = Side.BUY

        pnl = (fill_price - pos.entry_price) * pos.units
        self.cash += pnl
        self.cash -= self.commission_per_unit * abs(pos.units)

        self.fills.append(
            Fill(timestamp, self.symbol, exit_side, -pos.units, fill_price, reason)
        )
        trade = Trade(
            symbol=pos.symbol,
            side=pos.side,
            units=pos.units,
            entry_time=pos.entry_time,
            entry_price=pos.entry_price,
            exit_time=timestamp,
            exit_price=fill_price,
            pnl=pnl,
            exit_reason=reason,
        )
        self.trades.append(trade)
        return trade
