from collections import defaultdict
from pathlib import Path

lines = Path("day12.txt").read_text().replace(",", "").splitlines()
pipes: defaultdict[int, set[int]] = defaultdict(set)
for p in lines:
  match p.split():
    case [a, "<->", *bs]:
      bs = list(map(int, bs+[a]))
      pipes[int(a)].update(bs)
      for b in bs:
        pipes[b].update(bs)

for p in pipes:
  for b in list(pipes[p]):
    pipes[p].update(pipes[b])
    pipes[b].update(pipes[p])

inverse, groups = {}, 0
for p in pipes:
  if p not in inverse:
    groups += 1
    for b in pipes[p]:
      inverse[b] = p

print(len(pipes[0]), groups)
