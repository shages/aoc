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

def redo_match(scoreboard, i, nums):
    match = 0
    for j, x in enumerate(range(i, len(scoreboard))):
        if scoreboard[x] == nums[j]:
            match += 1
        else:
            break
    return match


scoreboard = [3, 7]
i = 0
nums = [1,1,0,2,0,1]
# nums = [5,9,4,1,4]
match_i = 2
match = 0
while True:
    # print(f"match={match}")
    # print(f"match_i={match_i}")
    i += 1
    # add recipes
    s = scoreboard[e1.current_recipe] + scoreboard[e2.current_recipe]
    if s >= 10:
        s1 = math.floor(s / 10)
        scoreboard.append(s1)
        if nums[match] == s1:
            match += 1
        else:
            while match_i <= len(scoreboard):
                match_i += 1
                match = redo_match(scoreboard, match_i, nums)
                if match == len(scoreboard) - match_i:
                    break
#            if match > 1:
#                print(f"new match={match}")
#                print(scoreboard[-len(nums):])
        if match == len(nums):
            print(f"completed after {len(scoreboard) - len(nums)} recipes")
            break
    s2 = s % 10
    scoreboard.append(s2)
    if nums[match] == s2:
        match += 1
    else:
        while match_i <= len(scoreboard):
            match_i += 1
            match = redo_match(scoreboard, match_i, nums)
            if match == len(scoreboard) - match_i:
                break
#        if match > 2:
#            print(f"new match={match}")
#            print(scoreboard[-len(nums):])
    if match == len(nums):
        print(f"completed after {len(scoreboard) - len(nums)} recipes")
        break

    # select new current recipe
    e1 = Employee(current_recipe=(e1.current_recipe + scoreboard[e1.current_recipe] + 1) % len(scoreboard))
    e2 = Employee(current_recipe=(e2.current_recipe + scoreboard[e2.current_recipe] + 1) % len(scoreboard))

