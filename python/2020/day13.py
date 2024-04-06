from math import ceil
from operator import itemgetter
from pathlib import Path

e, s = tuple(Path("day13.txt").read_text().splitlines())
e, s = int(e), [int(i) if i != "x" else None for i in s.split(",")]
bus = [(ceil(e / i) * i, i) for i in s if i]
mes, (mo, mx) = (
  [((b - o) % b, b) for o, b in enumerate(s) if b and b],
  max(filter(itemgetter(1), enumerate(s)), key=itemgetter(1)),
)
contest = next(T for T in range(999999999999222, 10**14, -mx) if all(T % b == o for o, b in mes))
print((min(bus)[0] - e) * min(bus)[1], contest)

# should take ~4 mins at magic 1op 4GHz (1047729918510 T in range(10**14,10**15,859), ~10**12 / 4*10**9 is ~250s)
# back of napkin for C is avg. ~3op per, took 1.5m, this should take proportionally ~100x as long
# pypy takes 82m, so within expectations

# print(", ".join(f"n%{b} == {o}" for o,b in mes)) # to plug into WA
# n%19 == 0, n%41 == 32, n%859 == 840, n%23 == 19, n%13 == 7, n%17 == 15, n%29 == 10, n%373 == 323, n%37 == 24
# n = 1361317053288127m + 905694340256752     (so constant is earliest result aka m=0 aka intersection)
# print((min(bus)[0]-e)*min(bus)[1], 905694340256752) # thanks WA
