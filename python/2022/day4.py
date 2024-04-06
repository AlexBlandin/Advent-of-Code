from itertools import starmap
from pathlib import Path

print(
  sum(
    starmap(
      lambda a, b, c, d: (a <= c <= b and a <= d <= b) or (c <= a <= d and c <= b <= d),
      jobs := [
        tuple(map(int, line.split(","))) for line in Path("day4.txt").read_text().replace("-", ",").splitlines()
      ],
    ),
  ),
  sum(
    starmap(
      lambda a, b, c, d: a <= c <= b or a <= d <= b or c <= a <= d or c <= b <= d,
      jobs,
    ),
  ),
)
