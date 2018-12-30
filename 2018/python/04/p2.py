import re
from datetime import datetime

with open('input') as f:
    inp = f.read()

r = re.compile(r"\[([^\]]+)\]\s*(.*)$")
entries = []
for line in inp.splitlines():
    m = r.match(line)
    if not m:
        raise RuntimeException('uh oh')
    tstamp = m.group(1)
    rest = m.group(2)
    t = datetime.strptime(tstamp, "%Y-%m-%d %H:%M")
    entries.append((t, rest))

class Sleep:
    def __init__(self, gid, start, end):
        self.gid = gid
        self.start = start
        self.end = end
    
    def duration(self):
        return self.end - self.start

re_start = re.compile(r"Guard #(\d+) begins shift")
sleeps = []
for time, rest in sorted(entries, key=lambda x: x[0]):
    print(time)
    if rest.startswith("Guard"):
        m = re_start.match(rest)
        if not m:
            raise RuntimeError('guard crapped')
        gid = m.group(1)
    elif rest.startswith("falls asleep"):
        s = Sleep(gid, time.minute, None)
    elif rest.endswith("wakes up"):
        s.end = time.minute
        sleeps.append(s)

guards = {}
for s in sleeps:
    if s.gid not in guards:
        guards[s.gid] = 0
    guards[s.gid] += s.duration()

ordered = sorted(guards.items(), key=lambda v: v[1], reverse=True)
def minute_most_asleep(gid, sleeps):
    """Return tuple of minute most asleep and how many times asleep."""
    sleeps_gid = (s for s in sleeps if s.gid == gid)
    minutes = [0 for i in range(60)]
    for s in sleeps_gid:
        for i in range(s.start, s.end):
            minutes[i] += 1
    return sorted(enumerate(minutes), key=lambda v: v[1], reverse=True)[0]

most = []
for gid in guards.keys():
    most.append([*minute_most_asleep(gid, sleeps), int(gid)])

mmost = sorted(most, key=lambda v: v[1], reverse=True)[0]
print(mmost[2] * mmost[0])

