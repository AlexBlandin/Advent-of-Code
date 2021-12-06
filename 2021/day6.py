from collections import Counter
from functools import reduce
from pathlib import Path
ages = list(map(int,Path("data/day6.txt").read_text().split(",")))
sim = dict(Counter(ages).items())
def dec(sim,_):
  d = {k-1:v for k,v in sim.items()}
  d[8] = d.get(-1,0)
  d[6] = d.get(-1,0) + d.get(6, 0)
  if -1 in d: del d[-1]
  return d
sim = reduce(dec, range(80), sim)
after80days = sum(sim.values())
sim = reduce(dec, range(256-80), sim)
after256days = sum(sim.values())
print(after80days, after256days)
