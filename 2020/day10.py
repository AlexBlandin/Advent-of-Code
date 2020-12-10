a = [0]+sorted([int(l.strip()) for l in open("data/day10.txt").readlines()])
a += [a[-1]+3]
b, G = [y-x for x,y in zip(a,a[1:])], {x:[y for y in range(x+1,x+4) if y in a] for x in a}

from functools import lru_cache
@lru_cache()
def rec(x): return 1 if x==a[-1] else sum(rec(y) for y in G[x])
print(b.count(1)*b.count(3), rec(0))
