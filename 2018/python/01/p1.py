
with open('input') as f:
    inp = f.read()

result = sum([int(x) for x in inp.splitlines()])
print(f"result = {result}")
