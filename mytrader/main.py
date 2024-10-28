#!/usr/bin/env python3

import json
from dotenv import load_dotenv
from collections import namedtuple

from mytrader.trader import Trader
from mytrader.exchanges.upbit import Upbit
from mytrader.strategies import Strategy
from mytrader.strategies.bollingerbandbreakout import BollingerbandBreakout
'''
Todo:
    - 거래소, 전략 지정 방식 및 전략 스크립트 실행 방식
    - trader, strategy 분리
    - logger 및 discord 연동
    - 한투 api 추가
'''
def main():
    dotenv = load_dotenv()
    if dotenv != True:
        raise FileNotFoundError('Cannot found or empty .env')
    
    try:
        with open('config.json') as f:
            config = json.load(f)
    except Exception as e:
        print(f'{e}')
    
    trader = Trader(config)
    trader.start_trading()
        
if __name__ == '__main__':
    main()

        