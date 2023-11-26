from pathlib import Path
from math import log2, prod

def peaks(row: list[int]):
  out, mrs, tbs, n = [0] * len(row), {}, 0, len(row)
  for i, t in enumerate(map(int, row[::-1])):
    tbs &= ~(2**t - 1)
    bit = tbs & -tbs
    if bit:
      out[n - i - 1] = i - mrs[int(log2(bit))]
    mrs[t] = i
    tbs |= 2**t
  return out

trees = [list(map(int, line)) for line in Path("day8.txt").read_text().splitlines()]
W, H, transpose, backwards = len(trees[0]), len(trees), lambda t: list(map(
  list,
  zip(*t, strict = True),
)), lambda t: list(map(
  lambda line: list(reversed(line)),
  t,
))
forest = [[peaks(row) for row in trees] for trees in [trees, backwards(trees), transpose(trees), backwards(transpose(trees))]]
sightlines = [(vis, (W - x - 1, x, H - y - 1, y))
              for y, rows in enumerate(zip(forest[0], backwards(forest[1]), transpose(forest[2]), transpose(backwards(forest[3])), strict = True))
              for x, vis in enumerate(zip(*rows, strict = True))]

print(
  sum(0 in vis for vis, _ in sightlines),
  max(prod(v if v else d for v, d in zip(vs, ds, strict = True)) for vs, ds in sightlines),
)
