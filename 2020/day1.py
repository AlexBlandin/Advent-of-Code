from itertools import combinations
from operator import itemgetter
from pathlib import Path
from math import prod

# print(list(filter(lambda x:x[0]==2020, map(lambda x: (sum(x),prod(x)),combinations(l,3))))[0][1])
print(*[
  next(
    map(itemgetter(1), filter(lambda x: x[0] == 2020, map(lambda x: (sum(x), prod(x)), combinations(map(int, Path("day1.txt").read_text().splitlines()), n))))
  )
  for n in (2, 3)
])  # what an amazing auto formatting job
