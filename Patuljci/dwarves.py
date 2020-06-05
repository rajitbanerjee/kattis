"""https://open.kattis.com/problems/patuljci"""

import itertools


def display(arr: tuple) -> None:
    for each in arr:
        print(each)


def main() -> None:
    nums = []
    for _ in range(9):
        nums.append(int(input()))

    for each in itertools.combinations(nums, 7):
        if sum(each) == 100:
            display(each)
            break


main()
