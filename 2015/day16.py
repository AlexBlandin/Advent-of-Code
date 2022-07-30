from collections import defaultdict
from pathlib import Path
from parse import parse

lines = Path("data/day16.txt").read_text().splitlines()
H, I = {}, defaultdict(lambda: defaultdict(set))

for line in lines:
  if p := parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", line):
    i, t0, v0, t1, v1, t2, v2 = p.fixed
    H[i] = {t0: v0, t1: v1, t2: v2}
    for t, v in H[i].items():
      I[t][v].add(i)

mfcsam = {
  "children": 3,
  "cats": 7,
  "samoyeds": 2,
  "pomeranians": 3,
  "akitas": 0,
  "vizslas": 0,
  "goldfish": 5,
  "trees": 3,
  "cars": 2,
  "perfumes": 1
}
outdated = {"cats", "trees", "pomeranians", "goldfish"}
comp = {"cats": +1, "trees": +1, "pomeranians": -1, "goldfish": -1, **{k: 0 for k in mfcsam if k not in outdated}}
comparator = lambda a, b: -1 if a < b else 1 if a > b else 0

S = {i: sum(1 for t, v in mfcsam.items() if i in I[t][v]) for i in range(1, 501)}
U = {i: sum(1 for t, v in mfcsam.items() if i in I[t][v] and comparator(H[i][t], v) == comp[t]) for i in range(1, 501)}
g = max(S, key = S.get)
r = max(U, key = U.get)
print(g, r)
