"""Trade journal and performance metrics.

Keep this honest: no Sharpe without a risk-free rate assumption,
no returns annualisation without a bar frequency. Small, explicit
metrics only.
"""

from __future__ import annotations

import csv
import math
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, List, Sequence

from .broker import Trade


@dataclass(frozen=True)
class Metrics:
    n_trades: int
    win_rate: float
    avg_win: float
    avg_loss: float
    profit_factor: float
    expectancy: float
    gross_pnl: float
    max_drawdown: float
    final_equity: float

    def as_dict(self) -> dict:
        return {
            "n_trades": self.n_trades,
            "win_rate": round(self.win_rate, 4),
            "avg_win": round(self.avg_win, 4),
            "avg_loss": round(self.avg_loss, 4),
            "profit_factor": round(self.profit_factor, 4)
            if math.isfinite(self.profit_factor)
            else self.profit_factor,
            "expectancy": round(self.expectancy, 4),
            "gross_pnl": round(self.gross_pnl, 2),
            "max_drawdown": round(self.max_drawdown, 2),
            "final_equity": round(self.final_equity, 2),
        }


def compute_metrics(trades: Sequence[Trade], starting_equity: float) -> Metrics:
    if not trades:
        return Metrics(0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, starting_equity)

    wins = [t.pnl for t in trades if t.pnl > 0]
    losses = [t.pnl for t in trades if t.pnl < 0]
    gross = sum(t.pnl for t in trades)

    gross_win = sum(wins)
    gross_loss = -sum(losses)
    profit_factor = (gross_win / gross_loss) if gross_loss > 0 else float("inf")

    avg_win = (sum(wins) / len(wins)) if wins else 0.0
    avg_loss = (sum(losses) / len(losses)) if losses else 0.0
    win_rate = len(wins) / len(trades)
    expectancy = gross / len(trades)

    # Equity curve and max drawdown.
    equity = starting_equity
    peak = equity
    max_dd = 0.0
    for t in trades:
        equity += t.pnl
        peak = max(peak, equity)
        dd = peak - equity
        if dd > max_dd:
            max_dd = dd

    return Metrics(
        n_trades=len(trades),
        win_rate=win_rate,
        avg_win=avg_win,
        avg_loss=avg_loss,
        profit_factor=profit_factor,
        expectancy=expectancy,
        gross_pnl=gross,
        max_drawdown=max_dd,
        final_equity=equity,
    )


def write_trades_csv(path: str | Path, trades: Iterable[Trade]) -> None:
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(
            [
                "symbol",
                "side",
                "units",
                "entry_time",
                "entry_price",
                "exit_time",
                "exit_price",
                "pnl",
                "exit_reason",
            ]
        )
        for t in trades:
            writer.writerow(
                [
                    t.symbol,
                    t.side.value,
                    t.units,
                    t.entry_time.isoformat(),
                    t.entry_price,
                    t.exit_time.isoformat(),
                    t.exit_price,
                    round(t.pnl, 4),
                    t.exit_reason,
                ]
            )


def format_metrics(m: Metrics) -> str:
    pf = f"{m.profit_factor:.2f}" if math.isfinite(m.profit_factor) else "inf"
    return (
        f"Trades: {m.n_trades}\n"
        f"Win rate: {m.win_rate:.1%}\n"
        f"Avg win: {m.avg_win:.2f}  Avg loss: {m.avg_loss:.2f}\n"
        f"Profit factor: {pf}\n"
        f"Expectancy per trade: {m.expectancy:.2f}\n"
        f"Gross PnL: {m.gross_pnl:.2f}\n"
        f"Max drawdown: {m.max_drawdown:.2f}\n"
        f"Final equity: {m.final_equity:.2f}"
    )
