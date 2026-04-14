import csv
from datetime import datetime, timezone

import pytest

from bot.data import Candle, CSVDataFeed, SyntheticDataFeed, write_csv


def test_candle_validation():
    with pytest.raises(ValueError):
        Candle(
            timestamp=datetime(2024, 1, 1, tzinfo=timezone.utc),
            open=1.0, high=0.9, low=0.5, close=0.8,
        )


def test_synthetic_feed_deterministic():
    a = list(SyntheticDataFeed(n_bars=100, seed=1))
    b = list(SyntheticDataFeed(n_bars=100, seed=1))
    assert len(a) == 100
    assert a == b


def test_round_trip_csv(tmp_path):
    feed = SyntheticDataFeed(n_bars=50, seed=3)
    bars = list(feed)
    path = tmp_path / "bars.csv"
    write_csv(path, bars)

    loaded = list(CSVDataFeed(path))
    assert len(loaded) == len(bars)
    for a, b in zip(bars, loaded):
        assert a.timestamp == b.timestamp
        assert abs(a.close - b.close) < 1e-9
