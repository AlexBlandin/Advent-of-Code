from functools import reduce
from operator import xor
from pathlib import Path
from math import prod

from circular import Circular

lengths = [*list(Path("day10.txt").read_bytes().strip()), 17, 31, 73, 47, 23]
circle, pos, skip = Circular(range(256)), 0, 0


def knot(lengths, circle, pos=0, skip=0):
  for r in lengths:
    circle[pos: pos + r] = circle[pos + r - 1: pos - 1: -1]
    pos += skip + r
    skip += 1
  return circle, pos, skip


def knot_a_hash(lengths):
  circle, pos, skip = Circular(range(256)), 0, 0
  for _ in range(64):
    circle, pos, skip = knot(lengths, circle, pos, skip)
  return bytes(reduce(xor, circle[i * 16: (i + 1) * 16]) for i in range(16)).hex()


if __name__ == "__main__":
  print(
    prod(knot(list(map(int, Path("day10.txt").read_text().strip().split(","))), Circular(range(256)))[0][:2]),
    knot_a_hash(lengths),
  )
