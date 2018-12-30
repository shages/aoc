
with open('input') as f:
    inp = f.read()

class BoxId:
    def __init__(self, _id):
        self._id = _id
        self.has_two = False
        self.has_three = False

        d = {}
        for char in _id:
            if char in d:
                d[char] += 1
            else:
                d[char] = 1

        for k, v in d.items():
            if v == 2:
                self.has_two = True
            if v == 3:
                self.has_three = True

    def __hash__(self):
        return hash(self._id)
    
    def __eq__(self, other):
        return self._id == other._id

    def close_to(self, other):
        diffs = 0
        for a, b in zip(self._id, other._id):
            if a != b:
                diffs += 1
            if diffs > 1:
                return False
        return diffs == 1
    
    def __sub__(self, other):
        common = ""
        for a, b in zip(self._id, other._id):
            if a != b:
                continue
            common += a
        return common

# exhaustive
for b1 in [BoxId(boxid) for boxid in inp.splitlines()]:
    for b2 in [BoxId(boxid) for boxid in inp.splitlines()]:
        if b1 == b2:
            continue
        if b1.close_to(b2):
            print(f"common={b1 - b2}")
            break

