import itertools
import re


def read_input():
    with open("input") as f:
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


def main():
    lines = parse_lines()
    h = 0
    d = 0
    aim = 0
    for line in lines:
        vals = line.split()
        if vals[0] == "forward":
            h += int(vals[1])
            d += aim * int(vals[1])
        elif vals[0] == "down":
            aim += int(vals[1])
        elif vals[0] == "up":
            aim -= int(vals[1])

    print(d * h)


if __name__ == "__main__":
    main()
