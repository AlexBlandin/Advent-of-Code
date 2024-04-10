from pathlib import Path

lines = Path("day2.txt").read_text().splitlines()
h, v = 0, 0
a, va = 0, 0
lines = [((ln := line.split())[0], int(ln[1])) for line in lines]
for d, x in lines:
  match d:
    case "forward":
      h += x
      va += x * a
    case "down":
      v += x
      a += x
    case "up":
      v -= x
      a -= x
      if v < 0:
        v = 0
print(h * v, h * va)
