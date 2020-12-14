""" day_14.py -- Advent of Code 2020 Day 14:

    Author: Chris Bowman
    Last Modified: 12/14/2020
    License: MIT
"""

import utils


def part_1(data):
    mem_addr = {}
    for line in data.splitlines():
        if line.startswith('mask'):
            mask = line[7:]
        else:
            mem, num = utils.integers(line)
            num = bin(num)[2:].zfill(36)
            total = ''
            for index, char in enumerate(mask):
                if char.isdigit():
                    total += char
                else:
                    total += num[index]
            mem_addr[mem] = int(total, 2)
    return sum(mem_addr.values())


def part_2():
    pass


def main():
    d = open('../inputs/14').read()

    print(part_1(d))
    print(part_2())


if __name__ == '__main__':
    main()
