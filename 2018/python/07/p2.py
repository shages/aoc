import re

with open("input") as f:
    lines = f.read().splitlines()

r = re.compile('Step (\S+) must be finished before step (\S+) can begin')

graph = {}
for line in lines:
    m = r.match(line)
    pred = m.group(1)
    cur = m.group(2)
    if pred not in graph:
        graph[pred] = set([])
    if cur not in graph:
        graph[cur] = set([])
    graph[cur].add(pred)

def available():
    return [k for k, v in graph.items() if len(v) == 0]

def first_available():
    return sorted(available())[0]

chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
def char_to_time(char):
    return chars.index(char) + 1

class Worker:
    def __init__(self):
        self.item = None
        self.time = None

    def start_work(self, item):
        self.item = item
        self.time = 60 + char_to_time(item)

    def has_work(self):
        return self.item is not None

    def work(self):
        self.time -= 1
    
    def done(self):
        return self.time <= 0

    def finish(self):
        self.time = None
        self.item = None

workers = [Worker() for i in range(5)]

def work_available():
    return len([w for w in workers if w.has_work()])

t = 0
while len(graph.keys()) or work_available():
    for w in workers:
        if w.item is None:
            # can work
            try:
                f = first_available()
            except IndexError:
                # nothing to do
                break 
            w.start_work(f)
            print(f"[t={t}] Starting item={f} for {w.time} seconds")
            graph.pop(f, None)

    for w in workers:
        if not w.has_work():
            continue
        w.work()
        if w.done():
            f = w.item
            print(f"[t={t}] Completed item={f}")
            w.finish()
            for k in graph.keys():
                try:
                    graph[k].remove(f)
                except KeyError as e:
                    pass
    t += 1
print(t)


