from itertools import count
from pathlib import Path

lines = dict(tuple(map(int, line.split())) for line in Path("day13.txt").read_text().replace(":", "").splitlines())
print(
  sum(d * r for d, r in lines.items() if d % (2 * r - 2) == 0),
  next(i for i in count() if sum(1 for d, r in lines.items() if (d + i) % (2 * r - 2) == 0) == 0)
)
