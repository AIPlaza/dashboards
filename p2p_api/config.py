from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    api_key: str = "test-api-key"
    testing: bool = False
    binance_p2p_search_url: str = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    binance_p2p_pairs_url: str = "https://p2p.binance.com/bapi/c2c/v2/public/c2c/asset-order/getAllSupportAsset"
    bybit_p2p_url: str = "https://www.bybit.com/fiat/trade/otc/buy/USDT/COP"
    secret_key: str = "c8b9a2f1d5e6f7a8b9c0d1e2f3a4b5c6d7e8f9a0b1c2d3e4f5a6b7c8d9e0f1a2"
    algorithm: str = "HS256"
    access_token_expire_minutes: int = 30

    class Config:
        env_file = ".env"
