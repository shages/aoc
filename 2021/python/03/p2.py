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

    def finder(lines, kind, pos=0):
        o = sum([l[pos] for l in lines if l[pos] == 1])
        z = len(lines) - o
        return (
            [l for l in lines if l[pos] == (0 if z <= o else 1)]
            if kind == "least"
            else [l for l in lines if l[pos] == (0 if z > o else 1)]
        )

    cur_lines = arr
    pos = 0
    while len(cur_lines) > 1:
        cur_lines = finder(cur_lines, "most", pos)
        pos += 1

    ox = int("".join(map(str, cur_lines[0])), 2)

    cur_lines = arr
    pos = 0
    while len(cur_lines) > 1:
        cur_lines = finder(cur_lines, "least", pos)
        pos += 1

    co = int("".join(map(str, cur_lines[0])), 2)

    print(ox * co)


if __name__ == "__main__":
    main()
