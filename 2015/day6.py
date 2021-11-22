from itertools import product
from parse import parse
with open("data/day6.txt") as o:
  lines = [line.strip() for line in o.readlines()]

bon, boff, bnot = lambda x: True, lambda x: False, lambda x: not x
don, doff, dnot = lambda x: x+1, lambda x: max(0,x-1), lambda x: x+2
bgrid = [[False for _ in range(1000)] for __ in range(1000)]
dgrid = [[0 for _ in range(1000)] for __ in range(1000)]
for line in lines:
  offset = 0
  bop, dop = boff, doff
  if line[6]=="n": # turn on
    offset = 7
    bop, dop = bon, don
  elif line[6]=="f": # turn off
    offset = 8
    bop, dop = boff, doff
  elif line[6]==" ": # toggle
    offset = 6
    bop, dop = bnot, dnot
  a,b,c,d = parse("{:d},{:d} through {:d},{:d}", line[offset:]).fixed
  for x,y in product(range(a,c+1),range(b,d+1)):
    bgrid[x][y] = bop(bgrid[x][y])
    dgrid[x][y] = dop(dgrid[x][y])

print(sum(map(sum,bgrid)),sum(map(sum,dgrid)))
