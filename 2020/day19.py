with open("data/day19.txt") as o:
  rules_, msgs = tuple(map(str.splitlines, o.read().split("\n\n", maxsplit = 1)))
  msgs: list[str]

rules = {} # { num : [[num]] } # except 86:"a" and 52:"b" which are special cases
for line in rules_:
  num, rule = line.split(":")
  num, rule = int(num), str(rule).strip()
  rules[num] = rule if rule in ['"a"', '"b"'] else [list(map(int, option.split())) for option in rule.split("|")]

for msg in msgs:
  ...