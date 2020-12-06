""" day_05.py -- Advent of Code 2020 Day 5: Binary Boarding

    Author: Chris Bowman
    Last Modified: 12/6/2020
    License: MIT
"""


def part_1(data):
    data = data.split('\n\n')
    return sum(len(set(''.join(i).replace('\n', ''))) for i in data)


def part_2(data):
    data = [(i.replace('\n', ''), i.count('\n') + 1) for i in data.split('\n\n')]
    return sum(sum(1 for let in set(item[0]) if item[0].count(let) == item[1]) for item in data)


def main():
    d = open('../inputs/06').read()
    print(part_1(d))
    print(part_2(d))


if __name__ == '__main__':
    main()
