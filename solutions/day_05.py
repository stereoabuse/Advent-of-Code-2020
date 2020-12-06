""" day_05.py -- Advent of Code 2020 Day 5: Binary Boarding

    Author: Chris Bowman
    Last Modified: 12/5/2020
    License: MIT
"""


def binary_space_parse(seats: list) -> list:
    def row(seat):
        return int(seat[:7].replace('F', '0').replace('B', '1'), 2)

    def column(seat):
        return int(seat[7:].replace('L', '0').replace('R', '1'), 2)

    return [row(seat) * 8 + column(seat) for seat in seats]


def part_1(ids: list) -> int:
    return max(ids)


def part_2(ids: list) -> int:
    for i in range(min(ids), max(ids)):
        if i not in ids:
            return i


def main():
    d = open('../inputs/05').read().splitlines()
    ids = binary_space_parse(d)
    print(part_1(ids))
    print(part_2(ids))


if __name__ == '__main__':
    main()
