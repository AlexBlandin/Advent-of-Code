a=sorted([0]+[int(l.strip())for l in open("data/day10.txt").readlines()])
a+=[a[-1]+3]
d,b=a[-1],[y-x for x,y in zip(a,a[1:])]

from itertools import product
G,g={},[(x,y) for x,y in product(a,a) if 1<=(y-x)<=3]
for x,y in g: G.setdefault(x,[]).append(y)

from functools import lru_cache
@lru_cache()
def rec(x): return 1 if x==161 else sum(rec(y) for y in G[x])
print(b.count(1)*b.count(3), rec(0))
