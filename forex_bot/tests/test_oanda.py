"""Tests for the OANDA fetcher.

No network: we test only the pure-Python helpers (parsing, env var
handling). The HTTP path is exercised in practice the first time
you run ``python main.py fetch ...`` with your OANDA key.
"""

import pytest

from bot.brokers.oanda import OandaError, _parse_candle, fetch_candles


def test_parse_incomplete_candle_returns_none():
    raw = {
        "time": "2024-01-01T00:00:00.000000000Z",
        "complete": False,
        "mid": {"o": "1.1", "h": "1.2", "l": "1.0", "c": "1.15"},
    }
    assert _parse_candle(raw) is None


def test_parse_complete_candle():
    raw = {
        "time": "2024-01-01T00:00:00.000000000Z",
        "complete": True,
        "volume": 42,
        "mid": {"o": "1.1000", "h": "1.1050", "l": "1.0950", "c": "1.1025"},
    }
    c = _parse_candle(raw)
    assert c is not None
    assert c.open == 1.1000
    assert c.close == 1.1025
    assert c.volume == 42
    assert c.timestamp.year == 2024


def test_parse_candle_malformed_raises():
    with pytest.raises(OandaError):
        _parse_candle({"time": "2024-01-01T00:00:00Z", "complete": True,
                       "mid": {"o": "bad"}})


def test_fetch_requires_api_key(monkeypatch):
    monkeypatch.delenv("OANDA_API_KEY", raising=False)
    with pytest.raises(OandaError, match="OANDA_API_KEY"):
        list(fetch_candles("EUR_USD", "H1", "2024-01-01T00:00:00Z",
                           "2024-01-02T00:00:00Z"))
