import sys
import itertools
import re

filename = "input"


def read_input():
    print("reading: %s" % filename)
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


def main():
    global filename
    # filename = "example"
    lines = parse_lines()
    nums = list(map(int, lines[0].split(",")))
    print(len(nums))
    diffs = []
    for i in range(max(nums)):
        tdiff = 0
        for n in nums:
            nd = abs(n - i)
            tdiff += ((nd * nd) + nd) / 2
        diffs.append((i, tdiff))

    mindiff = min([x[1] for x in diffs])

    print(mindiff)
    print([n for n in diffs if n[1] == mindiff])


if __name__ == "__main__":
    main()
