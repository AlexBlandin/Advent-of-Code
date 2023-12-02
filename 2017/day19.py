from functools import cache
from pathlib import Path
from typing import NamedTuple, Self
from string import ascii_uppercase

TILES = ascii_uppercase + "-|+ "
encode, decode = cache(TILES.index), TILES.__getitem__
GRID = [[encode(c) for c in row] for row in Path("day19.txt").read_text().splitlines()]
GRID = [
  [encode(c) for c in row]
  for row in """     |
     |  +--+
     A  |  C
 F---|----E|--+
     |  |  |  D
     +B-+  +--+
""".splitlines()
]
WIDTH, HEIGHT = len(GRID[0]), len(GRID)
SEEN: list[str] = []


@cache
def iscupdn(x: int):
  return x == encode("-")


@cache
def iscleri(x: int):
  return x == encode("|")


@cache
def isccnct(x: int):
  return x == encode("+")


@cache
def isapipe(x: int):
  return x == encode("-") or x == encode("+")


@cache
def islettr(x: int):
  return x in range(len(ascii_uppercase))


@cache
def isatile(x: int):
  return x in range(len(ascii_uppercase), len(TILES))


@cache
def notblank(x: int):
  return x in range(len(TILES) - 1)


@cache
def switchpipe(x: int):
  return encode("|") if x == encode("-") else encode("-")


class Point(NamedTuple):
  """
  A given point on the 2D taxicab `GRID`
  """

  x: int = 0
  y: int = 0

  @property
  def c(self):
    return GRID[self.y][self.x]

  @property
  def norm(self):
    assert not (self.x != 0 and self.y != 0)
    return Point(1 if self.x > 0 else -1 if self.x < 0 else 0, 1 if self.y > 0 else -1 if self.y < 0 else 0)

  def __call__(self):
    return Cardinal.neighbours(self)

  def __add__(self, other: Self):
    return Point(self.x + other.x, self.y + other.y)

  def __sub__(self, other: Self):
    return Point(self.x - other.x, self.y - other.y)

  def __abs__(self):
    return abs(self.x + self.y)

  def __truediv__(self, other: Self):  # distance
    return abs(self.x - other.x) + abs(self.y + other.y)

  def neighbours(self):
    return {k: p for k, p in self()._asdict().items() if 0 <= p.x < WIDTH and 0 <= p.y < HEIGHT and notblank(p.c)}


class Cardinal(NamedTuple):
  """
  The cardinal directions from a point (default `Point(0, 0)`),
  including "+1" points so we can see past pipes that overlap
  (as there are no `||` we need to worry about, only `|-|`, etc.)
  """

  up: Point = Point(0, -1)
  down: Point = Point(0, 1)
  left: Point = Point(-1, 0)
  right: Point = Point(1, 0)
  # upp: Point = Point(0, -2) # 1 extra to peek ahead of overlaps
  # downp: Point = Point(0, 2)
  # leftp: Point = Point(-2, 0)
  # rightp: Point = Point(2, 0)

  @staticmethod
  def neighbours(p: Point):
    c = Cardinal()
    return Cardinal(p + c[0], p + c[1], p + c[2], p + c[3])  # , p + c[4], p + c[5], p + c[6], p + c[7])


@cache
def pipefrom(p: Point):
  return encode("-") if p in {Point(1, 0), Point(-1, 0)} else encode("|")


start = Point(GRID[0].index(encode("|")))
curr, prev = start + Cardinal().down, start

while len(
  neighbours := [p for p in curr() if 0 <= p.x < WIDTH and 0 <= p.y < HEIGHT and p != prev and notblank(p.c)]
):  # there's maybe legal moves to make, we'll have breaks regardless
  print(curr, decode(curr.c), prev, decode(prev.c))
  if isccnct(curr.c):
    # 1. "turn", we are on a connector and so deciding which is next should be unambiguous, there should only be one not-prev direction that connects
    if len(neighbours) == 1:
      curr, prev = neighbours[0], curr
    else:
      print("ln113", curr, decode(curr.c), prev, decode(prev.c), [(n, decode(n.c)) for n in neighbours])
      break
  else:
    # 2. "forward", we are continuing along a pipe in the same direction (the next section can be the same as curr/prev, a letter, or connector)
    # 3. "overlap", we are going to continue in the same direction
    # (sometimes curr is a letter, which we treat as equal to prev if prev is a - or |, print if not so I fix)
    # however the next is the wrong direction, so peek one ahead to get the next section (the prev or +),
    # from what I gather there is no connector that does this so we only have to worry about this case when curr is a letter or -/|
    # but we'll print and halt if there's something unusal so that we can fix anything
    if islettr(curr.c):
      SEEN.append(decode(curr.c))
    direction = (curr - prev).norm  # our current direction, normalised in case we skipped a bunch
    nextpoint = curr + direction
    frompipe = curr.c if isapipe(curr.c) else prev.c if isapipe(prev.c) else pipefrom(direction)
    otherpipe = switchpipe(frompipe)
    if nextpoint.c == otherpipe:  # overlap, I think we handle it with just this
      nextpoint += direction
    curr, prev = nextpoint, prev if islettr(curr.c) else curr
  """
  ensure:
  - we don't loop back to prev
  - we don't move from a - to a | and vice versa
  - any + has only two neighbours, including prev
  """

  pass
print(
  "".join(SEEN),
)
