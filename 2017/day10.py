from functools import reduce
from operator import xor
from pathlib import Path
from math import prod

from circular import Circular

lengths = list(Path("day10.txt").read_bytes().strip()) + [17, 31, 73, 47, 23]
# lengths = list(b"AoC 2017") + [17, 31, 73, 47, 23]
circle, pos, skip = Circular(range(256)), 0, 0

def knot(lengths, circle = Circular(range(256)), pos = 0, skip = 0):
  for l in lengths:
    circle[pos:pos + l] = circle[pos + l - 1:pos - 1:-1]
    pos += skip + l
    skip += 1
  return circle, pos, skip

for _ in range(64):
  circle, pos, skip = knot(lengths, circle, pos, skip)

print(prod(knot(list(map(int, Path("day10.txt").read_text().strip().split(","))))[0][:2]), bytes(reduce(xor, circle[i * 16:(i + 1) * 16]) for i in range(16)).hex())
