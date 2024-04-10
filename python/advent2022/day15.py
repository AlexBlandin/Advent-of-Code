from functools import cmp_to_key, reduce
from itertools import groupby
from operator import itemgetter
from pathlib import Path
from typing import NamedTuple


class Point(NamedTuple):
  x: int
  y: int


class Square(NamedTuple):
  mid: Point
  x: range
  y: range


lines = [
  tuple(map(int, line[12:].replace(" y=", "").replace(" closest beacon is at x=", "").replace(":", ",").split(",")))
  for line in Path("day15.txt").read_text().splitlines()
]
sensors = list(
  map(
    Point,
    map(itemgetter(0), lines),
    map(itemgetter(1), lines),
  ),
)
beacons = list(
  map(
    Point,
    map(itemgetter(2), lines),
    map(itemgetter(3), lines),
  ),
)


def manhatten(sensor: Point, beacon: Point) -> int:
  return abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)


def coverage(sensor: Point, beacon: Point):
  r = manhatten(sensor, beacon)
  return Square(sensor, range(sensor.x - r, sensor.x + r + 1), range(sensor.y - r, sensor.y + r + 1))


@cmp_to_key
def disjoint(a: range, b: range):
  return a.stop < b.start


def simplify(ranges: list[range]):
  return reduce(lambda a, b: range(min(a.start, b.start), max(a.stop, b.stop)), ranges)


def ranges_at(y, sensors=sensors, beacons=beacons):
  def intersect(square: Square, y=y):
    if y in square.y:
      offset = abs(square.mid.y - y)
      return range(square.x.start + offset, square.x.stop - offset)
    return None

  ranges = sorted(filter(None, map(intersect, map(coverage, sensors, beacons))), key=disjoint)
  while len(ranges) != len(
    r := list(
      map(
        simplify,
        map(
          itemgetter(1),
          groupby(ranges, key=disjoint),
        ),
      ),
    ),
  ):
    ranges = r
  return ranges


where_it_isnt, y = [], 0
search_space, Y = (20, 10) if len(lines) == 14 else (4000000, 2000000)
for y in range(search_space + 1):
  where_it_isnt = ranges_at(y)
  if len(where_it_isnt) != 1:
    print(y, where_it_isnt)
    break
else:
  where_it_isnt = [range(0)]

y_at = ranges_at(Y)
print(
  sum(map(len, y_at)) - sum(b.x in r for b in filter(lambda b: b.y == Y, set(beacons)) for r in y_at),
  where_it_isnt[0].stop * 4000000 + y,
)

# so I think why we aren't finding it is because "where it isn't" isn't factoring in beacons which interrupt the range? maybe?
# except that's a beacon we know about, which we know the one we're looking for isn't
