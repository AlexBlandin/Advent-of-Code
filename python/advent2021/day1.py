from operator import gt
from pathlib import Path

lines = Path("day1.txt").read_text().splitlines()
lines = [int(line) for line in lines]

print(
  sum(map(gt, lines[1:], lines)),
  sum(
    map(
      gt,
      map(sum, zip(lines[1::], lines[2::], lines[3::], strict=False)),
      map(sum, zip(lines, lines[1::], lines[2::], strict=False)),
    )
  ),
)
