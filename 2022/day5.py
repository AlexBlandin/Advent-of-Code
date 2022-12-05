from operator import itemgetter
from pathlib import Path

stacks, moves = Path("day5.txt").read_text().split("\n\n", maxsplit = 1)
stacks = list(filter(None, map(list, map(lambda s: filter(str.isalpha, s), map(list, map(reversed, zip(*stacks.splitlines()[:-1])))))))
stack2 = [s[:] for s in stacks]
moves = list(map(lambda m: list(map(int, filter(str.isnumeric, m))), map(str.split, moves.splitlines())))
for n, a, b in moves:
  a, b = a - 1, b - 1
  for _ in range(n):
    stacks[b].append(stacks[a].pop())
for n, a, b in moves:
  a, b = a - 1, b - 1
  stack2[b] += stack2[a][-n:]
  stack2[a] = stack2[a][:-n]
print("".join(map(itemgetter(-1), stacks)), "".join(map(itemgetter(-1), stack2)))
# QMBMJDFTD NBTVTJNFJ
