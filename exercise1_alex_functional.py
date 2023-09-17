from abc import ABC, abstractmethod
from dataclasses import dataclass
from enum import StrEnum
from typing import Callable, Sequence


class SortingAlgorithm(StrEnum):
    bubble = "bubble"
    quick = "quick"


SortingFunction = Callable[[Sequence[int]], list[int]]


def bubble_sort(data: Sequence[int]) -> list[int]:
    data_copy = list(data)
    n = len(data)
    for i in range(n):
        for j in range(0, n - i - 1):
            if data_copy[j] > data_copy[j + 1]:
                data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
    return data_copy


def quick_sort(data: Sequence[int]) -> list[int]:
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
    return quick_sort(left) + [pivot] + quick_sort(right)


SORTING_ALGORITHMS: dict[SortingAlgorithm, SortingFunction] = {
    SortingAlgorithm.bubble: bubble_sort,
    SortingAlgorithm.quick: quick_sort,
}


def sort_sequence(data: Sequence[int], algo: SortingAlgorithm) -> list[int]:
    return SORTING_ALGORITHMS[algo](data)


def main() -> None:
    print(sort_sequence([5, 4, 2, 3, 1], algo=SortingAlgorithm.bubble))
    print(sort_sequence([5, 4, 3, 2, 1], algo=SortingAlgorithm.quick))


if __name__ == "__main__":
    main()
