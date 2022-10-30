from itertools import accumulate

with open("day1.txt") as o:
  print((s := str(o.read())).count("(") - s.count(")"),
        list(accumulate([1 if c == "(" else -1 for c in s if c in "()"])).index(-1) + 1)
