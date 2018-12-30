import re

with open('input') as f:
    inp = f.read()

re_line = re.compile(r"#(\d+)\s+@\s+(\d+),(\d+):\s*(\d+)x(\d+)$")
def parse(line):
    m = re_line.match(line)
    if not m:
        raise RuntimeError('crap')
    return int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))

grid = [[0 for x in range(1000)] for y in range(1000)]

for line in inp.splitlines():
    ll, tt, w, h = parse(line)
    for y in range(h):
        for x in range(w):
            grid[tt + y][ll + x] += 1

two_or_more = 0
for row in grid:
    for col in row:
        if col > 1:
            two_or_more += 1

print(two_or_more) 
