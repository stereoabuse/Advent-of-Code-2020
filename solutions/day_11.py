""" day_11.py -- Advent of Code 2020 Day 11: Seating System

    Author: Chris Bowman
    Last Modified: 12/11/2020
    License: MIT

    Make a cellular automata!
"""

EMP = 'L'
OCC = '#'
FLR = '.'


def adjacent(row, column, grid):
    nearest = []
    for x in range(row - 1, row + 2):
        for y in range(column - 1, column + 2):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) != (row, column):
                nearest.append(grid[x][y])
    return nearest


def visible_seats(row, column, grid):
    visible  = []
    for x in range(row - 1, row + 2):
        for y in range(column - 1, column + 2):
            if 0 <= x < len(grid) and 0 <= y < len(grid[0]) and (x, y) != (row, column):
                visible.append(grid[x][y])
    return visible


def part_1(seats):
    grid = seats
    count = 0
    while True:
        new = []
        count += 1
        for r in range(len(grid)):
            new_line = []
            for c in range(len(grid[r])):
                seat = grid[r][c]
                near = adjacent(r, c, grid)
                if seat == EMP and near.count(OCC) == 0:
                    new_line.append(OCC)
                elif seat == OCC and near.count(OCC) >= 4:
                    new_line.append(EMP)
                else:
                    new_line.append(seat)
            new.append(new_line)
        if grid == new:
            return sum(i.count(OCC) for i in new)
        grid = new


TEST = '''L.LL.LL.LL
LLLLLLL.LL
L.L.L..L..
LLLL.LL.LL
L.LL.LL.LL
L.LLLLL.LL
..L.L.....
LLLLLLLLLL
L.LLLLLL.L
L.LLLLL.LL'''.splitlines()


def main():
    seats = open('../inputs/11').read().splitlines()
    seats = TEST
    print(part_1(seats))


if __name__ == '__main__':
    main()
