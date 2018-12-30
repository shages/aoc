
with open("input") as f:
    inp = f.read().rstrip()

def reduce(polymer):
    my_polymer = ''
    for char in polymer:
        opp = char.upper() if char.islower() else char.lower()
        if len(my_polymer) and my_polymer[-1] == opp:
            my_polymer = my_polymer[:-1]
            continue
        my_polymer += char
    return my_polymer

def polymer_without_char(polymer, char):
    return (p for p in polymer if p != char and p != char.upper())

lens = [len(reduce(polymer_without_char(inp, c))) for c in 'abcdefghijklmnopqrstuvwxyz']
print(min(lens))
