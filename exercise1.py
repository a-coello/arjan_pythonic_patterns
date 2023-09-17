from enum import StrEnum
from typing import Sequence


class SortingAlgorithm(StrEnum):
    bubble = "bubble"
    quick = "quick"


def sort_data(data: Sequence[int], algo: SortingAlgorithm) -> list[int]:
    if algo == "bubble":
        data_copy = list(data)
        n = len(data)
        for i in range(n):
            for j in range(0, n - i - 1):
                if data_copy[j] > data_copy[j + 1]:
                    data_copy[j], data_copy[j + 1] = data_copy[j + 1], data_copy[j]
        return data_copy
    elif algo == "quick":

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
    else:
        raise ValueError("Unknown sorting algorithm")


def main() -> None:
    print(sort_data([5, 4, 2, 3, 1], algo=SortingAlgorithm.bubble))
    print(sort_data([5, 4, 3, 2, 1], algo=SortingAlgorithm.quick))


if __name__ == "__main__":
    main()
