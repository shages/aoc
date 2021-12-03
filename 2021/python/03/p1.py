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


def parse_bit_array():
    return [[int(c) for c in line] for line in parse_lines()]


def main():
    arr = parse_bit_array()

    count = len(arr)
    most = [
        round(sum([line[pos] for line in arr]) / count) for pos in range(len(arr[0]))
    ]
    least = [1 - m for m in most]

    g = int("".join(map(str, most)), 2)
    e = int("".join(map(str, least)), 2)
    print(g * e)


if __name__ == "__main__":
    main()
