from operator import itemgetter, or_
from pathlib import Path
from parse import parse

lines = Path("data/day13.txt").read_text().splitlines()
dots, folds = [], []
for line in lines:
  if p := parse("{:d},{:d}", line):
    dots.append(p.fixed)
  elif p := parse("fold along {}={:d}", line):
    folds.append(p.fixed)

w, h = max(map(itemgetter(0), dots)) + 1, max(map(itemgetter(1), dots)) + 1
paper = [[False] * w for _ in range(h)]
for x, y in dots:
  paper[y][x] = True

def fold_over(line: int):
  for row in paper:
    a, b = row[:line], row[line + 1:]
    if len(a) < len(b):
      a += [False] * (len(a) - len(b))
    else:
      b += [False] * (len(b) - len(a))
    row[:] = list(map(or_, a, reversed(b)))

def fold_up(line: int):
  a, b = paper[:line], paper[line + 1:]
  if len(a) < len(b):
    a += [[False] * w for _ in range(len(a) - len(b))]
  else:
    b += [[False] * w for _ in range(len(b) - len(a))]
  paper[:] = [list(map(or_, ra, rb)) for ra,rb in zip(a, reversed(b))]

first_fold, first_line = folds.pop(0)
if first_fold == "x": fold_over(first_line)
else: fold_up(first_line)
print(sum(map(sum, paper)))

for fold, line in folds:
  if fold == "x": fold_over(line)
  else: fold_up(line)

for row in paper:
  print("".join(map(lambda b: "#" if b else ".", row)))
