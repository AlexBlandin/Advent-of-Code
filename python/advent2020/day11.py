from copy import deepcopy
from functools import lru_cache
from pathlib import Path

m = [[None if c == "." else False for c in line.strip()] for line in Path("day11.txt").read_text().splitlines()]
mx, my = len(m[0]), len(m)


@lru_cache(maxsize=mx * my)
def neighbouring(x, y):
  return [
    (x + i, y + j)
    for i, j in [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    if 0 <= x + i < mx and 0 <= y + j < my
  ]


def neighbours(x, y):
  return [p[yj][xi] for xi, yj in neighbouring(x, y)]


@lru_cache(maxsize=mx * my)
def firsts_from(x, y):
  return [
    t
    for t in [
      next(g, None)
      for g in [
        ((xi, y) for xi in range(x + 1, mx) if p[y][xi] is not None),
        ((xi, y) for xi in reversed(range(x)) if p[y][xi] is not None),
        ((x, yj) for yj in range(y + 1, my) if p[yj][x] is not None),
        ((x, yj) for yj in reversed(range(y)) if p[yj][x] is not None),
        ((xi, yi) for xi, yi in zip(range(x + 1, mx), range(y + 1, my), strict=False) if p[yi][xi] is not None),
        ((xi, yi) for xi, yi in zip(reversed(range(x)), reversed(range(y)), strict=False) if p[yi][xi] is not None),
        ((xi, yi) for xi, yi in zip(range(x + 1, mx), reversed(range(y)), strict=False) if p[yi][xi] is not None),
        ((xi, yi) for xi, yi in zip(reversed(range(x)), range(y + 1, my), strict=False) if p[yi][xi] is not None),
      ]
    ]
    if t is not None
  ]


def sees(x, y):
  return [p[yi][xi] for xi, yi in firsts_from(x, y)]


P, p = deepcopy(m), [[]]
while m != p:
  p = deepcopy(m)
  for y, row in enumerate(m):
    for x, s in enumerate(row):
      if s is False and neighbours(x, y).count(True) == 0:
        m[y][x] = True
      elif s and neighbours(x, y).count(True) >= 4:
        m[y][x] = False
m, P, p = P, m, [[]]
while m != p:
  p = deepcopy(m)
  for y, row in enumerate(m):
    for x, s in enumerate(row):
      if s is False and sees(x, y).count(True) == 0:
        m[y][x] = True
      elif s and sees(x, y).count(True) >= 5:
        m[y][x] = False
print(sum(line.count(True) for line in P), sum(line.count(True) for line in m))
