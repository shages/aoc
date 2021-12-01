import re

def main():
    with open("input") as f:
        inp = f.read()

    lines = inp.splitlines()

    inc = 0
    for prev, cur in zip(lines, lines[1:]):
        print(f"{prev}, {cur}", end=" ")
        if int(cur) > int(prev: 
            print("yes")
            inc += 1
        else:
            print("no")
    print(inc)

if __name__ == "__main__":
    main()

