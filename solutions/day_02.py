""" day_02.py -- Advent of Code 2020 Day 2: pw Philosophy

    Author: Chris Bowman
    Last Modified: 12/2/2020
    License: MIT
"""

from utils import alphanums


def part_1(data):
    total = 0
    for lo, hi, let, pw in data:
        if int(lo) <= pw.count(let) <= int(hi):
            total += 1
    return total


def part_2(data):
    total = 0
    for lo, hi, let, pw in data:
        if (pw[int(lo)-1] == let) is not (pw[int(hi) -1] == let):
            total += 1
    return total


def main():
    d = [alphanums(i) for i in open('../inputs/02').readlines()]
    print(part_1(d))
    print(part_2(d))


if __name__ == '__main__':
    main()
