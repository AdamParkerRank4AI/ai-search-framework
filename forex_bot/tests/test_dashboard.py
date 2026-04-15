from datetime import datetime, timedelta, timezone

from bot.dashboard import render, write_dashboard
from bot.tracker import Tracker


def _make_tracker():
    t = Tracker(label="test", starting_equity=100.0)
    start = datetime(2024, 1, 1, tzinfo=timezone.utc)
    for i in range(30):
        t.record(start + timedelta(days=i), 100 + i, 100 + i, 0)
    return t


def test_render_produces_html():
    html = render(_make_tracker(), title="Test dashboard")
    assert "<!doctype html>" in html
    assert "Test dashboard" in html
    assert "Equity curve" in html
    assert "Monthly return" in html


def test_write_dashboard_file(tmp_path):
    out = tmp_path / "dash.html"
    path = write_dashboard(out, _make_tracker())
    assert path.exists()
    content = path.read_text()
    assert "<svg" in content
    assert "Tracking days" in content


def test_render_empty_tracker_does_not_crash():
    t = Tracker(label="empty", starting_equity=100.0)
    html = render(t)
    assert "<!doctype html>" in html
