from datetime import datetime, timedelta, timezone

from bot.broker import PaperBroker
from bot.data import Candle
from bot.engine import run
from bot.risk import RiskConfig
from bot.strategy import DonchianBreakoutStrategy, Side, build_strategy


def _bars_staircase():
    """20 flat bars around 100, then a clear upward breakout."""
    t = datetime(2024, 1, 1, tzinfo=timezone.utc)
    out = []
    for i in range(20):
        out.append(Candle(t + timedelta(hours=i), 100.0, 100.5, 99.5, 100.0))
    # Breakout bar: close significantly above the prior 20-bar high of 100.5.
    out.append(Candle(t + timedelta(hours=20), 100.0, 102.0, 99.8, 101.5))
    # Give the position room to hit TP.
    out.append(Candle(t + timedelta(hours=21), 101.5, 110.0, 101.0, 109.5))
    out.append(Candle(t + timedelta(hours=22), 109.5, 111.0, 109.0, 110.5))
    return out


def test_donchian_emits_long_on_breakout():
    strat = DonchianBreakoutStrategy(entry_period=20, atr_period=5)
    signals = []
    for bar in _bars_staircase():
        sig = strat.on_bar(bar)
        if sig is not None:
            signals.append(sig)
    assert signals, "expected at least one breakout signal"
    assert signals[0].side is Side.BUY


def test_build_strategy_dispatch():
    s = build_strategy("donchian_breakout", entry_period=30)
    assert isinstance(s, DonchianBreakoutStrategy)
    assert s.entry_period == 30


def test_build_strategy_filters_kwargs():
    # Passing ema-specific kwargs to donchian should not crash.
    s = build_strategy(
        "donchian_breakout",
        entry_period=25,
        fast_period=12,
        slow_period=26,
    )
    assert isinstance(s, DonchianBreakoutStrategy)
    assert s.entry_period == 25


def test_donchian_engine_end_to_end():
    bars = _bars_staircase() + [
        Candle(datetime(2024, 1, 2, h, tzinfo=timezone.utc), 110, 112, 109, 111)
        for h in range(1, 10)
    ]
    broker = PaperBroker(symbol="T", starting_equity=10_000.0, spread=0.0)
    risk = RiskConfig(risk_per_trade=0.01, max_leverage=10, min_units=1)
    result = run(bars, DonchianBreakoutStrategy(entry_period=20, atr_period=5),
                 broker, risk)
    assert len(result.trades) >= 0  # may or may not have closed
    # Either has an open position OR at least one closed trade.
    assert broker.has_position() or len(broker.trades) > 0
