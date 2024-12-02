from collections import Counter
from operator import itemgetter, sub
from pathlib import Path

lines = Path("day1.txt").read_text().splitlines()

pairs: list[tuple[int, int]] = [tuple(map(int, line.split())) for line in lines]
left, right = sorted(map(int, map(itemgetter(0), pairs))), sorted(map(int, map(itemgetter(1), pairs)))
diff = map(abs, map(sub, left, right))
count = Counter(right)
similarity = [n * count[n] for n in left]

print(
  sum(diff),
  sum(similarity),
)

# ruff: noqa: B905 E402
import collections
import itertools
import operator
import pathlib

print(
  *(
    sum(foo(bar(a)))
    for foo, bar, a in zip(
      (lambda a: map(abs, map(operator.sub, next(a), next(a))), lambda a: (n * a[1][n] for n in a[0])),
      (lambda a: iter(a), lambda a: (next(a), collections.Counter(next(a)))),
      itertools.tee(
        list(map(sorted, zip(*(map(int, line.split()) for line in pathlib.Path("day1.txt").read_text().splitlines()))))
      ),
    )
  )
)
