# Day 1: Report Repair


d = open('../inputs/01').read()
GOAL = 2020


def parse(data):
    return list(map(int, data.splitlines()))


def part_1(data):
    for a in parse(data):
        for b in parse(data):
            if a != b and a + b == GOAL:
                return a * b


def part_2(data):
    for a in parse(data):
        for b in parse(data):
            for c in parse(data):
                if a != b and b != c and a + b + c == GOAL:
                    return a * b * c


print(part_1(d))
print(part_2(d))
