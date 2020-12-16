""" day_16.py -- Advent of Code 2020 Day 16: Ticket Translation

    Author: Chris Bowman
    Last Modified: 12/16/2020
    License: MIT
"""

import re


def in_rules(tic, rules):
    for rule in rules:
        for sub_rule in rule:
            if tic in sub_rule:
                return True
    return False


def solve(data):
    rules = re.findall(r': (\d.*) or (\d.*)', data)
    rules = [[range(int(i.split('-')[0]), int(i.split('-')[1]) + 1) for i in rule] for rule in rules]
    tickets = re.findall(r'^([\d,]+)', data, re.MULTILINE)
    p1 = 0
    for ticket in tickets[1:]:
        for num in ticket.split(','):
            if not in_rules(int(num), rules):
                p1 += int(num)
    return p1


def main():
    d = open('../inputs/16').read()
    print(solve(d))


if __name__ == '__main__':
    main()
