from itertools import count, pairwise
from pathlib import Path

old = Path("day11.txt").read_text()
lenc = "abcdefghjkmnpqrstuvwxyz"
ldec = dict(zip(lenc, range(len(lenc)), strict=True))


def dec(s: str) -> int:
  ll = len(lenc)
  r = 0
  for i, c in enumerate(reversed(s)):
    r += ldec[c] * ll**i
  return r


def enc(n: int) -> str:
  ll = len(lenc)
  r = []
  while True:
    n, m = divmod(n, ll)
    r.append(lenc[m])
    if n == 0:
      break
  return "".join(reversed(r))


doubles = set(map("".join, zip(lenc, lenc, strict=True)))


def valid(n: int):
  p = enc(n)
  seq3 = any(ord(c0) == ord(c1) - 1 == ord(c2) - 2 for c0, c1, c2 in zip(p, p[1:], p[2:], strict=False))
  pairs = set(map("".join, pairwise(p)))
  pair2 = len(pairs & doubles) >= 2
  return seq3 and pair2


gen = filter(valid, count(dec(old)))
new = next(gen)
newnew = next(gen)
print(enc(new), enc(newnew))
