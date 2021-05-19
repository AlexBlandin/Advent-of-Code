from itertools import product

D = set() # our set of tuples representing "on" points, we convert from dict to set as a dunder copy
with open("data/day17.txt") as o:
  for x, line in enumerate(o):
    for y, v in enumerate(line.strip()):
      if v == "#": D.add((x,y,0))

def neighbours(p):
  x,y,z = p
  return [(x+dx,y+dy,z+dz) for dx,dy,dz in product((-1,0,1), (-1,0,1), (-1,0,1)) if (dx,dy,dz)!=(0,0,0)]

timesteps = 6
for t in timesteps:
  d = {} # our partial dict, we handle off points as adjacencies to points from D (so v>0), and the value is the number of adjacencies (active and v!=2|3 -> inactive, inactive and v==3 -> active)
  for p in D:
    for n in neighbours(p):
      d.setdefault(n, 0) += 1
  D = {p for p:v in d if v==3 or (p in D and v==2)}

print(len(D))