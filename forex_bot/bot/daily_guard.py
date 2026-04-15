"""Daily risk budget + profit target + trading session schedule.

Wraps a strategy so that:
  * No new signals are emitted outside the configured session windows.
  * Any open position is force-closed at session end.
  * Once daily loss cap is hit, the bot flatlines until the next day.
  * Once daily profit target is hit, the bot banks and stops for the day.

This is the mechanism behind the "grow my account by x% per day" idea,
but made honest: the cap is as important as the target, and both are
expressed as percentages of *current* equity, not of the original
deposit. If you lose, tomorrow's targets shrink too.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date, datetime, time, timedelta
from typing import List, Optional, Tuple

from .broker import PaperBroker
from .data import Candle
from .strategy import Signal, Strategy


@dataclass(frozen=True)
class SessionWindow:
    """A daily trading window in UTC."""

    start: time  # inclusive
    end: time    # exclusive
    label: str = ""

    def contains(self, ts: datetime) -> bool:
        t = ts.timetz().replace(tzinfo=None)
        return self.start <= t < self.end


@dataclass
class DailyGuardConfig:
    daily_loss_cap_pct: float = 0.02   # 2% of SoD equity -> stop for the day
    daily_profit_target_pct: float = 0.01  # 1% of SoD equity -> bank for the day
    sessions: List[SessionWindow] = field(default_factory=list)

    def __post_init__(self) -> None:
        if not 0 < self.daily_loss_cap_pct <= 0.1:
            raise ValueError("daily_loss_cap_pct must be in (0, 0.1]")
        if not 0 < self.daily_profit_target_pct <= 0.1:
            raise ValueError("daily_profit_target_pct must be in (0, 0.1]")


def default_fx_sessions() -> List[SessionWindow]:
    """London open + NY open. UTC."""
    return [
        SessionWindow(time(7, 0), time(11, 0), "london_open"),
        SessionWindow(time(12, 30), time(16, 0), "ny_open"),
    ]


@dataclass
class DailyGuard:
    """State machine that enforces the daily guard policy."""

    config: DailyGuardConfig
    _today: Optional[date] = None
    _sod_equity: float = 0.0  # start-of-day equity
    _stopped_today: bool = False
    _banked_today: bool = False
    # Diagnostics.
    day_log: List[Tuple[date, str, float]] = field(default_factory=list)
    # Entries: (date, status in {"loss_cap","target","ok"}, end_of_day_equity)

    def in_session(self, ts: datetime) -> bool:
        if not self.config.sessions:
            return True
        return any(s.contains(ts) for s in self.config.sessions)

    def on_bar(self, bar: Candle, broker: PaperBroker) -> None:
        """Called on every bar BEFORE the strategy sees it.

        Handles day rollover, records SoD equity, and enforces caps by
        force-closing any open position once a cap is breached.
        """
        bar_date = bar.timestamp.date()
        if self._today is None or bar_date != self._today:
            # End-of-day log for the previous day (if any).
            if self._today is not None:
                status = (
                    "loss_cap" if self._stopped_today
                    else "target" if self._banked_today
                    else "ok"
                )
                self.day_log.append((self._today, status, broker.equity(bar.open)))
            self._today = bar_date
            self._sod_equity = broker.equity(bar.open)
            self._stopped_today = False
            self._banked_today = False
            return

        if self._stopped_today or self._banked_today:
            if broker.has_position():
                broker.force_close_all(bar)
            return

        equity = broker.equity(bar.close)
        pct = (equity - self._sod_equity) / self._sod_equity if self._sod_equity > 0 else 0.0
        if pct <= -self.config.daily_loss_cap_pct:
            self._stopped_today = True
            if broker.has_position():
                broker.force_close_all(bar)
        elif pct >= self.config.daily_profit_target_pct:
            self._banked_today = True
            if broker.has_position():
                broker.force_close_all(bar)

    def accepts_signal(self, bar: Candle) -> bool:
        """Whether a new signal on this bar is allowed to open a position."""
        if self._stopped_today or self._banked_today:
            return False
        return self.in_session(bar.timestamp)

    def finalize(self, broker: PaperBroker, last_bar: Candle) -> None:
        """Flush end-of-day diagnostics at end of run."""
        if self._today is not None:
            status = (
                "loss_cap" if self._stopped_today
                else "target" if self._banked_today
                else "ok"
            )
            self.day_log.append((self._today, status, broker.equity(last_bar.close)))

    # ---- reporting ----------------------------------------------------

    def daily_hit_rates(self) -> dict:
        if not self.day_log:
            return {"days": 0, "target_pct": 0.0, "loss_cap_pct": 0.0, "ok_pct": 0.0}
        n = len(self.day_log)
        hits = sum(1 for _, s, _ in self.day_log if s == "target")
        losses = sum(1 for _, s, _ in self.day_log if s == "loss_cap")
        ok = n - hits - losses
        return {
            "days": n,
            "target_pct": round(hits / n * 100, 2),
            "loss_cap_pct": round(losses / n * 100, 2),
            "ok_pct": round(ok / n * 100, 2),
        }
