from pathlib import Path

b = list(map(tuple, map(str.split, Path("day8.txt").read_text().splitlines())))
h = set()
a, c = 0, 0
while c not in h and c < len(b):
  i, v = b[c]
  h.add(c)
  c += 1
  if i == "acc":
    a += int(v)
  elif i == "jmp":
    c += int(v) - 1
p = a
for s, op in enumerate(b):
  if op[0] in {"jmp", "nop"}:
    pb, b[s] = op, ("jmp" if op == "nop" else "nop", b[s][1])
    h = set()
    a, c = 0, 0
    while c not in h and c < len(b):
      i, v = b[c]
      h.add(c)
      c += 1
      if i == "acc":
        a += int(v)
      elif i == "jmp":
        c += int(v) - 1
    b[s] = pb
    if c >= len(b):
      print(p, a)
      break
