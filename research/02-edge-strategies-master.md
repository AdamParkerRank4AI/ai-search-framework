# Polymarket Edge Strategies — Master Taxonomy

## Strategy Hierarchy (7 Tiers)

```
Tier 0: Statistical Edge (Foundational)
Tier 1: Mathematical Arbitrage (Risk-Free)
Tier 2: Relative Value (Cross-Market)
Tier 3: Execution Edge (Speed & Efficiency)
Tier 4: Behavioral Edge (Market Psychology)
Tier 5: Speed Edge (Latency Arbitrage)
Tier 6: Domain Knowledge (Expert Information)
```

---

## Tier 0 — Statistical Edge (Foundational)

### 0.1 Systematic NO Strategy ("Nothing Ever Happens")
- **Base Rate**: 73.3% of Polymarket YES/NO questions resolve NO
- **Method**: Sell YES (or buy NO) on speculative event markets
- **Sweet Spot**: Markets with YES price 15-40¢ on events with no concrete catalyst
- **Categories**: Celebrity markets, "Will X happen by Y date?", speculative tech/crypto
- **Position Sizing**: Kelly Criterion — `f* = (bp - q) / b` where b = payout odds, p = true probability, q = 1-p
- **Risk**: Black swan events; mitigate via diversification across 50+ markets
- **Documented Edge**: ~8-12% annualised return over naive buy-and-hold

### 0.2 Calibration Exploits
- **Concept**: Polymarket crowds are systematically miscalibrated at extremes
- **Finding**: Events priced 90-95¢ resolve YES only ~80-85% of the time
- **Finding**: Events priced 5-10¢ resolve YES ~12-18% of the time (overpriced NO)
- **Play**: Fade extreme prices — sell at 95¢+, buy at 5¢-
- **Source**: Academic calibration studies on prediction markets (Metaculus, PredictIt analysis)

### 0.3 Time Decay Harvesting
- **Concept**: Markets with no new information drift toward resolution
- **Method**: Sell premium on stale markets where implied probability hasn't moved in 7+ days
- **Edge**: Theta-like decay as expiry approaches and uncertainty resolves
- **Best Markets**: Monthly resolution markets in final week with stable consensus

---

## Tier 1 — Mathematical Arbitrage (Risk-Free)

### 1.1 NegRisk Arbitrage (Multi-Outcome Markets)
- **Mechanism**: In N-outcome markets, all YES tokens must sum to $1.00
- **When sum < $1.00**: Buy all YES tokens → merge via MergePositions → receive USDC
- **When sum > $1.00**: Buy all NO tokens (equivalent to shorting the overpriced set)
- **Typical Spread**: 0.5-3% on markets with 5+ outcomes
- **Examples**: "Who will be next Pope?", "Which party wins?", award show winners
- **Execution**: Must buy atomically or near-atomically to avoid leg risk
- **Tools**: Custom smart contract that batches all buys + merge in single tx

### 1.2 YES + NO Arbitrage (Binary Markets)
- **Mechanism**: YES + NO must sum to $1.00
- **If YES(45¢) + NO(53¢) = 98¢**: Buy both → guaranteed 2¢ profit per share
- **Frequency**: Rare on liquid markets, more common on new/illiquid markets
- **Automation**: Monitor all binary markets for sum < $0.99

### 1.3 Cross-Platform Arbitrage
- **Polymarket vs Kalshi**: Same events, different prices, different user bases
- **Polymarket vs PredictIt**: PredictIt has 5% withdrawal fee — factor into arb calc
- **Polymarket vs Betfair**: Betfair has commission (2-5%) but different liquidity profile
- **Polymarket vs Metaculus**: Metaculus is non-monetary but provides calibrated probabilities as signals
- **Typical Spread**: 3-8% on political markets, 1-3% on crypto markets
- **Challenge**: Capital locked on both platforms simultaneously

### 1.4 Spread Compression Trades
- **Concept**: Wide bid-ask spreads on illiquid markets compress as volume arrives
- **Method**: Place limit orders at mid-price on wide-spread markets
- **Edge**: Earn the spread as both market maker and informed trader
- **Best Markets**: New markets (first 24-48 hours), niche markets with <$50K volume

---

## Tier 2 — Relative Value (Cross-Market)

### 2.1 Correlated Market Pairs
- **Example**: "Will BTC hit $100K by Dec?" trades at 40¢ while "Will BTC hit $80K by Dec?" trades at 55¢ — the spread should be wider given the $20K gap
- **Method**: Identify pairs where conditional probabilities are mispriced
- **Tools**: Build correlation matrix across all active markets

### 2.2 Conditional Probability Chains
- **Example**: P(Trump wins) × P(Tariffs | Trump wins) should ≈ P(Tariffs enacted)
- **If standalone tariff market is cheaper**: Buy tariff market, hedge with Trump market
- **Edge**: 2-5% on politically linked markets

### 2.3 Temporal Arbitrage
- **Concept**: Same question with different expiry dates should have monotonic probability relationship
- **Example**: "Will X happen by June?" should be ≤ "Will X happen by December?"
- **Play**: If June > December pricing, arbitrage the inversion

### 2.4 Index vs Component
- **Example**: "Will ANY G7 country have recession?" vs individual country recession markets
- **If individual countries all price low but aggregate prices high**: Sell the aggregate
- **Math**: P(any) = 1 - ∏(1 - P(individual_i))

---

## Tier 3 — Execution Edge (Speed & Efficiency)

### 3.1 Gas Optimization
- **Polygon gas**: Typically 30-100 gwei, but spikes during high activity
- **Method**: Pre-sign orders during low-gas periods, submit during spikes when others can't
- **Savings**: 10-50% on transaction costs during volatile periods

### 3.2 Smart Order Routing
- **Method**: Split large orders across price levels to minimize slippage
- **TWAP**: Time-weighted average price over minutes/hours for large positions
- **Iceberg Orders**: Show only partial size, refill automatically

### 3.3 MEV-Aware Execution
- **Risk**: Front-running on Polygon is less common but exists
- **Mitigation**: Use private mempools or Flashbots-style solutions on Polygon
- **Opportunity**: Back-run large trades that move the book

### 3.4 Maker vs Taker Strategy
- **Current fee structure**: 0% both sides (promotional)
- **When fees return**: Always prefer limit orders (maker) over market orders (taker)
- **Rebate farming**: If maker rebates are introduced, earn rebates by providing liquidity

---

## Tier 4 — Behavioral Edge (Market Psychology)

### 4.1 Sentiment Divergence
- **Concept**: When Polymarket price diverges from Twitter/Reddit/news sentiment
- **Tools**: FinBERT (97% accuracy financial sentiment), VADER, custom NLP
- **Method**: If sentiment is 80% positive but market prices only 60¢ → buy
- **Lag**: Sentiment leads price by 1-4 hours on breaking news

### 4.2 Anchoring Bias Exploitation
- **Finding**: Markets anchor to round numbers (50¢, 25¢, 75¢)
- **Method**: Place orders just above/below psychological levels
- **Example**: Bid at 49¢ when market trades at 50¢ during a dip — anchoring bias creates support at 50¢

### 4.3 Recency Bias Fade
- **Finding**: Markets overreact to recent events, especially in political markets
- **Method**: Fade large moves (>10¢) within 2 hours — mean reversion rate ~60%
- **Example**: Candidate gaffe → market drops 15¢ → typically recovers 8-10¢ within 24 hours
- **Exception**: Genuine structural changes (indictment, withdrawal from race)

### 4.4 Whale Watching
- **Method**: Track large wallets that consistently profit
- **Tool**: Dune Analytics queries, on-chain monitoring via Polygon RPC
- **Known Whales**: "Théo" (French trader, $50M+ portfolio), "Fredi9999" ($30M+), "swisstony" ($3.7M from $5)
- **Signal**: When 3+ profitable whales take same position → follow within 1 hour
- **Counter-Signal**: When whale enters illiquid market → likely moving price to exit later

### 4.5 Narrative Momentum Trading
- **Concept**: Markets move in narrative cycles — identify and ride them
- **Example**: AI hype → AI regulation markets move → AI company markets follow
- **Method**: Map narrative contagion paths between related markets

---

## Tier 5 — Speed Edge (Latency Arbitrage)

### 5.1 Social Media Speed Trading
- **Trump/Truth Social**: Use ProfileTracer webhook (~250ms latency from post)
- **Twitter/X**: Streaming API or firehose access
- **Pipeline**: Post detected → NLP classification → sentiment score → order placement
- **Total Latency Target**: <2 seconds from post to order
- **Edge Window**: 30 seconds to 5 minutes before market fully reprices
- **Documented Case**: Trump Iran tweet (7:04 AM ET) → suspicious Polymarket moves within minutes

### 5.2 News Wire Front-Running
- **Sources**: Reuters Eikon, Bloomberg Terminal, AP wire
- **Cost**: $2K-$25K/month for professional feeds
- **Edge**: 5-30 seconds ahead of social media propagation
- **Method**: Keyword triggers on wire headlines → automated order placement
- **Legal**: Not illegal on prediction markets (no insider trading laws apply to binary options on events)

### 5.3 Data Release Sniping
- **Targets**: CPI, GDP, jobs reports, Fed decisions
- **Method**: Pre-position based on nowcast models, add on release
- **BLS Release Time**: 8:30 AM ET — markets reprice within seconds
- **Edge**: Automated parsing of data releases faster than human traders
- **Tools**: FRED API, BLS API, custom parsers

### 5.4 On-Chain Oracle Monitoring
- **UMA Oracle**: Monitor proposer submissions before liveness period ends
- **Method**: If resolution is proposed but not yet final → trade on expected outcome
- **Risk**: Disputes can overturn proposals (rare, <0.3% of the time)
- **Edge**: 2-hour window where resolution is "known" but market hasn't fully adjusted

---

## Tier 6 — Domain Knowledge (Expert Information)

### 6.1 Weather Markets
- **Documented Case**: $1,000 → $79,000 on hurricane/temperature markets
- **Edge Sources**: ECMWF (European model), GFS (US model), private weather APIs
- **Method**: When ECMWF and GFS agree on extreme weather → market underprices certainty
- **Tools**: Open-Meteo API (free), WeatherAPI, NOAA data
- **Markets**: Hurricane landfall, temperature records, rainfall, snowfall

### 6.2 FDA/Biotech Markets
- **Edge**: Clinical trial data analysis, FDA advisory committee voting patterns
- **Method**: Track AdCom vote history — FDA follows AdCom recommendation 75-90% of time
- **Pre-AdCom Play**: If Phase 3 data is strong and AdCom historically favorable → buy YES
- **Sources**: ClinicalTrials.gov, FDA calendar, bioRxiv preprints

### 6.3 Sports Expert Models
- **Method**: Build ELO/Glicko-2 models for tennis, football, etc.
- **Edge**: Model output vs Polymarket price → bet when divergence > 5%
- **Data**: ATP/WTA rankings, head-to-head records, surface-specific performance
- **Tennis Specific**: In-match model using point-by-point data

### 6.4 Political Insider Knowledge
- **Legal Edge**: Following political scientists, poll aggregators, campaign finance data
- **Sources**: FEC filings, ActBlue/WinRed donation data, voter registration trends
- **Method**: Donation surge for candidate → market hasn't priced in → buy early
- **Midterm Pattern**: Dems priced at 84.5% House, 56.5% Senate (2026 cycle)

### 6.5 Crypto/DeFi Domain Knowledge
- **Unlock Schedules**: Token unlocks → price pressure → bet on price drop markets
- **Governance Votes**: Snapshot/Tally votes → trade outcome markets before vote closes
- **Protocol Events**: Merge, halving, hard fork → trade related Polymarket events

---

## Practical Execution Filter

### Viability Checklist (for each strategy)
1. **Capital Required**: <$1K (accessible) / $1K-$10K (moderate) / $10K+ (serious)
2. **Technical Complexity**: Low (manual) / Medium (scripts) / High (infrastructure)
3. **Time Commitment**: Passive (set & forget) / Active (daily) / Full-time (real-time)
4. **Edge Durability**: Days / Weeks / Months (before market adapts)
5. **Legal Risk**: None / Grey area / Jurisdiction-dependent
6. **Scalability**: Does the edge disappear with more capital?

### Top 5 Strategies by Risk-Adjusted Return
1. **Systematic NO** — Low risk, passive, proven base rate
2. **NegRisk Arbitrage** — Zero risk when executed correctly, limited by opportunities
3. **Weather Domain Knowledge** — High return, requires expertise, documented $79K case
4. **Social Media Speed Trading** — High return, high complexity, requires infrastructure
5. **Cross-Platform Arbitrage** — Medium return, low risk, capital-intensive

---

## Sources
- Polymarket Discord and community discussions
- Dune Analytics dashboards (polymarket_trades, polymarket_positions)
- Academic: "Prediction Market Accuracy in the Long Run" (Arrow et al.)
- Academic: "Information Aggregation in Prediction Markets" (Wolfers & Zitzewitz)
- GitHub repos: See 06-community-whales-tools.md for full catalog
- User-provided strategy framework and ranking system
