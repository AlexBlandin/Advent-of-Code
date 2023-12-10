from itertools import repeat
from math import prod
from pathlib import Path


def will_travel(ms_held: int, race_duration: int, _):
  return (race_duration - ms_held) * ms_held


Time, Dist, *_ = Path("day6.txt").read_text().splitlines()

print(
  prod(
    sum(1 for _ in filter(lambda x: will_travel(*x) > x[2], zip(range(t), repeat(t), repeat(d), strict=False)))
    for t, d in zip(map(int, Time.split()[1:]), map(int, Dist.split()[1:]), strict=True)
  ),
  next(
    sum(1 for _ in filter(lambda x: will_travel(*x) > x[2], zip(range(t), repeat(t), repeat(d), strict=False)))
    for t, d in [(int(Time.split(maxsplit=1)[1].replace(" ", "")), int(Dist.split(maxsplit=1)[1].replace(" ", "")))]
  ),
)
