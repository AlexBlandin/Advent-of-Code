from collections import defaultdict
from pathlib import Path

from parse import parse

lines = Path("day16.txt").read_text().splitlines()
A, B = {}, defaultdict(lambda: defaultdict(set))

for line in lines:
  if p := parse("Sue {:d}: {}: {:d}, {}: {:d}, {}: {:d}", line):
    i, t0, v0, t1, v1, t2, v2 = p.fixed  # type: ignore
    A[i] = {t0: v0, t1: v1, t2: v2}
    for t, v in A[i].items():
      B[t][v].add(i)

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
  "perfumes": 1,
}
outdated = {"cats", "trees", "pomeranians", "goldfish"}
comp = {"cats": +1, "trees": +1, "pomeranians": -1, "goldfish": -1, **{k: 0 for k in mfcsam if k not in outdated}}


def comparator(a, b):
  return -1 if a < b else 1 if a > b else 0


S = {i: sum(1 for t, v in mfcsam.items() if i in B[t][v]) for i in range(1, 501)}
U = {i: sum(1 for t, v in mfcsam.items() if i in B[t][v] and comparator(A[i][t], v) == comp[t]) for i in range(1, 501)}
g = max(S, key=S.get)  # type: ignore
r = max(U, key=U.get)  # type: ignore
print(g, r)
