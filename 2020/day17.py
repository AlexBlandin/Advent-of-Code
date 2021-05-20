from itertools import product

D, H = set(), set() # our sets of tuples representing "on" points
with open("data/day17.txt") as o:
  for x, line in enumerate(o):
    for y, v in enumerate(line.strip()):
      if v == "#":
        D.add((x,y,0))
        H.add((x,y,0,0))

def neighbours(p, dim):
  return [tuple(a+b for a,b in zip(p,c)) for c in product((0,-1,1), repeat=dim)][1:]

timesteps = 6
for t in range(timesteps):
  d, h = {}, {} # all adjacenct points from D|H, and the value is the number it's adjacent to
  for p in D:
    for n in neighbours(p, 3):
      d[n] = d.get(n, 0)+1
  for p in H:
    for n in neighbours(p, 4):
      h[n] = h.get(n, 0)+1
  D = {p for p, v in d.items() if v==3 or (p in D and v==2)} # filter to only the "on" points
  H = {p for p, v in h.items() if v==3 or (p in H and v==2)}

print(len(D), len(H)) # and we're done!
