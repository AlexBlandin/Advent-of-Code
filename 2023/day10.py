from enum import Enum
from itertools import combinations
from pathlib import Path

grid = Path("day10.txt").read_text().splitlines()
S = None
for y, row in enumerate(grid):
  for x, c in enumerate(row):
    if c == "S":
      S = (x, y)
      break
  else:
    continue
  break
assert S is not None
pos = was = S


class D(Enum):
  NORTH = (0, -1)
  SOUTH = (0, 1)
  EAST = (1, 0)
  WEST = (-1, 0)


UNDER = ""
for (x, y), (a, b) in combinations((D.NORTH.value, D.EAST.value, D.SOUTH.value, D.WEST.value), 2):
  match [(x, y), grid[S[1] + y][S[0] + x], (a, b), grid[S[1] + b][S[0] + a]]:
    case [D.NORTH.value, "|" | "7" | "F", D.SOUTH.value, "|" | "L" | "J"]:
      UNDER = "|"
      was = S[0] + a, S[1] + b
      break
    case [D.NORTH.value, "|" | "7" | "F", D.EAST.value, "-" | "J" | "7"]:
      UNDER = "L"
      was = S[0] + a, S[1] + b
      break
    case [D.NORTH.value, "|" | "7" | "F", D.WEST.value, "-" | "L" | "F"]:
      UNDER = "J"
      was = S[0] + a, S[1] + b
      break
    case [D.EAST.value, "-" | "J" | "7", D.SOUTH.value, "|" | "L" | "J"]:
      UNDER = "F"
      was = S[0] + a, S[1] + b
      break
    case [D.EAST.value, "-" | "J" | "7", D.WEST.value, "-" | "L" | "F"]:
      UNDER = "-"
      was = S[0] + a, S[1] + b
      break
    case [D.SOUTH.value, "|" | "L" | "J", D.WEST.value, "-" | "L" | "F"]:
      UNDER = "7"
      was = S[0] + a, S[1] + b
      break
grid[S[1]] = grid[S[1]].replace("S", UNDER)
loop: list[tuple[int, int]] = []
while True:
  loop.append(pos)
  match [grid[pos[1]][pos[0]], (was[0] - pos[0], was[1] - pos[1])]:
    case ["|", D.NORTH.value]:
      pos, was = (pos[0], pos[1] + 1), pos
    case ["|", D.SOUTH.value]:
      pos, was = (pos[0], pos[1] - 1), pos
    case ["-", D.EAST.value]:
      pos, was = (pos[0] - 1, pos[1]), pos
    case ["-", D.WEST.value]:
      pos, was = (pos[0] + 1, pos[1]), pos
    case ["L", D.NORTH.value]:
      pos, was = (pos[0] + 1, pos[1]), pos
    case ["L", D.EAST.value]:
      pos, was = (pos[0], pos[1] - 1), pos
    case ["J", D.NORTH.value]:
      pos, was = (pos[0] - 1, pos[1]), pos
    case ["J", D.WEST.value]:
      pos, was = (pos[0], pos[1] - 1), pos
    case ["F", D.SOUTH.value]:
      pos, was = (pos[0] + 1, pos[1]), pos
    case ["F", D.EAST.value]:
      pos, was = (pos[0], pos[1] + 1), pos
    case ["7", D.SOUTH.value]:
      pos, was = (pos[0] - 1, pos[1]), pos
    case ["7", D.WEST.value]:
      pos, was = (pos[0], pos[1] + 1), pos

  if pos == S:
    break

"""
first, classic "shape" pass, identifies all islands
second, "gap connection" pass, consolidate islands across channels (can just get a list of candidate gaps in first)
third, "inside outside" pass, everything outside the loop should be outside and ubiquitous, so we can group all that together
(basically, all adjacent shapes except loop, which breaks it up)
leaving then the shape of the loop itself, a shape for the outside (starts at ``(0,0)``?), and then all the shapes of the interior (sum their lens)
can simplify, if first pass presupposes loop as a shape then we just combine any adjacent points that aren't in the loop,
which means we just get inside/outside in one go, and then just have to add the connections
"""

loopshape = set(loop)
island2shape = {S: loopshape}
coord2island = {c: S for c in loopshape}
channel_candidates = {}  # map from point to adjacent points that it could form a channel with

# identify all "islands"
# with island defined as contiguous tiles not in the loop

for y, row in enumerate(grid):
  for x, c in enumerate(row):
    pos = x, y
    coord2island[pos] = pos
    island2shape[pos] = {pos}
    adjs = [((a, b), d) for (a, b), d in [((x - 1, y), D.WEST), ((x, y - 1), D.NORTH)] if a >= 0 and b >= 0]
    match [coord2island[adj] for adj, _ in adjs]:
      case [a, b] if a == b and a not in loopshape:
        coord2island[pos] = a
        island2shape[a].add(pos)
      case [a, b] if a not in loopshape and b not in loopshape:
        island2shape[a].update(island2shape[b])
        for coord in island2shape[b]:
          coord2island[coord] = a
        del island2shape[b]
      case [a, b] if a not in loopshape or b not in loopshape:
        c = a if a not in loopshape else b
        coord2island[pos] = c
        island2shape[c].add(pos)
      case [a] if a not in loopshape:
        coord2island[pos] = a
        island2shape[a].add(pos)
    for (a, b), _d in adjs:
      match grid[b][a]:  # channel candidates... for some reason grid[b][a] is returning a list???
        case e:  # use d D.WHATEV and so on and should just be able to do "L" | ...
          pass

print(island2shape)

# connect "channels"
# all `||` etc. (basically turns some insides to outsides, and ensure all "outside" are connected, meaning all others are inside shapes)

...

# et voila, sum up the lengths of shapes that aren't "outside" (connected/starting `(0,0)`) and aren't the loop itself, that's part 2

print(
  len(loop) // 2,
  ...,
)
