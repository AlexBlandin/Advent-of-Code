from pathlib import Path

from hexagon import Hex

dirs = Path("day11.txt").read_text().split(",")
pos = origin = Hex(0, 0, 0)
distance = furthest = 0
for d in dirs:
  match d:
    case "n":
      pos = pos.nn
    case "s":
      pos = pos.ss
    case "nw":
      pos = pos.nw
    case "ne":
      pos = pos.ne
    case "sw":
      pos = pos.sw
    case "se":
      pos = pos.se
  distance = pos.distance(origin)
  furthest = max(furthest, distance)

print(distance - 1, furthest)
