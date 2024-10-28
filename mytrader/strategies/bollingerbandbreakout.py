import talib as ta

from mytrader.strategies import Signal, Strategy

class BollingerbandBreakout(Strategy):
    def on_trading_iteration(self, candles, target_asset_value, volume_threshold, **kwargs):
        self.candles = candles
        self.asset_value = target_asset_value
        self.volume_threshold = volume_threshold
        
        self.price = self.candles['close'].iat[0]
        self.volume = self.candles['volume'].iat[0]
        reversed_close = self.candles['close'][::-1] # set index -1 is lastest candle
        
        bb_upper, bb_middle, bb_lower = map(lambda channel: channel.iat[-1], ta.BBANDS(reversed_close, timeperiod=20, nbdevup=2))
        sma_50 = ta.SMA(reversed_close, timeperiod=50).iat[-1]
        sma_100 = ta.SMA(reversed_close, timeperiod=100).iat[-1]
        sma_200 = ta.SMA(reversed_close, timeperiod=200).iat[-1]
        
        if self.price > bb_upper and self.asset_value == 0.0:
            print('bb_breakout long signal')
            if self.price > sma_50 > sma_100 > sma_200 and self.volume > self.volume_threshold: # filtering
                return Signal.LONG_ENTRY_SIGNAL
        
        if self.price <= bb_middle and self.asset_value > 0.0:
            print('close long')
            return Signal.LONG_EXIT_SIGNAL
