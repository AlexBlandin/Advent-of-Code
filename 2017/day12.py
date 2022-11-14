from collections import defaultdict
from pathlib import Path

lines = Path("day12.txt").read_text().replace(",", "").replace("<->","").splitlines()
pipes, inverse = defaultdict(set), set()
for p in lines:
  match list(map(int, p.split())):
    case [a, *bs] as p:
      pipes[a].update(p)
      for b in bs:
        pipes[b].update(p)

for p in pipes: # my pipes[b].update loop handles feed- forward/backward, so only 1 pass is needed
  pipes[p].update(*[pipes[b] for b in pipes[p]]) # set.update accepts multiple sets to union over!
  for b in pipes[p]:
    pipes[b].update(pipes[p])
groups = [inverse.update(bs) for p, bs in pipes.items() if p not in inverse]

print(len(pipes[0]), len(groups))
