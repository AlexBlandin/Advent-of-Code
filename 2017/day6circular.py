from operator import itemgetter, add
from pathlib import Path

from circular import Circular

banks = Circular(map(int, Path("day6.txt").read_text().split()))
n, history = len(banks), {}

while tuple(banks) not in history:
  history[tuple(banks)] = len(history)
  i, mx = max(enumerate(banks), key=itemgetter(1))
  banks[:] = map(add, banks.repeat(), [0] * (i + 1) + [1] * mx)
  banks[i] = 0

print(len(history), len(history) - history[tuple(banks)])
