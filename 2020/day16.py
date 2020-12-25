from random import sample
from parse import findall
samples = lambda s,k: sample(sorted(s),k) # 3.9 why you do this to me?

with open("data/day16-1.txt") as o:
  lines = [line.strip() for line in o.readlines()]

mine = [int(n) for n in lines[lines.index("your ticket:")+1].split(",")]
scanned = [[int(n) for n in line.split(",")] for line in lines[lines.index("nearby tickets:")+1:]]
inverse, rules = {},{}
for rule in findall("{}: {:d}-{:d} or {:d}-{:d}", " ".join(lines[:lines.index("your ticket:")-1])):
  field,a,b,x,y=rule.fixed
  field=field.strip()
  rules[field] = (range(a,b+1),range(x,y+1))
  for n in list(range(a,b+1))+list(range(x,y+1)): inverse.setdefault(n,[]).append(field)
inverse = {k:set(v) for k,v in inverse.items()}
ruleset = set(rules.keys())

errors = [value for ticket in scanned for value in ticket if value not in inverse]
scanned = [ticket for ticket in scanned if all(value in inverse for value in ticket)]

multiple = {k:v for k,v in inverse.items() if len(v)>1}
single = {k:v for k,v in inverse.items() if len(v)==1}

# ideally, we can do THIS but in some ever decreasing manner, with forced moves cascading to a (the?) solution
fields = [set.union(*[inverse[field] for field in [ticket[i] for ticket in scanned]]) for i in range(len(scanned[0]))]

# at least 19 rules per field... so they could be anything x_x
# print(min(min(len(inverse[field]) for field in ticket) for ticket in scanned))

"""
OH GOODIE, NOW WE SAT SOLVE. THAT SOUNDS SO VERY FUN. YAY.
"""
from z3 import *



print(sum(errors))
