from itertools import chain, repeat
from operator import attrgetter
from pathlib import Path


def bundle2lut(bundle: str):
  def line2ranges(line: str):
    dst, src, ln, *_ = list(map(int, line.split()))
    source, dest = range(src, src + ln), dst
    return source, dest

  return tuple(sorted(map(line2ranges, bundle.splitlines()[1:]), key=lambda tup: attrgetter("start", "stop")(tup[0])))


def seed2location(seed: int, maps: tuple[tuple[tuple[range, int], ...], ...]):
  pos = seed
  for m in maps:
    low, high, mid = 0, len(m) - 1, None
    while low <= high:
      mid = (low + high) // 2
      mmid = m[mid][0]
      start = mmid.start
      if pos in mmid:
        break
      elif start > pos:
        high = mid - 1
      elif start < pos:
        low = mid + 1
    else:
      mid = None
    if mid is not None:
      pos += m[mid][1] - m[mid][0].start
  return pos


bundles = Path("day5.txt").read_text().split("\n\n")
seeds = list(map(int, bundles[0].split(maxsplit=1)[1].split()))
many_seeds = chain.from_iterable(
  map(lambda src, n: range(src, src + n), seeds[::2], seeds[1::2])
)  # 1_737_205_559 seeds
LUTs = tuple(map(bundle2lut, bundles[1:]))
print(
  min(map(seed2location, seeds, repeat(LUTs))),
  min(map(seed2location, many_seeds, repeat(LUTs))),  # takes about 15 minutes with pypy... or over 4 hours with CPython
)
