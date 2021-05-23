from operator import add, mul

with open("data/day18.txt") as o:
  lines = [line.strip() for line in o]

class dot(dict): # as in a "dot dict", a dict you can access by a "."
  __getattr__, __setattr__ = dict.__getitem__, dict.__setitem__

results = []
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
  results.append(acc)

print(sum(results))
