from pathlib import Path
lines = Path("data/day3.txt").read_text().splitlines()
lines = [[int(c) for c in l] for l in lines]
cols = list(zip(*lines))
def avg(x): return sum(x)/max(len(x),1)
gb = [int(0.5+avg(c)) for c in cols]
eb = [0 if b else 1 for b in gb]
g = int("".join(map(str, gb)), 2)
e = int("".join(map(str, eb)), 2)
ox, co = set(range(len(lines))), set(range(len(lines)))
def at(l, ls): return [l[i] for i in ls]
oxy, co2 = 0, 0
for c in cols:
  if len(ox)==1: oxy = int("".join(map(str, lines[ox.pop()])), 2)
  if len(co)==1: co2 = int("".join(map(str, lines[co.pop()])), 2)
  ao, ac = avg(at(c, ox)), avg(at(c, co))
  if ao==0.5: ox = set(filter(lambda i: c[i], ox))
  else: ox = set(filter(lambda i: c[i]==int(0.5+ao), ox))
  if ac==0.5: co = set(filter(lambda i: not c[i], co))
  else: co = set(filter(lambda i: c[i]!=int(0.5+ac), co))
print(g*e, oxy*co2)