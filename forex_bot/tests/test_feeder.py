"""Tests for feeder.py helper functions (no network)."""

import csv
from datetime import datetime, timezone

from feeder import _last_timestamp, _append_bars
from bot.data import Candle


def test_last_timestamp_missing_file(tmp_path):
    p = tmp_path / "nonexistent.csv"
    assert _last_timestamp(p) is None


def test_last_timestamp_empty_file(tmp_path):
    p = tmp_path / "empty.csv"
    p.write_text("")
    assert _last_timestamp(p) is None


def test_append_creates_and_dedupes(tmp_path):
    p = tmp_path / "feed.csv"
    bars = [
        Candle(datetime(2024, 1, 1, tzinfo=timezone.utc), 1.0, 1.1, 0.9, 1.05),
        Candle(datetime(2024, 1, 1, 1, tzinfo=timezone.utc), 1.05, 1.15, 0.95, 1.10),
    ]
    n = _append_bars(p, bars)
    assert n == 2
    assert p.exists()
    # Second call: append one more.
    more = [
        Candle(datetime(2024, 1, 1, 2, tzinfo=timezone.utc), 1.10, 1.2, 1.0, 1.15),
    ]
    n2 = _append_bars(p, more)
    assert n2 == 1
    # Total rows (excluding header).
    with p.open() as fh:
        reader = csv.reader(fh)
        rows = list(reader)
    assert len(rows) == 4  # 1 header + 3 data
    last = _last_timestamp(p)
    assert "2024-01-01T02:00:00" in last
