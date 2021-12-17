import sys
import itertools
import re


def read_input():
    with open("input2") as f:
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


def main2():
    lines = parse_lines()

    arr = np.ndarray((10, 10), int)
    arr.fill(0)
    for line in lines:
        print(line)
        start, end = line.split(" -> ")
        sx, sy = list(map(int, start.split(",")))
        ex, ey = list(map(int, end.split(",")))
        if sx == ex:
            if sy < ey:
                arr[sy : ey + 1, sx] += 1
            else:
                arr[ey : sy + 1, sx] += 1
        elif sy == ey:
            if sx < ex:
                arr[sy, sx : ex + 1] += 1
            else:
                arr[sy, ex : sx + 1] += 1
    print(arr)
    print(sum([1 for row in arr for g in row if g > 1]))


def main():
    lines = parse_lines()

    vals = [line.split(" -> ") for line in lines]
    grid = [[0 for y in range(1000)] for x in range(1000)]

    for start, end in vals:
        sx, sy = list(map(int, start.split(",")))
        ex, ey = list(map(int, end.split(",")))
        if sy == ey:
            for x in range(min(sx, ex), max(sx, ex) + 1):
                grid[int(ey)][int(x)] += 1
        elif sx == ex:
            for y in range(min(sy, ey), max(sy, ey) + 1):
                grid[int(y)][int(sx)] += 1
        else:
            for x, y in zip(
                range(sx, ex, -1 if sx > ex else 1),
                range(sy, ey, -1 if sy > ey else 1),
            ):
                grid[y][x] += 1
            grid[ey][ex] += 1

    print(sum([1 for row in grid for g in row if g > 1]))


if __name__ == "__main__":
    main2()
