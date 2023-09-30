import statistics
from dataclasses import dataclass

from exchange import Exchange
from trading_bot import TradingBot


class AvgTradingBot(TradingBot):
    def should_buy(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:]
        return prices[-1] < statistics.mean(list_window)

    def should_sell(self, symbol: str) -> bool:
        prices = self.exchange.get_prices(symbol)
        list_window = prices[-3:]
        return prices[-1] > statistics.mean(list_window)
