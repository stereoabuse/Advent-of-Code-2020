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


def part_2(rules, color):
    bags = {}
    for line in rules:
        colors = re.findall(r'(\w* \w*) bag', line)
        primary = colors[0]
        secondary = list(zip(colors[1:], utils.integers(line)))
        bags[primary] = dict(secondary)

    def stack(bag):
        total = 1
        if bags[bag]:
            for inside in bags[bag]:
                total += bags[bag][inside] * stack(inside)
            return total
        return total

    return stack(color) - 1


def main():
    d = open('../inputs/07').read().splitlines()
    print(part_1(d, 'shiny gold'))
    print(part_2(d, 'shiny gold'))


if __name__ == '__main__':
    main()
