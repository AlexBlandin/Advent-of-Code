from pathlib import Path
fmt="""from pathlib import Path
lines = Path("data/day{day}.txt").read_text().splitlines()
"""
for year in [2015, 2016, 2017, 2018, 2019, 2020, 2021]:
  for day in range(1, 26):
    py = Path(f"{year}/day{day}.py")
    data = Path(f"{year}/data/day{day}.txt")
    if not py.exists():
      py.touch()
      py.write_text(fmt.format(day=day),newline="")
    if not data.exists():
      data.touch()
      data.write_text("",newline="\n")
