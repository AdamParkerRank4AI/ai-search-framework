from datetime import datetime, timedelta, timezone

from bot.tracker import Tracker


def test_round_trip(tmp_path):
    t = Tracker(label="demo", starting_equity=1000.0)
    start = datetime(2024, 1, 1, tzinfo=timezone.utc)
    for i in range(10):
        t.record(start + timedelta(hours=i), 1000 + i * 5, 1000 + i * 5, 0)
    path = tmp_path / "tracker.json"
    t.save(path)
    loaded = Tracker.load(path)
    assert loaded.label == "demo"
    assert loaded.starting_equity == 1000.0
    assert len(loaded.snapshots) == 10
    assert loaded.snapshots[-1].equity == 1045


def test_summary_basic():
    t = Tracker(label="x", starting_equity=100.0)
    start = datetime(2024, 1, 1, tzinfo=timezone.utc)
    # Ramp up then draw down.
    for i, eq in enumerate([100, 110, 120, 115, 108, 112, 118]):
        t.record(start + timedelta(days=i), eq, eq, 0)
    s = t.summary()
    assert s["starting_equity"] == 100.0
    assert s["final_equity"] == 118
    assert s["total_return_pct"] == 18.0
    assert s["max_drawdown_abs"] == 12.0  # peak 120 -> trough 108
    assert round(s["max_drawdown_pct"], 4) == 10.0


def test_monthly_returns():
    t = Tracker(label="x", starting_equity=100.0)
    # Two months of data.
    pts = [
        (datetime(2024, 1, 1, tzinfo=timezone.utc), 100.0),
        (datetime(2024, 1, 31, tzinfo=timezone.utc), 110.0),
        (datetime(2024, 2, 1, tzinfo=timezone.utc), 110.0),
        (datetime(2024, 2, 28, tzinfo=timezone.utc), 99.0),
    ]
    for ts, eq in pts:
        t.record(ts, eq, eq, 0)
    m = dict(t.monthly_returns())
    assert round(m["2024-01"], 4) == 0.10
    assert round(m["2024-02"], 4) == -0.10
