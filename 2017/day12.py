from collections import defaultdict
from pathlib import Path

lines = Path("day12.txt").read_text().splitlines()
pipes: defaultdict[int, set[int]] = defaultdict(set)
for p in lines:
  match p.split():
    case [a, "<->", *bs]:
      a = int(a)
      bs = list(map(int, "".join(bs).split(",")))
      bs.append(a)
      pipes[a].update(bs)
      for b in bs:
        pipes[b].update(bs)

s = -1
while s != sum(map(len, pipes.values())):
  s = sum(map(len, pipes.values()))
  for p in pipes:
    for b in list(pipes[p]):
      pipes[p].update(pipes[b])
      pipes[b].update(pipes[p])

inverse = {}
groups = 0
for p in pipes:
  if p not in inverse:
    groups += 1
    inverse[p] = p
    for b in pipes[p]:
      inverse[b] = p

print(len(pipes[0]), groups)
