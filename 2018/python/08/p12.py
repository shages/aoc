with open("input") as f:
    inp = f.read()

nums = [int(x) for x in inp.split()]
done = False

class Node:
    def __init__(self, parent, nc, nm):
        self.parent = parent 
        self.nc = nc
        self.nm = nm
        self.children = []
        self.metadata = []
    
    def value(self):
        if self.nc == 0:
            return sum(self.metadata)

        children = [self.children[c - 1] for c in self.metadata if c <= len(self.children) and c > 0]
        return sum([c.value() for c in children])
    
    def metadata_sum(self):
        return sum(self.metadata) + sum([c.metadata_sum() for c in self.children])

    def add_node(self, nc, nm):
        node = self.__class__(self, nc, nm)
        self.children.append(node)
        return node

nc, nm = nums[:2]
nums = nums[2:]
root = Node(None, nc, nm)
parent = root
while len(nums):
    if parent is None:
        break
    if len(parent.children) < parent.nc:
        nc, nm = nums[:2]
        node = parent.add_node(nc, nm)
        parent = node
        nums = nums[2:]
    else:
        parent.metadata = nums[:parent.nm]
        nums = nums[parent.nm:]
        parent = parent.parent

print(root.metadata_sum())
print(root.value())

