from functools import cmp_to_key, reduce
from itertools import groupby
from operator import itemgetter
from pathlib import Path
from typing import NamedTuple

lines = Path("day15.txt").read_text().splitlines()
_lines = """
Sensor at x=2, y=18: closest beacon is at x=-2, y=15
Sensor at x=9, y=16: closest beacon is at x=10, y=16
Sensor at x=13, y=2: closest beacon is at x=15, y=3
Sensor at x=12, y=14: closest beacon is at x=10, y=16
Sensor at x=10, y=20: closest beacon is at x=10, y=16
Sensor at x=14, y=17: closest beacon is at x=10, y=16
Sensor at x=8, y=7: closest beacon is at x=2, y=10
Sensor at x=2, y=0: closest beacon is at x=2, y=10
Sensor at x=0, y=11: closest beacon is at x=2, y=10
Sensor at x=20, y=14: closest beacon is at x=25, y=17
Sensor at x=17, y=20: closest beacon is at x=21, y=22
Sensor at x=16, y=7: closest beacon is at x=15, y=3
Sensor at x=14, y=3: closest beacon is at x=15, y=3
Sensor at x=20, y=1: closest beacon is at x=15, y=3
""".strip().splitlines()
lines = [tuple(map(int, line[12:].replace(" y=", "").replace(" closest beacon is at x=", "").replace(":", ",").split(","))) for line in lines]
Point = NamedTuple("Point", x = int, y = int)
Square = NamedTuple("Square", mid = Point, x = range, y = range)
sensors = list(map(Point, map(itemgetter(0), lines), map(itemgetter(1), lines)))
beacons = list(map(Point, map(itemgetter(2), lines), map(itemgetter(3), lines)))

def manhatten(sensor: Point, beacon: Point) -> int:
  return abs(sensor.x - beacon.x) + abs(sensor.y - beacon.y)

def coverage(sensor: Point, beacon: Point):
  r = manhatten(sensor, beacon)
  return Square(sensor, range(sensor.x - r, sensor.x + r + 1), range(sensor.y - r, sensor.y + r + 1))

@cmp_to_key
def disjoint(A: range, B: range):
  return A.stop < B.start

def simplify(ranges: list[range]):
  return reduce(lambda A, B: range(min(A.start, B.start), max(A.stop, B.stop)), ranges)

def ranges_at(y, sensors = sensors, beacons = beacons):
  def intersect(square: Square, y = y):
    if y in square.y:
      offset = abs(square.mid.y - y)
      return range(square.x.start + offset, square.x.stop - offset)
  
  ranges = sorted(filter(None, map(intersect, map(coverage, sensors, beacons))), key = disjoint)
  while len(ranges) != len(r := list(map(simplify, map(itemgetter(1), groupby(ranges, key = disjoint))))):
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
  where_it_isnt = [range(0, 0)]

y_at_Y = ranges_at(Y)
print(sum(map(len, y_at_Y)) - sum(b.x in r for b in filter(lambda b: b.y == Y, set(beacons)) for r in y_at_Y), where_it_isnt[0].stop * 4000000 + y)

# so I think why we aren't finding it is because "where it isn't" isn't factoring in beacons which interrupt the range? maybe?
# except that's a beacon we know about, which we know the one we're looking for isn't
