import jwt
import hashlib
import os
import requests
import uuid
from urllib.parse import urlencode, unquote

class Upbit():
    def __init__(self):
        self.__access_key = os.getenv('UPBIT_ACCESS_KEY')
        self.__secret_key = os.getenv('UPBIT_SECRET_KEY')
        self.__url = 'https://api.upbit.com'
        self.__no_query_auth_token = self._make_auth_token()
    
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
            hash.update(urlencode(query).encode())
            query_hash = hash.hexdigest()
            
            payload = {
                "access_key": self.__access_key,
                "nonce": str(uuid.uuid4),
                "query_hash": query_hash,
                "query_hash_alg": 'SHA512'
                
            }

        jwt_token = jwt.encode(payload, self.__secret_key)
        auth_token = 'Bearer {}'.format(jwt_token)
        
        return auth_token

    def get_account_value(self):
        headers = {
            'Authorization': self.__no_query_auth_token
        }
        
        return requests(self.__url + '/v1/accounts', headers=headers)