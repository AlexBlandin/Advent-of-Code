from collections import Counter, defaultdict
from itertools import combinations, chain
from operator import itemgetter
from pathlib import Path
from parse import parse


def kv_sort(d):
  return dict(sorted(sorted(d.items(), key=itemgetter(0)), key=itemgetter(1)))


D, C = defaultdict(int), set()
for line in Path("day13.txt").read_text().splitlines():
  if p := parse("{} would {} {:d} happiness units by sitting next to {}.", line):
    a, gain, d, b = p.fixed  # type: ignore
    a, b = min(a, b), max(a, b)
    D[(a, b)] += d if gain == "gain" else -d
    C |= {a, b}
D = kv_sort(D)


def delta(c):
  return sum(map(D.get, c))  # type: ignore


def hamiltonian(c):
  d, _s = list(Counter(chain(map(itemgetter(0), c), map(itemgetter(1), c))).values()), set(c)
  return d.count(2) == len(d) and {a for b in c for a in b} == C


optimal = max(filter(hamiltonian, combinations(iter(D), len(C))), key=delta)
assert delta(optimal) == 733  # 8s on 8700k, 10s on 4700U

for a in C:
  D[("Alex", a)] = 0
D = kv_sort(D)
C.add("Alex")

with_me = max(filter(hamiltonian, combinations(iter(D), len(C))), key=delta)
assert delta(with_me) <= 755  # 258s on 8700k, 345s on 4700U # 755 is too high???

print(delta(optimal), delta(with_me))

print(sum({c: D[c] for c in optimal}.values()), {c: D[c] for c in optimal})
print(sum({c: D[c] for c in with_me}.values()), {c: D[c] for c in with_me})
