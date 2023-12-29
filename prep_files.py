from functools import cache
from datetime import datetime
from pathlib import Path
from time import sleep
import tomllib
import re

from markdownify import markdownify as md
from tqdm.auto import trange
import requests

fmt = """from pathlib import Path

lines = Path("day{day}.txt").read_text().splitlines()

print(
  ...,
  ...,
)
"""
r"/.+?(?=abc)/"

CONFIG = "config.toml"
RE_DESC = re.compile(r"<article class=\"day-desc\">(.+?)</article>", re.DOTALL)
RE_EMPH = re.compile(r"<em>(.+?)</em>")
RE_BOLD = r"<strong>\1</strong>"
RE_CDEM = re.compile(r"<code><em>(.+?)</em></code>")
RE_EMCD = r"<em><code>\1</code></em>"


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
  desc = text.text
  desc = RE_CDEM.sub(RE_EMCD, desc)
  desc = RE_EMPH.sub(RE_BOLD, desc)
  desc = md("\n".join(RE_DESC.findall(desc)), heading_style="ATX", bullets="-")
  desc = desc.replace("\n\n\n", "\n\n")
  desc = desc.replace("\n\n```", "\n```")
  return desc, inpt.text.rstrip()


now = datetime.now()
for year in trange(2023, now.year + 1, desc="year", ncols=120):
  dir = Path(str(year))
  dir.mkdir(exist_ok=True)
  for day in trange(1, (25 if (year, now.month) != (now.year, 12) or now.day > 25 else now.day if now.hour >= 5 else now.day - 1) + 1, desc="day", leave=False):
    code = dir / f"day{day}.py"
    data = dir / f"day{day}.txt"
    desc = dir / f"day{day}.md"
    if not code.is_file():
      code.touch()
    if not data.is_file():
      data.touch()
    if not desc.is_file():
      desc.touch()

    if not code.read_text().strip() or code.read_text().strip().endswith(".read_text().splitlines()"):
      code.write_text(fmt.format(day=day), encoding="utf8", newline="\n")
    if not data.read_text().strip():
      _, input_data = download(year, day)
      data.write_text(input_data, encoding="utf8", newline="\n")
      sleep(0.5)
    if not desc.read_text().strip() or ("--- Part Two ---" not in desc.read_text() and "print(\n  ...," not in code.read_text().strip()):
      description, _ = download(year, day)
      desc.write_text(description, encoding="utf8", newline="\n")
      sleep(0.5)
