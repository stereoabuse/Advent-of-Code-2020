""" day_13.py -- Advent of Code 2020 Day 13: Shuttle Search

    Author: Chris Bowman
    Last Modified: 12/13/2020
    License: MIT
"""

import itertools
import utils


def part_1(timestamp, buses):
    for time in itertools.count(timestamp):
        for bus in buses:
            if time % bus == 0:
                return (time - timestamp) * bus


def main():
    d = open('../inputs/13').read().splitlines()
    timestamp = int(d[0])
    buses = utils.integers(d[1])

    print(part_1(timestamp, buses))


if __name__ == '__main__':
    main()