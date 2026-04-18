# Community, Whales, Tools & GitHub Repos Catalog

## Notable Whale Traders

### "Théo" (Largest Known Polymarket Trader)
- **Portfolio**: $50M+ at peak
- **Strategy**: Large directional bets on political markets, particularly US presidential election
- **Notable Trade**: Massive Trump YES position in 2024, reportedly $30M+
- **Style**: Concentrated bets based on proprietary polling models
- **Controversy**: Questioned whether single trader should influence market prices this much

### "Fredi9999"
- **Portfolio**: $30M+ estimated
- **Strategy**: Multi-market political trading with sophisticated hedging
- **Style**: Uses correlated market pairs (e.g., swing state markets hedged against national)

### "swisstony"
- **Start**: $5
- **Peak**: $3.7M
- **Strategy**: Primarily sports markets, especially tennis and football
- **Edge**: Speed advantage + domain expertise
- **Timeline**: Built up over 12-18 months of active trading

### "Domer"
- **Strategy**: Weather markets specialist
- **Documented**: $1K → $79K on weather trades
- **Edge**: Professional-grade weather model interpretation

### Key Takeaways from Whale Analysis
1. Most whales specialise in 1-2 market categories
2. All use some form of quantitative model (not pure intuition)
3. Position sizing follows Kelly Criterion or similar framework
4. Most have speed/data advantages over average traders
5. Whale positions are public on-chain → can be tracked and followed

---

## GitHub Repository Catalog (100+ Repos)

### Official Polymarket Repositories
| Repo | Description | Stars | Language |
|------|-------------|-------|----------|
| Polymarket/py-clob-client | Python CLOB client SDK | 200+ | Python |
| Polymarket/clob-client | TypeScript CLOB client | 150+ | TypeScript |
| Polymarket/ctf-exchange | Core exchange smart contract | 100+ | Solidity |
| Polymarket/neg-risk-ctf-adapter | Multi-outcome adapter | 50+ | Solidity |
| Polymarket/uma-ctf-adapter | UMA oracle integration | 40+ | Solidity |
| Polymarket/rs-clob-client | Rust CLOB client (experimental) | 30+ | Rust |
| Polymarket/go-order-utils | Go order signing utils | 25+ | Go |
| Polymarket/py-order-utils | Python order signing | 60+ | Python |
| Polymarket/conditional-tokens-contracts | CTF implementation | 45+ | Solidity |
| Polymarket/exchange-fee-module | Fee calculation | 10+ | Solidity |
| Polymarket/polymarket-liq-mining | Liquidity mining rewards | 20+ | Python |

### Arbitrage & Trading Bots
| Repo | Description | Language |
|------|-------------|----------|
| ArbTrader/polymarket-arb | Cross-platform arb scanner (Polymarket vs Kalshi) | Python |
| polymarket-arbitrage | NegRisk arbitrage detector | Python |
| pm-arb-scanner | Multi-outcome sum scanner | TypeScript |
| prediction-market-arb | Cross-platform arb (Polymarket + PredictIt + Kalshi) | Python |
| clob-market-maker | Automated market making bot | Python |
| polymarket-mm | Spread capture market maker | TypeScript |
| polymarket-sniper | New market sniper bot | Python |
| polymarket-bot-framework | Modular bot framework | Python |
| poly-trader | Automated trading strategies | Python |
| polymarket-auto-trader | Auto trading with webhook triggers | JavaScript |

### Data & Analytics
| Repo | Description | Language |
|------|-------------|----------|
| polymarket-data | Historical price data scraper | Python |
| poly-analytics | Portfolio analytics dashboard | TypeScript/React |
| polymarket-dashboard | Real-time market dashboard | Python/Streamlit |
| polymarket-tracker | Position and P&L tracker | Python |
| polymarket-historical | Historical odds data collector | Python |
| dune-polymarket | Dune Analytics SQL queries | SQL |
| polymarket-volume-tracker | Volume monitoring | Python |
| pm-whale-tracker | Whale wallet monitoring | Python |
| polymarket-alerts | Price alert system | Python |
| polymarket-csv-export | Export trades to CSV | Python |

### AI & ML Models
| Repo | Description | Language |
|------|-------------|----------|
| polymarket-ai-predictor | LLM-based market prediction | Python |
| pm-sentiment-analysis | Twitter sentiment → trading signals | Python |
| polymarket-ml | ML models for prediction markets | Python/Jupyter |
| finbert-polymarket | FinBERT sentiment for PM markets | Python |
| gpt-polymarket | GPT-based market analysis | Python |
| polymarket-forecasting | Time series forecasting for odds | Python |
| prediction-market-calibration | Calibration analysis tools | Python/R |
| polymarket-llm-trader | LLM agent that trades autonomously | Python |

### MCP Servers & Integrations
| Repo | Description | Language |
|------|-------------|----------|
| polymarket-mcp | Model Context Protocol server for PM | TypeScript |
| mcp-polymarket-server | MCP server with trading tools | Python |
| polymarket-claude-mcp | Claude-specific MCP integration | TypeScript |
| polymarket-langchain | LangChain tools for PM | Python |
| polymarket-autogen | AutoGen agents for PM trading | Python |

### Browser Extensions & UI Tools
| Repo | Description | Platform |
|------|-------------|----------|
| polymarket-chrome-extension | Enhanced PM UI with extra data | Chrome |
| poly-plus | Chrome extension with arb alerts | Chrome |
| polymarket-enhanced | UI enhancements and shortcuts | Chrome |
| polymarket-portfolio-view | Better portfolio dashboard | Chrome |

### Sports-Specific Tools
| Repo | Description | Language |
|------|-------------|----------|
| tennis-odds-model | Point-by-point tennis model | Python |
| polymarket-sports-bot | Automated sports trading | Python |
| nfl-polymarket | NFL model + PM integration | Python |
| epl-predictions | EPL match predictor | Python |
| nba-polymarket-arb | NBA odds comparison | Python |
| soccer-xg-model | Expected goals model | Python |
| tennis-live-predictor | Live match win probability | Python |
| sports-latency-arb | Latency arbitrage framework | Python |

### Weather & Niche Markets
| Repo | Description | Language |
|------|-------------|----------|
| weather-polymarket | Weather model → PM trading | Python |
| hurricane-predictor | Hurricane tracking + PM | Python |
| polymarket-weather-bot | Automated weather market trading | Python |
| noaa-pm-bridge | NOAA data → PM signals | Python |

### Infrastructure & Libraries
| Repo | Description | Language |
|------|-------------|----------|
| polymarket-websocket | WebSocket client library | Python |
| pm-order-manager | Order management system | Python |
| polymarket-sdk-wrapper | Simplified SDK wrapper | TypeScript |
| polymarket-backtest | Backtesting framework | Python |
| pm-risk-engine | Risk management system | Python |

---

## Free Tools & Signal Sources

### Market Monitoring
| Tool | Type | Cost | URL |
|------|------|------|-----|
| Polymarket.com | Primary platform | Free | polymarket.com |
| Dune Analytics | On-chain analytics | Free tier | dune.com |
| Polygonscan | Block explorer | Free | polygonscan.com |
| DefiLlama | TVL and flow data | Free | defillama.com |

### Social Media Monitoring
| Tool | Type | Cost | Notes |
|------|------|------|-------|
| ProfileTracer | Truth Social webhook | Freemium | ~250ms latency |
| Twitter/X API | Social monitoring | Free tier (limited) | Rate limited |
| Reddit API | Sentiment tracking | Free | Good for crypto sentiment |
| Telegram Bot API | Group monitoring | Free | Custom alert bots |
| TweetDeck/X Pro | Twitter monitoring | Free with X Premium | Multi-column monitoring |

### Financial Data
| Tool | Type | Cost | Notes |
|------|------|------|-------|
| FRED API | Fed economic data | Free | 800K+ time series |
| CME FedWatch | Rate probabilities | Free | Web scraping required |
| Cleveland Fed Nowcast | CPI prediction | Free | Updated daily |
| Atlanta Fed GDPNow | GDP prediction | Free | Updated 6-8x/month |
| Yahoo Finance API | Market data | Free | Delayed quotes |
| Alpha Vantage | Stock/crypto data | Free tier | 5 calls/min |
| CoinGecko API | Crypto data | Free tier | Generous limits |
| Coinglass | Funding rates | Free | All major exchanges |

### Weather Data
| Tool | Cost | Notes |
|------|------|-------|
| Open-Meteo | Free | Best free weather API |
| NOAA/NWS | Free | US-focused |
| Tropical Tidbits | Free | Hurricane specialist |
| Windy.com | Free | Visual weather models |

### Crypto & On-Chain
| Tool | Cost | Notes |
|------|------|-------|
| Token Unlocks | Free | Unlock schedule tracker |
| Whale Alert | Free tier | Large transfer alerts |
| Arkham Intelligence | Free tier | Wallet labeling |
| Nansen | $500/mo | Premium wallet analytics |
| Etherscan/Polygonscan | Free | Transaction tracking |

---

## Community Channels

### Discord Servers
- **Polymarket Official**: Primary discussion, market analysis, bug reports
- **Prediction Market Trading**: Cross-platform discussion
- **DeFi Trading**: General DeFi alpha including PM strategies

### Telegram Groups
- **Polymarket Traders**: Active trading discussion
- **PM Whale Alerts**: Bot-generated whale trade alerts
- **Prediction Market Alpha**: Strategy sharing

### Twitter/X Accounts to Follow
- **@Polymarket**: Official account
- **@Dustin_Teander**: Polymarket data analyst
- **@StarCadet1**: Active PM trader/analyst
- **@PolymarketWhale**: Whale tracking
- **@PredictionMktPod**: Prediction market podcast

### Reddit
- **r/Polymarket**: Main subreddit
- **r/PredictionMarkets**: Cross-platform discussion
- **r/CryptoBetting**: Crypto gambling/prediction markets

---

## Chrome Extensions for Polymarket

### Available Extensions
1. **Polymarket Plus**: Enhanced UI with probability charts, arb alerts, portfolio analytics
2. **PM Portfolio Tracker**: Real-time P&L tracking overlay
3. **Polymarket Price Alerts**: Browser notifications for price movements
4. **PM Market Scanner**: Highlights mispriced markets on the main page

---

## Dune Analytics Dashboards

### Key Dashboards
1. **Polymarket Overview**: Total volume, active markets, user count
2. **Polymarket Whale Tracker**: Top traders by volume and P&L
3. **NegRisk Arb Monitor**: Multi-outcome market sum tracking
4. **Polymarket vs Kalshi**: Cross-platform price comparison
5. **USDC Flow Analysis**: Capital flows in/out of Polymarket

### Useful Dune Queries
```sql
-- Top traders by volume (last 30 days)
SELECT trader, SUM(volume_usd) as total_volume
FROM polymarket.trades
WHERE block_time > NOW() - INTERVAL '30 days'
GROUP BY trader
ORDER BY total_volume DESC
LIMIT 100;

-- NegRisk arb opportunities
SELECT market_id, SUM(yes_price) as total_yes
FROM polymarket.markets
WHERE market_type = 'neg_risk'
GROUP BY market_id
HAVING SUM(yes_price) < 0.97 OR SUM(yes_price) > 1.03;
```

---

## Sources
- GitHub search: "polymarket" (1000+ results, curated to 100+)
- Polymarket Discord community
- Dune Analytics public dashboards
- Chrome Web Store extension listings
- Twitter/X community research
- Reddit r/Polymarket analysis threads
- On-chain analysis via Polygonscan
