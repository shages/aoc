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

while len(graph.keys()):
    f = first_available()
    for k in graph.keys():
        try:
            graph[k].remove(f)
        except KeyError as e:
            pass
    graph.pop(f, None)
    print(f, end='')

