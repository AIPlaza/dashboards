from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    database_url: str = "sqlite:///./test.db"
    api_key: str = "test-api-key"
    testing: bool = False
    binance_p2p_search_url: str = "https://p2p.binance.com/bapi/c2c/v2/friendly/c2c/adv/search"
    binance_p2p_pairs_url: str = "https://p2p.binance.com/bapi/c2c/v2/public/c2c/asset-order/getAllSupportAsset"
    bybit_p2p_url: str = "https://www.bybit.com/fiat/trade/otc/buy/USDT/COP"

    class Config:
        env_file = ".env"
