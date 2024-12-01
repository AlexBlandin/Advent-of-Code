from collections import Counter
from operator import itemgetter, sub
from pathlib import Path

lines = Path("day1.txt").read_text().splitlines()
# lines = """3   4
# 4   3
# 2   5
# 1   3
# 3   9
# 3   3""".splitlines()

pairs: list[tuple[int, int]] = [tuple(map(int, line.split())) for line in lines]
left, right = sorted(map(int, map(itemgetter(0), pairs))), sorted(map(int, map(itemgetter(1), pairs)))
diff = map(abs, map(sub, left, right))
count = Counter(right)
similarity = [n * count[n] for n in left]

print(
  sum(diff),
  sum(similarity),
)
