from collections import defaultdict
from pathlib import Path
lines = [tuple(line.split("-")) for line in Path("data/day12.txt").read_text().splitlines()]
C = defaultdict(set)
small = set()
for a,b in lines:
  C[a].add(b)
  C[b].add(a)
  small |= {c for c in (a,b) if c==c.lower()}

def search(n, v=set(), C=C):
  if n=="end": return 1
  if n not in v:
    if n in small: v = v|{n}
    return sum(search(m, v) for m in C[n])
  return 0

def research(n, v=set(), t=None, a=[], C=C):
  if n=="end": return {tuple(a+["end"])}
  if n not in v:
    if n in small: v = v|{n}
    return {r for m in C[n] for r in research(m, v, t, a+[n]) if r}
  elif t is None and n != "start":
    return {r for m in C[n] for r in research(m, v, n, a+[n]) if r}
  return set()

print(search("start"), len(research("start")))
