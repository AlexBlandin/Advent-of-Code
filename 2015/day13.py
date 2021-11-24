from collections import Counter, defaultdict
from itertools import combinations, chain
from operator import itemgetter
from pathlib import Path
from parse import parse

lines = Path("data/day13.txt").read_text().splitlines()

D, C = defaultdict(int), set()

for line in lines:
  if p := parse("{} would {} {:d} happiness units by sitting next to {}.", line):
    a, gain, d, b = p.fixed
    a,b = min(a,b),max(a,b)
    D[(a,b)] += d if gain=="gain" else -d
    C |= {a,b}
D = dict(sorted(sorted(D.items(), key=itemgetter(0)), key=itemgetter(1)))

def delta(c):
  return sum(map(D.__getitem__, c))

def hamiltonian(c):
  d, s = list(Counter(chain(map(itemgetter(0),c),map(itemgetter(1),c))).values()), set(c)
  return d.count(2)==len(d) and {a for b in c for a in b} == C and not any(True for a,b in c if (b,a) in s)

optimal = max(filter(hamiltonian, combinations(iter(D),len(C))), key=delta)
# optimal = 733

for a in C: D[("Alex",a)]=0
D = dict(sorted(sorted(D.items(), key=itemgetter(0)), key=itemgetter(1)))
C.add("Alex")

with_me = max(filter(hamiltonian, combinations(iter(D),len(C))), key=delta)
# 755 is too high

print(delta(optimal), delta(with_me)) # optimal takes ~8s, with_me takes ~3m30s (as with_me's search space is ~30x bigger)
