from itertools import chain, count
from operator import itemgetter
from pathlib import Path

lines = Path("day14.txt").read_text().splitlines()
collide: set[tuple[int, int]] = set()
for frm, to in chain.from_iterable(map(lambda lst: list(zip(lst, lst[1:])), map(lambda s: s.split(" -> "), lines))):
  (ax, ay), (bx, by) = map(int, frm.split(",", maxsplit = 1)), map(int, to.split(",", maxsplit = 1))
  collide |= {(ax, y) for y in range(min(ay, by), max(ay, by) + 1)} if ax == bx else {(x, ay) for x in range(min(ax, bx), max(ax, bx) + 1)}
ORIGIN, BELOW = (500, 0), max(collide, key = itemgetter(1))[1]
for i in count():
  x, y = ORIGIN
  while True:
    if y > BELOW:
      break
    if (down := (x, y + 1)) not in collide:
      x, y = down
    elif (left := (x - 1, y + 1)) not in collide:
      x, y = left
    elif (right := (x + 1, y + 1)) not in collide:
      x, y = right
    else:
      collide.add((x, y))
      break
  if y > BELOW:
    break
for j in count(i + 1): # since the i'th fell into the void
  x, y = ORIGIN
  while True:
    if (down := (x, y + 1)) not in collide and y < BELOW + 1:
      x, y = down
    elif (left := (x - 1, y + 1)) not in collide and y < BELOW + 1:
      x, y = left
    elif (right := (x + 1, y + 1)) not in collide and y < BELOW + 1:
      x, y = right
    else:
      collide.add((x, y))
      break
  if (x, y) == ORIGIN:
    break
print(i, j)
