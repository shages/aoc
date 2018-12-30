
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

boxids = [BoxId(boxid) for boxid in inp.splitlines()]
b2 = [b for b in boxids if b.has_two]
b3 = [b for b in boxids if b.has_three]
checksum = len(b2) * len(b3)
print(f"checksum={checksum}")

