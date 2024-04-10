from functools import cache
from itertools import pairwise
from pathlib import Path

a = [0, *sorted(map(int, Path("day10.txt").read_text().splitlines()))]
a += [a[-1] + 3]
b, G = [y - x for x, y in pairwise(a)], {x: [y for y in range(x + 1, x + 4) if y in a] for x in a}


@cache
def rec(x):
  return 1 if x == a[-1] else sum(rec(y) for y in G[x])


print(b.count(1) * b.count(3), rec(0))
