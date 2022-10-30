from itertools import combinations
from functools import reduce
from operator import mul

vs = [list(map(int, l.split("x"))) for l in open("day2.txt")]
print(
  sum(2 * sum(a * b for a, b in combinations(v, 2)) + min(a * b for a, b in combinations(v, 2)) for v in vs),
  sum(min(list(a + a + b + b for a, b in combinations(v, 2))) + reduce(mul, v) for v in vs)
)
