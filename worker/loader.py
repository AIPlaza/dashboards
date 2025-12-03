"""
Handles the transformation and loading of extracted P2P data into the database.
"""
import logging
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from datetime import datetime
import uuid

from .db import db_manager
from .models import (
    DimCryptocurrencies,
    DimFiatCurrencies,
    DimPaymentMethods,
    DimAdvertisers,
    FactOffers,
    FactOfferPaymentMethods,
)

logger = logging.getLogger(__name__)

class DataLoader:
    """
    Transforms and loads P2P offer data into the PostgreSQL database.
    """

    def __init__(self):
        self.processed_offers = 0
        self._fiat_cache = {}
        self._crypto_cache = {}
        self._payment_method_cache = {}
        self._advertiser_cache = {}

    def load_offers(self, offers: List[Dict[str, Any]], batch_id: uuid.UUID) -> None:
        """
        Main method to process and load a batch of offers into the database.

        Args:
            offers: A list of raw offer dictionaries from the extractor.
            batch_id: The UUID for the current extraction batch.
        """
        if not offers:
            logger.info("No offers to load.")
            return

        logger.info(f"Starting to load {len(offers)} offers for batch {batch_id}...")

        with db_manager.get_session() as session:
            try:
                self._load_dimensions(session, offers)
                self._load_facts(session, offers, batch_id)
                self.processed_offers += len(offers)
                logger.info(f"Successfully loaded {len(offers)} offers for batch {batch_id}.")
            except Exception as e:
                logger.error(f"Error loading offers for batch {batch_id}: {e}", exc_info=True)
                raise

    def _get_or_create(self, session: Session, model, cache: dict, **kwargs) -> int:
        """Generic get-or-create function."""
        cache_key = tuple(kwargs.values())
        if cache_key in cache:
            return cache[cache_key]

        instance = session.query(model).filter_by(**kwargs).first()
        if instance:
            cache[cache_key] = instance.id
            return instance.id
        else:
            instance = model(**kwargs)
            session.add(instance)
            session.flush()  # Use flush to get the ID without committing
            cache[cache_key] = instance.id
            return instance.id

    def _get_or_create_crypto(self, session: Session, symbol: str) -> int:
        if symbol in self._crypto_cache:
            return self._crypto_cache[symbol]
        
        crypto = session.query(DimCryptocurrencies).filter_by(symbol=symbol).first()
        if crypto:
            self._crypto_cache[symbol] = crypto.crypto_id
            return crypto.crypto_id
        else:
            new_crypto = DimCryptocurrencies(
                symbol=symbol,
                name=symbol,  # Placeholder, consider a better way to get the full name
                binance_asset_code=symbol
            )
            session.add(new_crypto)
            session.flush()
            self._crypto_cache[symbol] = new_crypto.crypto_id
            return new_crypto.crypto_id

    def _get_or_create_fiat(self, session: Session, code: str) -> int:
        if code in self._fiat_cache:
            return self._fiat_cache[code]

        fiat = session.query(DimFiatCurrencies).filter_by(currency_code=code).first()
        if fiat:
            self._fiat_cache[code] = fiat.fiat_id
            return fiat.fiat_id
        else:
            new_fiat = DimFiatCurrencies(
                currency_code=code,
                currency_name=code, # Placeholder
            )
            session.add(new_fiat)
            session.flush()
            self._fiat_cache[code] = new_fiat.fiat_id
            return new_fiat.fiat_id

    def _get_or_create_payment_method(self, session: Session, method_code: str, method_name: str) -> int:
        if method_code in self._payment_method_cache:
            return self._payment_method_cache[method_code]

        pm = session.query(DimPaymentMethods).filter_by(method_code=method_code).first()
        if pm:
            self._payment_method_cache[method_code] = pm.payment_method_id
            return pm.payment_method_id
        else:
            new_pm = DimPaymentMethods(method_code=method_code, method_name=method_name)
            session.add(new_pm)
            session.flush()
            self._payment_method_cache[method_code] = new_pm.payment_method_id
            return new_pm.payment_method_id

    def _get_or_create_advertiser(self, session: Session, adv_id: str, nickname: str) -> int:
        # For simplicity, this is not a full SCD Type 2 implementation.
        # It finds the current record or creates a new one if the advertiser is new.
        if adv_id in self._advertiser_cache:
            return self._advertiser_cache[adv_id]

        advertiser = session.query(DimAdvertisers).filter_by(advertiser_id=adv_id, is_current=True).first()
        if advertiser:
            self._advertiser_cache[adv_id] = advertiser.advertiser_sk
            return advertiser.advertiser_sk
        else:
            new_adv = DimAdvertisers(
                advertiser_id=adv_id,
                nickname=nickname,
                is_merchant=False, # Placeholder
                registration_days=0, # Placeholder
                effective_date=datetime.utcnow(),
                is_current=True
            )
            session.add(new_adv)
            session.flush()
            self._advertiser_cache[adv_id] = new_adv.advertiser_sk
            return new_adv.advertiser_sk

    def _load_dimensions(self, session: Session, offers: List[Dict[str, Any]]):
        """Pre-load all dimensions to leverage caching."""
        for offer in offers:
            self._get_or_create_crypto(session, offer['asset'])
            self._get_or_create_fiat(session, offer['fiat'])
            self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])
            for pm in offer['payment_methods']:
                self._get_or_create_payment_method(session, pm['identifier'], pm['tradeMethodName'])

    def _load_facts(self, session: Session, offers: List[Dict[str, Any]], batch_id: uuid.UUID):
        extraction_ts = datetime.utcnow()
        for offer in offers:
            crypto_id = self._get_or_create_crypto(session, offer['asset'])
            fiat_id = self._get_or_create_fiat(session, offer['fiat'])
            advertiser_sk = self._get_or_create_advertiser(session, offer['advertiser']['id'], offer['advertiser']['nickname'])

            fact = FactOffers(
                offer_external_id=offer['id'],
                batch_id=batch_id,
                extraction_timestamp=extraction_ts,
                crypto_id=crypto_id,
                fiat_id=fiat_id,
                advertiser_sk=advertiser_sk,
                trade_type=offer['trade_type'],
                price=offer['price'],
                available_amount=offer['available_amount'],
                min_limit=offer['min_limit'],
                max_limit=offer['max_limit'],
                completion_rate=offer['advertiser']['completion_rate'],
                total_orders_count=offer['advertiser']['total_orders'],
                terms_conditions=offer.get('terms'),
                is_available=True,
            )
            session.add(fact)
            session.flush() # Flush to get the offer_id for the bridge table

            for pm in offer['payment_methods']:
                pm_id = self._get_or_create_payment_method(session, pm['identifier'], pm['tradeMethodName'])
                offer_pm = FactOfferPaymentMethods(
                    offer_id=fact.offer_id,
                    extraction_timestamp=extraction_ts,
                    payment_method_id=pm_id
                )
                session.add(offer_pm)

# Global loader instance
loader = DataLoader()