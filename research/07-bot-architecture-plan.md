# Polymarket Bot Architecture — 3-Phase Build Plan

## Overview

A modular, scalable bot system for automated Polymarket trading across multiple strategy types. Designed for a solo operator or small team with Python/TypeScript skills.

---

## Architecture Diagram

```
┌─────────────────────────────────────────────────────┐
│                   SIGNAL LAYER                       │
│                                                      │
│  ┌──────────┐ ┌──────────┐ ┌──────────┐ ┌────────┐ │
│  │ Social   │ │ Data     │ │ On-Chain │ │ Domain │ │
│  │ Monitor  │ │ Feeds    │ │ Monitor  │ │ Models │ │
│  │(Twitter, │ │(FedWatch,│ │(Whales,  │ │(Weather│ │
│  │ Truth    │ │ CPI,     │ │ UMA,     │ │ Tennis,│ │
│  │ Social)  │ │ Deribit) │ │ NegRisk) │ │ xG)    │ │
│  └────┬─────┘ └────┬─────┘ └────┬─────┘ └───┬────┘ │
│       └──────┬─────┴──────┬─────┴──────┬─────┘      │
│              ▼            ▼            ▼             │
│         ┌────────────────────────────────┐           │
│         │        SIGNAL AGGREGATOR       │           │
│         │   (Scoring, Dedup, Priority)   │           │
│         └──────────────┬─────────────────┘           │
└────────────────────────┼─────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────┐
│                  DECISION LAYER                      │
│                                                      │
│  ┌──────────────┐  ┌────────────┐  ┌──────────────┐ │
│  │ Strategy     │  │ Risk       │  │ Position     │ │
│  │ Selector     │  │ Manager    │  │ Sizer        │ │
│  │ (Which edge  │  │ (Max loss, │  │ (Kelly       │ │
│  │  applies?)   │  │ correlation│  │  Criterion)  │ │
│  │              │  │  limits)   │  │              │ │
│  └──────┬───────┘  └─────┬──────┘  └──────┬───────┘ │
│         └────────┬───────┴────────┬────────┘         │
│                  ▼                ▼                   │
│         ┌────────────────────────────────┐           │
│         │        ORDER GENERATOR         │           │
│         │   (Limit/Market, Size, Side)   │           │
│         └──────────────┬─────────────────┘           │
└────────────────────────┼─────────────────────────────┘
                         ▼
┌─────────────────────────────────────────────────────┐
│                 EXECUTION LAYER                      │
│                                                      │
│  ┌──────────────┐  ┌────────────┐  ┌──────────────┐ │
│  │ Polymarket   │  │ Order      │  │ Gas          │ │
│  │ CLOB Client  │  │ Manager    │  │ Optimizer    │ │
│  │ (py-clob)    │  │ (Track,    │  │ (Polygon     │ │
│  │              │  │  cancel,   │  │  gas mgmt)   │ │
│  │              │  │  update)   │  │              │ │
│  └──────────────┘  └────────────┘  └──────────────┘ │
│                                                      │
│  ┌──────────────────────────────────────────────────┐│
│  │              MONITORING & LOGGING                ││
│  │  (P&L tracking, alerts, error handling)          ││
│  └──────────────────────────────────────────────────┘│
└─────────────────────────────────────────────────────┘
```

---

## Phase 1: Foundation (Week 1-2)

### Goal: Basic trading infrastructure + one simple strategy

### Components to Build

#### 1.1 Polymarket Client Wrapper
```python
# polymarket_client.py
from py_clob_client.client import ClobClient

class PolymarketClient:
    def __init__(self, config):
        self.client = ClobClient(
            host=config.CLOB_HOST,
            key=config.API_KEY,
            chain_id=137,
            funder=config.WALLET,
            signature_type=2,
            private_key=config.PRIVATE_KEY
        )
    
    def get_all_markets(self):
        """Fetch all active markets from Gamma API"""
        pass
    
    def get_orderbook(self, token_id):
        """Get current order book"""
        pass
    
    def place_limit_order(self, token_id, side, price, size):
        """Place a limit order with validation"""
        pass
    
    def cancel_order(self, order_id):
        """Cancel an existing order"""
        pass
    
    def get_positions(self):
        """Get all current positions"""
        pass
```

#### 1.2 Market Scanner
```python
# scanner.py
class MarketScanner:
    def scan_negisk_arb(self):
        """Find multi-outcome markets where YES prices don't sum to $1"""
        pass
    
    def scan_binary_arb(self):
        """Find binary markets where YES + NO < $0.99"""
        pass
    
    def scan_systematic_no(self):
        """Find YES/NO markets in 15-40¢ range with no catalyst"""
        pass
    
    def scan_spread(self):
        """Find markets with wide bid-ask spreads"""
        pass
```

#### 1.3 Risk Manager
```python
# risk.py
class RiskManager:
    def __init__(self, config):
        self.max_position_pct = 0.05   # 5% max per market
        self.max_portfolio_risk = 0.25  # 25% max total at risk
        self.max_correlation = 3        # max 3 positions in same category
    
    def kelly_size(self, edge, odds):
        """Calculate Kelly Criterion position size"""
        b = odds  # payout ratio
        p = edge  # estimated true probability
        q = 1 - p
        f = (b * p - q) / b
        return max(0, f * 0.5)  # half-Kelly for safety
    
    def check_limits(self, proposed_trade, portfolio):
        """Validate trade against risk limits"""
        pass
```

#### 1.4 First Strategy: NegRisk Arbitrage Scanner
- Scan all multi-outcome markets every 30 seconds
- Calculate YES sum for each market
- If sum < $0.97: calculate exact profit after gas
- If profitable: execute atomic buy-all + merge transaction
- Log all opportunities (including missed ones) for analysis

### Deliverables
- [ ] Working client wrapper with all basic operations
- [ ] Market scanner running on 30-second loop
- [ ] Risk manager with Kelly sizing
- [ ] NegRisk arb scanner (detect only — manual execution initially)
- [ ] Logging to file + Telegram alerts for opportunities
- [ ] P&L tracking spreadsheet/dashboard

---

## Phase 2: Signal Integration (Week 3-4)

### Goal: Add data feeds and automated signal generation

### Components to Build

#### 2.1 Social Media Monitor
```python
# signals/social.py
class SocialMonitor:
    def __init__(self):
        self.sources = [
            TruthSocialMonitor(),  # ProfileTracer webhook
            TwitterMonitor(),       # X API v2
            RedditMonitor(),        # Reddit API
        ]
    
    def start(self):
        """Start monitoring all social sources"""
        for source in self.sources:
            source.on_post(self.process_post)
    
    def process_post(self, post):
        """NLP classification → trading signal"""
        sentiment = finbert_classify(post.text)
        relevant_markets = self.match_markets(post)
        if sentiment.confidence > 0.8 and relevant_markets:
            self.emit_signal(Signal(
                source='social',
                markets=relevant_markets,
                direction=sentiment.direction,
                confidence=sentiment.confidence,
                urgency='HIGH'  # social signals decay fast
            ))
```

#### 2.2 Financial Data Feed
```python
# signals/financial.py
class FinancialFeed:
    def __init__(self):
        self.sources = {
            'fedwatch': FedWatchScraper(),
            'cleveland_nowcast': ClevelandFedAPI(),
            'gdpnow': AtlantaFedAPI(),
            'deribit': DeribitOptionsAPI(),
            'funding_rates': CoingleassAPI(),
        }
    
    def check_divergences(self):
        """Compare financial data to Polymarket prices"""
        for name, source in self.sources.items():
            data = source.fetch()
            pm_markets = self.find_related_markets(name)
            for market in pm_markets:
                divergence = data.implied_prob - market.price
                if abs(divergence) > 0.03:  # 3% threshold
                    self.emit_signal(Signal(
                        source=name,
                        market=market,
                        divergence=divergence,
                        confidence=data.confidence
                    ))
```

#### 2.3 On-Chain Monitor
```python
# signals/onchain.py
class OnChainMonitor:
    def __init__(self, rpc_url):
        self.w3 = Web3(Web3.HTTPProvider(rpc_url))
    
    def watch_whales(self, whale_addresses):
        """Monitor known profitable wallets"""
        pass
    
    def watch_uma_proposals(self):
        """Monitor UMA oracle resolution proposals"""
        pass
    
    def watch_usdc_flows(self):
        """Track large USDC flows to/from Polymarket"""
        pass
```

#### 2.4 Signal Aggregator
```python
# signals/aggregator.py
class SignalAggregator:
    def __init__(self):
        self.signals = PriorityQueue()
    
    def receive_signal(self, signal):
        """Score and queue incoming signal"""
        score = self.calculate_score(signal)
        self.signals.put((-score, signal))  # negative for max-heap
    
    def calculate_score(self, signal):
        """Composite score based on confidence, urgency, edge size"""
        return (
            signal.confidence * 0.4 +
            signal.urgency_score * 0.3 +
            abs(signal.divergence) * 0.3
        )
    
    def get_top_signals(self, n=5):
        """Get top N actionable signals"""
        pass
```

### Deliverables
- [ ] ProfileTracer integration for Truth Social monitoring
- [ ] Twitter/X API monitoring for key accounts
- [ ] FedWatch scraper running daily
- [ ] Deribit options implied probability calculator
- [ ] Whale wallet monitoring (top 20 addresses)
- [ ] Signal aggregator with priority scoring
- [ ] Automated signal → order pipeline (with human approval gate)

---

## Phase 3: Full Automation (Week 5-8)

### Goal: Autonomous trading with multiple strategies, monitoring, and risk controls

### Components to Build

#### 3.1 Strategy Engine
```python
# strategies/engine.py
class StrategyEngine:
    strategies = [
        NegRiskArbStrategy(),
        SystematicNOStrategy(),
        FedWatchDivergenceStrategy(),
        SocialSpeedStrategy(),
        WeatherModelStrategy(),
        TennisLatencyStrategy(),
        SpreadCompressionStrategy(),
    ]
    
    def evaluate(self, signal, market):
        """Determine which strategy to apply"""
        applicable = [s for s in self.strategies if s.matches(signal, market)]
        if not applicable:
            return None
        best = max(applicable, key=lambda s: s.expected_edge(signal, market))
        return best.generate_order(signal, market)
```

#### 3.2 Portfolio Manager
```python
# portfolio.py
class PortfolioManager:
    def rebalance(self):
        """Check all positions, close stale ones, update stops"""
        pass
    
    def calculate_pnl(self):
        """Real-time P&L across all positions"""
        pass
    
    def correlation_check(self):
        """Ensure portfolio isn't over-concentrated"""
        pass
    
    def generate_report(self):
        """Daily summary: trades, P&L, open positions, signals"""
        pass
```

#### 3.3 Monitoring Dashboard
```python
# dashboard.py (Streamlit or Grafana)
# Real-time display of:
# - Open positions and P&L
# - Active signals and their scores
# - Trade history
# - Strategy performance breakdown
# - Risk metrics (VaR, max drawdown, Sharpe)
# - System health (API latency, error rates)
```

#### 3.4 Alert System
```python
# alerts.py
class AlertSystem:
    channels = [
        TelegramChannel(bot_token, chat_id),
        EmailChannel(smtp_config),
    ]
    
    def alert(self, level, message):
        """Send alert to all channels"""
        # CRITICAL: System errors, large losses
        # HIGH: Trade executed, large signal detected
        # MEDIUM: New opportunity found
        # LOW: Daily summary, minor updates
        pass
```

### Deliverables
- [ ] Multi-strategy engine with strategy selection logic
- [ ] Portfolio manager with rebalancing
- [ ] Streamlit dashboard for monitoring
- [ ] Telegram bot for alerts and remote control
- [ ] Automated daily P&L reports
- [ ] Backtesting harness using historical data
- [ ] Kill switch (emergency stop all trading)
- [ ] Rate limit handling and API error recovery

---

## Tech Stack

### Core
| Component | Technology | Reason |
|-----------|-----------|--------|
| Language | Python 3.11+ | Best SDK support, ML libraries |
| Trading SDK | py-clob-client | Official, most maintained |
| Database | SQLite (dev) / PostgreSQL (prod) | Trade history, signals |
| Queue | Redis | Signal buffering, rate limiting |
| Scheduler | APScheduler | Periodic tasks (scanning, reporting) |

### Data & ML
| Component | Technology | Reason |
|-----------|-----------|--------|
| NLP | FinBERT + transformers | Financial sentiment |
| ML Framework | scikit-learn | Calibration models, feature engineering |
| Data Processing | pandas + numpy | Time series, statistical analysis |
| Web Scraping | httpx + BeautifulSoup | FedWatch, news sites |

### Infrastructure
| Component | Technology | Reason |
|-----------|-----------|--------|
| Hosting | VPS (Hetzner/DigitalOcean) | Low latency, cheap ($20/mo) |
| Monitoring | Grafana + Prometheus | System metrics |
| Alerts | Telegram Bot API | Free, instant, mobile |
| Logging | structlog → file + stdout | Structured logging |
| Secrets | .env + python-dotenv | API keys, private keys |

### Estimated Costs
| Item | Monthly Cost |
|------|-------------|
| VPS (4GB RAM, 2 vCPU) | $20 |
| Sportradar API (optional) | $500-2,000 |
| Twitter/X API (Basic) | $100 |
| ProfileTracer (Pro) | $50-200 |
| Total (without Sportradar) | $170-320/mo |
| Total (with Sportradar) | $670-2,320/mo |

---

## Security Considerations

### Private Key Management
- NEVER commit private keys to git
- Use environment variables or hardware wallet (Ledger via WalletConnect)
- Separate trading wallet from main wallet
- Maximum balance in trading wallet: Amount you can afford to lose

### API Key Security
- Rotate API keys monthly
- Use separate keys for read-only (scanning) and trading
- Rate limit all outbound requests
- Log all API calls for audit trail

### Operational Security
- Kill switch accessible via Telegram command
- Maximum daily loss limit (auto-stop at -5% portfolio)
- Maximum single trade size (2% of portfolio)
- All trades logged with timestamp, signal, and rationale

---

## Performance Targets

| Metric | Phase 1 | Phase 2 | Phase 3 |
|--------|---------|---------|---------|
| Active Strategies | 1 | 3-4 | 7+ |
| Markets Monitored | 50 | 200 | All active |
| Signal Sources | 1 (scanner) | 5 | 10+ |
| Trades/Day | 1-3 | 5-15 | 20-50 |
| Target Monthly Return | 3-5% | 5-10% | 8-15% |
| Maximum Drawdown | 5% | 10% | 15% |
| Uptime | 95% | 99% | 99.9% |

---

## Sources
- Polymarket API documentation (docs.polymarket.com)
- py-clob-client GitHub repo and examples
- FinBERT paper: "FinBERT: Financial Sentiment Analysis with Pre-Trained Language Models"
- Kelly Criterion: "Fortune's Formula" by William Poundstone
- Bot architecture patterns from crypto trading bot communities
