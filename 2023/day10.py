from enum import Enum
from itertools import combinations
from pathlib import Path


class D(Enum):
  NORTH = (0, -1)
  SOUTH = (0, 1)
  EAST = (1, 0)
  WEST = (-1, 0)


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

UNDER = ""
for (x, y), (isle_a, isle_b) in combinations((D.NORTH.value, D.EAST.value, D.SOUTH.value, D.WEST.value), 2):
  match [(x, y), grid[S[1] + y][S[0] + x], (isle_a, isle_b), grid[S[1] + isle_b][S[0] + isle_a]]:
    case [D.NORTH.value, "|" | "7" | "F", D.SOUTH.value, "|" | "L" | "J"]:
      UNDER = "|"
      was = S[0] + isle_a, S[1] + isle_b
      break
    case [D.NORTH.value, "|" | "7" | "F", D.EAST.value, "-" | "J" | "7"]:
      UNDER = "L"
      was = S[0] + isle_a, S[1] + isle_b
      break
    case [D.NORTH.value, "|" | "7" | "F", D.WEST.value, "-" | "L" | "F"]:
      UNDER = "J"
      was = S[0] + isle_a, S[1] + isle_b
      break
    case [D.EAST.value, "-" | "J" | "7", D.SOUTH.value, "|" | "L" | "J"]:
      UNDER = "F"
      was = S[0] + isle_a, S[1] + isle_b
      break
    case [D.EAST.value, "-" | "J" | "7", D.WEST.value, "-" | "L" | "F"]:
      UNDER = "-"
      was = S[0] + isle_a, S[1] + isle_b
      break
    case [D.SOUTH.value, "|" | "L" | "J", D.WEST.value, "-" | "L" | "F"]:
      UNDER = "7"
      was = S[0] + isle_a, S[1] + isle_b
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


# identify all "islands"
# with island defined as contiguous tiles not in the loop

loopshape = set(loop)
island2shape = {S: loopshape}
channel2shape = {}
coord2island = {c: S for c in loopshape}
coord2channel = {}

for y, row in enumerate(grid):
  for x, c in enumerate(row):
    pos = x, y
    under = grid[y][x]
    adjs = [((a, b), d) for (a, b), d in [((x - 1, y), D.WEST), ((x, y - 1), D.NORTH)] if a >= 0 and b >= 0]
    match [coord2island[adj] for adj, _ in adjs]:
      case [isle_a, isle_b] if isle_a == isle_b and isle_a not in loopshape:  # join only island
        coord2island[pos] = isle_a
        island2shape[isle_a].add(pos)
      case [isle_a] if isle_a not in loopshape:  # join only island
        coord2island[pos] = isle_a
        island2shape[isle_a].add(pos)
      case [isle_a, isle_b] if isle_a not in loopshape and isle_b not in loopshape:  # merge two islands
        coord2island[pos] = isle_a
        island2shape[isle_a].add(pos)
        island2shape[isle_a].update(island2shape[isle_b])
        for coord in island2shape[isle_b]:
          coord2island[coord] = isle_a
        del island2shape[isle_b]
      case [isle_a, isle_b] if isle_a not in loopshape or isle_b not in loopshape:  # join island that isn't in loop
        c = isle_a if isle_a not in loopshape else isle_b
        coord2island[pos] = c
        island2shape[c].add(pos)
      case _:  # no (non-loop) neighbours, new island
        coord2island[pos] = pos
        island2shape[pos] = {pos}
    match adjs:
      case [((a, b), D.WEST), ((c, d), D.NORTH)]:
        match (grid[b][a], under, grid[d][c]):
          case ("|", "|", "|"): ...
      case _:
        pass  # do nothing as we can't form a channel at the boundary

insidecandidates = {}


# for y, row in enumerate(grid):
#   for x, c in enumerate(row):
#     print(c if (y, x) in island2shape[(77, 25)] else " ", end="")
#   print()

print(*island2shape)  # if we've only got 2 shapes, it's not added the insides yet

# connect "channels"
# all `||` etc. (basically turns some insides to outsides, and ensure all "outside" are connected, meaning all others are inside shapes)

...

# et voila, sum up the lengths of shapes that aren't "outside" (connected/starting `(0,0)`) and aren't the loop itself, that's part 2

"""
first, classic "shape" pass, identifies all islands
second, "gap connection" pass, consolidate islands across channels (can just get a list of candidate gaps in first)
third, "inside outside" pass, everything outside the loop should be outside and ubiquitous, so we can group all that together
(basically, all adjacent shapes except loop, which breaks it up)
leaving then the shape of the loop itself, a shape for the outside (starts at ``(0,0)``?), and then all the shapes of the interior (sum their lens)
can simplify, if first pass presupposes loop as a shape then we just combine any adjacent points that aren't in the loop,
which means we just get inside/outside in one go, and then just have to add the connections
"""

print(
  len(loop) // 2,
  len(island2shape[(77, 25)]),  # 13572 is too high (upper bound, no channels)
)
