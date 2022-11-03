from operator import add, itemgetter
from pathlib import Path

banks = list(map(int, Path("day6.txt").read_text().split()))
n, history = len(banks), {}

while tuple(banks) not in history:
  history[tuple(banks)] = len(history)
  i, mx = max(enumerate(banks), key = itemgetter(1))
  div, rem = divmod(mx, n)
  banks[:] = map(add, map(add, banks, [div] * n), [0 if (i - (n - rem)) < j <= i or (i - (n - rem) + 1 < 0 and n - ((n - rem) - i) < j < n) else 1 for j in range(n)])
  banks[i] = 0

print(len(history), len(history) - history[tuple(banks)])
