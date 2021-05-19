from itertools import product

D, H = set(), set() # our sets of tuples representing "on" points
with open("data/day17.txt") as o:
  for x, line in enumerate(o):
    for y, v in enumerate(line.strip()):
      if v == "#":
        D.add((x,y,0))
        H.add((x,y,0,0))

def neighbours3d(p):
  x,y,z = p
  return [(x+dx,y+dy,z+dz) for dx,dy,dz in product((0,-1,1), (0,-1,1), (0,-1,1))][1:] # we don't return p
def neighbours4d(p):
  x,y,z,w = p
  return [(x+dx,y+dy,z+dz,w+dw) for dx,dy,dz,dw in product((0,-1,1), (0,-1,1), (0,-1,1), (0,-1,1))][1:]

timesteps = 6
for t in range(timesteps):
  d, h = {}, {} # all adjacencies points from D|H, and the value is the number of adjacencies
  for p in D:
    for n in neighbours3d(p):
      d[n] = d.get(n, 0)+1
  for p in H:
    for n in neighbours4d(p):
      h[n] = h.get(n, 0)+1
  D = {p for p, v in d.items() if v==3 or (p in D and v==2)} # filter to only the "on" points
  H = {p for p, v in h.items() if v==3 or (p in H and v==2)}

print(len(D), len(H)) # and we're done!
