from pathlib import Path

lines = Path("day3.txt").read_text().splitlines()
lines = [[int(c) for c in ln] for ln in lines]
cols = list(zip(*lines, strict = True))

def avg(x):
  return sum(x) / max(len(x), 1)

gb = [int(0.5 + avg(c)) for c in cols]
eb = [0 if b else 1 for b in gb]
g = int("".join(map(str, gb)), 2)
e = int("".join(map(str, eb)), 2)
ox, co = set(range(len(lines))), set(range(len(lines)))

def at(ln, ls):
  return [ln[i] for i in ls]

oxy, co2 = 0, 0
for c in cols:
  if len(ox) == 1:
    oxy = int("".join(map(str, lines[ox.pop()])), 2)
  if len(co) == 1:
    co2 = int("".join(map(str, lines[co.pop()])), 2)
  ao, ac = avg(at(c, ox)), avg(at(c, co))
  ox = set(filter(lambda i: c[i], ox)) if ao == 0.5 else set(filter(lambda i: c[i] == int(0.5 + ao), ox))
  co = set(filter(lambda i: not c[i], co)) if ac == 0.5 else set(filter(lambda i: c[i] != int(0.5 + ac), co))
print(g * e, oxy * co2)
