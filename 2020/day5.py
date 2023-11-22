from pathlib import Path

lines = Path("day5.txt").read_text().splitlines()
print(
  max(s := sorted([int(s[:7].replace("B", "1").replace("F", "0"), 2) * 8 + int(s[7:-1].replace("R", "1").replace("L", "0"), 2) for s in lines])),
  next(iter(set(range(s[0], s[-1] + 1)) - set(s))),
)
