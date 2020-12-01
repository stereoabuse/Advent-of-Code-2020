import re


def integers(s: str) -> tuple:
    """Takes a string and return just digits split into tuple"""
    return tuple(int(i) for i in re.split(r'\D+', s) if i)


def mapl(s: str) -> list:
    """Takes a string and return just digits split into list"""
    return [int(i) for i in re.split(r'\D+', s) if i]


def taxi_distance(x,y=(0,0)):
    """Return integer of Manhattan distance of 2 points"""
    return abs(x[0] - x[1]) + abs(y[0] - y[1])


print(integers('sdgfsdh2332n2234n5655n'))