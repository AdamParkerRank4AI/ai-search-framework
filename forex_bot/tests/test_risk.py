import math

import pytest

from bot.risk import RiskConfig, size_position
from bot.strategy import Side, Signal


def test_risk_config_bounds():
    with pytest.raises(ValueError):
        RiskConfig(risk_per_trade=0.10)
    with pytest.raises(ValueError):
        RiskConfig(risk_per_trade=0.0)
    with pytest.raises(ValueError):
        RiskConfig(max_leverage=0)


def test_size_respects_risk_per_trade():
    sig = Signal(
        side=Side.BUY, price=1.1000, stop_loss=1.0950, take_profit=1.1100
    )
    cfg = RiskConfig(risk_per_trade=0.01, max_leverage=100, min_units=1)
    units = size_position(sig, equity=10_000, config=cfg)
    # Risk = 0.01 * 10000 = 100. Stop distance = 0.005. Units = 20000.
    assert math.isclose(units, 20_000, rel_tol=1e-6)


def test_size_capped_by_leverage():
    sig = Signal(
        side=Side.BUY, price=1.1000, stop_loss=1.0999, take_profit=1.1100
    )
    cfg = RiskConfig(risk_per_trade=0.01, max_leverage=5, min_units=1)
    units = size_position(sig, equity=10_000, config=cfg)
    # By-risk would be huge; leverage caps at equity*lev/price.
    expected = (10_000 * 5) / 1.1000
    assert math.isclose(units, expected, rel_tol=1e-6)


def test_size_zero_when_below_min_units():
    sig = Signal(
        side=Side.BUY, price=1.1000, stop_loss=1.0000, take_profit=1.1100
    )
    cfg = RiskConfig(risk_per_trade=0.01, max_leverage=5, min_units=1000)
    units = size_position(sig, equity=10, config=cfg)
    assert units == 0.0


def test_short_sign():
    sig = Signal(
        side=Side.SELL, price=1.1000, stop_loss=1.1050, take_profit=1.0900
    )
    cfg = RiskConfig(risk_per_trade=0.01, max_leverage=100, min_units=1)
    units = size_position(sig, equity=10_000, config=cfg)
    assert units < 0
