from operator import add, itemgetter
from pathlib import Path

banks = list(map(int, Path("day6.txt").read_text().split()))
lb = len(banks)
history = {}

while tuple(banks) not in history:
  history[tuple(banks)] = len(history)
  i, mx = max(enumerate(banks), key = itemgetter(1))
  div, mod = divmod(mx, lb)
  banks[:] = map(add, map(add, banks, [div] * lb), [0 if (i - (lb - mod)) < j <= i or (i - (lb - mod) + 1 < 0 and lb - ((lb - mod) - i) < j < lb) else 1 for j in range(lb)])
  banks[i] = 0

print(len(history), len(history) - history[tuple(banks)])
