from itertools import combinations, chain
from collections import Counter
from operator import itemgetter
from pathlib import Path
from parse import parse

lines = Path("data/day9.txt").read_text().splitlines()
kv_sort = lambda d: dict(sorted(sorted(d.items(), key=itemgetter(0)), key=itemgetter(1)))
D, C = {}, set()

for line in lines:
  if p := parse("{} to {} = {:d}", line):
    a,b,d = p.fixed
    a,b = min(a,b),max(a,b)
    D[(a,b)] = d
    C |= {a,b}
D = kv_sort(D)

def distance(c: tuple):
  return sum(map(D.get, c))

def hamiltonian(c):
  d, s = list(Counter(chain(map(itemgetter(0),c),map(itemgetter(1),c))).values()), set(c)
  return d.count(1)+d.count(2)==len(d) and {a for b in c for a in b} == C and not any(True for a,b in c if (b,a) in s)

mn = min(filter(hamiltonian, combinations(iter(D),len(C)-1)), key=distance)
mx = max(filter(hamiltonian, combinations(iter(D),len(C)-1)), key=distance)
print(distance(mn), distance(mx))
# print({*map(" -> ".join, mn)})
# print({*map(" -> ".join, mx)})
# print(C)
