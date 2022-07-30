from collections import Counter
from pathlib import Path

from tqdm import tqdm

lines = Path("data/day14.txt").read_text().splitlines()
base = lines[0]
insert, letters, pairs = {}, Counter(base), Counter(zip(base, base[1:]))
for rule in lines[2:]:
  pair, mid = rule.split(" -> ", maxsplit = 1)
  insert[tuple(pair)] = mid

def ex(insert: dict, letters: Counter, pairs: Counter):
  for p, n in list(pairs.items()):
    p0, p1 = p
    l = insert[p]
    pairs[p] -= n
    letters[l] += n
    pairs[(p0, l)] += n
    pairs[(l, p1)] += n

for i in tqdm(range(40)):
  ex(insert, letters, pairs)
  if i == 9:
    c = max(letters.values()) - min(letters.values())
d = max(letters.values()) - min(letters.values())

print(c, d)
