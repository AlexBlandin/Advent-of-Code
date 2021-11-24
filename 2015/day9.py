from collections import Counter, defaultdict
from itertools import combinations, chain
from operator import itemgetter
from pathlib import Path
from parse import parse

lines = Path("data/day9.txt").read_text().splitlines()

G, D, C = defaultdict(set), {}, set()

for line in lines:
  if p := parse("{} to {} = {:d}", line):
    a,b,d = p.fixed
    a,b = min(a,b),max(a,b)
    D[(a,b)] = d
    D[(b,a)] = d
    G[a].add(b)
    C |= {a,b}
D = dict(sorted(D.items(), key=itemgetter(1)))

def distance(c: tuple):
  return sum(map(D.get, c))

def pair(G):
  return {(a,b) for a,c in G.items() for b in c}

def hamiltonian(c):
  d, s = list(Counter(chain(map(itemgetter(0),c),map(itemgetter(1),c))).values()), set(c)
  return d.count(1)+d.count(2)==len(d) and {a for b in c for a in b} == C and not any(True for a,b in c if (b,a) in s)

mn = min(filter(hamiltonian, combinations(pair(G),len(C)-1)), key=distance)
mx = max(filter(hamiltonian, combinations(pair(G),len(C)-1)), key=distance)
print(distance(mn), distance(mx))
# print({*map(" -> ".join, mn)})
# print({*map(" -> ".join, mx)})
# print(C)
