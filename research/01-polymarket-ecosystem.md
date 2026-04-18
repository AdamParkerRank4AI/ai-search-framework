# Polymarket GitHub Ecosystem & API Architecture

## Organisation Overview

**GitHub Org**: [github.com/Polymarket](https://github.com/Polymarket)
- 95+ public repositories
- Core focus: CLOB infrastructure, conditional tokens, smart contracts, SDKs
- Active development across Python, TypeScript, Rust, Go, Solidity

---

## Core Architecture

### Settlement Layer
- **Chain**: Polygon (MATIC) — low gas, fast finality
- **Token Standard**: Conditional Token Framework (CTF) by Gnosis
- **Collateral**: USDC (bridged via Polygon PoS bridge)
- **Oracle**: UMA Optimistic Oracle — 2-hour liveness window, managed proposer whitelist (99.7% accuracy)

### Trading Layer — CLOB (Central Limit Order Book)
- Off-chain order matching (hybrid model)
- On-chain settlement via Exchange contract
- Maker-taker fee structure: 0% maker / 0% taker (current promo, subject to change)
- Minimum tick size: $0.01
- Orders signed via EIP-712

---

## The 4-Part API

### 1. Gamma API (Market Discovery)
- **Base URL**: `https://gamma-api.polymarket.com`
- **Purpose**: Market metadata, descriptions, tags, resolution criteria
- **Key Endpoints**:
  - `GET /markets` — list all markets with filters
  - `GET /markets/{id}` — single market detail
  - `GET /events` — grouped market events
- **Rate Limits**: Generous (no published hard limit, ~100 req/s observed)
- **No auth required**

### 2. CLOB API (Trading)
- **Base URL**: `https://clob.polymarket.com`
- **Purpose**: Order placement, cancellation, order book data
- **Key Endpoints**:
  - `GET /book` — full order book for a token
  - `GET /midpoint` — current midpoint price
  - `GET /price` — best bid/ask
  - `POST /order` — place order (requires API key + L1/L2 auth headers)
  - `DELETE /order/{id}` — cancel order
  - `GET /trades` — trade history
- **Auth**: API key + HMAC signature (L2 headers) or Polymarket proxy wallet
- **Rate Limits**: ~100 req/s per key

### 3. Data API (Positions & History)
- **Purpose**: Portfolio positions, P&L, historical data
- **Endpoints**:
  - `GET /positions` — current positions
  - `GET /profit-loss` — P&L by market

### 4. WebSocket API (Real-Time)
- **URL**: `wss://ws-subscriptions-clob.polymarket.com/ws`
- **Channels**:
  - `market` — real-time price/volume updates
  - `user` — order fills, cancellations
- **Protocol**: Standard WebSocket with JSON messages
- **Heartbeat**: Ping/pong every 30s

---

## Key Repositories

### Smart Contracts
| Repo | Description | Language |
|------|-------------|----------|
| `ctf-exchange` | Core CLOB exchange contract (order matching, settlement) | Solidity |
| `neg-risk-ctf-adapter` | NegRisk adapter for multi-outcome markets | Solidity |
| `conditional-tokens-contracts` | Gnosis CTF implementation (fork) | Solidity |
| `uma-ctf-adapter` | UMA oracle integration for market resolution | Solidity |
| `exchange-fee-module` | Fee calculation module | Solidity |

### SDKs & Client Libraries
| Repo | Language | Status | Notes |
|------|----------|--------|-------|
| `py-clob-client` | Python | Active | Most popular, best documented |
| `clob-client` | TypeScript | Active | Full featured |
| `rs-clob-client` | Rust | Experimental | Incomplete, community contributions welcome |
| `go-order-utils` | Go | Active | Order signing utilities |
| `py-order-utils` | Python | Active | Low-level order construction |

### Infrastructure
| Repo | Description |
|------|-------------|
| `polymarket-liq-mining` | Liquidity mining reward calculator |
| `terra-bridge` | Cross-chain bridge (deprecated) |
| `polaris` | Internal tooling framework |

### Frontend & UI
| Repo | Description |
|------|-------------|
| `polymarket-web` | Main web app (older version) |
| `widgets` | Embeddable market widgets |
| `embed` | iFrame embed integration |

---

## SDK Deep Dive: py-clob-client

```python
from py_clob_client.client import ClobClient
from py_clob_client.clob_types import OrderArgs, OrderType

# Initialize
client = ClobClient(
    host="https://clob.polymarket.com",
    key=API_KEY,
    chain_id=137,  # Polygon
    funder=WALLET_ADDRESS,
    signature_type=2,  # POLY_GNOSIS_SAFE
    private_key=PRIVATE_KEY
)

# Get order book
book = client.get_order_book(token_id=TOKEN_ID)

# Place limit order
order = client.create_and_post_order(OrderArgs(
    token_id=TOKEN_ID,
    price=0.55,
    size=100,
    side="BUY",
    order_type=OrderType.GTC
))

# Cancel order
client.cancel(order_id=ORDER_ID)
```

---

## NegRisk System (Multi-Outcome Markets)

### How It Works
- Markets with >2 outcomes use NegRisk adapter
- Each outcome has a YES and NO token
- All YES tokens across outcomes sum to $1.00
- `MergePositions` contract allows converting complete sets back to USDC
- Enables arbitrage between correlated outcomes

### Key Insight for Bots
- If YES prices across all outcomes sum to < $1.00 → buy all YES tokens, merge for risk-free profit
- If YES prices sum to > $1.00 → buy all NO tokens
- Typical spread: 0.5-3% on multi-outcome markets (e.g., "Who will be the next Pope?")

---

## What's Missing (Gaps & Opportunities)

### No Official Tools For:
1. **Portfolio analytics** — no P&L dashboard beyond basic positions
2. **Historical price charts API** — must scrape or use community tools
3. **Market creation SDK** — markets created by Polymarket team only
4. **Automated resolution tracking** — must monitor UMA oracle manually
5. **Cross-market correlation tools** — no official way to track related markets
6. **Backtesting framework** — no historical order book data API
7. **Alert/notification system** — no official price alert API
8. **Bulk order management** — SDK handles one order at a time

### Community-Filled Gaps:
- `polymarket-resolve` — community resolution tracker
- Various Dune Analytics dashboards for on-chain data
- Telegram bots for price alerts (unofficial)
- Chrome extensions for enhanced UI

---

## Rate Limits & Practical Considerations

| API | Rate Limit | Auth Required | Best For |
|-----|-----------|---------------|----------|
| Gamma | ~100/s | No | Market discovery, scanning |
| CLOB | ~100/s | Yes (API key) | Trading, order book |
| WebSocket | 1 connection | Yes | Real-time monitoring |
| On-chain | N/A (Polygon RPC) | No | Settlement verification |

### Latency Observations
- Gamma API: 50-150ms response time
- CLOB API: 20-80ms response time
- WebSocket: 10-50ms for price updates
- Order execution: 100-500ms (off-chain matching)
- On-chain settlement: 2-5 seconds (Polygon block time)

---

## Sources
- https://github.com/Polymarket
- https://docs.polymarket.com
- https://learn.polymarket.com
- https://github.com/Polymarket/py-clob-client
- https://github.com/Polymarket/clob-client
- https://github.com/Polymarket/ctf-exchange
- https://github.com/Polymarket/neg-risk-ctf-adapter
