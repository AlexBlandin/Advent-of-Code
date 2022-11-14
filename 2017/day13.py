from pathlib import Path

lines = Path("day13.txt").read_text().replace(":","").splitlines()
for i, line in enumerate(lines):
  match line.split():
    case [a, b]:
      pass
    case _:
      raise SyntaxError(f"parse error on line {i+1}")