from functools import partial
from operator import itemgetter, mul, add
from pathlib import Path
from collections.abc import Callable
from math import prod, lcm

def last_word(lines: list[str], target: int | slice = -1, post: Callable = int):
  return map(post, map(itemgetter(target), map(str.split, lines)))

LINES = Path("day11.txt").read_text().replace(",", "").replace("* old", "** 2").splitlines()
ITEMS = list(last_word(LINES[1::7], slice(2, None), lambda xs: list(map(int, xs))))
OP = {"+": add, "*": mul, "**": pow}
OPS = [partial(op, exp = v) if op is pow else partial(op, v) for op, v in zip(last_word(LINES[2::7], -2, post = OP.get), last_word(LINES[2::7]), strict = True)]
MODULOS, TTHROW, FTHROW = list(last_word(LINES[3::7])), last_word(LINES[4::7]), last_word(LINES[5::7])
TEST = map(lambda m, t, f: lambda x: f if x % m else t, MODULOS, TTHROW, FTHROW)
ZOT = zip(OPS, TEST, strict = False)
LCM = lcm(*MODULOS)

def play(n = 20, relief = False, items = ITEMS, unpack = tuple(ZOT), lcm = LCM):
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
        v %= lcm
        t, g = g, th(v)
      t = g
  return prod(sorted(seen)[-2:])

print(play(relief = True), play(10000))
