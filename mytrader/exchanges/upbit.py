import jwt
import hashlib
import os
import requests as rq
import uuid
import pandas as pd
from urllib.parse import urlencode, unquote

class Upbit():
    def __init__(self):
        self.__access_key = os.getenv('UPBIT_ACCESS_KEY')
        self.__secret_key = os.getenv('UPBIT_SECRET_KEY')
        self.__url = 'https://api.upbit.com'
    
    def _make_auth_token(self, query=None) -> str:
        if query is None:
            payload = {
                "access_key": self.__access_key,
                "nonce": str(uuid.uuid4())
            }
        else:
            if not isinstance(query, dict):
                raise TypeError()
            
            hash = hashlib.sha512()
            hash.update(unquote(urlencode(query, doseq=True)).encode('utf-8'))
            query_hash = hash.hexdigest()
            payload = {
                "access_key": self.__access_key,
                "nonce": str(uuid.uuid4()),
                "query_hash": query_hash,
                "query_hash_alg": 'SHA512'
            }

        jwt_token = jwt.encode(payload, self.__secret_key)
        auth_token = 'Bearer {}'.format(jwt_token)
        
        return auth_token

    def get_account_asset_value(self, currency: str) -> float:
        headers = {
            'Authorization': self._make_auth_token()
        }
        
        res = rq.get(self.__url + '/v1/accounts', headers=headers)
        if res.status_code != 200:
            print(f'{res.status_code} {res.reason}')
        assets = res.json() # list of account assets
        value = 0.0
        for asset in assets:
            if asset['currency'] == currency:
                value = float(asset['balance'])
        return value
    
    def get_ohlcv(self, timeframe, unit, params):
        headers = {
            "accept": "application/json"
        }
        url = self.__url + f'/v1/candles/{timeframe}/{unit}'
        res = rq.get(url, params=params, headers=headers)
        if res.status_code != 200:
            print(f'{res.status_code} {res.reason}')
        data = res.json()
        df = pd.DataFrame(data, columns=['candle_date_time_kst', 'opening_price', 'high_price', 'low_price', 'trade_price', 'candle_acc_trade_volume'])
        df.rename(columns={'candle_date_time_kst': 'timestamp', 
                           'opening_price': 'open',
                           'high_price': 'high',
                           'low_price': 'low',
                           'trade_price': 'close',
                           'candle_acc_trade_volume': 'volume'}, 
                          inplace=True)
        df.set_index('timestamp', inplace=True)
        return df
    
    def submit_order(self, params):
        url = self.__url + '/v1/orders'
        headers={
            'Authorization': self._make_auth_token(params)
        }
        res = rq.post(url, json=params, headers=headers)
        if res.status_code != 201:
            print(f'{res.status_code} {res.reason}')
        return res.json()