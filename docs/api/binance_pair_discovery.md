# Binance P2P Pair Discovery

## URL

`/api/v1/binance/pairs`

## Method

`GET`

## Description

Returns active combinations of fiat/asset/tradeType with available offers on Binance P2P.
This endpoint provides a quick way to see which currency pairs are currently active and can be queried for offers.

## Response

A JSON array of objects, where each object represents an active fiat/asset/tradeType combination.

```json
[
  {"fiat": "VES", "asset": "USDT", "tradeType": "BUY"},
  {"fiat": "USD", "asset": "BTC", "tradeType": "SELL"},
  {"fiat": "EUR", "asset": "ETH", "tradeType": "BUY"}
]
```

## Example Usage

```
http://127.0.0.1:8000/api/v1/binance/pairs
```

This endpoint is useful for dynamically populating dropdowns or lists of available trading pairs in a frontend application, ensuring that users only see options for which offers currently exist.

## Considerations

*   **Dynamic Nature:** The list of supported pairs can change frequently based on market demand, regional availability, and Binance's operational decisions. Relying on the dynamic discovery endpoint is crucial for accuracy.
*   **Trade Type:** A pair might be supported for `BUY` but not `SELL`, or vice-versa. This endpoint will indicate the `tradeType` for which offers exist.