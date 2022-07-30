from operator import itemgetter
from pathlib import Path
from parse import parse

lines = Path("data/day13.txt").read_text().splitlines()
dots, folds = [], []
for line in lines:
  if p := parse("{:d},{:d}", line):
    dots.append(p.fixed)
  elif p := parse("fold along {}={:d}", line):
    folds.append(p.fixed)
w, h = max(map(itemgetter(0), dots)), max(map(itemgetter(1), dots))
