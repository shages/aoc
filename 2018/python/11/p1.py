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
for x, (x1, x2, x3) in enumerate(zip(grid, grid[1:], grid[2:])):
    for y, (y1, y2, y3) in enumerate(zip(
        zip(x1, x1[1:], x1[2:]),
        zip(x2, x2[1:], x2[2:]),
        zip(x3, x3[1:], x3[2:]),
    )):
        s = sum([sum(bundle) for bundle in (y1, y2, y3)])
        sums.append((s, (x, y)))

m = max(sums, key=lambda v: v[0])
print(m)
