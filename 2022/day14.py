from itertools import pairwise, repeat, count, chain
from operator import itemgetter
from pathlib import Path

lines, collide = Path("day14.txt").read_text().splitlines(), set()
for (ax, ay), (bx, by) in chain.from_iterable(
  map(
    lambda lst: pairwise(lst),
    map(
      lambda a: list(
        map(
          lambda b: list(map(int, b.split(","))),
          a,
        )
      ),
      map(
        lambda s: s.split(" -> "),
        lines,
      ),
    ),
  )
):
  collide |= {(ax, y) for y in range(min(ay, by), max(ay, by) + 1)} if ax == bx else {(x, ay) for x in range(min(ax, bx), max(ax, bx) + 1)}
ORIGIN, BELOW = (500, 0), max(collide, key=itemgetter(1))[1]
i, j = 0, 0
for i, (x, y) in zip(count(), repeat(ORIGIN)):  # noqa: B007
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
for j, (x, y) in zip(count(i + 1), repeat(ORIGIN)):  # since the i'th fell into the void # noqa: B007
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
