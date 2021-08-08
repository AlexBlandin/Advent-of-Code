# *l,=map(int, open("data/day1.txt").readlines())
# i={}
# for x in l:
  # if x not in i:
    # i[2020-x]=x
  # else:
    # print(x * i[x])
    # break

from itertools import combinations
from operator import itemgetter
try:
  from math import prod # 3.9
except:
  from functools import reduce
  from operator import mul
  def prod(iterable, start=1): return reduce(mul, iterable, initial=start) # not 3.9 (ie, pypy)
# print(list(filter(lambda x:x[0]==2020, map(lambda x: (sum(x),prod(x)),combinations(l,3))))[0][1])

print(*[list(map(itemgetter(1),filter(lambda x:x[0]==2020, map(lambda x: (sum(x),prod(x)),combinations(map(int, open("data/day1.txt").readlines()),n)))))[0] for n in (2,3)])
