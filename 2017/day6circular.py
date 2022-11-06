from itertools import count
from operator import itemgetter, add
from pathlib import Path
from typing import SupportsIndex

class Circular(list):
  """a circularly addressable list, where Circular([0, 1, 2, 3, 4])[-5:10] is [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]"""
  def __getitem__(self, x: int | slice):
    if isinstance(x, slice):
      return [self[x] for x in range(0 if x.start is None else x.start, len(self) if x.stop is None else x.stop, 1 if x.step is None else x.step)]
    return super().__getitem__(x.__index__() % max(1, len(self)))
  
  def __setitem__(self, x: SupportsIndex | slice, val):
    if isinstance(x, slice) and (hasattr(val, "__iter__") or hasattr(val, "__getitem__")):
      m = max(1, len(self))
      for i, v in zip(count(0 if x.start is None else x.start, 1 if x.step is None else x.step), val) if x.stop is None else zip(range(0 if x.start is None else x.start, len(self) if x.stop is None else x.stop, 1 if x.step is None else x.step), val):
        super().__setitem__(i.__index__() % m, v)
    else:
      super().__setitem__(x.__index__() % max(1, len(self)), val)

  def repeat(self, times: None | int = None):
    if times is None:
      while True:
        yield from iter(self)
    else:
      for _ in range(times):
        yield from iter(self)

banks = Circular(map(int, Path("day6.txt").read_text().split()))
n, history = len(banks), {}

while tuple(banks) not in history:
  history[tuple(banks)] = len(history)
  i, mx = max(enumerate(banks), key = itemgetter(1))
  banks[i] = 0
  banks[:] = map(add, banks.repeat(), [0] * (i+1) + [1] * mx)

print(len(history), len(history) - history[tuple(banks)])
