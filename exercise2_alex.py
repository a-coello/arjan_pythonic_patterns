# Strategy pattern example for a payment system

from abc import ABC
from dataclasses import dataclass, field


@dataclass
class Item:
    name: str
    price: int


class ShippingStrategy(ABC):
    def calculate_shipping_cost(self, items: list[Item]) -> int:
        ...


class StandardShippingStrategy(ShippingStrategy):
    def calculate_shipping_cost(self, items: list[Item]) -> int:
        total = sum(item.price for item in items)
        return 5 if total < 50 else 0


class ExpressShippingStrategy(ShippingStrategy):
    def calculate_shipping_cost(self, items: list[Item]) -> int:
        total = sum(item.price for item in items)
        return 10 if total < 50 else 5


class OvernightShippingStrategy(ShippingStrategy):
    def calculate_shipping_cost(self, items: list[Item]) -> int:
        return 50


@dataclass
class ShoppingCart:
    items: list[Item] = field(default_factory=list)

    def calculate_total_cost(self, shipping_strategy: ShippingStrategy) -> int:
        items_cost = sum(item.price for item in self.items)
        shipping_cost = shipping_strategy.calculate_shipping_cost(self.items)
        return items_cost + shipping_cost

    def add_item(self, item: Item) -> None:
        self.items.append(item)


def print_amount(amount: int) -> None:
    print(f"${amount:.2f}")


def main() -> None:
    shopping_cart = ShoppingCart()
    shopping_cart.add_item(Item(name="laptop", price=150))
    shopping_cart.add_item(Item(name="mouse", price=3))
    shopping_cart.add_item(Item(name="keyboard", price=4))
    print_amount(shopping_cart.calculate_total_cost(StandardShippingStrategy()))
    print_amount(shopping_cart.calculate_total_cost(ExpressShippingStrategy()))
    print_amount(shopping_cart.calculate_total_cost(OvernightShippingStrategy()))


if __name__ == "__main__":
    main()
