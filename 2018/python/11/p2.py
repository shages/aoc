import math

size = 300

sn = 9810

def power(x, y, sn):
    rid = x + 10
    p = (rid * y + sn) * rid
    hund = math.floor((p % 1000) / 100)
    return hund - 5

def pprint(grid):
    tgrid = [[0 for x in range(size)] for y in range(size)]
    for x, col in enumerate(grid):
        for y, val in enumerate(col):
            tgrid[y][x] = val
    print("\n".join(["".join([f"{c:3d}" for c in row]) for row in tgrid]))


grid = [[power(x, y, sn) for y in range(1, size+1)] for x in range(1, size+1)]

pprint(grid)

sums = []
m = (0, None, None)
for gridsize in range(1, size + 1):
    print(f"gridsize={gridsize}")
    for x, grids in enumerate(zip(*[grid[i:] for i in range(gridsize)])):
        for y, ys in enumerate(zip(*[zip(*[g[i:] for i in range(gridsize)]) for g in grids])):
            s = sum([sum(bundle) for bundle in ys])
            if s > m[0]:
                m = (s, (x, y), gridsize)
                print(f"new max={m}")
print(m)
