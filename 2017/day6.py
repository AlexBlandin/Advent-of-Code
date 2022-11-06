from operator import itemgetter, add
from pathlib import Path

banks = list(map(int, Path("day6.txt").read_text().split()))
n, history = len(banks), {}

while tuple(banks) not in history:
  history[tuple(banks)] = len(history)
  i, mx = max(enumerate(banks), key = itemgetter(1))
  banks[i] = 0
  for i in range(i + 1, i + 1 + mx):
    banks[i % len(banks)] += 1 # mx ended up being small, so this is fine
  if False:
    div, rem = divmod(mx, n)
    banks[:] = map(add, map(add, banks, [div] * n), [0 if (i - (n - rem)) < j <= i or (i - (n - rem) + 1 < 0 and n - ((n - rem) - i) < j < n) else 1 for j in range(n)])

print(len(history), len(history) - history[tuple(banks)])
