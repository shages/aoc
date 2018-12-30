
with open('input') as f:
    inp = f.read()

freqs = set([])
cur = 0

def ylines(inp):
    while True:
        for x in inp:
            yield int(x)

for change in ylines(inp.splitlines()):
    cur += change
    if cur in freqs:
        break
    freqs.add(cur)

print(f"Frequency seen twice: {cur}")

