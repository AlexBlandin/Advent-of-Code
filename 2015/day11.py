from pathlib import Path

lines = Path("day11.txt").read_text().splitlines()
old = lines[0]

lenc = "abcdefghjkmnpqrstuvwxyz"
ldec = dict(zip(lenc, range(len(lenc))))

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
    if n == 0: break
  return "".join(reversed(r))

doubles = set(map("".join, zip(lenc, lenc)))

def valid(n: int):
  p = enc(n)
  seq3 = any(ord(c0) == ord(c1) - 1 == ord(c2) - 2 for c0, c1, c2 in zip(p, p[1:], p[2:]))
  pairs = set(map("".join, zip(p, p[1:])))
  pair2 = len(pairs & doubles) >= 2
  return seq3 and pair2

from itertools import count

gen = filter(valid, count(dec(old)))
new = next(gen)
newnew = next(gen)
print(enc(new), enc(newnew))
