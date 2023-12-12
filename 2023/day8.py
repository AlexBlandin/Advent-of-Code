import math
from itertools import chain, repeat
from pathlib import Path

lines = Path("day8.txt").read_text().replace("= ", "").replace("(", "").replace(",", "").replace(")", "").splitlines()
just_nodes = sorted(set(chain.from_iterable(map(str.split, lines[2:]))))
leftright, nodes = list(map(lambda line: 0 if line == "L" else 1, lines[0])), {k: (left, right) for k, left, right in map(str.split, lines[2:])}
Z_nodes = {node for node in just_nodes if node.endswith("Z")}
p1_node, p1_found_in = "AAA", None
p2_nodes, p2_found_in, p2_found = [node for node in just_nodes if node.endswith("A")], [None for _ in Z_nodes], [False for _ in Z_nodes]
for i, lr in enumerate(chain.from_iterable(repeat(leftright))):
  if p1_node == "ZZZ" and p1_found_in is None:
    p1_found_in = i
  elif p1_found_in is None:
    p1_node = nodes[p1_node][lr]
  for j in range(len(Z_nodes)):
    node, recur, p2_nodes[j] = p2_nodes[j], p2_found_in[j], nodes[p2_nodes[j]][lr]
    if node.endswith("Z"):
      p2_found_in[j] = i
      p2_found[j] = True
  if all(p2_found):
    break
print(p1_found_in, math.lcm(*p2_found_in))
