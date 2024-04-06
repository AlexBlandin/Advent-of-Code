from itertools import count
from pathlib import Path

lines = {int(a): int(b) for a, b, *_ in map(str.split, Path("day13.txt").read_text().replace(":", "").splitlines())}
print(
  sum(d * r for d, r in lines.items() if d % (2 * r - 2) == 0),
  next(i for i in count() if not any(1 for d, r in lines.items() if (d + i) % (2 * r - 2) == 0)),
)
