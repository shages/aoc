import sys
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


class Spot:
    def __init__(self, val):
        self.val = val
        self.marked = False

    def mark(self):
        self.marked = True

    def __str__(self):
        return f"({self.val}, {self.marked})"

    def __repr__(self):
        return self.__str__()


class Board:
    def __init__(self, b):
        self.spots = [[Spot(x) for x in row] for row in b]
        print(self.spots)
        self.done = False

    def num(self, val):
        for row in self.spots:
            for spot in row:
                if spot.val == val:
                    spot.mark()

        self.check(val)

    def check(self, val):
        if self.done:
            return
        res = False
        for col in range(5):
            if all([row[col].marked for row in self.spots]):
                res = True

        for row in self.spots:
            if all([s.marked for s in row]):
                res = True

        if res:
            print(sum([s.val for row in self.spots for s in row if not s.marked]) * val)
            print("ME")
            self.done = True

    def __str__(self):
        return "\n".join(map(str, self.spots))


def main():
    lines = parse_lines()
    draws = lines[0]

    board = []
    boards = []
    for line in lines[1:]:
        print(f"line={line}")
        if line == "":
            print("end")
            # new board
            if len(board):
                boards.append(Board(board))
            board = []
        else:
            board.append([int(x) for x in line.split()])

    if len(board):
        boards.append(Board(board))

    for draw in draws.split(","):
        print(f"num={draw}")
        for board in boards:
            board.num(int(draw))
            print(board)
        if all([b.done for b in boards]):
            break


if __name__ == "__main__":
    main()
