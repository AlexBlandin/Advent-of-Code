from pathlib import Path

m = list(map(int, Path("day15.txt").read_text().split(","))) # and False or [0,3,6]
sm, im = set(m[:-1]), {n: i for i, n in enumerate(m, 1)}
for i in range(len(m), 30000000):
  n = m[-1]
  if n not in sm:
    m += [0]
    sm.add(n)
    im[n] = i
  else:
    a = i - im[n]
    im[n] = i
    m += [a]

print(m[2020 - 1], m[-1])
