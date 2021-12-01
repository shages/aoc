from collections import OrderedDict

class Unit(object):
    def __init__(self, is_elf, hp=200):
        self.is_elf, self.hp = is_elf, hp

walls, initial_units = set(), {}
with open('input') as puzzle_file:
    for y, line in enumerate(puzzle_file):
        for x, c in enumerate(line):
            if c == '#':
                walls.add((y, x))
            elif c == 'E':
                initial_units[(y, x)] = True
            elif c == 'G':
                initial_units[(y, x)] = False

def adjs(pos):
    y, x = pos
    return ((y - 1, x), (y, x - 1), (y, x + 1), (y + 1, x))

def nearest(start, goals, excludes):
    visited, queue = set(excludes), {start}
    while queue:
        reached = queue.intersection(goals)
        if reached:
            return min(reached)
        visited.update(queue)
        queue = {adj for pos in queue for adj in adjs(pos) if adj not in visited}
    return None

def dbg(units):
    for y in range(min(y for y, _ in walls), max(y for y, _ in walls) + 1):
        row = ''.join('#' if (y, x) in walls else 'GE'[units[(y, x)].is_elf]
                      if (y, x) in units else '.'
                      for x in range(min(x for _, x in walls), max(x for _, x in walls) + 1))
        etc = ', '.join('{}({})'.format('GE'[unit.is_elf], unit.hp)
                        for _, unit in sorted(
                            ((pos[1], unit) for pos, unit in units.items() if pos[0] == y),
                            key=lambda item: item[1]))
        print(row + '   ' + etc if etc else row)

for elf_power in range(3, 201):
    dead_elves, full_rounds = 0, 0
    units = {pos: Unit(is_elf) for pos, is_elf in initial_units.items()}
    while len(set(unit.is_elf for unit in units.values())) > 1:
        #print('After {} round{}:'.format(full_rounds, 's' if full_rounds > 1 else '') if full_rounds else 'Initially:')
        #dbg(units)
        #print('')
        queue, units = OrderedDict(sorted(units.items())), {}
        while queue:
            pos, unit = queue.popitem(last=False)
            other_units = units.copy()
            other_units.update(queue)
            excludes = walls.union(other_units)
            enemies = {k: v for k, v in other_units.items() if unit.is_elf != v.is_elf}
            if not set(adjs(pos)).intersection(enemies):
                enemy_ranges = {adj for enemy_pos in enemies.keys() for adj in adjs(enemy_pos)}
                nearest_enemy_range = nearest(pos, enemy_ranges, excludes)
                if nearest_enemy_range:
                    pos = nearest(nearest_enemy_range, adjs(pos), excludes) or pos
            adjacent_enemies = [(adj, enemies[adj]) for adj in adjs(pos) if adj in enemies]
            if adjacent_enemies:
                target, enemy = min(adjacent_enemies, key=lambda item: (item[1].hp, item[0]))
                enemy.hp -= elf_power if unit.is_elf else 3
                if enemy.hp <= 0:
                    units.pop(target, None)
                    queue.pop(target, None)
                    if enemy.is_elf:
                        dead_elves += 1
            units[pos] = unit
            if not enemies:
                units.update(queue)
                break
        else:
            full_rounds += 1
    #print('Finally:')
    #dbg(units)
    #print('')
    total_hp = sum(unit.hp for unit in units.values())
    print(u'power: {}\trounds: {}\t\u2211hp: {}\tscore: {}\tdead: {}'.format(
        elf_power, full_rounds, total_hp, full_rounds * total_hp, dead_elves))
    #print('\n')
    if not dead_elves:
        break
