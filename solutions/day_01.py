# Day 1: Report Repair

from utils import integers

GOAL = 2020

d = open('../inputs/01').read()
d = list(integers(d))


def part_1(data):
    for a in data:
        for b in data:
            if a != b and a + b == GOAL:
                return a * b


def part_2(data):
    for a in data:
        for b in data:
            for c in data:
                if a != b and b != c and a + b + c == GOAL:
                    return a * b * c


print(part_1(d))
print(part_2(d))
