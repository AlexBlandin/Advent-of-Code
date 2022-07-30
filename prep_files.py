from pathlib import Path
from datetime import date

fmt = """from pathlib import Path
from parse import parse

lines = Path("data/day{day}.txt").read_text().splitlines()
for line in lines:
  if p := parse("", line):
    p.fixed

"""

for year in range(2015, date.today().year + 1):
  for day in range(1, 26):
    py = Path(f"{year}/day{day}.py")
    data = Path(f"{year}/data/day{day}.txt")
    py.touch()
    data.touch()
    if not py.exists(): py.write_text(fmt.format(day = day), encoding="utf8", newline = "")
    if not data.exists(): data.write_text("", encoding="utf8", newline = "\n")
