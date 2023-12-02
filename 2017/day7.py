from statistics import mode
from functools import cache
from pathlib import Path

lines = Path("day7.txt").read_text().splitlines()
up, down, masses = {}, {}, {}
for line in lines:
  match line.split():
    case [name, mass]:
      masses[name] = int(mass.removeprefix("(").removesuffix(")"))
      if name not in up:
        up[name] = None
      if name not in down:
        down[name] = None
    case [name, mass, "->", *kids]:
      masses[name] = int(mass.removeprefix("(").removesuffix(")"))
      if name not in up:
        up[name] = None
      if name not in down:
        down[name] = None
      kids = list(map(lambda s: s.removesuffix(","), kids))
      down[name] = kids
      for kid in kids:
        up[kid] = name
root = next(iter(up))
while up[root]:
  root = up[root]


@cache
def weight(node: str) -> int:  # shhh I know that's not right, but shhh
  if down[node]:
    return masses[node] + sum(weight(kid) for kid in down[node])
  else:
    return masses[node]


def balance(node: str) -> int | None:
  kids = down[node]
  if kids:
    ws = list(map(weight, kids))
    correct = mode(ws)
    index = 0
    for i, w in enumerate(ws):
      if w != correct:
        index = i
        break
    else:
      return 0
    if b := balance(kids[index]):
      return b
    else:
      return correct - ws[index] + masses[kids[index]]


print(root, balance(root))
