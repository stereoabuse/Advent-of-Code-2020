""" day_08.py -- Advent of Code 2020 Day 8: Handheld Halting

    Author: Chris Bowman
    Last Modified: 12/8/2020
    License: MIT
"""


def part_1():
    def console(instructions):
        accumulator = 0
        seen = set()
        index = 0
        while True:
            if index in seen:
                return accumulator
            if index == len(instructions):
                return accumulator
            seen.add(index)
            operation, val = instructions[index]
            if operation == 'nop':
                index += 1
            elif operation == 'acc':
                accumulator += int(val)
                index += 1
            elif operation == 'jmp':
                index += int(val)
            if index >= len(instructions) + 1:
                return accumulator

    d = [i.split() for i in open('../inputs/08').read().splitlines()]
    return console(d)


# Duplicated codes need to be refactored to one single console program.
def part_2():
    def console(instructions):
        accumulator = 0
        seen = set()
        index = 0
        while True:
            if index in seen:
                return None
            if index == len(instructions):
                return accumulator
            seen.add(index)
            operation, val = instructions[index]
            if operation == 'nop':
                index += 1
            elif operation == 'acc':
                accumulator += int(val)
                index += 1
            elif operation == 'jmp':
                index += int(val)
            if index >= len(instructions) + 1:
                return accumulator

    d = open('../inputs/08').read().splitlines()

    for i in range(len(d)):
        d = [i.split() for i in open('../inputs/08').read().splitlines()]

        if d[i][0] == 'nop':
            d[i][0] = 'jmp'
        elif d[i][0] == 'jmp':
            d[i][0] = 'nop'
        if console(d):
            return console(d)


def main():
    print(part_2())
    print(part_1())


if __name__ == '__main__':
    main()
