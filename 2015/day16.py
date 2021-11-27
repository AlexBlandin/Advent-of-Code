from pathlib import Path
lines = Path("data/day16.txt").read_text().splitlines()
from parse import parse
from collections import defaultdict
I = defaultdict(lambda: defaultdict(set))
H = {}
for line in lines:
  if p := parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", line):
    i, t0, v0, t1, v1, t2, v2 = p.fixed
    H[i] = {t0: v0, t1: v1, t2: v2}
    for t, v in H[i].items():
      I[t][v].add(i)

mfcsam = {"children": 3,"cats": 7,"samoyeds": 2,
          "pomeranians": 3,"akitas": 0,"vizslas": 0,
          "goldfish": 5,"trees": 3,"cars": 2,"perfumes": 1}
outdated = {"cats", "trees", "pomeranians", "goldfish"}
nuclear_decay = {"cats", "trees"}
modial_interaction = {"pomeranians", "goldfish"}

def retro_encabulator(i):
  m = sum(1 for t,v in mfcsam.items() if i in I[t][v] and t not in outdated)
  for t in outdated:
    v = mfcsam[t]
    if t in nuclear_decay and t in H[i]:
      if H[i][t]>v: m += 1
    if t in modial_interaction and t in H[i]:
      if H[i][t]<v: m += 1
  return m

S = {i:sum(1 for t,v in mfcsam.items() if i in I[t][v]) for i in set(range(1, 501))}
U = {i:retro_encabulator(i) for i in set(range(1, 501))}
g = max(S, key=S.get)
print("May the real Auntie Sue please stand up?")
r = max(U, key=U.get)
print(g, r)
