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

def sum_manhattan(x, y, pairs):
    s = sum([manhattan(x, y, ax, ay) for ax, ay in pairs])
    return 1 if s < 10000 else 0

print(sum([
    sum_manhattan(x, y, pairs) 
    for x in range(minx, maxx + 1) 
    for y in range(miny, maxy + 1)
]))

