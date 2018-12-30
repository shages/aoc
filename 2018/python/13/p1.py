curves = {
    "\\": {
        "^": "<",
        "v": ">",
        ">": "v",
        "<": "^"
    },
    "/": {
        "^": ">",
        "v": "<",
        ">": "^",
        "<": "v"
    },
}

turns = {
    "^": {
        "left": "<",
        "right": ">",
        "straight": "^"
    },
    "v": {
        "left": ">",
        "right": "<",
        "straight": "v"
    },
    ">": {
        "left": "^",
        "right": "v",
        "straight": ">"
    },
    "<": {
        "left": "v",
        "right": "^",
        "straight": "<"
    }
}


w = 150

class Cart:
    def __init__(self, i, direction, location):
        self.i = i
        self.next_turn = "left"
        self.direction = direction 
        self.location = location
        self.removed = False

    def __ne__(self, other):
        return not self.__eq__(other)

    def __eq__(self, other):
        return self.i == other.i

    def rank(self):
        x, y = self.location
        return y * w + x

    def turn(self):
        self.direction = turns[self.direction][self.next_turn]
        if self.next_turn == "left":
            self.next_turn = "straight"
        elif self.next_turn == "straight": 
            self.next_turn = "right"
        else:
            self.next_turn = "left"

    def __str__(self):
        return self.direction

    def move(self, grid):
        """Return new location."""
        x, y = self.location
        track = grid[y][x]
        # turn if needed
        if track.type == "+":
            self.turn()
        elif track.type == "/" or track.type == "\\":
            self.direction = curves[track.type][self.direction]

        # then move
        if self.direction == "^":
            self.location = (x, y - 1)
        elif self.direction == ">":
            self.location = (x + 1, y)
        elif self.direction == "<":
            self.location = (x - 1, y)
        elif self.direction == "v":
            self.location = (x, y + 1)
        else:
            raise RuntimeError('shit')


class Track:
    def __init__(self, track_type):
        self.type = track_type
    def __str__(self):
        return self.type


def check_crash(last_cart, carts):
    for cart in carts:
        if cart == last_cart or cart.removed:
            continue
        if cart.location == last_cart.location:
            cart.removed = True
            last_cart.removed = True
            return [c for c in carts if c != cart and c != last_cart]
    return carts


def main():
    grid = [[None for x in range(150)] for y in range(150)]

    # with open("NmsuN6SP.txt") as f:
    with open("input") as f:
        inp = f.read()
    cart_types = set(["<", ">", "v", "^"])
    track_types = set(["-", "|", "/", "\\", "+"])
    carts = []
    for y, row in enumerate(inp.splitlines()):
        for x, char in enumerate(row):
            if char in cart_types:
                if char == "<" or char == ">":
                    char2 = "-"
                else:
                    char2 = "|"
                grid[y][x] = Track(char2)
                carts.append(Cart(len(carts), char, (x, y)))
            elif char in track_types:
                grid[y][x] = Track(char)

    t = 0
    printing = False
    while True:
        t += 1
        if t > 11928:
            printing = True
        else:
            printing = False
        # move carts
        for cart in sorted(carts, key=lambda c: c.rank()):
            cart.move(grid)
            if printing:
                print(f"[{t}] {cart.direction}@{cart.location}")
            if cart.removed:
                continue
            new_carts = check_crash(cart, carts)
            if len(new_carts) != len(carts):
                print(f"[{t}] Crash @ {cart.location}")
                with open(f"out.{t}.{cart.i}", "w") as f:
                    f.write(pprint(grid, carts))
        carts = [c for c in carts if not c.removed]
        if len(carts) <= 1:
            print(f"[{t}] Last cart @ {carts[0].location}")
            break
        # with open("out." + str(t), "w") as f:
        #     f.write(pprint(grid, carts))

def pprint(grid, carts):
    g = [r[:] for r in grid]
    for cart in carts:
        x, y = cart.location
        g[y][x] = cart
    lines = []
    for row in g:
        chars = ""
        for col in row:
            if col is None:
                c = " "
            else:
                c = str(col)
            chars += c
        lines.append(chars)
    return "\n".join(lines)
    

if __name__ == "__main__":
    main()

