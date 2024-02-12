from collections import Counter, defaultdict
from itertools import chain, combinations
from operator import itemgetter
from pathlib import Path

distances = defaultdict(int)
connected = set()
for line in Path("day9.txt").read_text().splitlines():
  match line.split():
    case [a, "to", b, "=", d]:
      a, b = min(a, b), max(a, b)
      distances[(a, b)] = int(d)
      connected |= {a, b}


def distance(c: tuple[tuple[str, str], ...]) -> int:
  return sum(filter(None, map(distances.get, c)))


def hamiltonian(connection: tuple[str, str]):
  dists = list(Counter(chain(map(itemgetter(0), connection), map(itemgetter(1), connection))).values())
  return dists.count(1) + dists.count(2) == len(dists) and {a for b in connection for a in b} == connected


ham = tuple(filter(hamiltonian, combinations(iter(distances), len(connected) - 1)))  # type: ignore
mn = min(ham, key=distance)
mx = max(ham, key=distance)
print(distance(mn), distance(mx))
