from parse import *
from operator import add, mul

with open("data/day18.txt") as o:
  lines = [line.strip() for line in o]

@with_pattern(r"[\*\+]")
def parse_op(text):
  return {"*": mul, "+": add}[text]

results, log = [], []
for line in lines:
  
  simple = findall("{a:d} {op:Op} {b:d}", line, {"Op":parse_op}) # they have their .named values and .spans (lets us navigate)
  parens = findall("{a:d} {op:Op} (", line, {"Op":parse_op})
  
  results.append()
  log.append((,))
