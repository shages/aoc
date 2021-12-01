
def rings():
    # yield ring sizes
    yield 1
    i = 2
    while True:
        yield i * 4
        i += 2

def ring_num(n):
    cum = 0
    prev_size = 0
    prev_cum = 0
    for i, rs in enumerate(rings()):
        prev_cum = cum
        prev_size = rs
        cum += rs
        if n <= cum:
            # index, size, remainder
            return (i, prev_size, n - prev_cum)

def offset_steps(size, rem):
    """Provided the size of a ring and the remaining steps, determine
    the shortest orthogonal offset towards the center of the spiral."""
    single_side = size / 4
    local_offset = int(rem % single_side)
    center_offset = abs(local_offset - single_side / 2)
    print(local_offset)
    print(center_offset)
    return center_offset


def main():
    input = 312051

    # get ring number
    # count remainder steps from ring origin (bottom-right)
    #  to determine the point on the ring
    (index, size, remainder) = ring_num(input)
    print(f'ring={index}, size={size}, remainder={remainder}')
    offset = offset_steps(size, remainder)
    print(f'total steps = {index + offset}')

if __name__ == '__main__':
    main()
