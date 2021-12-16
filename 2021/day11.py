from itertools import count
from pathlib import Path
grid = [list(map(int, line)) for line in Path("data/day11.txt").read_text().splitlines()]

def neighbours(x,y): return [(x+xo,y+yo) for xo in (1,-1,0) for yo in (1,-1,0) if (xo,yo)!=(0,0) and x+xo in range(10) and y+yo in range(10)]
sfilter = lambda f, starlist: filter(lambda s: f(*s), starlist)
turns, flashes, syncs = 100, 0, 0
coords = lambda: [(x,y) for x in range(10) for y in range(10)]
for i in count(1):
  flashed = [[False for _ in range(10)] for _ in range(10)]
  for x,y in coords():
    grid[x][y] += 1
  while f := list(sfilter(lambda x, y: grid[x][y]>9 and not flashed[x][y], coords())):
    for x,y in f:
      flashed[x][y] = True
      for nx,ny in neighbours(x,y):
        if not flashed[nx][ny]:
          grid[nx][ny] += 1
  have_flashed = sum(map(sum, flashed))
  if i <= 100: flashes += have_flashed
  if have_flashed == 100:
    syncs = i
    break
  for x,y in coords():
    if flashed[x][y]:
      grid[x][y] = 0

print(flashes, syncs)
