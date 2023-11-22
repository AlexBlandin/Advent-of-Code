from pathlib import Path

lines = Path("day2.txt").read_text().replace("-", " ").replace(":", " ").splitlines()
print(
  len([p for a, b, c, p in map(str.split, lines) if int(a) <= p.count(c) <= int(b)]),
  len([p for a, b, c, p in map(str.split, lines) if (p[int(a) - 1] == c) != (p[int(b) - 1] == c)]),
)
