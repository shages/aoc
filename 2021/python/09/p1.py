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


def main():
    global filename
    lines = parse_lines()
    nums = [list(map(int, line)) for line in lines]
    print(nums)
    h = 0
    lows = []
    for row in range(len(nums)):
        for col in range(len(nums[0])):
            n = nums[row][col]
            if row == 0:
                if col == 0:
                    if n < nums[row + 1][col] and n < nums[row][col + 1]:
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
                elif col == len(nums[0]) - 1:
                    if n < nums[row + 1][col] and n < nums[row][col - 1]:
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
                else:
                    if (
                        n < nums[row + 1][col]
                        and n < nums[row][col - 1]
                        and n < nums[row][col + 1]
                    ):
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
            elif row == len(nums) - 1:
                if col == 0:
                    if n < nums[row - 1][col] and n < nums[row][col + 1]:
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
                elif col == len(nums[0]) - 1:
                    if n < nums[row - 1][col] and n < nums[row][col - 1]:
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
                else:
                    if (
                        n < nums[row - 1][col]
                        and n < nums[row][col - 1]
                        and n < nums[row][col + 1]
                    ):
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
            else:
                if col == 0:
                    if (
                        n < nums[row + 1][col]
                        and n < nums[row - 1][col]
                        and n < nums[row][col + 1]
                    ):
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
                elif col == len(nums[0]) - 1:
                    if (
                        n < nums[row + 1][col]
                        and n < nums[row - 1][col]
                        and n < nums[row][col - 1]
                    ):
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
                else:
                    if (
                        n < nums[row + 1][col]
                        and n < nums[row - 1][col]
                        and n < nums[row][col + 1]
                        and n < nums[row][col - 1]
                    ):
                        print(f"low={n}")
                        h += 1 + n
                        lows.append((row, col, n))
    print(h)

    bs = []
    for row, col, n in lows:
        in_basin = [(row, col)]
        checked = [(row, col)]
        unchecked = [
            (row, col + 1),
            (row, col - 1),
            (row + 1, col),
            (row - 1, col),
        ]
        while len(unchecked):
            sr, sc = unchecked.pop()
            checked.append((sr, sc))
            if sr < 0 or sr > len(nums):
                continue
            if sc < 0 or sc > len(nums[0]):
                continue
            try:
                if nums[sr][sc] == 9:
                    continue
                else:
                    in_basin.append((sr, sc))
                    unchecked.extend(
                        [
                            x
                            for x in [
                                (sr, sc + 1),
                                (sr, sc - 1),
                                (sr + 1, sc),
                                (sr - 1, sc),
                            ]
                            if x not in checked
                        ]
                    )
            except IndexError:
                continue
        print(in_basin)
        bs.append(len(set(in_basin)))
    for b in bs:
        print(b)
    ans = list(sorted(bs))[-3:]
    print(ans[0] * ans[1] * ans[2])


def main2():
    global filename
    filename = "example"
    lines = parse_lines()
    nums = [list(map(int, line)) for line in lines]
    d = defaultdict(lambda: 9)
    for r in range(len(nums)):
        for c in range(len(nums[0])):
            d[r, c] = nums[r][c]

    h = 0
    for r in range(len(nums)):
        for c in range(len(nums[0])):
            al, ar, at, ab = (
                d[r, c - 1],
                d[r, c + 1],
                d[r - 1, c],
                d[r + 1, c],
            )
            n = nums[r][c]
            if n < al and n < ar and n < at and n < ab:
                h += n + 1
    print(h)


if __name__ == "__main__":
    main2()
