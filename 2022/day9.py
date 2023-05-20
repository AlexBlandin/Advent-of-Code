from pathlib import Path
from typing import NamedTuple
from enum import IntEnum, auto

class Direction(IntEnum):
  """
  The WUNREDSLC enum, where:
  ```
     W       U       N
     L       C       R
     S       D       E
  ```
  is:
  ```
  (-1,-1) ( 0,-1) ( 1,-1)
  (-1, 0) ( 0, 0) ( 1, 0)
  (-1, 1) ( 0, 1) ( 1, 1)
  ```
  """
  W, U, N, R, E, D, S, L, C = [auto()] * 9

moves = [(Direction[d], int(n)) for d, n in map(str.split, Path("day9.txt").read_text().splitlines())]
moves = [(Direction[d], int(n)) for d, n in zip("RULDRDLR", [4, 4, 3, 1, 4, 1, 5, 2])]

# I think I'm just going to make it follow the rules, starting from the head and moving with substeps until everything is in place




"""what I previously did is below, probably best ignoring it"""
exit()

class Point(NamedTuple):
  """Point(x,y) with easy combination or difference"""
  x: int
  y: int
  
  def __add__(self, other):
    return Point(self.x + other.x, self.y + other.y)
  
  def __sub__(self, other):
    return Point(self.x - other.x, self.y - other.y)

DirectionVec = {
  Direction.W: Point(-1, -1),
  Direction.U: Point(0, -1),
  Direction.N: Point(1, -1),
  Direction.R: Point(1, 0),
  Direction.E: Point(1, 1),
  Direction.D: Point(0, 1),
  Direction.S: Point(-1, 1),
  Direction.L: Point(-1, 0),
  Direction.C: Point(0, 0)
}

# may need not only to have the wider board, but also to consider diagonals
# so I'll use NSEW at a quarter turn to the cardinal UDLR
# being reasonable, it should go around like WUNREDSLI (I for Identity)
# though that'll mean switching the LUT below

# (-2,-2) (-1,-2) ( 0,-2) ( 1,-2) ( 2,-2)
# (-2,-1) (-1,-1) ( 0,-1) ( 1,-1) ( 2,-1)
# (-2, 0) (-1, 0) ( 0, 0) ( 1, 0) ( 2, 0)
# (-2, 1) (-1, 1) ( 0, 1) ( 1, 1) ( 2, 1)
# (-2, 2) (-1, 2) ( 0, 2) ( 1, 2) ( 2, 2)

# step[H - T][d: WUNREDSLI] = T', d' # relative (x,y) space around H
step = {
  Point(-1, -1): {
    Direction.U: (Point(-1, 0), Direction.C),
    Direction.D: (Point(0, -1), Direction.R),
    Direction.L: (Point(0, -1), Direction.U),
    Direction.R: (Point(-1, 0), Direction.D),
    Direction.C: (Point(-1, -1), Direction.C)
  },
  Point(0, -1): {
    Direction.U: (Point(0, 0), Direction.C),
    Direction.D: (Point(0, -1), Direction.D),
    Direction.L: (Point(1, -1), Direction.C),
    Direction.R: (Point(-1, -1), Direction.C),
    Direction.C: (Point(0, -1), Direction.C)
  },
  Point(1, -1): {
    Direction.U: (Point(1, 0), Direction.C),
    Direction.D: (Point(0, -1), Direction.L),
    Direction.L: (Point(1, 0), Direction.D),
    Direction.R: (Point(0, -1), Direction.C),
    Direction.C: (Point(1, -1), Direction.C)
  },
  Point(-1, 0): {
    Direction.U: (Point(-1, 1), Direction.C),
    Direction.D: (Point(-1, -1), Direction.C),
    Direction.L: (Point(0, 0), Direction.C),
    Direction.R: (Point(-1, 0), Direction.R),
    Direction.C: (Point(-1, 0), Direction.C)
  },
  Point(0, 0): {
    Direction.U: (Point(0, 1), Direction.C),
    Direction.D: (Point(0, -1), Direction.C),
    Direction.L: (Point(1, 0), Direction.C),
    Direction.R: (Point(-1, 0), Direction.C),
    Direction.C: (Point(0, 0), Direction.C)
  },
  Point(1, 0): {
    Direction.U: (Point(1, 1), Direction.C),
    Direction.D: (Point(1, -1), Direction.C),
    Direction.L: (Point(1, 0), Direction.L),
    Direction.R: (Point(0, 0), Direction.C),
    Direction.C: (Point(1, 0), Direction.C)
  },
  Point(-1, 1): {
    Direction.U: (Point(0, 1), Direction.R),
    Direction.D: (Point(-1, 0), Direction.C),
    Direction.L: (Point(0, 1), Direction.C),
    Direction.R: (Point(-1, 0), Direction.U),
    Direction.C: (Point(-1, 1), Direction.C)
  },
  Point(0, 1): {
    Direction.U: (Point(0, 1), Direction.U),
    Direction.D: (Point(0, 0), Direction.C),
    Direction.L: (Point(1, 1), Direction.C),
    Direction.R: (Point(-1, 1), Direction.C),
    Direction.C: (Point(0, 1), Direction.C)
  },
  Point(1, 1): {
    Direction.U: (Point(0, 1), Direction.L),
    Direction.D: (Point(1, 0), Direction.C),
    Direction.L: (Point(1, 0), Direction.U),
    Direction.R: (Point(0, 1), Direction.C),
    Direction.C: (Point(1, 1), Direction.C)
  },
}

knots = [Point(0, 0) for _ in range(10)]
v1, v9 = {knots[1]}, {knots[9]}
for j, (d, n) in enumerate(moves): # moves contains the initial d
  hd = d
  for _ in range(n):
    for i, H, T in zip(range(1, len(knots)), knots[:], knots[1:]): # copy so don't need to go backwards
      knots[i], d = step[H - T][d] # the issue is everything moves in d, which is wrong
      if i == 1:
        v1.add(knots[i])
      if i == 9:
        v9.add(knots[i])
    dv = DirectionVec[hd]
    knots[0] = Point(knots[0].x + dv.x, knots[0].y + dv.y)

print(len(v1), len(v9))
