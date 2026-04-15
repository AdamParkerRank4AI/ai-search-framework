"""Equity and performance tracking.

Records equity snapshots over time, derives period returns
(daily/monthly) and persists everything to JSON so paper-mode runs
can be resumed and a dashboard can be regenerated at any time.

The tracker is append-only: snapshots are added as bars close. Nothing
is ever rewritten, which matches how you'd want a 2-year live log
to behave.
"""

from __future__ import annotations

import json
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import date, datetime, timezone
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Tuple

from .broker import Trade


@dataclass(frozen=True)
class EquitySnapshot:
    timestamp: datetime
    equity: float
    cash: float
    open_positions: int

    def to_dict(self) -> dict:
        return {
            "timestamp": self.timestamp.isoformat(),
            "equity": round(self.equity, 4),
            "cash": round(self.cash, 4),
            "open_positions": self.open_positions,
        }

    @classmethod
    def from_dict(cls, d: dict) -> "EquitySnapshot":
        ts = d["timestamp"]
        if isinstance(ts, str):
            ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        return cls(
            timestamp=ts,
            equity=float(d["equity"]),
            cash=float(d["cash"]),
            open_positions=int(d["open_positions"]),
        )


@dataclass(frozen=True)
class TradeRecord:
    """Flat trade record suitable for JSON."""

    symbol: str
    side: str
    units: float
    entry_time: str
    entry_price: float
    exit_time: str
    exit_price: float
    pnl: float
    exit_reason: str

    @classmethod
    def from_trade(cls, t: Trade) -> "TradeRecord":
        return cls(
            symbol=t.symbol,
            side=t.side.value,
            units=float(t.units),
            entry_time=t.entry_time.isoformat(),
            entry_price=float(t.entry_price),
            exit_time=t.exit_time.isoformat(),
            exit_price=float(t.exit_price),
            pnl=float(t.pnl),
            exit_reason=t.exit_reason,
        )


@dataclass
class Tracker:
    """Stateful performance tracker.

    Use ``record(bar.timestamp, broker.equity(bar.close), broker.cash,
    len(broker.positions))`` on every bar you want to snapshot, and
    ``record_trades(new_trades)`` when the broker closes trades. Call
    ``save(path)`` to persist.
    """

    label: str = "default"
    starting_equity: float = 10_000.0
    snapshots: List[EquitySnapshot] = field(default_factory=list)
    trades: List[TradeRecord] = field(default_factory=list)

    # ---- recording ----------------------------------------------------

    def record(
        self,
        timestamp: datetime,
        equity: float,
        cash: float,
        open_positions: int,
    ) -> None:
        self.snapshots.append(
            EquitySnapshot(timestamp=timestamp, equity=equity, cash=cash,
                           open_positions=open_positions)
        )

    def record_trades(self, trades: Iterable[Trade]) -> None:
        for t in trades:
            self.trades.append(TradeRecord.from_trade(t))

    # ---- persistence --------------------------------------------------

    def to_dict(self) -> dict:
        return {
            "label": self.label,
            "starting_equity": self.starting_equity,
            "snapshots": [s.to_dict() for s in self.snapshots],
            "trades": [asdict(t) for t in self.trades],
        }

    def save(self, path: str | Path) -> None:
        path = Path(path)
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("w") as fh:
            json.dump(self.to_dict(), fh, indent=2)

    @classmethod
    def load(cls, path: str | Path) -> "Tracker":
        path = Path(path)
        with path.open() as fh:
            data = json.load(fh)
        t = cls(label=data.get("label", "default"),
                starting_equity=float(data.get("starting_equity", 10_000.0)))
        t.snapshots = [EquitySnapshot.from_dict(s) for s in data.get("snapshots", [])]
        t.trades = [TradeRecord(**tr) for tr in data.get("trades", [])]
        return t

    # ---- derived series -----------------------------------------------

    def equity_curve(self) -> List[Tuple[datetime, float]]:
        return [(s.timestamp, s.equity) for s in self.snapshots]

    def daily_returns(self) -> List[Tuple[date, float]]:
        """Return (date, daily_return_pct) using last snapshot of each day."""
        by_day: Dict[date, float] = {}
        for s in self.snapshots:
            by_day[s.timestamp.date()] = s.equity
        days = sorted(by_day)
        out: List[Tuple[date, float]] = []
        prev: Optional[float] = None
        for d in days:
            eq = by_day[d]
            if prev is not None and prev > 0:
                out.append((d, (eq - prev) / prev))
            prev = eq
        return out

    def monthly_returns(self) -> List[Tuple[str, float]]:
        """Return (YYYY-MM, month_return_pct) using first/last of month."""
        first: Dict[str, float] = {}
        last: Dict[str, float] = {}
        order: List[str] = []
        for s in self.snapshots:
            key = f"{s.timestamp.year:04d}-{s.timestamp.month:02d}"
            if key not in first:
                first[key] = s.equity
                order.append(key)
            last[key] = s.equity
        out: List[Tuple[str, float]] = []
        for key in order:
            base = first[key]
            if base > 0:
                out.append((key, (last[key] - base) / base))
        return out

    # ---- summary metrics ----------------------------------------------

    def summary(self) -> dict:
        final_equity = self.snapshots[-1].equity if self.snapshots else self.starting_equity
        total_return = (
            (final_equity - self.starting_equity) / self.starting_equity
            if self.starting_equity > 0 else 0.0
        )
        # Max drawdown from equity curve.
        peak = self.starting_equity
        max_dd = 0.0
        max_dd_pct = 0.0
        for s in self.snapshots:
            peak = max(peak, s.equity)
            dd = peak - s.equity
            if dd > max_dd:
                max_dd = dd
                max_dd_pct = dd / peak if peak > 0 else 0.0

        # Win/loss stats.
        wins = [t for t in self.trades if t.pnl > 0]
        losses = [t for t in self.trades if t.pnl < 0]
        win_rate = len(wins) / len(self.trades) if self.trades else 0.0
        gross_win = sum(t.pnl for t in wins)
        gross_loss = -sum(t.pnl for t in losses)
        profit_factor = (gross_win / gross_loss) if gross_loss > 0 else float("inf")

        # Trading period in days.
        if self.snapshots:
            span = self.snapshots[-1].timestamp - self.snapshots[0].timestamp
            days = max(span.days, 1)
        else:
            days = 0

        return {
            "label": self.label,
            "starting_equity": self.starting_equity,
            "final_equity": final_equity,
            "total_return_pct": total_return * 100,
            "max_drawdown_abs": max_dd,
            "max_drawdown_pct": max_dd_pct * 100,
            "n_trades": len(self.trades),
            "win_rate_pct": win_rate * 100,
            "profit_factor": profit_factor if profit_factor != float("inf") else None,
            "tracking_days": days,
        }


def trades_by_month(trades: Iterable[TradeRecord]) -> Dict[str, List[TradeRecord]]:
    bucket: Dict[str, List[TradeRecord]] = defaultdict(list)
    for t in trades:
        ts = datetime.fromisoformat(t.exit_time.replace("Z", "+00:00"))
        key = f"{ts.year:04d}-{ts.month:02d}"
        bucket[key].append(t)
    return dict(bucket)


def now_utc() -> datetime:
    return datetime.now(timezone.utc)
