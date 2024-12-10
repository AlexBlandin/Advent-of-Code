from collections import defaultdict
from pathlib import Path

lines = Path("day4.txt").read_text().splitlines()
trans = ["".join(s) for s in zip(*lines)]
diagonals, antidiags = defaultdict(list), defaultdict(list)
for i, row in enumerate(lines):
  for j, a in enumerate(row):
    diagonals[i + j].append(a)
    antidiags[i - j].append(a)
diags, adias = ["".join(v) for v in diagonals.values()], ["".join(v) for v in antidiags.values()]
xmas = {
  tuple(g.translate({ord("1"): letter1, ord("2"): letter2, ord("3"): letter3, ord("4"): letter4}) for g in group)
  for group in (
    ("M1S", "2A3", "M4S"),
    ("S1M", "2A3", "S4M"),
    ("M1M", "2A3", "S4S"),
    ("S1S", "2A3", "M4M"),
  )
  for letter1 in "XMAS"
  for letter2 in "XMAS"
  for letter3 in "XMAS"
  for letter4 in "XMAS"
}

print(
  sum(s.count("XMAS") + s.count("SAMX") for s in lines)
  + sum(s.count("XMAS") + s.count("SAMX") for s in trans)
  + sum(s.count("XMAS") + s.count("SAMX") for s in diags)
  + sum(s.count("XMAS") + s.count("SAMX") for s in adias),
  sum(
    ((lines[i - 1][j - 1 : j + 2], lines[i][j - 1 : j + 2], lines[i + 1][j - 1 : j + 2]) in xmas)
    for i in range(len(lines))
    for j in range(len(trans))
    if 1 <= i < len(lines) - 1 and 1 <= j < len(lines) - 1
  ),
)
