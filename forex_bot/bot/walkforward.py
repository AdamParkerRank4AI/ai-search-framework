"""Walk-forward validation.

Splits a long history into consecutive windows and runs the strategy
on each one OUT-OF-SAMPLE -- i.e. parameters are fixed up front, the
bot has not seen the data it is tested on, and we measure how the
performance holds up window to window.

This is the single most effective filter against "I backtested and
it printed money." If the OOS windows are wildly inconsistent, the
backtest was noise.

Unlike a proper parameter-optimising walk-forward, this variant is
deliberately simple: it assumes you have ALREADY chosen your
parameters (no re-fitting per window). That matches how you'd actually
run a 2-year live tracking period: one configuration, many months.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta
from typing import Callable, List, Sequence

from .broker import PaperBroker, Trade
from .data import Candle
from .engine import run
from .risk import RiskConfig
from .strategy import Strategy


@dataclass(frozen=True)
class Window:
    start: datetime
    end: datetime  # exclusive
    label: str

    def contains(self, ts: datetime) -> bool:
        return self.start <= ts < self.end


@dataclass
class WindowResult:
    label: str
    start: datetime
    end: datetime
    starting_equity: float
    final_equity: float
    n_trades: int
    win_rate: float
    pnl: float
    max_drawdown: float

    @property
    def return_pct(self) -> float:
        if self.starting_equity <= 0:
            return 0.0
        return (self.final_equity - self.starting_equity) / self.starting_equity * 100

    def to_dict(self) -> dict:
        return {
            "label": self.label,
            "start": self.start.isoformat(),
            "end": self.end.isoformat(),
            "starting_equity": round(self.starting_equity, 2),
            "final_equity": round(self.final_equity, 2),
            "return_pct": round(self.return_pct, 3),
            "n_trades": self.n_trades,
            "win_rate": round(self.win_rate, 4),
            "pnl": round(self.pnl, 2),
            "max_drawdown": round(self.max_drawdown, 2),
        }


@dataclass
class WalkForwardReport:
    windows: List[WindowResult] = field(default_factory=list)

    def to_dict(self) -> dict:
        return {
            "windows": [w.to_dict() for w in self.windows],
            "summary": self.summary(),
        }

    def summary(self) -> dict:
        if not self.windows:
            return {"n_windows": 0}
        rets = [w.return_pct for w in self.windows]
        positive = sum(1 for r in rets if r > 0)
        mean_ret = sum(rets) / len(rets)
        # Sample stdev for small-n honesty.
        if len(rets) > 1:
            var = sum((r - mean_ret) ** 2 for r in rets) / (len(rets) - 1)
            std = var ** 0.5
        else:
            std = 0.0
        # Return/risk ratio across windows (rough signal-to-noise).
        ratio = (mean_ret / std) if std > 0 else 0.0
        return {
            "n_windows": len(self.windows),
            "pct_positive_windows": positive / len(self.windows) * 100,
            "mean_return_pct": round(mean_ret, 3),
            "stdev_return_pct": round(std, 3),
            "return_over_stdev": round(ratio, 3),
            "worst_return_pct": round(min(rets), 3),
            "best_return_pct": round(max(rets), 3),
        }


def make_month_windows(bars: Sequence[Candle]) -> List[Window]:
    """Split candles into calendar-month windows."""
    if not bars:
        return []
    out: List[Window] = []
    cur_year = bars[0].timestamp.year
    cur_month = bars[0].timestamp.month
    start = bars[0].timestamp
    for bar in bars[1:]:
        if bar.timestamp.year != cur_year or bar.timestamp.month != cur_month:
            end = bar.timestamp
            out.append(Window(start=start, end=end,
                              label=f"{cur_year:04d}-{cur_month:02d}"))
            start = bar.timestamp
            cur_year = bar.timestamp.year
            cur_month = bar.timestamp.month
    # Final window.
    end = bars[-1].timestamp + timedelta(microseconds=1)
    out.append(Window(start=start, end=end,
                      label=f"{cur_year:04d}-{cur_month:02d}"))
    return out


def make_fixed_windows(bars: Sequence[Candle], days: int) -> List[Window]:
    """Split into fixed-length windows measured in days."""
    if not bars or days <= 0:
        return []
    out: List[Window] = []
    step = timedelta(days=days)
    start = bars[0].timestamp
    last_ts = bars[-1].timestamp + timedelta(microseconds=1)
    i = 1
    while start < last_ts:
        end = start + step
        if end > last_ts:
            end = last_ts
        out.append(Window(start=start, end=end, label=f"window-{i:03d}"))
        start = end
        i += 1
    return out


def run_walk_forward(
    bars: Sequence[Candle],
    windows: Sequence[Window],
    strategy_factory: Callable[[], Strategy],
    risk: RiskConfig,
    symbol: str,
    starting_equity: float,
    spread: float = 0.0001,
    commission_per_unit: float = 0.0,
) -> WalkForwardReport:
    """Run each window independently with a fresh strategy and broker.

    ``strategy_factory`` returns a fresh ``Strategy`` instance per
    window so indicator state does not leak across windows.
    """
    report = WalkForwardReport()
    # Pre-bucket bars by window for O(N) total work.
    bucketed: List[List[Candle]] = [[] for _ in windows]
    idx = 0
    for bar in bars:
        while idx < len(windows) and bar.timestamp >= windows[idx].end:
            idx += 1
        if idx >= len(windows):
            break
        if windows[idx].contains(bar.timestamp):
            bucketed[idx].append(bar)

    for window, window_bars in zip(windows, bucketed):
        if not window_bars:
            continue
        strat = strategy_factory()
        broker = PaperBroker(symbol=symbol, starting_equity=starting_equity,
                             spread=spread, commission_per_unit=commission_per_unit)
        run(window_bars, strat, broker, risk)
        # Close any open position at the final bar for clean accounting.
        if broker.has_position():
            broker.force_close_all(window_bars[-1])

        trades = broker.trades
        wins = sum(1 for t in trades if t.pnl > 0)
        wr = wins / len(trades) if trades else 0.0
        pnl = sum(t.pnl for t in trades)
        # Per-window max drawdown from trade sequence.
        eq = starting_equity
        peak = eq
        max_dd = 0.0
        for t in trades:
            eq += t.pnl
            peak = max(peak, eq)
            dd = peak - eq
            if dd > max_dd:
                max_dd = dd

        report.windows.append(WindowResult(
            label=window.label,
            start=window.start,
            end=window.end,
            starting_equity=starting_equity,
            final_equity=eq,
            n_trades=len(trades),
            win_rate=wr,
            pnl=pnl,
            max_drawdown=max_dd,
        ))
    return report
