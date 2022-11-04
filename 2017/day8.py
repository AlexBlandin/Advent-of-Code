from collections import defaultdict
from pathlib import Path

lines = Path("day8.txt").read_text().splitlines()
regs, peak = defaultdict(int), 0
for line in lines:
  reg, op, n, _, creg, cond, cval = line.split()
  n, cval, do = int(n), int(cval), False
  match cond:
    case "<":
      do = regs[creg] < cval
    case ">":
      do = regs[creg] > cval
    case "==":
      do = regs[creg] == cval
    case "!=":
      do = regs[creg] != cval
    case "<=":
      do = regs[creg] <= cval
    case ">=":
      do = regs[creg] >= cval
  if do:
    if op == "inc": regs[reg] += n
    elif op == "dec": regs[reg] -= n
  peak = max(regs[reg], peak)
print(max(regs.values()), peak)
