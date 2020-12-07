""" day_07.py -- Advent of Code 2020 Day 7:

    Author: Chris Bowman
    Last Modified: 12/7/2020
    License: MIT
"""

import re
import utils


def part_1(rules: list, start_bag: str) -> int:
    bags = [start_bag]
    counter = 0
    while counter < len(bags):
        for line in rules:
            if bags[counter] in line:
                new_bag = ' '.join(line.split()[0:2])
                if new_bag not in bags:
                    bags.append(new_bag)
        counter += 1
    return len(bags) - 1


def part_2(*args):  # in progress
    class Bag:
        def __init__(self, rule):
            self.main = re.findall(r'(\w* \w*) bag', rule)[0]
            self.bag_count = utils.integers(rule)
            if self.bag_count[0] == 0:
                self.inside_cols = '0'
            else:
                self.inside_cols = re.findall(r'(\w* \w*) bag', rule)[1:]

        def parsed(self):
            return dict(zip(self.inside_cols, self.bag_count))

    dd = {}
    for rule in args:
        bag = Bag(rule)
        dd[bag.main] = bag.parsed()

    return 'In progress...'


def main():
    d = open('../inputs/07').read().splitlines()
    print(part_1(d, 'shiny gold'))
    print(part_2())  # in progress


if __name__ == '__main__':
    main()
