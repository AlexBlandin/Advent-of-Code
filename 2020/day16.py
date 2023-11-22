from collections import defaultdict
from pathlib import Path
from parse import findall
from math import prod

lines = Path("day16.txt").read_text().splitlines()
mine = [int(n) for n in lines[lines.index("your ticket:") + 1].split(",")]
scanned = [[int(n) for n in line.split(",")] for line in lines[lines.index("nearby tickets:") + 1:]]
inverse: defaultdict[int, set[str]] = defaultdict(set)
rules = {}
for rule in findall("{}: {:d}-{:d} or {:d}-{:d}", "\n".join(lines[:lines.index("your ticket:") - 1])):
  field, a, b, x, y = rule.fixed # type: ignore
  field = field.strip()
  rules[field] = (range(a, b + 1), range(x, y + 1))
  for n in list(range(a, b + 1)) + list(range(x, y + 1)):
    inverse[n].add(field)
ruleset = set(rules.keys())
field_count = len(ruleset)

errors = [value for ticket in scanned for value in ticket if value not in inverse]
scanned = [ticket for ticket in scanned if all(value in inverse for value in ticket)]

solved = [""] * field_count
fields = [set.intersection(*[inverse[field] for field in [ticket[i] for ticket in scanned]]) for i in range(field_count)]
while max(map(len, fields)):
  for i, candidates in enumerate(fields):
    if len(candidates) == 1:
      solved[i] = candidates.pop() # so they're emptied as it goes
      for others in fields:
        others.discard(solved[i])
departure = [mine[i] for i, rule in enumerate(solved) if rule.startswith("departure")]

print(sum(errors), prod(departure))
