
with open("input") as f:
    inp = f.read().rstrip()

my_polymer = ''
for char in inp:
    opp = char.upper() if char.islower() else char.lower()
    if len(my_polymer) and my_polymer[-1] == opp:
        my_polymer = my_polymer[:-1]
        continue
    my_polymer += char
print(len(my_polymer))
