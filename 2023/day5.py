from itertools import chain
from operator import attrgetter
from pathlib import Path

bundles = Path("day5.txt").read_text().split("\n\n")
_bundles = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4""".split("\n\n")

range_cmp = attrgetter("start", "stop")  # if we sort ranges for log(n) lookup


def bundle2lut(bundle: str):
  def line2ranges(line: str):
    dst, src, ln, *_ = list(map(int, line.split()))
    source, dest = range(src, src + ln), dst
    return source, dest

  return tuple(sorted(map(line2ranges, bundle.splitlines()[1:]), key=lambda tup: range_cmp(tup[0])))


seeds = list(map(int, bundles[0].split(maxsplit=1)[1].split()))
many_seeds = chain.from_iterable(map(lambda src, n: range(src, src + n), seeds[::2], seeds[1::2]))  # 1_737_205_559 seeds
LUTs = tuple(map(bundle2lut, bundles[1:]))


def seed2location(seed: int, maps: tuple[tuple[tuple[range, int], ...], ...] = LUTs):
  pos = seed
  for m in maps:
    # for src, dst in m.items():  # linear search is slower
    #   if pos in src:
    #     pos += dst - src.start
    #     break
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


print(
  min(map(seed2location, seeds)),  # 278755257
  min(map(seed2location, many_seeds)),  # 26829166 # takes about 15 minutes with pypy... or over 4 hours with CPython
)
