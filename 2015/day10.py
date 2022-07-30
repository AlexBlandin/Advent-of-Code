from pathlib import Path

lines = Path("data/day10.txt").read_text().splitlines()
s = lines[0]

def looksay(s, _):
  p, c = s[0], 1
  o = []
  for n in s[1:]:
    if n == p:
      c += 1
    else:
      o.append(f"{c}{p}")
      p, c = n, 1
  o.append(f"{c}{p}")
  return "".join(o)

from functools import reduce

r40 = reduce(looksay, range(40), s)
r50 = reduce(looksay, range(50), s)
print(len(r40), len(r50))
