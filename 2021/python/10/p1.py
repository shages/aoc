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


def main():
    global filename
    lines = parse_lines()

    score = 0
    scores = []
    for line in lines:
        corrupt = False
        stack = []
        print(line)
        for char in line:
            if char in types.keys():
                # open
                stack.append(types[char])
            else:
                if char != stack[-1]:
                    # corrupt
                    # score += scores[char]
                    corrupt = True
                else:
                    stack.pop()
        if corrupt:
            continue
        print(stack)
        if len(stack):
            # inc
            csum = 0
            for rem in reversed(stack):
                csum *= 5
                csum += scores2[rem]
            scores.append(csum)

    scores = list(sorted(scores))
    print("\n".join(map(str, scores)))
    ml = int((len(scores) + 1) / 2) - 1
    print("")
    print(list(sorted(scores))[ml])


if __name__ == "__main__":
    main()
