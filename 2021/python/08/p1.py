import sys
import itertools
import re

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


p = {2: [1], 3: [7], 4: [4], 6: [0, 6, 9], 5: [2, 3, 5], 7: [8]}

num_to_alpha = {
    0: "abcefg",
    1: "cf",
    2: "acdeg",
    3: "acdfg",
    4: "bcdf",
    5: "abdfg",
    6: "abdefg",
    7: "acf",
    8: "abcdefg",
    9: "abcdfg",
}
alpha_to_num = {v: k for k, v in num_to_alpha.items()}

perms = list(itertools.permutations("abcdefg", 7))


def main2():
    lines = parse_lines()
    summ = 0
    for line in lines:
        left, right = line.split(" | ")
        inputs = left.split()
        outputs = right.split()

        # find valid permutation
        for perm in perms:
            lookup = dict(zip(perm, "abcdefg"))
            nums = []
            try:
                for input in inputs:
                    key = "".join(sorted([lookup[char] for char in input]))
                    nums.append(alpha_to_num[key])
            except KeyError:
                continue
            break

        # apply to output
        nums = []
        for output in outputs:
            key = "".join(sorted([lookup[char] for char in output]))
            nums.append(alpha_to_num[key])

        summ += int("".join(map(str, nums)))
    print(summ)


def main():
    global filename
    filename = "input"
    lines = parse_lines()
    count = 0
    summ = 0

    for line in lines:

        alpha = {
            "a": set(["a", "b", "c", "d", "e", "f", "g"]),
            "b": set(["a", "b", "c", "d", "e", "f", "g"]),
            "c": set(["a", "b", "c", "d", "e", "f", "g"]),
            "d": set(["a", "b", "c", "d", "e", "f", "g"]),
            "e": set(["a", "b", "c", "d", "e", "f", "g"]),
            "f": set(["a", "b", "c", "d", "e", "f", "g"]),
            "g": set(["a", "b", "c", "d", "e", "f", "g"]),
        }

        left, right = line.split(" | ")
        nleft = left.split()
        nright = right.split()
        for ex in nright:
            digits = len(ex)
            possible = p[digits]
            if len(possible) == 1:
                count += 1
        for ex in nleft:
            digits = len(ex)
            possible = p[digits]
            if len(possible) == 1:
                pnum = possible[0]
                # we know the number
                for char in num_to_alpha[pnum]:
                    alpha[char] &= set([c for c in ex])
                segs_for_pnum = num_to_alpha[pnum]
                other_segs = set("abcdefg") - set(segs_for_pnum)

                # exclude these chars from all other alpha additionally
                for seg in other_segs:
                    alpha[seg] -= set([c for c in ex])

        common_twos = {}
        for k, v in alpha.items():
            if len(v) == 1:
                # exclude from others
                char = list(v)[0]
                for x in set("abcdefg") - set(k):
                    alpha[x] -= v
            else:
                key = "".join(sorted(list(v)))
                if key in common_twos:
                    # remove this key from this k and other k
                    other_k = common_twos[key]
                    for other in "abcdefg":
                        if other in [k, other_k]:
                            continue
                        alpha[other] -= set(key)

                else:
                    common_twos[key] = k

        arr = [list(alpha[a]) for a in "abcdefg"]
        print("arr")
        print(alpha)
        print(arr)
        for a, b, c, d, e, f, g in itertools.product(*arr):
            rev = {a: "a", b: "b", c: "c", d: "d", e: "e", f: "f", g: "g"}
            unique_vals = {v for k, v in rev.items()}
            if len(unique_vals) != 7:
                continue
            print("trying")
            print(rev)
            try:
                nums = []
                # rev = {v: k for k, v in rev.items()}
                for out in nright:
                    key = ""
                    for char in out:
                        key += rev[char]
                    key = "".join(sorted(key))
                    num = alpha_to_num[key]
                    nums.append(num)
                final_nums = nums
                break
            except KeyError:
                continue
        else:
            print("fuck")
            # print(sols)
            print(alpha)
            print(nleft)
            print(nright)
            return

        # print(alpha)
        summ += int("".join(map(str, final_nums)))
    print(summ)


if __name__ == "__main__":
    main2()
