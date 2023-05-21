from functools import partial
from operator import itemgetter, mul, add
from pathlib import Path
from typing import Callable, Union
from math import prod, lcm

def last_word(lines: list[str], target: Union[int, slice] = -1, post: Callable = int):
  return map(post, map(itemgetter(target), map(str.split, lines)))

LINES = Path("day11.txt").read_text().replace(",", "").replace("* old", "** 2").splitlines()
ITEMS = list(last_word(LINES[1::7], slice(2, None), lambda xs: list(map(int, xs))))
OP = {"+": add, "*": mul, "**": pow}
OPS = [partial(op, exp = v) if op is pow else partial(op, v) for op, v in zip(last_word(LINES[2::7], -2, post = OP.get), last_word(LINES[2::7]))]
MODULOS = list(last_word(LINES[3::7]))
TTHROW = last_word(LINES[4::7])
FTHROW = last_word(LINES[5::7])
TEST = map(lambda m, t, f: lambda x: f if x % m else t, MODULOS, TTHROW, FTHROW)
PACKED = list(zip(OPS, TEST))
LCM = lcm(*MODULOS)

def play(n = 20, relief = False, unpack = PACKED, items = ITEMS):
  seen = [0 for _ in items]
  item = [(monkey, worry) for monkey, holding in enumerate(items) for worry in holding]
  for t, v in item:
    g = t
    for _ in range(n):
      while g >= t:
        seen[g] += 1
        op, th = unpack[g]
        v = op(v)
        if relief:
          v //= 3
        v %= LCM
        t, g = g, th(v)
      t = g
  return prod(sorted(seen)[-2:])

print(play(relief = True), play(10000))
