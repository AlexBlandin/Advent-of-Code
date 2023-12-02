from itertools import takewhile, count
from pathlib import Path
from math import sqrt, ceil

position = int(Path("day3.txt").read_text().strip())  # hi Ulam
spokes = list(takewhile(lambda n: n <= position, (ceil((n**2 + n + 1) / 4) for n in count())))
spokes += [ceil(((len(spokes)) ** 2 + (len(spokes)) + 1) / 4)]

width = ceil((sqrt(position) - 1) / 2) * 2
x, y = width // 2, width // 2
m = [[0] * width for _ in range(width)]
neighbours = [(1, 1), (1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0), (-1, -1)]
m[y][x] = acc = 1
x += 1
while acc < position:
  m[y][x] = acc = sum(m[y + yo][x + xo] for xo, yo in neighbours)
  if m[y + 1][x] and not m[y][x + 1]:
    x += 1
  elif m[y][x + 1] and not m[y - 1][x]:
    y -= 1
  elif m[y][x - 1] and not m[y + 1][x]:
    y += 1
  elif m[y - 1][x] and not m[y][x - 1]:
    x -= 1

print(
  ceil((sqrt(position) - 1) / 2) + min(abs(position - spokes[-1]), abs(position - spokes[-2])),
  acc,
)
