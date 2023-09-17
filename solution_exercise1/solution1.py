from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Sequence


class SortStrategy(ABC):
    @abstractmethod
    def sort(self, data: Sequence[int]) -> list[int]:
        pass


class BubbleSortStrategy(SortStrategy):
    def sort(self, data: Sequence[int]) -> list[int]:
        data_copy = list(data)
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data_copy[j] > data_copy[j + 1]:
                    data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
        return data_copy


class QuickSortStrategy(SortStrategy):
    def sort(self, data: Sequence[int]) -> list[int]:
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
        return self.sort(left) + [pivot] + self.sort(right)


@dataclass
class SortingContext:
    strategy: SortStrategy

    def sort_data(self, data: Sequence[int]):
        return self.strategy.sort(data)


def main() -> None:
    context = SortingContext(strategy=BubbleSortStrategy())
    print(context.sort_data([5, 4, 2, 3, 1]))
    context = SortingContext(strategy=QuickSortStrategy())
    print(context.sort_data([5, 4, 3, 2, 1]))


if __name__ == "__main__":
    main()
