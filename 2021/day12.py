from collections import defaultdict
from pathlib import Path

lines = [tuple(line.split("-")) for line in Path("day12.txt").read_text().splitlines()]
C = defaultdict(set)
small = set()
for a, b in lines:
  C[a].add(b)
  C[b].add(a)
  small |= {c for c in (a, b) if c == c.lower()}


def search(n, v=None, c=C):
  if v is None:
    v = set()
  if n == "end":
    return 1
  if n not in v:
    if n in small:
      v = v | {n}
    return sum(search(m, v) for m in c[n])
  return 0


def research(n, v=None, t=None, a=None, c=C):
  if a is None:
    a = []
  if v is None:
    v = set()
  if n == "end":
    return {tuple([*a, "end"])}
  if n not in v:
    if n in small:
      v = v | {n}
    return {r for m in c[n] for r in research(m, v, t, [*a, n]) if r}
  elif t is None and n != "start":
    return {r for m in c[n] for r in research(m, v, n, [*a, n]) if r}
  return set()


print(search("start"), len(research("start")))
