import sys
import itertools
import re
import math

filename = "input"


def read_input():
    with open(filename) as f:
        return f.read()


def parse_lines():
    return read_input().splitlines()


def parse_lines_int():
    return [int(line) for line in parse_lines()]


def parse_lines_float():
    return [float(line) for line in parse_lines()]


def parse_chars():
    return read_input().rstrip()


def parse_words():
    return read_input().rstrip().split()


def parse_digits():
    return [int(c) for c in parse_chars()]


def parse_space_ints():
    return [int(c) for c in parse_chars().split()]


def parse_space_floats():
    return [float(c) for c in parse_chars().split()]


def parse_bit_array():
    return [[int(c) for c in line] for line in parse_lines()]


import numpy as np
from collections import defaultdict

neighbors = [
    (-1, -1),
    (-1, 0),
    (-1, 1),
    (0, -1),
    (0, 1),
    (1, -1),
    (1, 0),
    (1, 1),
]


def main():
    global filename
    filename = "example"
    lines = parse_lines()

    with open("input") as f:
        dots, instrs = f.read().split("\n\n")

    d = defaultdict(int)
    maxx = 0
    maxy = 0
    for dot in dots.splitlines():
        x, y = tuple(map(int, dot.split(",")))
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        d[(x, y)] = 1

    for fold in instrs.splitlines():
        print(f"fold={fold}")
        ax, along = fold.split(" ")[2].split("=")
        along = int(along)
        print(d.items())
        newd = d.copy()
        for (x, y), val in d.items():
            if val == 0:
                continue
            if ax == "x":
                if x <= along:
                    continue
                mirrored = (along - (x - along), y)
                newd[mirrored] = 1
                newd[(x, y)] = 0
            elif ax == "y":
                if y <= along:
                    continue
                mirrored = (x, along - (y - along))
                newd[mirrored] = 1
                newd[(x, y)] = 0
        d = newd
        break

    print(sum(d.values()))


def main2():
    global filename
    filename = "example"
    lines = parse_lines()

    with open("input") as f:
        dots, instrs = f.read().split("\n\n")

    d = defaultdict(int)
    maxx = 0
    maxy = 0
    for dot in dots.splitlines():
        x, y = tuple(map(int, dot.split(",")))
        maxx = max(x, maxx)
        maxy = max(y, maxy)
        d[(x, y)] = 1

    for fold in instrs.splitlines():
        print(f"fold={fold}")
        ax, along = fold.split(" ")[2].split("=")
        along = int(along)
        print(d.items())
        newd = d.copy()
        for (x, y), val in d.items():
            if val == 0:
                continue
            if ax == "x":
                if x <= along:
                    continue
                mirrored = (along - (x - along), y)
                newd[mirrored] = 1
                newd[(x, y)] = 0
            elif ax == "y":
                if y <= along:
                    continue
                mirrored = (x, along - (y - along))
                newd[mirrored] = 1
                newd[(x, y)] = 0
        d = newd

    for y in range(maxy + 1):
        for x in range(maxx + 1):
            val = d[(x, y)]
            print("." if val == 0 else "#", end="")
            if x > 46:
                break
        print("")
        if y > 6:
            break


if __name__ == "__main__":
    main2()
