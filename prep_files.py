from functools import cache
from datetime import date
from pathlib import Path
from time import sleep
import tomllib
import re

from markdownify import markdownify as md
from tqdm.auto import trange
import requests

fmt = """from pathlib import Path

lines = Path("day{day}.txt").read_text().splitlines()
"""
r"/.+?(?=abc)/"

CONFIG = "config.toml"
RE_DESC = re.compile(r"<article class=\"day-desc\">(.+?)</article>", re.DOTALL)


@cache
def download(year: int, day: int):
  with open(CONFIG, "rb") as cfg:
    session = tomllib.load(cfg)["session"]
  text = requests.get(f"https://adventofcode.com/{year}/day/{day}", cookies={"session": session})  # type: ignore
  inpt = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session})  # type: ignore
  if not inpt.ok or not text.ok:
    for response in inpt, text:
      if response.status_code == 404:
        raise FileNotFoundError(response.text)
      raise RuntimeError(response.status_code, response.content)
  return md("\n".join(RE_DESC.findall(text.text)), heading_style="ATX", bullets="-").replace("\n\n\n", "\n\n"), inpt.text.rstrip()


for year in trange(2015, date.today().year + 1, desc="year"):
  dir = Path(str(year))
  dir.mkdir(exist_ok=True)
  for day in trange(1, 26, desc="day", leave=False):
    py = dir / f"day{day}.py"
    data = dir / f"day{day}.txt"
    desc = dir / f"day{day}.md"
    if not py.is_file():
      py.touch()
    if not data.is_file():
      data.touch()
    if not desc.is_file():
      desc.touch()

    if py.read_text().strip() == "":
      py.write_text(fmt.format(day=day), encoding="utf8", newline="\n")
    if data.read_text().strip() == "":
      _, input_data = download(year, day)
      data.write_text(input_data, encoding="utf8", newline="\n")
      sleep(0.5)
    if desc.read_text().strip() == "":
      description, _ = download(year, day)
      desc.write_text(description, encoding="utf8", newline="\n")
      sleep(0.5)
