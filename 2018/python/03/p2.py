import re

with open('input') as f:
    inp = f.read()

re_line = re.compile(r"#(\d+)\s+@\s+(\d+),(\d+):\s*(\d+)x(\d+)$")
def parse(line):
    m = re_line.match(line)
    if not m:
        raise RuntimeError('crap')
    return int(m.group(1)), int(m.group(2)), int(m.group(3)), int(m.group(4)), int(m.group(5))

grid = [[0 for x in range(1000)] for y in range(1000)]

claims = set([])

for line in inp.splitlines():
    claim, ll, tt, w, h = parse(line)
    claims.add(claim)
    for y in range(h):
        for x in range(w):
            cur = grid[tt + y][ll + x]
            # check for overlap
            if cur != 0:
                # overlap
                try:
                    claims.remove(cur)
                except KeyError:
                    pass
                try:
                    claims.remove(claim)
                except KeyError:
                    pass
            grid[tt + y][ll + x] = claim

print(claims) 
