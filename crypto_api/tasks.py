from celery import shared_task
import requests
import redis
from .models import Organization,CryptoPrice
import logging
import time
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'organization.settings')

redis_conn = redis.Redis(host='localhost',port=6379,db=0)


logger = logging.getLogger(__name__)

@shared_task
def fetch_crypto_prices(crypto):
    cached_price = redis_conn.get(f"crypto_prices{crypto}")
    if cached_price:
        logger.info(f"Present in cache: {cached_price}")
        return float(cached_price)
    
    url = f'https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd'
    response = requests.get(url)
    if response.status_code == 429:
        logger.warning("Rate limit exceeded wait for retry...")
        time.sleep(100)
        response = requests.get(url)
    response = response.json()
    logger.info(f"API Response: {response}")
    if response.get('error'):
        logger.error(f"API error : {response.get('error')}")
        return 0
    price = response.get(crypto,{}).get('usd',0)
    logger.info(f"Price : {price}")
    redis_conn.setex(f"crypto_prices.{crypto}",3600,price)
    logger.info(f"Cached price for {crypto} : {price}")
    return price

@shared_task
def update_crypto_prices():
    print("Update Crypto Prices task started")
    cryptos = ['bitcoin','ethereum','ripple','tether','binancecoin','solana','usd-coin','dogecoin','cardano','tron']
    for crypto in cryptos:
        print(f"crypto available : {crypto}")
    for org in Organization.objects.all():
        for crypto in cryptos:
            price = fetch_crypto_prices(crypto)
            logger.info(f"Price : {price}")
            logger.info(f"crypto: {crypto}")
            if price is None or price <=0:
                logger.error(f"Not able to retrieve price for {crypto}")
                continue
            print(f"Saving {crypto} in db with {price}")
            try:
                crypto_price = CryptoPrice.objects.create(org_id=org,symbol=crypto.upper(),price=price)
                logger.info(f"Object of crypto price: {crypto_price}")
            except Exception as e:
                logger.error(f"Problem saving {crypto.upper()} in db : {str(e)}")
    return "Crypto Prices has been updated" 

@shared_task
def debug_task():
    print("Celery is working")