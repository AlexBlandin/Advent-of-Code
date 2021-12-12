from math import prod
from pathlib import Path
heightmap = [list(map(int, line)) for line in Path("data/day9.txt").read_text().splitlines()]
side = len(heightmap)
def lowest(xy):
  x,y = xy
  return all(heightmap[x][y]<heightmap[a][b] for a,b in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)] if 0<=a<side and 0<=b<side)
lows = list(filter(lowest, [(x,y) for x in range(side) for y in range(side)]))
risk = len(lows)+sum(heightmap[x][y] for x,y in lows)
inbasin = {} # basin origin -> [coords in it]
a_basin = {} # inverse indices, (x,y) -> basin it's in, acts as "seen" flag
def basin(xy: tuple):
  if xy not in a_basin:
    search = {xy}
    inbasin[xy] = []
    while len(search):
      x,y = search.pop()
      a_basin[(x,y)] = xy
      inbasin[xy].append((x,y))      
      search |= {(a,b) for a,b in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)] if 0<=a<side and 0<=b<side and heightmap[a][b]!=9 and (a,b) not in a_basin}
      for ab in [(a,b) for a,b in [(x+1,y),(x,y+1),(x-1,y),(x,y-1)] if 0<=a<side and 0<=b<side and heightmap[a][b]!=9 and (a,b) in a_basin]:
        if a_basin[ab]!=xy:
          for cd in inbasin[a_basin[ab]]:
            if cd != ab: a_basin[cd] = a_basin[xy]
          inbasin[a_basin[xy]] += inbasin[a_basin[ab]]
          del inbasin[a_basin[ab]]
          a_basin[ab] = a_basin[xy]

for low in lows:
  basin(low)

biggest = prod(sorted(map(len, inbasin.values()), reverse=True)[:3])
print(risk, biggest)
