from random import sample
from parse import findall
try:
  from math import prod # 3.9
except:
  from functools import reduce
  from operator import mul
  def prod(iterable, start=1): return reduce(mul, iterable, initial=start) # not 3.9 (ie, pypy)
samples = lambda s,k: sample(sorted(s),k) # 3.9 why you do this to me?

with open("data/day16.txt") as o:
  lines = [line.strip() for line in o.readlines()]

mine = [int(n) for n in lines[lines.index("your ticket:")+1].split(",")]
scanned = [[int(n) for n in line.split(",")] for line in lines[lines.index("nearby tickets:")+1:]]
field_count = len(scanned[0])
inverse, rules = {},{}
for rule in findall("{}: {:d}-{:d} or {:d}-{:d}", " ".join(lines[:lines.index("your ticket:")-1])):
  field,a,b,x,y=rule.fixed
  field = field.strip()
  rules[field] = (range(a,b+1),range(x,y+1))
  for n in list(range(a,b+1))+list(range(x,y+1)): inverse.setdefault(n,set()).add(field)
# inverse = {k:set(v) for k,v in inverse.items()}
ruleset = set(rules.keys())
assert(len(ruleset)==field_count)

errors = [value for ticket in scanned for value in ticket if value not in inverse]
scanned = [ticket for ticket in scanned if all(value in inverse for value in ticket)]

multiple = {k:v for k,v in inverse.items() if len(v)>1}
single = {k:v for k,v in inverse.items() if len(v)==1}

# ideally, we can do THIS but in some ever decreasing manner, with forced moves cascading to a (the?) solution
fields = [set.intersection(*[inverse[field] for field in [ticket[i] for ticket in scanned]]) for i in range(field_count)]

# do without full SAT solver, just by DPLL elimination
solved = [None]*field_count
while max(map(len,fields)):
  tomb = set()
  for i,candidates in enumerate(fields):
    if len(candidates)==1:
      solved[i]=candidates.pop()
      tomb.add(solved[i])
  for candidates in fields:
    candidates -= tomb
departure = [mine[i] for i,rule in enumerate(solved) if rule.startswith("departure")]
# print(solved)
# print(departure)
print(sum(errors), prod(departure))
