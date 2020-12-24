from parse import findall
with open("data/day16.txt") as o: lines=[line.strip() for line in o.readlines()]
mine=[int(n) for n in lines[lines.index("your ticket:")+1].split(",")]
scanned=[[int(n) for n in line.split(",")] for line in lines[lines.index("nearby tickets:")+1:]]
inverse = {}
for rule in findall("{}: {:d}-{:d} or {:d}-{:d}", " ".join(lines[:lines.index("your ticket:")-1])):
  field,a,b,x,y=rule.fixed
  field=field.strip()
  for n in list(range(a,b+1))+list(range(x,y+1)): inverse.setdefault(n,[]).append(field)
inverse = {k:set(v) for k,v in inverse.items()}
errors = [value for ticket in scanned for value in ticket if value not in inverse]
scanned = [ticket for ticket in scanned if all(value in inverse for value in ticket)]
multiple = {k:v for k,v in inverse.items() if len(v)>1}
single = {k:v for k,v in inverse.items() if len(v)==1}

fields = [set.union(*[inverse[field] for field in [ticket[i] for ticket in scanned]]) for i in range(len(scanned[0]))]

"""
OH GOODIE, NOW WE SAT SOLVE. THAT SOUNDS SO VERY FUN. YAY.
"""

print(sum(errors))
