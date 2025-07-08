# 📄 PRD – Binance P2P API: Offers + Pairs + Históricos

## 🧠 Propósito  
Proveer una API robusta, escalable y documentada para acceder a datos P2P de Binance, incluyendo ofertas actuales, descubrimiento de pares disponibles, y futura persistencia de históricos.

---

## 📌 Requisitos Funcionales

| Código | Requisito |
|--------|-----------|
| RF-1 | Exponer endpoint `/api/v1/binance/offers` con filtros dinámicos por `fiat`, `asset`, `tradeType`, `page` y `rows`. |
| RF-2 | Exponer endpoint `/api/v1/binance/pairs` que devuelva combinaciones activas de fiat/crypto/tradeType. |
| RF-3 | Implementar capa opcional de caché en ambos endpoints para evitar sobrecarga hacia Binance (TTL configurable). |
| RF-4 | Preparar estructura para guardar histórico de ofertas en base de datos relacional (PostgreSQL recomendado). |
| RF-5 | Documentar endpoints en Markdown para facilitar adopción. |

---

## 🎛️ Endpoints y Parámetros

### 1. `/api/v1/binance/offers`  
**Método:** `GET`  
**Descripción:** Retorna ofertas activas con filtros.

| Parámetro | Tipo | Default | Descripción |
|----------|------|---------|-------------|
| `fiat` | string | `VES` | Moneda fiat |
| `asset` | string | `USDT` | Criptoactivo |
| `tradeType` | string | `BUY` | Tipo de operación |
| `page` | int | `1` | Número de página |
| `rows` | int | `20` | Cantidad de resultados por página |

**Ejemplo:**  
`/api/v1/binance/offers?fiat=USD&asset=BTC&tradeType=SELL&page=1&rows=50`

---

### 2. `/api/v1/binance/pairs`  
**Método:** `GET`  
**Descripción:** Devuelve combinaciones activas fiat/asset/tradeType con ofertas disponibles.

**Output ejemplo:**
```json
[
  {"fiat": "VES", "asset": "USDT", "tradeType": "BUY"},
  {"fiat": "USD", "asset": "BTC", "tradeType": "SELL"}
]
```

---

## 🔄 Caché

**Objetivo:** reducir llamadas repetidas al endpoint de Binance.

| Endpoint | TTL sugerido | Observación |
|----------|--------------|-------------|
| `/offers` | 30 segundos | Ideal para frontend en producción |
| `/pairs` | 2 minutos | Cambio lento de disponibilidad de pares |

Se puede implementar con `functools.lru_cache`, `diskcache` o Redis.

---

## 🗃️ Persistencia: Base de Datos para Históricos

**Recomendación:**  
Implementar **PostgreSQL** como base de datos relacional:

- Escalable, robusta y con soporte de queries complejas
- Permite guardar timestamp, fiat, asset, precio, métodos de pago, etc.
- Ideal para crear dashboards históricos, alertas y simuladores

**Modelo sugerido:**
Tabla `offers` con campos:
- `timestamp`, `fiat`, `asset`, `price`, `available`, `limits`, `payment_methods`, `trade_type`, `advertiser`

---

## 🧪 Casos de Uso

- Dashboard que consulta ofertas actuales por país.
- Simulador que detecta spread entre pares.
- Validación de existencia de par fiat/asset para frontend dinámico.
- Análisis de tendencias basado en datos históricos.

---

## 🔧 Tecnologías Clave

- **FastAPI** para endpoints
- **Requests** para scraping
- **Uvicorn** como servidor ASGI
- **PostgreSQL** + SQLAlchemy (sugerido)
- **Redis** (opcional) para caché en producción

---

## 🗂️ Documentación Markdown Incluida

- `/docs/api/binance_offers.md`
- `/docs/api/binance_pair_discovery.md`
- `/docs/api/root_endpoint.md`

---

## ✅ Conclusión

Este PRD cubre todos los aspectos clave para declarar **cerrado el backend del MVP de Binance** y habilitar integración visual, almacenamiento histórico y escalabilidad futura hacia otros exchanges como Bybit.