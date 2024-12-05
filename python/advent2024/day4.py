from collections import defaultdict
from pathlib import Path

lines = Path("day4.txt").read_text().splitlines()
_lines = """MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX""".splitlines()
trans = ["".join(s) for s in zip(*lines)]
assert len(lines) == len(trans)  # squares are easier to reason about # noqa: S101
diagonals: defaultdict[int, list[str]] = defaultdict(list)
antidiags: defaultdict[int, list[str]] = defaultdict(list)
for i, row in enumerate(lines):
  for j, a in enumerate(row):
    diagonals[i + j].append(a)
    antidiags[i - j].append(a)
diags = ["".join(v) for v in diagonals.values()]
adias = ["".join(v) for v in antidiags.values()]
xmas = {
  tuple(g.translate({ord("1"): letter1, ord("2"): letter2, ord("3"): letter3, ord("4"): letter4}) for g in group)
  for group in (
    ("1M2", "MAS", "3S4"),
    ("1S2", "MAS", "3M4"),
    ("1S2", "SAM", "3M4"),
    ("1M2", "SAM", "3S4"),
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
xxmas = {
  tuple(g.translate({ord("1"): letter1, ord("2"): letter2, ord("3"): letter3, ord("4"): letter4}) for g in group)
  for group in (
    ("1M2", "MAS", "3S4"),
    ("1S2", "MAS", "3M4"),
    ("1S2", "SAM", "3M4"),
    ("1M2", "SAM", "3S4"),
    ("M1S", "2A3", "M4S"),
    ("S1M", "2A3", "S4M"),
    ("M1M", "2A3", "S4S"),
    ("S1S", "2A3", "M4M"),
  )
  for letter1 in "MS"
  for letter2 in "MS"
  for letter3 in "MS"
  for letter4 in "MS"
  if letter1 != letter4 and letter2 != letter3
}
mx = len(lines) - 1


def nearby(i: int, j: int, lines=lines, mx=mx) -> tuple[str, str, str]:
  return (
    (lines[i - 1][j - 1 : j + 2], lines[i][j - 1 : j + 2], lines[i + 1][j - 1 : j + 2])
    if 1 <= i < mx and 1 <= j < mx
    else ("", "", "")
  )


print(
  sum(s.count("XMAS") + s.count("SAMX") for s in lines)
  + sum(s.count("XMAS") + s.count("SAMX") for s in trans)
  + sum(s.count("XMAS") + s.count("SAMX") for s in diags)
  + sum(s.count("XMAS") + s.count("SAMX") for s in adias),
  sum((nearby(i, j) in xxmas) + (nearby(i, j) in xmas) for i in range(len(lines)) for j in range(len(trans))),
)
# 1933 is too high
