from itertools import combinations
from operator import itemgetter
from math import prod

# print(list(filter(lambda x:x[0]==2020, map(lambda x: (sum(x),prod(x)),combinations(l,3))))[0][1])
print(*[list(map(itemgetter(1),filter(lambda x:x[0]==2020, map(lambda x: (sum(x),prod(x)),combinations(map(int, open("day1.txt").readlines()),n)))))[0] for n in (2,3)])
