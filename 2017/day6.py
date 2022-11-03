from operator import add, itemgetter
from pathlib import Path

banks = list(map(int, Path("day6.txt").read_text().split()))
lb, sb = len(banks), sum(banks)
history = {}

while tuple(banks) not in history:
  history[tuple(banks)] = len(history)
  assert sum(banks) == sb
  assert len(banks) == lb
  i, mx = max(enumerate(banks), key = itemgetter(1))
  banks[i] = 0
  div, mod = divmod(mx, lb)
  zeroes = lb - mod
  rem = [0 if (i - zeroes) < j <= i or (i - zeroes + 1 < 0 and lb - (zeroes - i) < j < lb) else 1 for j in range(lb)]
  banks[:] = map(add, map(add, banks, [div] * lb), rem)

print(len(history), len(history) - history[tuple(banks)])
