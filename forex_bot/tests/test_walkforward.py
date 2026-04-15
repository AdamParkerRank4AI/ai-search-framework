from datetime import datetime, timedelta, timezone

from bot.data import SyntheticDataFeed
from bot.risk import RiskConfig
from bot.strategy import EmaCrossRsiStrategy
from bot.walkforward import make_fixed_windows, make_month_windows, run_walk_forward


def test_month_windows():
    feed = SyntheticDataFeed(
        n_bars=24 * 30 * 3,
        seed=9,
        start=datetime(2024, 1, 1, tzinfo=timezone.utc),
        timeframe=timedelta(hours=1),
    )
    bars = list(feed)
    windows = make_month_windows(bars)
    assert len(windows) >= 2
    assert windows[0].label.startswith("2024-")
    # Windows should cover all bars contiguously.
    assert windows[0].start == bars[0].timestamp
    assert windows[-1].end > bars[-1].timestamp


def test_fixed_windows():
    feed = SyntheticDataFeed(
        n_bars=24 * 10,
        seed=1,
        start=datetime(2024, 6, 1, tzinfo=timezone.utc),
        timeframe=timedelta(hours=1),
    )
    bars = list(feed)
    windows = make_fixed_windows(bars, days=3)
    assert len(windows) >= 3


def test_walkforward_runs():
    feed = SyntheticDataFeed(
        n_bars=24 * 30 * 3,  # ~3 months
        seed=11,
        volatility=0.0015,
        start=datetime(2024, 1, 1, tzinfo=timezone.utc),
        timeframe=timedelta(hours=1),
    )
    bars = list(feed)
    windows = make_month_windows(bars)
    report = run_walk_forward(
        bars=bars,
        windows=windows,
        strategy_factory=lambda: EmaCrossRsiStrategy(),
        risk=RiskConfig(risk_per_trade=0.01, max_leverage=5, min_units=1),
        symbol="TEST",
        starting_equity=10_000.0,
    )
    assert report.windows, "expected at least one window result"
    s = report.summary()
    # Summary keys exist and are well-formed.
    assert s["n_windows"] == len(report.windows)
    assert "mean_return_pct" in s
    assert "worst_return_pct" in s
