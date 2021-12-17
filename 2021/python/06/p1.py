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


def main2():
    global filename
    # filename = "example"
    lines = parse_lines()
    fish = list(map(int, lines[0].split(",")))

    for day in range(256):
        print(f"day={day}")
        newf = []
        for i, f in enumerate(fish):
            if f == 0:
                fish[i] = 6
                newf.append(8)
            else:
                fish[i] -= 1
        fish.extend(newf)
    print(len(fish))


import math


def main():
    global filename
    lines = parse_lines()
    fish = list(map(int, lines[0].split(",")))

    fish = [sum([1 for f in fish if f == i]) for i in range(9)]

    for day in range(256):
        f = fish[0]
        ffish = fish[1:] + [f]
        ffish[6] += f
        fish = ffish
    print(sum(fish))


if __name__ == "__main__":
    main()
