# Sports Market Edges — Tennis, Football & Beyond

## Tennis Latency Arbitrage (Primary Edge)

### The Opportunity
Polymarket's tennis markets have a significant structural latency gap that creates exploitable arbitrage windows.

### Data Feed Architecture
```
Live Match Event (point scored)
    ↓ ~0.5s
Sportradar / Official ATP Feed
    ↓ ~1-3s
Betfair / Traditional Bookmakers
    ↓ ~5-60s (!!!)
Polymarket Order Book Update
```

### Key Findings
- **Sportradar Feed Latency**: 1-3 seconds from point completion
- **Betfair Repricing**: 2-5 seconds (mature infrastructure, professional market makers)
- **Polymarket Repricing**: 5-60 seconds (thinner books, fewer automated market makers)
- **Exploitable Window**: 3-57 seconds where Polymarket price is stale
- **3-Second Taker Delay**: Polymarket enforces a 3-second delay on market orders — this HELPS latency arbs who use limit orders (no delay) and HURTS reactive market makers

### The $8M Bot
- A single bot reportedly made $8M+ on Polymarket sports markets
- Strategy: Automated trading using faster data feeds than Polymarket's market makers
- Operated across tennis, football, and basketball markets
- Used point-by-point live data to calculate real-time win probabilities
- Placed aggressive limit orders when Polymarket price diverged from model

### "swisstony" Case Study
- Turned $5 into $3.7M primarily on sports markets
- Used a combination of domain expertise and speed advantage
- Focused on tennis and football where latency gaps are widest
- Active during live matches when price movements are fastest

### How to Execute Tennis Latency Arb

#### Phase 1: Data Infrastructure
1. **Fast Data Source**: Sportradar API ($500-$2K/month) or free alternatives:
   - FlashScore web scraping (2-5s latency)
   - ATP/WTA live scoring pages (3-8s latency)
   - Tennis Abstract API (free, 5-10s latency)
2. **Win Probability Model**: Point-by-point model using:
   - Current score state (sets, games, points)
   - Server/returner advantage
   - Player ELO/Glicko-2 ratings
   - Surface-specific performance
   - Historical match completion patterns
3. **Pre-computed Lookup Table**: Generate win probabilities for every possible score state before match starts

#### Phase 2: Execution
1. Monitor score changes via fast feed
2. Look up pre-computed win probability for new score state
3. Compare to current Polymarket price
4. If divergence > threshold (typically 3-5¢): place limit order
5. Wait for market to catch up → close position or let it ride

#### Phase 3: Risk Management
- Maximum position per match: 5% of bankroll
- Stop loss if model divergence exceeds 15¢ (suggests model error, not market error)
- Avoid matches with injury risk (retirement invalidates most markets)
- Track actual vs expected P&L to calibrate model

### In-Play Tennis Model (Simplified)
```
P(player wins) = f(
    sets_won, games_won, points_won,   # current state
    is_serving,                          # serve advantage
    elo_rating_diff,                     # player strength
    surface_factor,                      # clay/grass/hard
    fatigue_factor,                      # match duration
    h2h_record                          # historical matchup
)
```

Key model parameters:
- Average hold percentage (serve): 62-65% (hard), 55-60% (clay), 65-70% (grass)
- Break point conversion: ~40% average
- Tiebreak win correlation with set win: 50/50 (independent of rating)

---

## Football (Premier League & European Leagues)

### EPL Edges on Polymarket

#### 1. Broadcast Delay Arbitrage
- **UK TV broadcast**: 5-8 second delay from live action
- **Stadium attendees**: Real-time (0s delay)
- **In-stadium phone apps**: 1-2s delay
- **Method**: If you have access to real-time data (stadium, certain streams), you can trade ahead of TV-watching crowd
- **Practical Issue**: Most Polymarket football bettors are watching delayed feeds

#### 2. Expected Goals (xG) Models
- **Concept**: Build xG model that better estimates match outcome than market
- **Data Sources**: 
  - StatsBomb (free tier available for select leagues)
  - FBref.com (free, comprehensive)
  - Understat.com (free xG data)
  - WhoScored.com (free ratings)
- **Edge**: When model probability differs from market by >5%
- **Best Markets**: Match outcome (1X2), both teams to score, over/under goals

#### 3. Team News Edge
- **Method**: Follow club-specific journalists on Twitter for early team news
- **Timeline**: Lineups officially released 1 hour before kickoff
- **Early Leaks**: Sometimes 2-4 hours before via journalist speculation
- **Key Players**: If a star player (Haaland, Salah, etc.) is unexpectedly absent → market moves 5-15¢
- **Automation**: Twitter API monitoring for specific journalist accounts

#### 4. Manager Rotation Patterns
- **Finding**: Certain managers rotate predictably for mid-week matches
- **Example**: Guardiola rotates 4-5 players for League Cup vs PL matches
- **Play**: If rotation expected → adjusted team strength → trade early

#### 5. Fixture Congestion Analysis
- **Concept**: Teams playing 3 matches in 7 days perform 8-12% worse in 3rd match
- **Data**: Cross-reference fixture list with squad depth and rotation patterns
- **Markets**: Match result, goals scored, clean sheet markets

### Football Model Framework
```
P(home_win) = base_rate × elo_adjustment × home_advantage × form × fatigue × injuries
```

Base rates (EPL):
- Home win: 46%
- Draw: 26%
- Away win: 28%
- Home advantage adjustment: +0.3 to +0.5 goals expected

---

## Other Sports Opportunities

### Basketball (NBA)
- **Edge**: Injury report monitoring — official reports updated 5:30 PM ET
- **Polymarket Response Time**: Often 10-30 minutes after official report
- **Play**: Monitor NBA injury API → trade when star player ruled out

### Boxing/MMA
- **Edge**: Weigh-in data — failed weight cuts affect performance
- **Method**: Monitor weigh-in results → trade if fighter comes in significantly over/under
- **Polymarket Lag**: Hours between weigh-in and market adjustment

### Cricket
- **Edge**: Toss result in cricket heavily influences match outcome on certain pitches
- **Method**: If Polymarket offers pre-toss markets, trade immediately after toss
- **Subcontinental Pitches**: Toss winner wins 60-65% on spinning tracks

### Golf
- **Edge**: Weather forecast for specific tee times
- **Method**: If PM tee time faces rain/wind and AM doesn't → early starters gain 1-2 strokes
- **Data**: Minute-by-minute weather forecasts for tournament venues

---

## Sports Arbitrage Tools & Resources

### Free Data Sources
| Source | Sports | Latency | Cost |
|--------|--------|---------|------|
| FlashScore | All | 2-5s | Free |
| FBref | Football | N/A (stats) | Free |
| Tennis Abstract | Tennis | 5-10s | Free |
| Understat | Football | N/A (xG) | Free |
| NBA API | Basketball | Real-time | Free |
| ESPN API | Multiple | 5-15s | Free |

### Premium Data Sources
| Source | Sports | Latency | Cost |
|--------|--------|---------|------|
| Sportradar | All | 1-3s | $500-2K/mo |
| Opta (Stats Perform) | Football | 1-2s | $1K-5K/mo |
| Second Spectrum | Basketball | Real-time | Enterprise |
| Hawkeye | Tennis/Cricket | Real-time | Enterprise |

### Key Metrics for Sports Model Quality
- **Brier Score**: Measures calibration (lower = better, target < 0.20)
- **Log Loss**: Penalises confident wrong predictions
- **ROI**: After fees and slippage, target > 3% per bet
- **Closing Line Value (CLV)**: If you consistently beat the closing price, you have edge

---

## Sources
- Polymarket Discord sports trading channels
- Documented $8M bot analysis (Twitter threads, on-chain analysis)
- swisstony on-chain history (Polygonscan)
- Sportradar API documentation
- StatsBomb open data (GitHub)
- FBref.com EPL historical data
- Academic: "Efficiency of Tennis Betting Markets" (various)
- Academic: "The Favourite-Longshot Bias in Football" (various)
