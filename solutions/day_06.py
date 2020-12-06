""" day_06.py -- Advent of Code 2020 Day 5: Binary Boarding

    Author: Chris Bowman
    Last Modified: 12/6/2020
    License: MIT
"""


def part_1(data: list) -> int:
    """Takes list of tuples and returns the total sum of unique values in each item"""
    return sum(len(set(i[0])) for i in data)


def part_2(data: list) -> int:
    """Takes list of tuples and returns the sum of sum of letters who appear in each line of a data sub-item"""
    return sum(sum(1 for let in set(item[0]) if item[0].count(let) == item[1]) for item in data)


def main():
    d = open('../inputs/06').read().split('\n\n')
    d = [(i.replace('\n', ''), i.count('\n') + 1) for i in d]
    print(part_1(d))
    print(part_2(d))


if __name__ == '__main__':
    main()
