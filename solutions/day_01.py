""" day_01.py -- Advent of Code 2020 Day 1: Report Repair

    Author: Chris Bowman
    Last Modified: 12/2/2020
    License: MIT
"""

from utils import integers

GOAL = 2020


def part_1(data: list) -> int:
    for index_a, a in enumerate(data):
        for b in data[index_a:]:
            if a + b == GOAL:
                return a * b


def part_2(data: list) -> int:
    for index_a, a in enumerate(data):
        for index_b, b in enumerate(data[index_a:]):
            for c in data[index_b:]:
                if a + b + c == GOAL:
                    return a * b * c


def main():
    d = integers(open('../inputs/01').read())
    print(part_1(d))
    print(part_2(d))


if __name__ == '__main__':
    main()
