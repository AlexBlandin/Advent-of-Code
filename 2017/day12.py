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

for p, bs in pipes.items(): # bs.update loop handles feed-forward/backward, one pass needed!
  for b in bs: # do this first, because that makes these updates way smaller, so way faster!
    pipes[b].update(bs)
  bs.update(*[pipes[b] for b in bs]) # set.update accepts multiple sets to union over!

groups = [inverse.update(bs) for p, bs in pipes.items() if p not in inverse]
print(len(pipes[0]), len(groups))
