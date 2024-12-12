from enum import Enum, auto
from itertools import groupby
from operator import itemgetter
from pathlib import Path

type XY = tuple[int, int]
lines = Path("day6.txt").read_text().splitlines()
_lines = """
....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...
""".strip().splitlines()
width, height = len(lines[0]), len(lines)


class Facing(Enum):
  N = auto()
  S = auto()
  E = auto()
  W = auto()

  def rotate(self) -> "Facing":
    match self:
      case Facing.N:
        return Facing.W
      case Facing.W:
        return Facing.S
      case Facing.S:
        return Facing.E
      case Facing.E:
        return Facing.N

  def __repr__(self) -> str:
    return self.name


walls: set[XY] = {(x, y) for x, row in enumerate(lines) for y, c in enumerate(row) if c == "#"}


def walk(position: XY, walls: set[XY] = walls, width: int = width, height: int = height) -> set[XY] | None:
  visited, touched = {position}, set()
  facing = Facing.N
  x, y = position
  cycle = False
  while 0 <= x < width and 0 <= y < height:
    match facing:
      case Facing.N:
        position = x - 1, y
      case Facing.S:
        position = x + 1, y
      case Facing.E:
        position = x, y - 1
      case Facing.W:
        position = x, y + 1
    if position in walls:
      touch = (position, facing)
      if touch in touched:
        cycle = True
        break
      touched.add(touch)
      facing = facing.rotate()
    else:
      x, y = position
      visited.add(position)
  return None if cycle else visited


starting_position = next((x, y) for x, row in enumerate(lines) for y, c in enumerate(row) if c == "^")
free_space = {(x, y) for x, row in enumerate(lines) for y, c in enumerate(row) if c == "."}
print(
  len(walk(starting_position)) - 1,  # touching 147 / 771 walls
  sum(1 for candidate in free_space if walk(starting_position, walls | {candidate}) is None),
)

# this is the start of a better solution... but I'm hungry, so dinner first
walls_in_row = {int(k): list(v) for k, v in groupby(sorted(walls), key=itemgetter(0))}
walls_in_col = {int(k): list(v) for k, v in groupby(sorted(walls, key=itemgetter(1, 0)), key=itemgetter(1))}

for wx, wy in walls:
  for x, y, facing in (wx + 1, wy, Facing.N), (wx - 1, wy, Facing.S), (wx, wy + 1, Facing.E), (wx, wy - 1, Facing.W):
    if 0 <= x < width and 0 <= y < height:
      facing.rotate()
