from pathlib import Path

from parse import parse

lines = Path("day5.txt").read_text().splitlines()
segments: list[tuple[int, ...]] = []
for line in lines:
  if p := parse("{:d},{:d} -> {:d},{:d}", line):
    x1, y1, x2, y2 = p.fixed  # type: ignore
    segments.append((x1, x2, y1, y2))
gridmax = max(map(max, segments)) + 1
grid = [[0 for _ in range(gridmax)] for _ in range(gridmax)]
for x1, x2, y1, y2 in segments:
  if x1 == x2:
    dy = 1 if y1 < y2 else -1
    for y in range(y1, y2 + dy, dy):
      grid[y][x1] += 1
  if y1 == y2:
    dx = 1 if x1 < x2 else -1
    for x in range(x1, x2 + dx, dx):
      grid[y1][x] += 1
crossings = sum(col >= 2 for row in grid for col in row)
for x1, x2, y1, y2 in segments:
  if x1 != x2 and y1 != y2 and abs(x2 - x1) == abs(y2 - y1):
    dx = 1 if x1 < x2 else -1
    dy = 1 if y1 < y2 else -1
    for x, y in zip(range(x1, x2 + dx, dx), range(y1, y2 + dy, dy), strict=True):
      grid[y][x] += 1

cross_with_diag = sum(col >= 2 for row in grid for col in row)
print(crossings, cross_with_diag)
