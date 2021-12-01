import math


def adjacent_indices(x, y):
    return [
        index_from_xy(x + 1, y),
        index_from_xy(x + 1, y + 1),
        index_from_xy(x    , y + 1),
        index_from_xy(x - 1, y + 1),
        index_from_xy(x - 1, y),
        index_from_xy(x - 1, y - 1),
        index_from_xy(x    , y - 1),
        index_from_xy(x + 1, y - 1),
    ]


def rings():
    # yield ring sizes
    yield 1
    i = 2
    while True:
        yield i * 4
        i += 2


def index_from_xy(x, y):
    if x == y == 0:
        return 0
    # determine the ring
    if abs(x) > abs(y):
        ring = abs(x)
    else:
        ring = abs(y)

    # determine base index for any given ring
    base_index = 0
    for i, rs in enumerate(rings()):
        if i >= ring:
            break
        base_index += rs

    side_len = (ring + 1) * 2 - 2
    # determine additional offset
    off = 0
    if x == ring and y > -ring:
        # right edge
        off = y + math.floor(side_len / 2) - 1
        return base_index + off
    elif x == -ring and y < ring:
        # left edge
        off = math.floor(side_len / 2) - y - 1
        return base_index + 2 * side_len + off
    elif y == ring and x >= -ring:
        # top edge
        off = math.floor(side_len / 2) - x - 1
        return base_index + 1 * side_len + off
    else:
        # bottom edge
        off = math.floor(side_len / 2) + x - 1
        return base_index + 3 * side_len + off

def xy_from_index(index, ring=1):
    ring_len = 4 * (ring * 2 - 2)
    if ring_len == 0:
        ring_len = 1
    if index < ring_len:
        if ring == 1:
            return (0, 0)
        # calculate XY
        single_side = math.ceil(ring_len / 4)
        side = math.floor(index / single_side)
        local_offset = int(index % single_side)
        center_offset = int(local_offset - single_side / 2)
        if side == 0:
            x = ring - 1
            y = center_offset + 1
        elif side == 2:
            x = -ring + 1
            y = -center_offset - 1
        elif side == 1:
            y = ring - 1
            x = -center_offset - 1
        else:
            y = -ring + 1
            x = center_offset + 1
        return (x, y)
    return xy_from_index(index - ring_len, ring + 1)


def main():
    input = 312051
    vals = [1]
    i = 1
    while vals[-1] < input:
        adj = adjacent_indices(*xy_from_index(i))
        s = 0
        for a in adj:
            if a < len(vals):
                s += vals[a]
        vals.append(s)
        i += 1
    print(vals[-1])
    return

if __name__ == '__main__':
    main()
