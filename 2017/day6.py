from operator import itemgetter
from pathlib import Path

banks = list(map(int, Path("day6.txt").read_text().split()))
n, history = len(banks), {}

while tuple(banks) not in history:
  history[tuple(banks)] = len(history)
  i, mx = max(enumerate(banks), key=itemgetter(1))
  banks[i] = 0
  for j in range(i + 1, i + 1 + mx):
    banks[j % len(banks)] += 1  # mx ended up being small, so this is fine

print(
  len(history),
  len(history) - history[tuple(banks)],
)
