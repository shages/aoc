pairs = []
with open("input") as f:
    for line in f:
        x, y = line.split(', ')
        pairs.append((int(x), int(y)))

xs = [x for x, y in pairs]
ys = [y for x, y in pairs]

minx = min(xs)
maxx = max(xs)
miny = min(ys)
maxy = max(ys)

def manhattan(x1, y1, x2, y2):
    return abs(x2-x1) + abs(y2-y1)

def min_manhattan(x, y, pairs):
    distances = []
    for i, (ax, ay) in enumerate(pairs):
        distances.append((manhattan(x, y, ax, ay), i))
    s = sorted(distances, key=lambda x: x[0])
    if s[0][0] == s[1][0]:
        return -1
    return s[0][1]

grid = [
    [min_manhattan(x, y, pairs) for x in range(maxx + 1)]
    for y in range(maxy + 1)
]

pair_ids = set(range(len(pairs)))
for c in [*grid[0], *grid[-1], *[r[0] for r in grid], *[r[-1] for r in grid]]:
    try:
        pair_ids.remove(c)
    except KeyError:
        pass

m = {}
for row in grid:
    for col in row:
        if col not in pair_ids:
            continue
        if col not in m:
            m[col] = 0
        m[col] += 1

most = sorted(m.items(), key=lambda x: x[1], reverse=True)[0]
print(f"size={most[1]}")

def map_to_char(c):
    chars = 'abcdefghijklmnopqrstuvwxyz'
    chars += chars.upper()
    chars += '0123456789 '
    return chars[c]

# print('\n'.join([''.join([map_to_char(c) for c in row]) for row in grid]))

