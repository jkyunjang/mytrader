from enum import Enum
from abc import ABC, abstractmethod

class Signal(Enum):
    LONG_ENTRY_SIGNAL = 1
    LONG_EXIT_SIGNAL = 2
    SHORT_ENTRY_SIGNAL = 3
    SHORT_EXIT_SIGNAL = 4

class Strategy(ABC):
    @abstractmethod
    def on_trading_iteration(self, candles, asset_value, volume_threshold, **kwargs):
        pass