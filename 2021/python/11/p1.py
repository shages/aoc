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

types = {"(": ")", "[": "]", "{": "}", "<": ">"}

scores = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}
scores2 = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
}


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
    lines = parse_lines()
    oct = {}
    for row, line in enumerate(lines):
        for col, char in enumerate(line):
            oct[(row, col)] = int(char)

    flashes = 0
    for i in range(10000000000):
        fiter = 0
        newoct = {k: v + 1 for k, v in oct.items()}

        pending = {k: v for k, v in newoct.items() if v > 9}
        comp = set()
        while len(pending):
            first = list(pending.keys())[0]
            del pending[first]

            if first in comp:
                continue
            comp.add(first)

            # print(f"flash on {first}")
            fiter += 1
            newoct[first] = 0
            # inc adjacent
            for n in neighbors:
                nfirst = (first[0] + n[0], first[1] + n[1])
                if nfirst in comp:
                    continue
                try:
                    newoct[nfirst] += 1
                    if newoct[nfirst] > 9:
                        pending[nfirst] = newoct[nfirst]
                except KeyError:
                    pass
        if len(comp) >= 100:
            print(i)
            sys.exit()
        flashes += fiter

        oct = newoct

    # inc 1
    # > 9 flash
    #  +1 adjacent


if __name__ == "__main__":
    main()
