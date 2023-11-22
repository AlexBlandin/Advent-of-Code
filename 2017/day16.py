from pathlib import Path
from string import ascii_lowercase

moves = Path("day16.txt").read_text().split(",")
tidied: list[tuple[int, int, int]] = []
for move in moves:
  if move[0] == "s":
    tidied.append((0, int(move[1:]), 0))
  else:
    a, b = move[1:].split("/")
    if move[0] == "x":
      tidied.append((1, int(a), int(b)))
    else:
      tidied.append((2, ascii_lowercase.index(a), ascii_lowercase.index(b)))
moves = tidied

def repeat(moves: list[tuple[int, int, int]]):
  while True:
    yield from iter(moves)

def dance(steps: int, moves: list[tuple[int, int, int]], programs: list[int]):
  loop = {}
  for i, (t, a, b) in zip(range(steps), repeat(moves), strict = False):
    if t == 0:
      programs = programs[-a:] + programs[:-a]
    else:
      if t == 2:
        a, b = programs.index(a), programs.index(b)
      programs[a], programs[b] = programs[b], programs[a]
    state = (i % len(moves), tuple(programs))
    if state in loop: # use repeating pattern for speedup
      return dance(steps % i, moves, list(range(16)))
    loop[state] = i
  return "".join([ascii_lowercase[p] for p in programs])

print(dance(len(moves), moves, list(range(16))), dance(1000000000 * len(moves), moves, list(range(16))))
