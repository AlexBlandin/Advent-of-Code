parent={}
child={outer:dict(inner + [parent.setdefault(i,set()).add(outer) for i,c in inner]*0) for outer, inner in [(outer,list(map(lambda i: tuple(reversed(i.strip().split(" ",1))), inner.replace("bags","").replace("bag","").replace(".","").split(","))) if "other" not in inner else []) for outer,inner in [tuple(rule.split(" bags contain ",1)) for rule in open("data/day7-1.txt").readlines()]]}
s,l=set(parent.setdefault("shiny gold",set())),len(parent["shiny gold"])
while len(s:=s.union(*[parent[i] for i in s if i in parent]))>l: l=len(s)
def r(c): return 1 if child[c]=={} else sum(int(v)*r(i) for i,v in child[c].items())
print(l,r("shiny gold"))
print(child["shiny gold"])
print(child)