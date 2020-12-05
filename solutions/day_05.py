""" day_05.py -- Advent of Code 2020 Day 5: Binary Boarding

    Author: Chris Bowman
    Last Modified: 12/5/2020
    License: MIT
"""


def binarize(seats):
    def row(seat):
        return int(seat[:7].replace('F', '0').replace('B', '1'), 2)

    def column(seat):
        return int(seat[7:].replace('L', '0').replace('R', '1'), 2)

    return [row(seat) * 8 + column(seat) for seat in seats]


def part_1(seats):
    return max(binarize(seats))


def part_2(seats):
    ids = binarize(seats)
    for i in range(min(ids), max(ids)):
        if i not in ids:
            return i


def main():
    d = open('../inputs/05').read().splitlines()
    print(part_1(d))
    print(part_2(d))


if __name__ == '__main__':
    main()
