from abc import ABC, abstractmethod
from typing import Protocol


class TradingEngine(Protocol):
    def buy(self, amount: int) -> None:
        """Buy the given amount."""

    def sell(self, amount: int) -> None:
        """Sell the given amount."""

    def should_buy(self, prices: list[int]) -> bool:
        """Should the bot buy?"""

    def should_sell(self, prices: list[int]) -> bool:
        """Should the bot sell?"""

    def get_price_data(self) -> list[int]:
        """Get the price data."""

    def get_amount(self) -> int:
        """Get the amount to trade."""


def trade(engine: TradingEngine) -> None:
    prices = engine.get_price_data()
    amount = engine.get_amount()

    if engine.should_buy(prices):
        engine.buy(amount)
    if engine.should_sell(prices):
        engine.sell(amount)
