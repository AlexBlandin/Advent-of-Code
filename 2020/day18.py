from operator import add, mul

with open("data/day18.txt") as o:
  lines = [line.strip() for line in o]

# Examples
# lines = ["1 + (2 * 3) + (4 * (5 + 6))","2 * 3 + (4 * 5)","5 + (8 * 3 + 9 + 3 * 4 * 3)", "5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))", "((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2"]

class dot(dict): # as in a "dot dict", a dict you can access by a "."
  __getattr__, __setattr__ = dict.__getitem__, dict.__setitem__

results1 = []
for line in lines:
  stack, acc, op, set_op = [], 0, add, False
  # stack grows on "(", pushing (acc,op) pair, pops on ")" and sets acc = top.op(top.acc,pop.acc) then pops the old (acc,op) so we can add on next "("
  # if starts "(" we push (0,add) and so carry forward acc on subsequent ")" (basically it's pretending to be a no-op preserving acc)
  # print(line)
  for section in line.split():
    # print(section,end=" ")
    while section[0]=="(":
      section=section[1:]
      stack.append(dot(acc=acc,op=op))
      acc,op=0,add # so we can have multiple nestings
    to_pop = section.count(")")
    if to_pop > 0: section=section[:-to_pop]
    if section in "*+": 
      op = {"*":mul,"+":add}[section]
      set_op=True
    elif set_op:
      acc=op(acc,int(section))
      set_op=False
    else:
      acc=int(section)
    while to_pop > 0:
      to_pop -= 1
      top = stack.pop()
      acc = top.op(top.acc, acc)
    # print(acc, op, set_op, stack)
  # print(f"{line} = {acc}")
  results1.append(acc)

from dataclasses import dataclass
results2 = []
log=[]
@dataclass
class Moon:
  x: int
  def __add__(self, o):  return Moon(self.x*o.x)# if isinstance(o, Moon) else Moon(self.x*o)
  def __radd__(self, o): return Moon(self.x*o.x)# if isinstance(o, Moon) else Moon(self.x*o)
  def __mul__(self, o):  return Moon(self.x+o.x)# if isinstance(o, Moon) else Moon(self.x+o)
  def __rmul__(self, o): return Moon(self.x+o.x)# if isinstance(o, Moon) else Moon(self.x+o)

for line in lines:
  log.append(line)
  for i in range(1,10): line = line.replace(f"{i}", f"Moon({i})")
  line = line.replace("*","-").replace("+","*").replace("-","+")
  res = eval(line, globals()).x
  log[-1]=f"{log[-1]} -> {line} = {res}"
  results2.append(res)

# print("\n".join(log[:5]))
print(sum(results1), sum(results2))
