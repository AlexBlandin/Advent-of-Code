from pathlib import Path

gs = Path("day6.txt").read_text().split("\n\n")
print(
  sum([len(set(g) - set("\n")) for g in gs]),
  sum([len(set.intersection(*g)) for g in [list(map(set, g.splitlines())) for g in gs]]),
)
