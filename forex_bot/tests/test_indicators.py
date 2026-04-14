import math

from bot.indicators import ATR, EMA, RSI, SMA


def test_sma_basic():
    sma = SMA(3)
    assert sma.value is None
    sma.update(1.0)
    sma.update(2.0)
    assert not sma.ready
    sma.update(3.0)
    assert sma.ready
    assert math.isclose(sma.value, 2.0)
    sma.update(4.0)
    assert math.isclose(sma.value, 3.0)


def test_ema_converges():
    ema = EMA(5)
    for _ in range(20):
        ema.update(100.0)
    assert ema.ready
    assert math.isclose(ema.value, 100.0, abs_tol=1e-6)


def test_atr_basic():
    atr = ATR(3)
    atr.update(10, 9, 9.5)
    atr.update(11, 10, 10.5)
    atr.update(10, 9, 9.5)
    assert atr.ready
    assert atr.value is not None and atr.value > 0


def test_rsi_bounds():
    rsi = RSI(14)
    price = 100.0
    for i in range(50):
        # Pure uptrend -> RSI should saturate near 100.
        price += 0.5
        rsi.update(price)
    assert rsi.value is not None
    assert 90 < rsi.value <= 100
