from itertools import permutations
from pathlib import Path
lines = Path("data/day8.txt").read_text().splitlines()
n1478 = sum(len(list(filter(lambda x: x<5 or x>6, map(len, line.split(" | ")[1].split())))) for line in lines)
def fl(n, list): return filter(lambda x: len(x)==n, list)
def find_encoding(signals):
  return next(
    dict(zip([zero, one, two, three, four, five, six, seven, eight, nine], map(str,range(10))))
    for one in fl(2, signals)
    for four in fl(4, signals)
    for seven in fl(3, signals)
    for eight in fl(7, signals)
    for two, three, five,*_ in permutations(fl(5, signals))
    for zero, six, nine,*_ in permutations(fl(6, signals))
    for up,mid,down,tl,tr,bl,br in permutations("abcdefg") if
    up not in one and up not in four and
    mid not in zero and mid not in one and mid not in seven and
    down not in one and down not in four and down not in seven and
    tl not in one and tl not in two and tl not in three and tl not in seven and
    tr not in five and tr not in six and
    bl not in one and bl not in three and bl not in four and bl not in five and bl not in seven and bl not in nine and
    br not in two and
    True
  )
result = 0
for line in lines:
  signals, values, *_ = " ".join(map("".join,map(sorted, line.split()))).split(" | ")
  sl, vl = set(signals.split()), values.split()
  result += int("".join(map(find_encoding(sl).get, vl)))
print(n1478, result)
