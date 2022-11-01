from collections import Counter
from pathlib import Path

pp = list(map(str.split, Path("day4.txt").read_text().splitlines()))
print(sum(all(c==1 for c in Counter(p).values()) for p in pp), sum(all(c==1 for c in Counter(map(frozenset, p)).values()) for p in pp))
