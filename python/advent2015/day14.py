from operator import itemgetter
from pathlib import Path

from parse import parse

lines = Path("day14.txt").read_text().splitlines()
R = {}
for line in lines:
  if p := parse("{} can fly {:d} km/s for {:d} seconds, but then must rest for {:d} seconds.", line):
    w, s, d, r = p.fixed  # who, speed, duration, rest
    R[w] = (s, d, r)


def distance(r, T=2503):
  s, d, r = R[r]
  m, n = divmod(T, d + r)
  return s * d * m + s * min(d, n)


def points(T=2503):
  P = {r: 0 for r in R}
  for s in range(1, T + 1):
    D = dict(sorted(zip(iter(R), (distance(r, s) for r in R), strict=False), key=itemgetter(1), reverse=True))
    m = max(D.values())
    for r, d in D.items():
      if d == m:
        P[r] += 1
      else:
        break
  return max(P.values())


r = max(iter(R), key=distance)
p = points()
print(distance(r), p)
