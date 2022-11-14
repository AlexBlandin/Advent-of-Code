from collections import defaultdict
from pathlib import Path

lines = Path("day12.txt").read_text().replace(",", "").replace("<->","").splitlines()
pipes, inverse = defaultdict(set), set()
for ps in lines:
  match list(map(int, ps.split())):
    case [p, *bs] as ps:
      pipes[p].update(ps)
      for b in bs:
        pipes[b].update(ps)

for p, bs in pipes.items():
  bs.update(*[pipes[b].update(bs) or pipes[b] for b in bs])

groups = [inverse.update(bs) for p, bs in pipes.items() if p not in inverse]
print(len(pipes[0]), len(groups))
