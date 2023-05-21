from operator import itemgetter
from pathlib import Path
from math import prod, lcm

lines = Path("day11.txt").read_text().replace(",", "").splitlines()

OP = {"+": 1, "*": 0}
START = list(map(lambda xs: list(map(int, xs)), map(itemgetter(slice(2, None)), map(str.split, lines[1::7]))))
OPS = list(map(lambda op: (0, 0) if op[1] == "old" else (OP[op[0]], int(op[1])), map(itemgetter(-2, -1), map(str.split, lines[2::7]))))
DIVISORS = list(map(int, map(itemgetter(-1), map(str.split, lines[3::7]))))
TRUES = list(map(int, map(itemgetter(-1), map(str.split, lines[4::7]))))
FALSES = list(map(int, map(itemgetter(-1), map(str.split, lines[5::7]))))

LCM = lcm(*DIVISORS)
PACKED = list(zip(OPS, DIVISORS, TRUES, FALSES))

def play(n = 20, relief = False, unpack = PACKED):
  sn = [0 for _ in START]
  it = [(i, t) for i, it in enumerate(START) for t in it]
  for t, v in it:
    g = t
    for _ in range(n):
      while g >= t:
        t = g
        sn[t] += 1
        (op, x), d, tr, fa = unpack[t]
        if op:
          v += x
        elif x:
          v *= x
        else:
          v *= v
        if relief:
          v //= 3
        v %= LCM # this line here is what defines the performance, almost all else is micro
        if v % d:
          g = fa
        else:
          g = tr
      t = g
  return sn

print(prod(sorted(play(relief = True))[-2:]), prod(sorted(play(10000))[-2:]))
