""" day_03.py -- Advent of Code 2020 Day 3: Toboggan Trajectory

    Author: Chris Bowman
    Last Modified: 12/3/2020
    License: MIT
"""

import math


def part_1(data: list, slope: tuple) -> int:
    trees = 0
    right, down = (0, 0)
    while down < len(data):
        if data[down][right % len(data[0])] == '#':
            trees += 1
        right += slope[0]
        down += slope[1]
    return trees


def part_2(data: list, slopes: tuple) -> int:
    return math.prod(part_1(data, slope) for slope in slopes)


def main():
    d = open('../inputs/03').read().splitlines()
    slopes = [(1, 1), (3, 1), (5, 1), (7, 1), (1, 2)]
    print(part_1(d, slopes[1]))
    print(part_2(d, slopes))


if __name__ == '__main__':
    main()
