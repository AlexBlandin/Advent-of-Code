from itertools import pairwise
from pathlib import Path
from typing import NamedTuple
from enum import Enum

class XY(NamedTuple):
  """XY(x,y) with easy combination or difference"""
  x: int
  y: int
  
  def __add__(self, other: "XY"):
    return XY(self.x + other.x, self.y + other.y)
  
  def __sub__(self, other: "XY"):
    return XY(self.x - other.x, self.y - other.y)
  
  def __mul__(self, n: int):
    return XY(self.x * n, self.y * n)
  
  def __rshift__(self, target: "XY"):
    delta = target - self
    if delta in adjacent:
      return self
    for point in (c.value for c in Coord.cardinals()):
      if delta == point * 2:
        return self + point
    for point in (c.value for c in Coord.diagonals()):
      if delta - point in adjacent:
        return self + point
    return self

class Coord(Enum):
  """
  The relative cardinal coordinates:
  ```
     W       U       N
     L       C       R
     S       D       E
  ```
  """
  W = XY(-1, -1)
  U = XY(0, -1)
  N = XY(1, -1)
  L = XY(-1, 0)
  C = XY(0, 0)
  R = XY(1, 0)
  S = XY(-1, 1)
  D = XY(0, 1)
  E = XY(1, 1)
  
  @classmethod
  def cardinals(cls):
    return Coord.U, Coord.D, Coord.L, Coord.R
  
  @classmethod
  def diagonals(cls):
    return Coord.W, Coord.N, Coord.S, Coord.E

adjacent = {c.value: c for c in Coord}

moves = [(Coord[d], int(n)) for d, n, *_ in map(str.split, Path("day9.txt").read_text().splitlines())]

def step(move: Coord, knots: list[XY], seen: set[XY]):
  knots[0] = knots[0] + move.value
  for i, (head, node) in enumerate(pairwise(knots), 1):
    if head - node in adjacent:
      break
    knots[i] = node >> head
  seen.add(knots[-1])

def process(moves: list[tuple[Coord, int]], knot_count: int):
  knots = [XY(0, 0)] * knot_count
  seen = {XY(0, 0)}
  for move, n in moves:
    for _ in range(n):
      step(move, knots, seen)
  return len(seen)

print(process(moves, 2), process(moves, 10))
