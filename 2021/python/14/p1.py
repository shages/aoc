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
    # filename = "example"
    [first_line, _, *rest] = parse_lines()

    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in rest}
    poly = first_line
    print(poly)
    for i in range(40):
        print("iter=" + str(i))
        print(len(poly))
        new_poly = ""
        for j, (l, r) in enumerate(itertools.pairwise(poly)):
            c = l + r
            try:
                rule = rules[c]
                if j == 0:
                    new_poly += l + rule + r
                else:
                    new_poly += rule + r
            except KeyError:
                if j == 0:
                    new_poly += l + r
                else:
                    new_poly += r
            poly = new_poly
        # print(poly)

    d = defaultdict(int)
    for char in poly:
        d[char] += 1
    min = list(sorted(d.values()))[0]
    max = list(sorted(d.values()))[-1]
    print(max - min)


def main2():
    global filename
    filename = "example"
    [first_line, _, *rest] = parse_lines()

    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in rest}
    poly = first_line
    print(poly)

    dicts = {}
    for rkey in rules.keys():
        poly = rkey
        for i in range(40):
            print("iter=" + str(i))
            print(len(poly))
            print(f"poly={poly}")
            new_poly = ""
            for j, (l, r) in enumerate(itertools.pairwise(poly)):
                c = l + r
                try:
                    rule = rules[c]
                    if j == 0:
                        new_poly += l + rule + r
                    else:
                        new_poly += rule + r
                except KeyError:
                    if j == 0:
                        new_poly += l + r
                    else:
                        new_poly += r
                poly = new_poly
            # print(poly)

        d = defaultdict(int)
        for char in poly:
            d[char] += 1
        dicts[rkey] = d

    poly = first_line

    fd = defaultdict(int)
    for l, r in itertools.pairwise(poly):
        pair = l + r
        if pair in dicts:
            for char, count in dicts[pair].items():
                fd[char] += count
        else:
            fd[l] += 1
            fd[r] += 1

    min = list(sorted(d.values()))[0]
    max = list(sorted(d.values()))[-1]
    print(max - min)


def main3():
    global filename
    filename = "example"
    [first_line, _, *rest] = parse_lines()

    rules = {line.split(" -> ")[0]: line.split(" -> ")[1] for line in rest}
    poly = first_line
    print(poly)

    d = defaultdict(int)
    t = 0

    def descend(l, r, iter=0):
        nonlocal t
        t += 1
        print(f"descend={iter},{t}, {l}{r}")
        print(d)
        if iter == 30:
            return
        pair = l + r
        if pair in rules:
            insert = rules[pair]
            d[insert] += 1
            descend(l, insert, iter + 1)
            descend(insert, r, iter + 1)

    print("poly=" + poly)
    for j, (l, r) in enumerate(itertools.pairwise(poly)):
        print(f"{l}{r}")
        if j == 0:
            d[l] += 1
        d[r] += 1
        descend(l, r)

    min = list(sorted(d.values()))[0]
    max = list(sorted(d.values()))[-1]
    print(max - min)


if __name__ == "__main__":
    main3()
