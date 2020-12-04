""" day_04.py -- Advent of Code 2020 Day 4: Passport Processing

    Author: Chris Bowman
    Last Modified: 12/4/2020
    License: MIT
"""

KEYS = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']


def part_1(data, fields):
    return sum(1 for pw in data if all(key[:4] in pw for key in fields))


def main():
    d = open('../inputs/04').read().strip()
    d = d.split('\n\n')
    print(part_1(d, KEYS))


if __name__ == '__main__':
    main()
