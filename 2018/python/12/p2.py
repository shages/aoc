import re
from itertools import product

class Rule:
    def __init__(self, i, o):
        self.i = i
        self.o = o

    def __eq__(self, other):
        return self.i == other.i and self.o == other.o

    def __hash__(self):
        return hash(self.i + self.o)

class Pot:
    def __init__(self, plant=False):
        self.plant = plant

    def simple(self):
        return "#" if self.plant else "."


def generation(pots, rulemap):
    new_pots = init_pots(len(pots))
    for i, p in pots.items():
        try:
            row = [
                pots[i-2],
                pots[i-1],
                pots[i],
                pots[i+1],
                pots[i+2],
            ]
        except KeyError:
            continue
        s = "".join([r.simple() for r in row])
        try:
            plant = rulemap[s].o == "#"
        except KeyError:
            plant = False
        new_pots[i] = Pot(plant=plant)
    return new_pots

def init_pots(size):
    buf = 300
    return {i: Pot() for i in range(-10, size+buf)}

def ppots(pots, gen="X"):
    print(f"{gen:3d} ", end="")
    for i in range(-3, 200):
        try:
            print(pots[i].simple(), end="")
        except KeyError:
            print(".", end="")
    print()

def main():
    with open("input") as f:
        inp = f.read()

    lines = inp.splitlines()
    init = lines[0][15:]
    rules = lines[2:]

    re_rule = re.compile(r"([\.#]{5}) => ([\.#])")
    rulemap = {}
    for rule in rules:
        m = re_rule.match(rule)
        r = Rule(m.group(1), m.group(2))
        rulemap[r.i] = r

    pots = init_pots(len(init))
    for i, c in enumerate(init):
        if c == "#":
            pots[i].plant = True

    history = []
    ppots(pots, -1)
    for gen in range(1000):
        if gen % 1000 == 0:
            print(f"gen={gen}")
        pots = generation(pots, rulemap)
        # history.append(pots)
        # patterns = identify_patterns(history)
        # ppots(pots, gen)

        s = sum([i for i, p in pots.items() if p.plant])
        try:
            delta = s - history[-1]
            print(f"gen={gen}, sum={s}, delta={delta}")
        except IndexError:
            print(f"gen={gen}, sum={s}")
        history.append(s)

if __name__ == "__main__":
    main()

