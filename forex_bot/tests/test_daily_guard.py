from datetime import datetime, time, timedelta, timezone

import pytest

from bot.broker import PaperBroker
from bot.daily_guard import DailyGuard, DailyGuardConfig, SessionWindow
from bot.data import Candle, SyntheticDataFeed
from bot.engine import run
from bot.risk import RiskConfig
from bot.strategy import EmaCrossRsiStrategy, Side, Signal


def test_config_bounds():
    with pytest.raises(ValueError):
        DailyGuardConfig(daily_loss_cap_pct=0.5)
    with pytest.raises(ValueError):
        DailyGuardConfig(daily_profit_target_pct=0.0)


def test_session_window_contains():
    win = SessionWindow(time(8, 0), time(11, 0))
    assert win.contains(datetime(2024, 1, 1, 8, 30, tzinfo=timezone.utc))
    assert win.contains(datetime(2024, 1, 1, 10, 59, tzinfo=timezone.utc))
    assert not win.contains(datetime(2024, 1, 1, 11, 0, tzinfo=timezone.utc))
    assert not win.contains(datetime(2024, 1, 1, 7, 59, tzinfo=timezone.utc))


def test_loss_cap_triggers_close():
    """If equity drops below SoD - cap, guard should force-close any open position."""
    cfg = DailyGuardConfig(daily_loss_cap_pct=0.02, daily_profit_target_pct=0.05, sessions=[])
    guard = DailyGuard(cfg)
    broker = PaperBroker(symbol="T", starting_equity=1000.0, spread=0.0)

    now = datetime(2024, 1, 1, 8, 0, tzinfo=timezone.utc)
    bar0 = Candle(now, 100, 100, 100, 100)
    # First bar: SoD marker.
    guard.on_bar(bar0, broker)

    # Open a losing long position.
    bar1 = Candle(now + timedelta(hours=1), 100, 100, 95, 95)
    sig = Signal(side=Side.BUY, price=100.0, stop_loss=90.0, take_profit=110.0)
    broker.submit(sig, units=10, at_bar=bar1)  # 10 units long at ~100
    # Equity at close=95 is 1000 + (95-100)*10 = 950, -5% -> well past -2%.
    guard.on_bar(bar1, broker)
    assert not broker.has_position()
    assert not guard.accepts_signal(bar1)


def test_sessions_filter_signals():
    """Signals outside session windows must be rejected."""
    cfg = DailyGuardConfig(sessions=[SessionWindow(time(8, 0), time(9, 0))])
    guard = DailyGuard(cfg)

    inside = Candle(datetime(2024, 1, 1, 8, 30, tzinfo=timezone.utc), 1, 1, 1, 1)
    outside = Candle(datetime(2024, 1, 1, 14, 0, tzinfo=timezone.utc), 1, 1, 1, 1)
    broker = PaperBroker(symbol="T", starting_equity=1000.0)
    guard.on_bar(inside, broker)
    assert guard.accepts_signal(inside)
    assert not guard.accepts_signal(outside)


def test_engine_with_guard_runs():
    """End-to-end: engine accepts a guard and still produces valid trades."""
    feed = SyntheticDataFeed(n_bars=500, seed=3, volatility=0.002,
                             timeframe=timedelta(hours=1))
    bars = list(feed)
    broker = PaperBroker(symbol="DEMO", starting_equity=10_000.0, spread=0.0001)
    risk = RiskConfig(risk_per_trade=0.01, max_leverage=5, min_units=1)
    guard = DailyGuard(DailyGuardConfig(
        daily_loss_cap_pct=0.02,
        daily_profit_target_pct=0.01,
        sessions=[],
    ))
    result = run(bars, EmaCrossRsiStrategy(), broker, risk, guard=guard)
    assert isinstance(result.trades, list)
    hr = guard.daily_hit_rates()
    assert hr["days"] > 0
    # Rates should sum to ~100.
    assert abs(hr["target_pct"] + hr["loss_cap_pct"] + hr["ok_pct"] - 100.0) < 0.01
