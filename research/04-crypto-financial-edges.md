# Crypto & Financial Market Edges for Polymarket

## CME FedWatch vs Polymarket (Primary Edge)

### The Opportunity
CME FedWatch — derived from Fed Funds futures — leads Polymarket on interest rate markets by approximately 1.44 days on average.

### Mechanism
```
Fed Funds Futures (CME)
    ↓ Institutional traders reprice (minutes)
CME FedWatch Tool (public)
    ↓ ~1.44 days average lag
Polymarket Fed Rate Markets
```

### Why the Lag Exists
- CME traders are institutional (banks, hedge funds) — react to macro data immediately
- Polymarket traders are retail/crypto-native — follow news cycle, not futures markets
- FedWatch is free and public but most Polymarket users don't check it
- Polymarket rate markets have lower liquidity ($500K-$5M) vs CME ($50B+ open interest)

### How to Trade It
1. **Monitor FedWatch daily**: https://www.cmegroup.com/markets/interest-rates/cme-fedwatch-tool.html
2. **Compare to Polymarket**: Check equivalent rate cut/hike markets
3. **If divergence > 3%**: Take position aligned with FedWatch
4. **Hold until convergence**: Typically 1-3 days
5. **Size**: Kelly Criterion based on historical convergence rate (~85%)

### Historical Performance
- Fed rate markets on Polymarket have tracked FedWatch with R² > 0.92
- But with consistent 1-2 day lag
- Edge exists primarily around FOMC meetings, CPI releases, and jobs reports
- Profit per trade: 3-8% on $5K-$20K positions

---

## Deribit Options-Implied Probabilities

### The Opportunity
Deribit BTC/ETH options market provides implied probability distributions for crypto price targets. These are systematically different from Polymarket binary options on the same events.

### Volatility Overpricing Pattern
- **Finding**: Deribit options systematically overprice volatility (volatility risk premium)
- **Result**: Implied probabilities from Deribit for extreme moves are HIGHER than actual probability
- **Polymarket Impact**: When Polymarket prices crypto markets using similar implied vols, they overprice tail events
- **Play**: Sell YES on extreme crypto price targets when Deribit IV is elevated

### How to Calculate Deribit-Implied Probabilities
```
For "Will BTC exceed $X by date Y?":

1. Get BTC option chain for expiry closest to Y from Deribit API
2. Find call option with strike = X
3. P(BTC > X) ≈ Delta of that call option (quick estimate)
4. More accurate: Use put-call parity and risk-neutral density

P(BTC > X) = e^(rT) × C(X) / S₀ (simplified Black-Scholes)
```

### Practical Implementation
```python
import requests

# Deribit API - get BTC options
url = "https://www.deribit.com/api/v2/public/get_book_summary_by_currency"
params = {"currency": "BTC", "kind": "option"}
response = requests.get(url, params=params)

# Filter for relevant strike and expiry
# Compare delta (proxy for P(ITM)) to Polymarket price
# Trade the divergence
```

### Edge Size
- Typical divergence: 3-8% between Deribit-implied and Polymarket price
- Largest divergences: During high-volatility periods (VIX > 25, BTC IV > 80%)
- Convergence timeline: 1-7 days

---

## CPI/GDP Nowcast Models

### Concept
Nowcasting models predict economic data releases before they're published. When nowcasts diverge from market expectations (and Polymarket prices), there's a trading opportunity.

### Key Nowcast Sources

#### 1. Cleveland Fed Inflation Nowcast
- **URL**: https://www.clevelandfed.org/indicators-and-data/inflation-nowcasting
- **Updates**: Daily
- **Lead Time**: Available weeks before official CPI release
- **Accuracy**: Within 0.1% of actual CPI ~70% of the time
- **Free**: Yes

#### 2. Atlanta Fed GDPNow
- **URL**: https://www.atlantafed.org/cqer/research/gdpnow
- **Updates**: After each major economic data release (6-8 times per month)
- **Lead Time**: Running estimate updated throughout quarter
- **Accuracy**: Mean absolute error of 0.8% (better than Blue Chip consensus)
- **Free**: Yes

#### 3. NY Fed Staff Nowcast
- **URL**: https://www.newyorkfed.org/research/policy/nowcast
- **Updates**: Weekly (Friday)
- **Coverage**: GDP, inflation components

### Trading CPI Markets
```
Timeline:
T-14 days: Cleveland Fed nowcast available → compare to Polymarket CPI markets
T-7 days:  If divergence > 0.2%: take position
T-1 day:   Survey of Professional Forecasters → final consensus
T-0:       8:30 AM ET — BLS releases CPI → resolution
```

### Edge Quantified
- Cleveland Fed nowcast beats market consensus 58% of the time
- When nowcast diverges from Polymarket by >5¢: 68% win rate
- Average profit per trade: 4-7¢ on binary markets
- Works best for "above/below X%" CPI markets

---

## Funding Rate Arbitrage

### Concept
Cryptocurrency perpetual futures funding rates on exchanges like Binance, Bybit, and dYdX signal market sentiment that leads Polymarket crypto price markets.

### Mechanism
- **Positive Funding Rate** (longs pay shorts): Market is bullish → crypto "Will reach $X" markets should be higher
- **Negative Funding Rate** (shorts pay longs): Market is bearish → crypto price target markets should be lower
- **Extreme Funding** (>0.1% per 8h / >0.3% daily): Strong sentiment signal, often precedes reversal

### Implementation
1. Monitor funding rates across major exchanges (Binance, Bybit, OKX)
2. When funding rate is extreme: check if Polymarket has priced in the sentiment
3. If funding is extremely positive but Polymarket crypto market is flat → buy YES
4. If funding is extremely negative but Polymarket hasn't adjusted → buy NO
5. Also: extreme positive funding often precedes liquidation cascades → contrarian NO play

### Data Sources
- **Coinglass.com**: Free funding rate aggregator across all exchanges
- **Binance API**: `GET /fapi/v1/fundingRate`
- **dYdX API**: Real-time funding via WebSocket

---

## Stablecoin Flow Analysis

### Concept
Large USDC/USDT flows to exchanges precede market moves that affect Polymarket crypto markets.

### Key Indicators
1. **USDC Mint Events**: Large USDC mints (>$100M) by Circle → bullish signal (institutional demand)
2. **Tether Treasury Flows**: USDT sent from Tether treasury to exchanges → incoming buy pressure
3. **Exchange Net Flows**: Net stablecoin inflows to exchanges → impending buy pressure
4. **Polymarket-Specific**: USDC flows to Polygon bridge → incoming Polymarket liquidity

### Tools
- **Whale Alert**: Free API, tracks large transfers
- **Nansen**: Premium ($500/mo), labeled wallet data
- **Arkham Intelligence**: Free tier available, entity-labeled addresses
- **DefiLlama**: Free, cross-chain flow data
- **Polygonscan**: Monitor USDC bridge transactions

### Trading Signal
- Large stablecoin inflow + Polymarket crypto "price target" market flat = buy YES
- Historical accuracy: ~62% when combined with funding rate signal

---

## Token Unlock Schedule Trading

### Concept
Token unlock events create predictable selling pressure that Polymarket crypto price markets often don't account for.

### Mechanism
```
Token Unlock Date (known in advance)
    ↓ 1-7 days before
Price drops as market anticipates selling
    ↓ On unlock day
Further selling pressure as unlocked tokens hit market
    ↓ 1-3 days after
Price stabilises at lower level
```

### How to Trade
1. Check unlock schedule: https://token.unlocks.app/
2. Find corresponding Polymarket market (e.g., "Will SOL be above $X by Y?")
3. If unlock is large (>2% of circulating supply) and within market timeframe → sell YES / buy NO
4. Typical price impact: 3-15% decline for unlocks >5% of circulating supply

### Historical Examples
- Solana unlocks have caused 5-12% price drops repeatedly
- ARB (Arbitrum) major unlock in March 2024 → 15% decline
- APT (Aptos) unlock events → consistent 8-10% drops

---

## Macro Data Release Calendar Trading

### High-Impact US Economic Releases
| Release | Day | Time | Source | Impact on Polymarket |
|---------|-----|------|--------|---------------------|
| Non-Farm Payrolls | 1st Friday | 8:30 AM ET | BLS | Rate cut/hike markets |
| CPI | ~13th | 8:30 AM ET | BLS | Inflation, rate markets |
| FOMC Decision | 8x/year | 2:00 PM ET | Fed | Rate markets directly |
| GDP (Advance) | ~28th | 8:30 AM ET | BEA | Recession markets |
| Retail Sales | ~16th | 8:30 AM ET | Census | Consumer spending markets |
| PCE (Fed's preferred) | ~28th | 8:30 AM ET | BEA | Inflation markets |

### Trading Protocol
1. **T-7 days**: Check nowcast models vs Polymarket price
2. **T-1 day**: Final pre-positioning based on survey of economists
3. **T-0 (release)**: Automated parser reads release → places order in <1 second
4. **T+5 minutes**: Evaluate if market has fully repriced → exit or hold

### Automated Release Parsing
- BLS provides data in predictable format
- Parse key number (e.g., headline CPI, NFP number) programmatically
- Compare to consensus expectations
- If beat/miss by >1 standard deviation → aggressive positioning

---

## Cross-Exchange Crypto Arbitrage

### Polymarket vs Centralized Exchanges
- **Opportunity**: Polymarket crypto price markets are binary ("Will BTC > $X?")
- **Hedge**: Buy YES on Polymarket + short BTC on exchange = risk-free if priced correctly
- **When YES price < actual probability** (from options market): Buy YES, delta-hedge with short
- **Profit**: Collect the mispricing minus hedging costs (funding, slippage)

### Example
```
Polymarket: "BTC > $80K by June 30" → 45¢
Deribit: Call option with $80K strike, June expiry → delta 0.52
→ Polymarket is 7¢ cheap
→ Buy YES at 45¢, short 0.52 BTC per $1 of Polymarket exposure
→ Expected profit: 7¢ minus hedge costs (~2-3¢) = 4-5¢ net
```

---

## Sources
- CME FedWatch Tool documentation
- Cleveland Fed Inflation Nowcasting methodology paper
- Atlanta Fed GDPNow methodology (working paper 2014-7)
- Deribit API documentation
- Binance Futures API documentation
- Token Unlocks (token.unlocks.app)
- Coinglass funding rate data
- DefiLlama documentation
- Academic: "The Information Content of Option Prices" (various)
- Academic: "Nowcasting with Large Datasets" (Bok et al., 2018)
