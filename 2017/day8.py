from collections import defaultdict
from pathlib import Path

lines = Path("day8.txt").read_text().splitlines()
regs, peak = defaultdict(int), 0
for line in lines:
  reg, op, n, _, creg, cond, cval = line.split()
  n, cval, do_op = int(n), int(cval), False
  match cond:
    case "<":
      do_op = regs[creg] < cval
    case ">":
      do_op = regs[creg] > cval
    case "==":
      do_op = regs[creg] == cval
    case "!=":
      do_op = regs[creg] != cval
    case "<=":
      do_op = regs[creg] <= cval
    case ">=":
      do_op = regs[creg] >= cval
  match op:
    case "inc" if do_op:
      regs[reg] += n
    case "dec" if do_op:
      regs[reg] -= n
  peak = max(regs[reg], peak)
print(max(regs.values()), peak)
