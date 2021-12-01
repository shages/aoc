import math
from collections import namedtuple 


Employee = namedtuple("Employee", ("current_recipe"))

e1 = Employee(current_recipe=0)
e2 = Employee(current_recipe=1)

def draw_scoreboard(scoreboard, e1, e2):
    for i, item in enumerate(scoreboard):
        if e1.current_recipe == i:
            print(f"({item})", end="")
        elif e2.current_recipe == i:
            print(f"[{item}]", end="")
        else:
            print(f"{item:2d} ", end="")
    print()

scoreboard = [3, 7]
i = 0
limit = 110201
while True:
    i += 1
    if len(scoreboard) > limit + 10:
        print("".join([str(i) for i in scoreboard[limit:limit+10]]))
        break
    # add recipes
    s = scoreboard[e1.current_recipe] + scoreboard[e2.current_recipe]
    if s >= 10:
        scoreboard.append( math.floor(s / 10))
    scoreboard.append(s % 10)

    # select new current recipe
    e1 = Employee(current_recipe=(e1.current_recipe + scoreboard[e1.current_recipe] + 1) % len(scoreboard))
    e2 = Employee(current_recipe=(e2.current_recipe + scoreboard[e2.current_recipe] + 1) % len(scoreboard))

    # draw_scoreboard(scoreboard, e1, e2)

