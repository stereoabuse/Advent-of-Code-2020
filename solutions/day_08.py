""" day_08.py -- Advent of Code 2020 Day 8: Handheld Halting

    Author: Chris Bowman
    Last Modified: 12/8/2020
    License: MIT
"""


def part_1(instructions):
    accumulator = 0
    index = 0
    seen = set()
    while True:
        if index in seen:
            return accumulator
        seen.add(index)
        op, val = instructions[index]
        if op == 'jmp':
            index += int(val)
            continue
        if op == 'acc':
            accumulator += int(val)
        if op == 'nop':
            pass
        index += 1


def game_console(instructions):
    accumulator = 0
    index = 0
    seen = set()
    while True:
        if index == len(instructions):
            return accumulator
        if index in seen:
            return None
        seen.add(index)
        op, val = instructions[index]
        if op == 'jmp':
            index += int(val)
            continue
        if op == 'acc':
            accumulator += int(val)
        if op == 'nop':
            pass
        index += 1


def part_2(d):
    for i in range(len(d)):
        d = [i.split() for i in open('../inputs/08').read().splitlines()]
        if 'nop' in d[i]:
            d[i][0] = 'jmp'
        elif 'jmp' in d[i]:
            d[i][0] = 'nop'
        if game_console(d):
            return game_console(d)


def main():
    d = [i.split() for i in open('../inputs/08').read().splitlines()]
    print(part_1(d))
    print(part_2(d))


if __name__ == '__main__':
    main()
