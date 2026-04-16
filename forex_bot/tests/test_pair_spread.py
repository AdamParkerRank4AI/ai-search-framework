import csv
import math
from datetime import datetime, timedelta, timezone

from bot.broker import PaperBroker
from bot.data import Candle, CSVDataFeed
from bot.engine import run
from bot.pair_spread import PairSpreadStrategy, build_spread_csv
from bot.risk import RiskConfig
from bot.strategy import Side, build_strategy


def _write_csv(path, bars):
    with path.open("w", newline="") as fh:
        writer = csv.writer(fh)
        writer.writerow(["timestamp", "open", "high", "low", "close", "volume"])
        for b in bars:
            writer.writerow([b.timestamp.isoformat(), b.open, b.high, b.low, b.close, 0])


def _synth_pair(base_price, n, seed_offset=0):
    """Two correlated series that diverge then converge."""
    import random
    rng = random.Random(42 + seed_offset)
    bars = []
    p = base_price
    t = datetime(2024, 1, 1, tzinfo=timezone.utc)
    for i in range(n):
        step = rng.gauss(0, 0.001) * p
        p += step
        o = p
        c = p + rng.gauss(0, 0.0003) * p
        h = max(o, c) + abs(rng.gauss(0, 0.0003)) * p
        l = min(o, c) - abs(rng.gauss(0, 0.0003)) * p
        bars.append(Candle(t + timedelta(hours=i), round(o, 5), round(h, 5),
                           round(l, 5), round(c, 5)))
    return bars


def test_build_spread_csv(tmp_path):
    a_bars = _synth_pair(1.1000, 100, seed_offset=0)
    b_bars = _synth_pair(1.2700, 100, seed_offset=10)
    _write_csv(tmp_path / "a.csv", a_bars)
    _write_csv(tmp_path / "b.csv", b_bars)
    n = build_spread_csv(tmp_path / "a.csv", tmp_path / "b.csv",
                         tmp_path / "spread.csv")
    assert n == 100
    spread_bars = list(CSVDataFeed(tmp_path / "spread.csv"))
    assert len(spread_bars) == 100
    # Spread should be roughly a_price / b_price.
    ratio0 = a_bars[0].close / b_bars[0].close
    assert abs(spread_bars[0].close - ratio0) < 0.01


def test_pair_spread_strategy_emits_signals():
    """Feed a spread series with an artificial spike: expect a signal."""
    bars = []
    t = datetime(2024, 1, 1, tzinfo=timezone.utc)
    # 60 bars of stable ratio around 0.87.
    for i in range(80):
        p = 0.8700
        bars.append(Candle(t + timedelta(hours=i), p, p + 0.001, p - 0.001, p))
    # Spike: ratio jumps to 0.92 (well above 2-sigma).
    for i in range(80, 90):
        p = 0.9200
        bars.append(Candle(t + timedelta(hours=i), p, p + 0.001, p - 0.001, p))
    # Reversion back.
    for i in range(90, 110):
        p = 0.8700
        bars.append(Candle(t + timedelta(hours=i), p, p + 0.001, p - 0.001, p))

    strat = PairSpreadStrategy(lookback=60, entry_z=2.0, exit_z=0.5, atr_period=14)
    signals = []
    for bar in bars:
        sig = strat.on_bar(bar)
        if sig is not None:
            signals.append(sig)
    assert len(signals) >= 1
    # The spike is above mean -> short signal expected.
    assert signals[0].side is Side.SELL


def test_pair_spread_build_strategy_dispatch():
    s = build_strategy("pair_spread", lookback=30, entry_z=1.5)
    assert isinstance(s, PairSpreadStrategy)
    assert s.lookback == 30
    assert s.entry_z == 1.5


def test_pair_spread_engine_end_to_end():
    """Run the pair_spread strategy through the full engine on synthetic data."""
    bars = []
    t = datetime(2024, 1, 1, tzinfo=timezone.utc)
    import random
    rng = random.Random(99)
    p = 0.87
    for i in range(300):
        step = rng.gauss(0, 0.002)
        # Every 100 bars, inject a mean-reversion opportunity.
        if 100 <= i < 110 or 200 <= i < 210:
            step += 0.01
        elif 120 <= i < 130 or 220 <= i < 230:
            step -= 0.01
        p = max(p + step, 0.01)
        o = p
        c = p + rng.gauss(0, 0.001)
        h = max(o, c) + abs(rng.gauss(0, 0.001))
        l = min(o, c) - abs(rng.gauss(0, 0.001))
        bars.append(Candle(t + timedelta(hours=i), round(o, 5), round(h, 5),
                           round(l, 5), round(c, 5)))

    broker = PaperBroker(symbol="SPREAD", starting_equity=10_000, spread=0.0001)
    risk = RiskConfig(risk_per_trade=0.01, max_leverage=5, min_units=1)
    strat = PairSpreadStrategy(lookback=60, entry_z=2.0, atr_period=14)
    result = run(bars, strat, broker, risk)
    assert isinstance(result.trades, list)
    # The engine should have processed bars without errors.
    assert broker.cash > 0
