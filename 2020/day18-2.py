from parse import *
from operator import add, mul

with open("data/day18.txt") as o:
  lines = [line.strip() for line in o]

@with_pattern(r"[\*\+]")
def parse_op(text):
  return {"*": mul, "+": add}[text]

results, log = [], []
for line in lines:
  # Result() has .named values and .spans (lets us navigate)
  parens = list(findall("(", line))
  closes = list(findall(")", line))
  simple = list(findall("{a:d} {op:Op} {b:d}", line, extra_types=dict(Op=parse_op)))
  leading = list(findall("{a:d} {op:Op} (", line, extra_types=dict(Op=parse_op)))
  trailing = list(findall(") {op:Op} {b:d}", line, extra_types=dict(Op=parse_op)))
  
  # results.append()
  log.append((parens, simple,leading, trailing))

print(log[:3])