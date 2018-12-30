import math
import os
import time
import re

with open("input") as f:
    inp = f.read()

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Velocity:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Point:
    def __init__(self, pos, vel):
        self.pos = pos
        self.vel = vel

r = re.compile("position=<\s*([\-\+]?\d+),\s*([\-\+]?\d+)> velocity=<\s*([\-\+]?\d+),\s*([\-\+]?\d+)>")
points = []
for line in inp.splitlines():
    # print(line)
    m = r.match(line)
    point = Point(
        pos=Position(
            x=int(m.group(1)),
            y=int(m.group(2)),
        ),
        vel=Velocity(
            x=int(m.group(3)),
            y=int(m.group(4)),
        ),
    )
    points.append(point)


def move(points, tscale=1):
    print("moving points...")
    new_points = []
    for point in points:
        new_points.append(
            Point(
                pos=Position(
                    point.pos.x + point.vel.x * tscale,
                    point.pos.y + point.vel.y * tscale,
                ),
                vel=point.vel
            )
        )
    return new_points

def print_points(points):
    xs = [p.pos.x for p in points]
    ys = [p.pos.y for p in points]
    minx = min(xs)
    maxx = max(xs)
    miny = min(ys)
    maxy = max(ys)
    print(minx)
    print(maxx)
    print(miny)
    print(maxy)

    print("printing points...")
    # scale points
    w = 80
    h = 10
    def transform(point):
        spanx = maxx - minx
        spany = maxy - miny
        newx = int((point.pos.x - minx) / spanx * w)
        newy = int((point.pos.y - miny) / spany * h)
        return newx, newy
    grid = [["." for x in range(w)] for y in range(h)]
    print("grid initialized...")

    # grid = [['.' for x in range(minx, maxx+1)] for y in range(miny, maxy+1)]
    for p in points:
        # print(f"orig=({p.pos.x}, {p.pos.y})")
        x, y = transform(p)
        # print(f"after=({x}, {y})")
        if x >= 0 and x < w and y >= 0 and y < h:
            grid[y][x] = "#"
    print(
        "\n".join(["".join([c for c in row]) for row in grid])
    )

tscale = 100
ttime = 0
for t in range(1000000):
    ttime += tscale
    time.sleep(0.001)
    os.system("clear")
    print(t)
    print(f"ttime={ttime}")
    points = move(points, tscale)
    maxx = max([p.pos.x for p in points])
    print_points(points)
    if maxx < 800:
        tscale = 1
        time.sleep(0.5)

