from math import prod
from pathlib import Path

lines = Path("day3.txt").read_text().splitlines()
coord = tuple[int, int]
num_starts: dict[coord, coord] = {}  # number at coord starts at coord
starting: dict[coord, int] = {}  # number starting at coord
symbols: set[coord] = set()  # coord of symbol
keep: set[coord] = set()  # starting coords
maybe_gear: dict[coord, set[coord]] = {}  # candidates for gears (aka, coords of "*" with their neighbours)
gears: set[coord] = set()  # confirmed gears (have 2 nums adjacent)
for y, line in enumerate(lines):
  run = False  # run of digits
  start = 0
  for x, c in enumerate(line):
    xy = x, y
    if c == "*":
      maybe_gear[xy] = set()
    if c.isdigit():
      if not run:
        start, run = x, True
      num_starts[xy] = (start, y)
    else:
      if c != ".":
        symbols.add(xy)
      if run:
        starting[(start, y)] = int(line[start:x])
        run = False
  if run and len(line[start:]):
    starting[(start, y)] = int(line[start:])
    run = False

for x, y in symbols:
  for xy in [(x + i, y + j) for i in (1, 0, -1) for j in (1, 0, -1)]:
    if num := num_starts.get(xy, None):
      keep.add(num)
      if (nums := maybe_gear.get((x, y), None)) is not None:
        nums.add(num)

print(
  sum(starting[xy] for xy in keep),
  sum(prod(starting[xy] for xy in nums) for nums in maybe_gear.values() if len(nums) == 2),
)
