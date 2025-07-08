# Binance P2P Offers

## URL

`/api/v1/binance/offers`

## Method

`GET`

## Description

Fetches P2P offers from Binance based on specified criteria.

## Query Parameters

| Parameter | Type | Optional | Default | Description |
|---|---|---|---|---|
| `fiat` | string | Yes | `VES` | The fiat currency (e.g., `VES`, `USD`, `EUR`). |
| `asset` | string | Yes | `USDT` | The crypto asset (e.g., `USDT`, `BTC`, `ETH`). |
| `tradeType` | string | Yes | `BUY` | The trade type (`BUY` or `SELL`). |
| `page` | integer | Yes | `1` | The page number for results. |
| `rows` | integer | Yes | `20` | The number of results per page. |

## Example Usage

```
http://127.0.0.1:8000/api/v1/binance/offers?fiat=USD&asset=BTC&tradeType=SELL&page=1&rows=50
```

## Response

A JSON array of P2P offers, each containing details like `advertiser`, `price`, `available`, `limits`, and `payment_methods`.

```json
[
  {
    "advertiser": "CriptoDealerVzla",
    "price": "40.00 VES",
    "available": "1000 USDT",
    "limits": "10 - 500 VES",
    "payment_methods": ["BankTransfer", "Zelle"]
  }
]
```