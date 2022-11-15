from collections import defaultdict
from pathlib import Path

from day10 import knot_a_hash

key = list(Path("day14.txt").read_bytes().strip())
lengths = [key + [ord("-")] + list(f"{i}".encode("utf8")) + [17, 31, 73, 47, 23] for i in range(128)]
rows = [int(knot_a_hash(lengths[i]), 16) for i in range(128)]
srow = [list(map(bool, map(int, f"{rows[i]:0128b}"))) for i in range(128)]

def group():
  invers, groups = {}, defaultdict(set)
  for x, y in ((x, y) for x in range(128) for y in range(128)):
    if srow[y][x]:
      nbs = [(x, y) for x, y in ((x, y), (x, y - 1), (x - 1, y), (x, y + 1), (x + 1, y))
             if -1 < x < 128 and -1 < y < 128 and srow[y][x]]
      gps = [invers[nb] for nb in nbs if nb in invers] # groups in your area
      if len(gps) == 0: # we create our own group! with...
        vers = (x, y)
      elif len(gps) == 1: # we join their group, and bring our buddies
        vers = gps[0]
      else: # there's competition, we need to pick a side; I vote the big one!
        vers = max(gps, key = lambda g: len(groups[g]))
        for gp in gps:
          if gp != vers:
            for nb in groups[gp]:
              invers[nb] = vers
            groups[vers].update(groups[gp])
            del groups[gp]
      for nb in nbs:
        invers[nb] = vers
      groups[vers].update(nbs)
  
  return groups

print(sum(map(int.bit_count, rows)), len(group()))
