""" day_10.py -- Advent of Code 2020 Day 10: Adapter Array

    Author: Chris Bowman
    Last Modified: 12/10/2020
    License: MIT
"""

from collections import Counter
from functools import lru_cache


def make_adapters(data):
    data.append(0)
    data.append(max(data) + 3)
    return sorted(data)


def part_1(adapters):
    jolts = 0
    diffs = []
    for item in adapters:
        if item - jolts in [1, 2, 3]:
            diffs.append(item - jolts)
            jolts = item
    a = Counter(diffs)
    return a[1] * a[3]


def part_2(adapters):
    @lru_cache(maxsize=128)
    def run(index):
        if index + 1 == len(adapters):
            return 1
        ans = 0
        for x in range(index + 1, len(adapters)):
            if adapters[x] - adapters[index] in [1, 2, 3]:
                ans += run(x)
        return ans

    return run(0)


def main():
    d = make_adapters([int(i) for i in open('../inputs/10').readlines()])
    print(f'Part 1:  {part_1(d)}')
    print(f'Part 2:  {part_2(d)}')


if __name__ == '__main__':
    main()