from collections import Counter
from itertools import pairwise
from pathlib import Path

lines = Path("day14.txt").read_text().splitlines()
base = lines[0]
insert, letters, pairs = {}, Counter(base), Counter(pairwise(base))
for rule in lines[2:]:
  pair, mid = rule.split(" -> ", maxsplit=1)
  insert[tuple(pair)] = mid


def ex(insert: dict, letters: Counter, pairs: Counter):
  for p, n in list(pairs.items()):
    p0, p1 = p
    ln = insert[p]
    pairs[p] -= n
    letters[ln] += n
    pairs[(p0, ln)] += n
    pairs[(ln, p1)] += n


c = 0
for i in range(40):
  ex(insert, letters, pairs)
  if i == 9:
    c = max(letters.values()) - min(letters.values())
d = max(letters.values()) - min(letters.values())

print(c, d)
