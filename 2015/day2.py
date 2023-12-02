from itertools import combinations
from functools import reduce
from operator import mul
from pathlib import Path

vs = [list(map(int, ln.split("x"))) for ln in Path("day2.txt").read_text().splitlines()]
print(
  sum(2 * sum(a * b for a, b in combinations(v, 2)) + min(a * b for a, b in combinations(v, 2)) for v in vs),
  sum(min(list(a + a + b + b for a, b in combinations(v, 2))) + reduce(mul, v) for v in vs),
)
