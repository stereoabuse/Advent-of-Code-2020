""" day_04.py -- Advent of Code 2020 Day 4: Passport Processing

    Author: Chris Bowman
    Last Modified: 12/4/2020
    License: MIT
"""

import re


def part_1(data: list, regexps: list) -> int:
    return sum(1 for pp in data if all(re.search(reg[1:4], pp) for reg in regexps))


def part_2(data: list, regexps: list) -> int:
    return sum(1 for pp in data if all(re.search(reg, pp) for reg in regexps))


def main():
    d = open('../inputs/04').read().split('\n\n')
    regexps = [r'(byr:(19[2-8][0-9]|199[0-9]|200[0-2]))',
               r'(iyr:(201[0-9]|2020))',
               r'(eyr:(202[0-9]|2030))',
               r'(hgt:(1[5-8][0-9]|19[0-3])cm|(59|6[0-9]|7[0-6])in)',
               r'(hcl:#([0-9]|[a-f]){6})',
               r'(ecl:(amb|blu|brn|gry|grn|hzl|oth))',
               r'(pid:\d{9}(?!\S))']

    print(part_1(d, regexps))
    print(part_2(d, regexps))


if __name__ == '__main__':
    main()
