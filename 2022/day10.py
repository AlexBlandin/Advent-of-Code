from pathlib import Path

ops = list(map(str.split, Path("day10.txt").read_text().splitlines()))
x, c, s, screen = 1, 1, 0, [[False for _ in range(40)] for _ in range(6)]
def step(c, x):
  j, i = divmod(c - 1, 40)
  if i in (x - 1, x, x + 1): screen[j][i] = True
  return c * x if (c - 20) % 40 == 0 else 0
for op in ops:
  s += step(c, x)
  c += 1
  if len(op) == 2:
    s += step(c, x)
    c += 1
    x += int(op[1])

print(s, "\n".join("".join("#" if c else "." for c in row) for row in screen), sep = "\n")
