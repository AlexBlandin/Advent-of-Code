from itertools import product
from pathlib import Path

n = [int(x) for x in Path("day9.txt").read_text().splitlines() if len(x)]
for i in range(25, len(n)):
  if n[i] not in [x + y for x, y in product(n[i - 25:i], n[i - 25:i])]:
    a, s = 0, 0
    for j, x in enumerate(n):
      a += x
      while a > n[i]:
        a -= n[s]
        s += 1
      if a == n[i]:
        print(n[i], min(n[s:j + 1]) + max(n[s:j + 1]))
        break
