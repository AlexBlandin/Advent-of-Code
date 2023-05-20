from datetime import date
from pathlib import Path

fmt = """from pathlib import Path

lines = Path("day{day}.txt").read_text().splitlines()
"""

# from pathlib import Path
# from parse import parse

# lines = Path("day{day}.txt").read_text().splitlines()
# for line in lines:
#   if p := parse("", line):
#     p.fixed

for year in range(2015, date.today().year + 1):
  dir = Path(str(year))
  dir.mkdir(exist_ok = True)
  for day in range(1, 26):
    py = dir / f"day{day}.py"
    data = dir / f"day{day}.txt"
    py.touch()
    data.touch()
    if py.read_text().strip() == "":
      py.write_text(fmt.format(day = day), encoding = "utf8", newline = "\n")
    if data.read_text().strip() == "":
      data.write_text("", encoding = "utf8", newline = "\n")
