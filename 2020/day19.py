from pathlib import Path

rules_, msgs = tuple(map(str.splitlines, Path("day19.txt").read_text(encoding="utf8").split("\n\n", maxsplit=1)))

rules = {}  # { num : [[num]] } # except 86:"a" and 52:"b" which are special cases
for line in rules_:
  num, rule = line.split(":")
  num, rule = int(num), str(rule).strip()
  rules[num] = rule if rule in {'"a"', '"b"'} else [list(map(int, option.split())) for option in rule.split("|")]

for _msg in msgs: ...
