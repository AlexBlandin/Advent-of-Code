import math
from itertools import chain, repeat
from pathlib import Path

lines = Path("day8.txt").read_text().replace("=", "").replace("(", "").replace(",", "").replace(")", "").splitlines()
just_nodes = sorted(set(chain.from_iterable(map(str.split, lines[2:]))))
leftright = [0 if line == "L" else 1 for line in lines[0]]
nodes = {k: (left, right) for k, left, right in map(str.split, lines[2:])}
goal = {node for node in just_nodes if node.endswith("Z")}

path, found_in, found = [node for node in just_nodes if node.endswith("A")], [None for _ in goal], [False for _ in goal]
for i, lr in enumerate(chain.from_iterable(repeat(leftright))):
  for j in range(len(goal)):
    if path[j].endswith("Z") and not found[j]:
      found_in[j] = i
      found[j] = True
    path[j] = nodes[path[j]][lr]
  if all(found):
    break
print(found_in[0], math.lcm(*found_in))
