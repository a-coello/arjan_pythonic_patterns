from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum
from typing import Sequence


class SortingStrategy(ABC):
    @abstractmethod
    def sort(self, data: Sequence[int]) -> list[int]:
        """Sorts the given data."""


class BubbleSort(SortingStrategy):
    def sort(self, data: Sequence[int]) -> list[int]:
        data_copy = list(data)
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data_copy[j] > data_copy[j + 1]:
                    data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
        return data_copy


class QuickSort(SortingStrategy):
    def sort(self, data: Sequence[int]) -> list[int]:
        def quicksort(data: Sequence[int]) -> list[int]:
            if len(data) <= 1:
                return list(data)
            pivot = data[0]
            left: list[int] = []
            right: list[int] = []
            for item in data[1:]:
                if item < pivot:
                    left.append(item)
                else:
                    right.append(item)
            return quicksort(left) + [pivot] + quicksort(right)

        return quicksort(data)


@dataclass
class Order:
    sorting_strategy: SortingStrategy

    def sort_sequence(self, data: Sequence[int]) -> list[int]:
        return self.sorting_strategy.sort(data)


def main() -> None:
    order = Order(sorting_strategy=BubbleSort())
    order2 = Order(sorting_strategy=QuickSort())
    print(order.sort_sequence([5, 4, 3, 2, 1]))
    print(order2.sort_sequence([5, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
