""" day_09.py -- Advent of Code 2020 Day 9:

    Author: Chris Bowman
    Last Modified: 12/9/2020
    License: MIT
"""

from itertools import combinations
from utils import integers


def xmas(preamble, data):
    for index, _ in enumerate(data):
        if index > preamble:
            before = data[index - preamble:index]
            if not any(sum(i) == data[index] for i in combinations(before, 2)):
                return data[index]


def part_2(preamble, data):
    ans = xmas(preamble, data)
    target = data.index(xmas(preamble, data))
    for x, _ in enumerate(data[:target]):
        for y in range(x):
            if sum(data[y:x]) == ans:
                return min(data[y:x]) + max(data[y:x])


def main():
    d = integers(open('../inputs/09').read())
    print(xmas(25, d))
    print(part_2(25, d))


if __name__ == '__main__':
    main()
