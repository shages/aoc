import re

def main():
    with open("input") as f:
        inp = f.read()

    lines = inp.splitlines()

    inc = 0
    for prev, cur in zip(
        zip(lines, lines[1:], lines[2:]),
        zip(lines[1:], lines[2:], lines[3:]),
    ):
        psum = sum([int(x) for x in prev])
        csum = sum([int(x) for x in cur])
        print(f"{psum}, {csum}", end=" ")
        if csum > psum:
            print("yes")
            inc += 1
        else:
            print("no")
    print(inc)

if __name__ == "__main__":
    main()

