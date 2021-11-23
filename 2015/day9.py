from itertools import combinations, repeat
from collections import defaultdict
from operator import itemgetter
from pathlib import Path
from parse import parse

lines = Path("data/day9.txt").read_text().splitlines()
D = {}
G = defaultdict(set)
C = set()
for line in lines:
  if p := parse("{} to {} = {:d}", line):
    a,b,d = p.fixed
    a,b = min(a,b),max(a,b)
    D[(a,b)] = d
    D[(b,a)] = d
    G[a].add(b)
    C |= {a,b}
D = dict(sorted(D.items(), key=itemgetter(1)))

def distance(candidates: tuple):
  return sum(map(D.get, candidates))

def pair(G):
  return set.union(*[set(zip(repeat(a),b)) for a,b in G.items()])

def hamiltonian(c):
  d = defaultdict(int)
  for a,b in c:
    d[a]+=1
    d[b]+=1
  d = list(d.values())
  return d.count(1)+d.count(2)==len(d) and set.union(*[{a,b} for a,b in c]) == C

mn = min(filter(hamiltonian, combinations(pair(G),len(C)-1)), key=distance)
mx = max(filter(hamiltonian, combinations(pair(G),len(C)-1)), key=distance)
print(distance(mn), distance(mx))
# print({*map(" -> ".join, mn)}, {*map(" -> ".join, mx)})
