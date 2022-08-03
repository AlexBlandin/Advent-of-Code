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
  dir = Path(str(year))
  dta = dir / "data"
  if not dir.is_dir(): dir.mkdir()
  if not dta.is_dir(): dta.mkdir()
  for day in range(1, 26):
    py = dir / f"day{day}.py"
    data = dta / f"day{day}.txt"
    if py.read_text().strip() == "": py.write_text(fmt.format(day = day), encoding = "utf8", newline = "")
    if data.read_text().strip() == "": data.write_text("", encoding = "utf8", newline = "\n")
