# Binance P2P Supported Pairs

This document outlines the approach to identifying supported fiat-crypto pairs on Binance P2P.

## Dynamic Discovery via `/api/v1/binance/pairs`

The recommended method for determining currently supported and active pairs is to use the `/api/v1/binance/pairs` endpoint. This endpoint dynamically queries the Binance P2P platform to return combinations of `fiat`, `asset`, and `tradeType` for which offers are currently available.

**Endpoint:** `/api/v1/binance/pairs`
**Method:** `GET`

**Example Response:**
```json
[
  {"fiat": "VES", "asset": "USDT", "tradeType": "BUY"},
  {"fiat": "USD", "asset": "BTC", "tradeType": "SELL"}
]
```

This approach ensures that your application always reflects the most up-to-date and active trading pairs on the platform.

## Considerations

*   **Dynamic Nature:** The list of supported pairs can change frequently based on market demand, regional availability, and Binance's operational decisions. Relying on the dynamic discovery endpoint is crucial for accuracy.
*   **Trade Type:** A pair might be supported for `BUY` but not `SELL`, or vice-versa. The `/api/v1/binance/pairs` endpoint will indicate the `tradeType` for which offers exist.

For detailed information on how to use the `/api/v1/binance/pairs` endpoint, refer to the `binance_pair_discovery.md` documentation.