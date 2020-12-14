""" day_12.py -- Advent of Code 2020 Day 12: Rain Risk

    Author: Chris Bowman
    Last Modified: 12/12/2020
    License: MIT
"""


def navigate(instructions):
    x, y = (0, 0)
    heading = 0
    for instr in instructions:
        action, value = instr[0], int(instr[1:])
        if action == 'N':
            y += value
        elif action == 'S':
            y -= value
        elif action == 'E':
            x += value
        elif action == 'W':
            x -= value
        elif action == 'R':
            heading -= value
        elif action == 'L':
            heading += value
        elif action == 'F':
            heading = heading % 360
            if heading == 0:
                x += value
            elif heading == 90:
                y += value
            elif heading == 180:
                x -= value
            elif heading == 270:
                y -= value
    return abs(x) + abs(y)


def main():
    d = open('../inputs/12').read().splitlines()
    print(d)
    print(navigate(d))


if __name__ == '__main__':
    main()