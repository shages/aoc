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
    lines = parse_lines()

    nodes = set()
    edges = []

    for line in lines:
        left, right = line.split("-")
        nodes.add(left)
        nodes.add(right)
        edges.append((left, right))

    def search(node, path=[], visited=defaultdict(int)):
        next_edges = [e for e in edges if node in e]
        paths = []
        for left, right in next_edges:
            ne: str = left if node == right else right
            if ne == "start":
                continue
            elif ne == "end":
                paths.append([*path, "end"])
            elif ne.upper() == ne:
                # large node, go!
                # print(f"copying visited (node={node}, ne={ne})")
                # print(visited)
                # v = visited.copy()
                # print(v)
                # v[ne] += 1
                # print(v)
                paths.extend(search(ne, path=[*path, node], visited=visited))
            else:
                # small node
                if visited[ne] == 0 or (
                    visited[ne] == 1
                    and all([v <= 1 for k, v in visited.items() if k != ne])
                ):
                    v = visited.copy()
                    v[ne] += 1
                    paths.extend(search(ne, path=[*path, node], visited=v))
        return paths

    paths = search("start")
    print(len(paths))


def main2():
    global filename
    filename = "example"
    lines = parse_lines()

    nodes = set()
    edges = []

    for line in lines:
        left, right = line.split("-")
        nodes.add(left)
        nodes.add(right)
        edges.append((left, right))

    degrees = {n: len([e for e in edges if n in e]) for n in nodes}
    print(degrees)
    nodes_copy = nodes.copy()
    for node in nodes:
        if node.lower() == node and degrees[node] == 1:
            edges = [e for e in edges if not (node in e and str(e).lower() == str(e))]
    nodes= set([v for e in edges for v in e))
    print(nodes)
    print(edges)

    def search(node, path=[], visited=defaultdict(int)):
        next_edges = [e for e in edges if node in e]
        paths = []
        for left, right in next_edges:
            ne: str = left if node == right else right
            if ne == "start":
                continue
            elif ne == "end":
                paths.append([*path, "end"])
            elif ne.upper() == ne:
                # large node, go!
                # print(f"copying visited (node={node}, ne={ne})")
                # print(visited)
                # v = visited.copy()
                # print(v)
                # v[ne] += 1
                # print(v)
                paths.extend(search(ne, path=[*path, node], visited=visited))
            else:
                # small node
                if visited[ne] == 0 or (
                    visited[ne] == 1
                    and all([v <= 1 for k, v in visited.items() if k != ne])
                ):
                    v = visited.copy()
                    v[ne] += 1
                    paths.extend(search(ne, path=[*path, node], visited=v))
        return paths

    paths = search("start")
    for path in paths:
        print(path)
    print(len(paths))


if __name__ == "__main__":
    main2()
