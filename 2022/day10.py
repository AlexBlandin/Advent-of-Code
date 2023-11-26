from pathlib import Path

ops = list(map(str.split, Path("day10.txt").read_text().splitlines()))
x, c, s, screen = 1, 0, 0, [[False for _ in range(40)] for _ in range(6)]

def step(c, x):
  j, i = divmod(c, 40)
  if x - 1 <= i <= x + 1:
    screen[j][i] = True
  return 0 if (c - 19) % 40 else (c + 1) * x

for op in ops:
  s += step(c, x)
  c += 1
  if len(op) == 2:
    s += step(c, x)
    c += 1
    x += int(op[1])

print(
  s,
  "\n".join("".join("#" if c else "." for c in row) for row in screen),
  sep = "\n",
)
