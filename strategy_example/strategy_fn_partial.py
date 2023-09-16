from dataclasses import dataclass
from functools import partial
from typing import Callable

DiscountFunction = Callable[[int], int]


def percentage_discount(price: int, percentage: float) -> int:
    return int(price * percentage)


def fixed_discount(_: int, fixed: int) -> int:
    return fixed


@dataclass
class Order:
    price: int
    quantity: int
    discount: DiscountFunction

    def compute_total(self) -> int:
        discount = self.discount(self.price * self.quantity)
        return self.price * self.quantity - discount


def main() -> None:
    perc_discount = partial(percentage_discount, percentage=0.12)
    order = Order(price=100_00, quantity=2, discount=perc_discount)
    print(order)
    print(f"Total: ${order.compute_total()/100:.2f}")


if __name__ == "__main__":
    main()
