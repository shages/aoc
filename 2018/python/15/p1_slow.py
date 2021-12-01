import sys
import math
import time
import os

class CannotMoveError(Exception):
    pass


class Unit:

    width = None 

    def __init__(self, location):
        self.loc = location
        self.alive = True
        self.hp = 200
        self.ap = 3

    @property
    def turn_order(self):
        x, y = self.loc
        return self.__class__.width * y + x

    def move_to(self, loc, grid):
        cx, cy = self.loc
        tx, ty = loc
        self.loc = loc
        grid[cy][cx] = "."
        target = grid[ty][tx] 
        if target != ".":
            raise CannotMoveError
        grid[ty][tx] = self.__class__.__name__[0]

    def attack(self, other):
        other.hp -= self.ap
        if other.hp <= 0:
            self.kill(other)
        return other.hp

    def kill(self, other):
        other.alive = False

    def __str__(self):
        return f"{self.__class__.__name__[0]}({self.hp})"

class Goblin(Unit):
    pass
class Elf(Unit):
    pass

def ppgrid(grid, units=[]):
    if len(units) == 0:
        return "\n".join([
            "".join([c for c in row])
            for row in grid
        ])

    rows = []
    units_alive = [u for u in units if u.alive]
    for y, row in enumerate(grid):
        units_in_row = [u for u in units_alive if u.loc[1] == y]
        units_sorted = sorted(units_in_row, key=lambda u: u.loc[0])
        grow = "".join([c for c in row])

        if len(units_sorted):
            grow += "   " + ", ".join([str(u) for u in units_sorted])
        rows.append(grow)
    return "\n".join(rows)

def print_grid(grid):
    print(ppgrid(grid))

def main():
    with open(sys.argv[1]) as f:
        contents = f.read()

    width = len(contents.splitlines()[0])
    Unit.width = width
    
    elves = []
    goblins = []
    grid = []
    for y, line in enumerate(contents.splitlines()):
        row = []
        for x, char in enumerate(line):
            row.append(char)
            if char == "G":
                goblin = Goblin((x, y))
                goblins.append(goblin)
            elif char == "E":
                elf = Elf((x, y))
                elves.append(elf)
        grid.append(row)

    def reading_order(loc):
        x, y = loc
        return y * width + x

    def units():
        nonlocal elves
        nonlocal goblins
        return elves + goblins

    # rounds
    rounds = 0
    end = False
    while not end:
        os.system("clear")
        rounds += 1
        print(f"rounds={rounds}")
        # print_grid(grid)
        turn_units = units()
        with open(f"out.{rounds}", "w") as f:
            f.write(ppgrid(grid, units=turn_units))

        # determine turn order
        ordered = sorted(turn_units, key=lambda u: u.turn_order)
        for unit in ordered:
            if not unit.alive:
                continue
            targets = elves if isinstance(unit, Goblin) else goblins
            targets = [t for t in targets if t.alive]
            # print(f"targets={targets}")
            if len(targets) == 0:
                # combat ends
                end = True

            # check adjacent tiles for attack, in reading order
            x, y = unit.loc
            adj = [
                *[t for t in targets if t.loc == (x, y-1)], # above
                *[t for t in targets if t.loc == (x-1, y)], # left
                *[t for t in targets if t.loc == (x+1, y)], # right
                *[t for t in targets if t.loc == (x, y+1)], # below
            ]
            if len(adj):
                # attack
                min_hp = sorted(adj, key=lambda t: t.hp)[0].hp
                adj_min_hp = [t for t in adj if t.hp == min_hp]
                target = adj_min_hp[0]
                other_hp = unit.attack(target)
                if other_hp <= 0:
                    tx, ty = target.loc
                    grid[ty][tx] = "."
                    print(f"Unit died: {target}")
                continue

            range_locs = []
            target_paths = []
            for target in targets:
                tx, ty = target.loc
                locations = [rloc for rloc in [
                        (tx, ty + 1),
                        (tx, ty - 1),
                        (tx + 1, ty),
                        (tx - 1, ty),
                    ]
                    if grid[rloc[1]][rloc[0]] == "."
                ]
                for loc in locations:
                    paths = find_path_between(unit, loc, target, grid)
                    #print(f"paths to {target}")
                    #print(f"{paths}")
                    if len(paths):
                        target_paths.append((target, loc, paths[0]))
                range_locs.extend(locations)

            if len(target_paths) == 0:
                # print(f"Skipping, no paths")
                continue
            
            sorted_paths = list(sorted(target_paths, key=lambda i: len(i[2])))
            min_len = len(sorted_paths[0][2])
            nearest_paths = [p for p in target_paths if len(p[2]) == min_len]
            chosen_path = list(sorted(nearest_paths, key=lambda i: reading_order(i[1])))[0]
            # print(f"chosen_path={chosen_path}")
            
            # unit should move
            unit.move_to(chosen_path[2][0], grid)
            # os.system("clear")
            # print_grid(grid)
            
            # attack after move
            x, y = unit.loc
            adj = [
                *[t for t in targets if t.loc == (x, y-1)], # above
                *[t for t in targets if t.loc == (x-1, y)], # left
                *[t for t in targets if t.loc == (x+1, y)], # right
                *[t for t in targets if t.loc == (x, y+1)], # below
            ]
            if len(adj):
                # attack
                min_hp = sorted(adj, key=lambda t: t.hp)[0].hp
                adj_min_hp = [t for t in adj if t.hp == min_hp]
                target = adj_min_hp[0]
                other_hp = unit.attack(target)
                if other_hp <= 0:
                    tx, ty = target.loc
                    grid[ty][tx] = "."
                    print(f"Unit died: {target}")


        if len(turn_units) <= 1:
            break
        # print(f"round={round}")
        # time.sleep(0.5)
    print(f"Combat ended in round {rounds}")
    shp = sum([u.hp for u in units() if u.alive])
    print(f"Sum of remaining units = {shp}")
    print(f"part 1 = {shp * (rounds - 1)}")

def find_path_between(unit, tloc, target, grid):
    now = time.time()
    # print_grid(grid)
    # time.sleep(3)
    ngrid = [[math.inf if x == "." else -math.inf for x in row] for row in grid]
    ngrid[unit.loc[1]][unit.loc[0]] = 0
    ngrid[tloc[1]][tloc[0]] = math.inf
    nodes = set([(x, y) for y, row in enumerate(ngrid) for x, v in enumerate(row) if v != -math.inf])

    def adjacent_nodes(x, y):
        return [
            (x, y + 1),
            (x, y - 1),
            (x + 1, y),
            (x - 1, y),
        ]

    current = unit.loc
    paths = []
    while len(nodes):
        #print(current)
        #print(target.loc)
        adjacent = adjacent_nodes(*current)
        for adj in adjacent:
            x, y = adj
            try:
                n = ngrid[y][x]
            except IndexError:
                continue
            delta = ngrid[current[1]][current[0]] + 1
            if n == math.inf or n > delta:
                ngrid[y][x] = delta

        nodes.remove(current)
        if len(nodes) == 0:
            raise RuntimeError("no path to target")

        # select new current
        remaining = [(n, (x, y)) for y, row in enumerate(ngrid) for x, n in enumerate(row) if (x, y) in nodes]
        remaining_min = sorted(remaining, key=lambda n: n[0])[0]
        #print(f"remaining_min={remaining_min}")
        if remaining_min[0] == math.inf:
            # print(f"remaining is inf")
            break
        current = remaining_min[1]
        if current == tloc:
            # done - find shortest route back to start
            path = []
            nextnode = current
            while nextnode != unit.loc:
                path.append(nextnode)
                adj = [(ngrid[y][x], (x,y)) for x,y in adjacent_nodes(*nextnode) if ngrid[y][x] != -math.inf]
                adj_min = sorted(adj, key=lambda n: n[0])[0]
                nextnode = adj_min[1]
            paths.append(list(reversed(path)))
            break
    end = time.time()
    rt = end - now
    print(f"dijkstra's <{unit}> completed in: {rt:2.3f} seconds")
    return paths

if __name__ == "__main__":
    main()



