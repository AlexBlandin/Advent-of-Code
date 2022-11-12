from functools import reduce
from operator import xor
from pathlib import Path

from circular import Circular

lengths = list(map(int, Path("day10.txt").read_text().strip().split(",")))
circle = Circular(range(256))

pos = skip = 0
for l in lengths:
  rev = list(reversed(circle[pos:pos + l]))
  circle[pos:pos + l] = circle[pos + l - 1:pos - 1:-1]
  assert circle[pos:pos + l] == rev
  pos += skip + l
  skip += 1

part1 = circle[0] * circle[1]
lengths = list(Path("day10.txt").read_bytes().strip()) + [17, 31, 73, 47, 23]
circle = Circular(range(256))
pos = skip = 0

# lengths = list(b"AoC 2017") + [17, 31, 73, 47, 23]

def round(circle, lengths, pos, skip):
  for l in lengths:
    rev = list(reversed(circle[pos:pos + l]))
    circle[pos:pos + l] = circle[pos + l - 1:pos - 1:-1]
    assert circle[pos:pos + l] == rev
    pos += skip + l
    skip += 1
  return circle, pos, skip

for _ in range(64):
  circle, pos, skip = round(circle, lengths, pos, skip)
print(circle)

dense = bytes([reduce(xor, circle[i * 16:(i + 1) * 16]) for i in range(16)]).hex()

print(part1, dense)
