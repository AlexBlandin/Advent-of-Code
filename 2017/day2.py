from pathlib import Path

lines = list(map(lambda s: list(map(int, s.split())), Path("day2.txt").read_text().splitlines()))
print(
  sum(max(line) - min(line) for line in lines),
  sum(next(max(a // b, b // a) for i, a in enumerate(line) for b in line[i + 1:] if a % b == 0 or b % a == 0) for line in lines),
)
