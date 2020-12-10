from itertools import product
from functools import lru_cache

G, a = {}, [0]+sorted([int(l.strip()) for l in open("data/day10.txt").readlines()])
a += [a[-1]+3]
b, g = [y-x for x,y in zip(a,a[1:])], [(x,y) for x,y in product(a,a) if 1<=(y-x)<=3]
for x,y in g: G.setdefault(x,[]).append(y)

@lru_cache()
def rec(x): return 1 if x==161 else sum(rec(y) for y in G[x])
print(b.count(1)*b.count(3), rec(0))
