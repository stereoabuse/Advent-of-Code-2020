""" day_15.py -- Advent of Code 2020 Day 15: Rambunctious Recitation

    Author: Chris Bowman
    Last Modified: 12/15/2020
    License: MIT
"""

import utils


def part_1(data):
    spoken = data
    while len(spoken) < 2020:
        if spoken[-1] not in spoken[:-1]:
            spoken.append(0)
        else:
            spoken.append(list(reversed(spoken[:-1])).index(spoken[-1])+1)
    return spoken[-1]


def main():
    d = utils.integers(open('../inputs/15').read())
    print(part_1(d))


if __name__ == '__main__':
    main()