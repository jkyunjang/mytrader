import sys
import asyncio
from datetime import datetime

from mytrader.exchanges.upbit import Upbit
from mytrader.strategies import Signal
from mytrader.strategies.bollingerbandbreakout import BollingerbandBreakout

# config.json으로부터 받은 설정 파일을 파싱하여 저장해야 함
# 어떤 거래소에서 어떤 전략을 수행해야 하는지 
class Trader:
    def __init__(self, config):
        # self.mappings = []
                        # for exchange, property in config:
        #     if property['activate'] == True:
        #         match exchange:
        #             case 'Upbit':
        #                 self.mappings.append((Upbit(), ))
        #             # case 'KoreaInvestment':
        #             #     self.mappings.append((KoreaInvestment(), property['strategies']))
        #             case _:
        #                 raise Exception
        pass

    def start_trading(self):
        print('start trading')
        upbit = Upbit()
        bb_breakout = BollingerbandBreakout()

        while True:
            now = datetime.now().strftime('%Y-%m-%d, %H:%M:%S')
            account_btc_value = self.exchange.get_account_asset_value('BTC')
            entry_qty = str(int(self.exchange.get_account_asset_value('KRW') * 0.1))
            candles = self.exchange.get_ohlcv('minutes', '240', {
                "market": 'KRW-BTC',
                "count": 200
            })
            bb_breakout_signal = bb_breakout.on_trading_iteration(candles, account_btc_value)
            if bb_breakout_signal == Signal.LONG_ENTRY_SIGNAL:
                print(f'entry long: {self.price}({now})')
                res = self.exchange.submit_order({
                    'market': 'KRW-BTC',
                    'side': 'bid',
                    'price': entry_qty,
                    'ord_type': 'price',
                })
            if bb_breakout_signal == Signal.LONG_EXIT_SIGNAL:
                print('exit signal')
                res = self.exchange.submit_order({
                    'market': 'KRW-BTC',
                    'side': 'ask',
                    'volume': str(account_btc_value),
                    'ord_type': 'market',
                })
                
            

        
