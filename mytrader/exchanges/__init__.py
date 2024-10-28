from abc import ABC, abstractmethod

class Exchange(ABC):
    def __init__(self, name, value):
        self.name = name
        pass
    
    @abstractmethod
    def get_account_asset_value(self, currency: str) -> float:
        pass
    
    @abstractmethod
    def get_ohlcv(self, timeframe, unit, params):
        pass
    
    @abstractmethod
    def submit_order(self, params):
        pass
    