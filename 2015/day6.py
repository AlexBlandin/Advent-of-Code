from pathlib import Path

import numpy as np


def square(a, b, c, d):
  return slice(int(a), int(c) + 1), slice(int(b), int(d) + 1)


bools = np.zeros((1000, 1000), bool)
ints = np.zeros((1000, 1000), np.int32)
for line in Path("day6.txt").read_text().replace(",", " ").splitlines():
  match line.split():
    case ["turn", "on", a, b, "through", c, d]:
      x, y = square(a, b, c, d)
      bools[x, y] = True
      ints[x, y] += 1
    case ["turn", "off", a, b, "through", c, d]:
      x, y = square(a, b, c, d)
      bools[x, y] = False
      ints[x, y] = np.maximum(0, ints[x, y] - 1)
    case ["toggle", a, b, "through", c, d]:
      x, y = square(a, b, c, d)
      bools[x, y] = ~bools[x, y]
      ints[x, y] += 2

print(bools.sum(), ints.sum())
