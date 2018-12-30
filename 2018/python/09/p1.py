import re
from copy import deepcopy

with open("input") as f:
    inp = f.read()

m = re.match(r"(\d+) players; last marble is worth (\d+) points", inp)
n = int(m.group(1))
p = int(m.group(2)) * 100

class CircleMarble:
    def __init__(self, i, cw=None, ccw=None):
        self.i = deepcopy(i)
        self.cw = self if cw is None else cw
        self.ccw = self if ccw is None else ccw
        self.current = False

    def simple(self):
        if self.current:
            return f"({self.i})"
        else:
            return f"{self.i}"

    def __eq__(self, other):
        return self.i == other.i

    def __ne__(self, other):
        return not self.__eq__(other)

    def __str__(self):
        return f"M<{self.i}{'X' if self.current else ''}|{self.cw.i}|{self.ccw.i}>"

    def __repr__(self):
        return self.__str__()


def insert_between(i, curr):
    # print(f"ib({i}, {curr})")
    if curr is None:
        marble = CircleMarble(i)
        marble.current = True
        return marble
    curr.current = False
    a = curr.cw
    b = curr.cw.cw
    # print(f"ib->{a}, {b}")
    if a != b:
        marble = CircleMarble(i, cw=b, ccw=a)
        a.cw = marble
        b.ccw = marble
        marble.current = True
        return marble
    else:
        marble = CircleMarble(i, cw=a, ccw=a)
        a.cw = marble
        a.ccw = marble
        marble.current = True
        return marble

marbles = []
current = None

class Player:
    def __init__(self, i):
        self.i = i
        self.next = None
        self.prev = None
        self.score = 0

def remove_marble(m):
    ccw = m.ccw
    cw = m.cw
    ccw.cw = cw
    cw.ccw = ccw
    m.cw = None
    m.ccw = None
    return cw

players = [Player(0)]
for i in range(1, n):
    player = Player(i)
    players[-1].next = player
    player.prev = players[-1]
    players.append(player)

players[0].prev = players[-1]
players[-1].next = players[0]
player = players[0]


def print_circle(player):
    print(f"[{player.i}] ", end="")
    m = marbles[0]
    print(m.simple(), end=" ")
    c = m.cw
    while c != m:
        print(c.simple(), end=" ")
        c = c.cw
    print()


i = 0
while True:
    if i != 0 and i % 23 == 0:
        seven_ccw = current.ccw.ccw.ccw.ccw.ccw.ccw.ccw
        player.score += i + seven_ccw.i
        current.current = False
        current = remove_marble(seven_ccw)
        current.current = True
    else:
        current = insert_between(i, current)
        marbles.append(current)
    # print_circle(player)

    if i == p:
        break

    i += 1
    player = player.next

highest = sorted(players, key=lambda p: p.score)[-1]
print(highest.score)

