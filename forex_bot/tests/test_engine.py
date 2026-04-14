from datetime import datetime, timedelta, timezone

from bot.broker import PaperBroker
from bot.data import Candle, SyntheticDataFeed
from bot.engine import run
from bot.risk import RiskConfig
from bot.strategy import EmaCrossRsiStrategy, Side, Signal


def _bar(ts, o, h, l, c):
    return Candle(ts, o, h, l, c)


def test_broker_stop_hit_long():
    broker = PaperBroker(symbol="TEST", starting_equity=10_000, spread=0.0)
    now = datetime(2024, 1, 1, tzinfo=timezone.utc)
    entry_bar = _bar(now, 100, 101, 99, 100)
    sig = Signal(side=Side.BUY, price=100.0, stop_loss=99.0, take_profit=102.0)
    broker.submit(sig, units=10, at_bar=entry_bar)
    assert broker.has_position()

    # Next bar wicks below the stop.
    next_bar = _bar(now + timedelta(hours=1), 100, 100.5, 98.5, 99.5)
    closed = broker.on_bar(next_bar)
    assert len(closed) == 1
    t = closed[0]
    assert t.exit_reason == "stop"
    # Loss ~ (99 - 100) * 10 = -10
    assert t.pnl < 0


def test_broker_take_profit_short():
    broker = PaperBroker(symbol="TEST", starting_equity=10_000, spread=0.0)
    now = datetime(2024, 1, 1, tzinfo=timezone.utc)
    entry_bar = _bar(now, 100, 101, 99, 100)
    sig = Signal(side=Side.SELL, price=100.0, stop_loss=102.0, take_profit=98.0)
    broker.submit(sig, units=-10, at_bar=entry_bar)

    next_bar = _bar(now + timedelta(hours=1), 99, 99.5, 97.5, 98.0)
    closed = broker.on_bar(next_bar)
    assert len(closed) == 1
    assert closed[0].exit_reason == "take_profit"
    assert closed[0].pnl > 0


def test_engine_runs_end_to_end():
    feed = SyntheticDataFeed(n_bars=500, seed=7)
    strat = EmaCrossRsiStrategy()
    broker = PaperBroker(symbol="DEMO", starting_equity=10_000, spread=0.0001)
    risk = RiskConfig(risk_per_trade=0.01, max_leverage=5, min_units=1)
    result = run(feed, strat, broker, risk)
    # With 500 bars of noisy synthetic data we expect at least some
    # signals to have fired; but the exact count is not guaranteed.
    assert isinstance(result.trades, list)
    # Equity shouldn't have exploded or gone negative beyond reason
    # (risk cap = 1% per trade).
    final_eq = broker.cash
    assert final_eq > 0
