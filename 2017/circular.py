from itertools import count
from typing import SupportsIndex


class Circular(list):
  """a circularly addressable list, where Circular([0, 1, 2, 3, 4])[-5:10] is [0, 1, 2, 3, 4, 0, 1, 2, 3, 4, 0, 1, 2, 3, 4]."""

  def __getitem__(self, x: int | slice):
    if isinstance(x, slice):
      return [self[x] for x in range(0 if x.start is None else x.start, len(self) if x.stop is None else x.stop, 1 if x.step is None else x.step)]
    return super().__getitem__(x.__index__() % max(1, len(self)))

  def __setitem__(self, x: SupportsIndex | slice, val) -> None:
    if isinstance(x, slice):
      if not (hasattr(val, "__iter__") or not hasattr(val, "__getitem__")):
        raise TypeError(val)
      m = max(1, len(self))
      for i, v in (
        zip(count(0 if x.start is None else x.start, 1 if x.step is None else x.step), val)
        if x.stop is None
        else zip(range(0 if x.start is None else x.start, len(self) if x.stop is None else x.stop, 1 if x.step is None else x.step), val, strict=False)
      ):
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
