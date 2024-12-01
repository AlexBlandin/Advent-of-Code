"""Prep files for advent, update those we can."""

import os
import re
from functools import cache
from pathlib import Path
from time import sleep

import pendulum
import requests
import tomllib
from markdownify import markdownify as md
from tqdm.auto import trange

fmt = """from pathlib import Path

lines = Path("day{day}.txt").read_text().splitlines()

print(
  ...,
  ...,
)
"""
r"/.+?(?=abc)/"

CONFIG = Path(__file__).parent / "config.toml"
RE_DESC = re.compile(r"<article class=\"day-desc\">(.+?)</article>", re.DOTALL)
RE_EMPH = re.compile(r"<em>(.+?)</em>")
RE_BOLD = r"<strong>\1</strong>"
RE_CDEM = re.compile(r"<code><em>(.+?)</em></code>")
RE_EMCD = r"<em><code>\1</code></em>"


@cache
def download(year: int, day: int) -> tuple[str, str]:
  "Downloads the description and input for a given day."
  with CONFIG.open("rb") as cfg:
    session = tomllib.load(cfg)["session"]
  text = requests.get(f"https://adventofcode.com/{year}/day/{day}", cookies={"session": session}, timeout=10)
  inpt = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session}, timeout=10)
  if not inpt.ok or not text.ok:
    for response in inpt, text:
      if response.status_code == 404:  # noqa: PLR2004
        raise FileNotFoundError(response.text)
      raise RuntimeError(response.status_code, response.content)
  desc = text.text
  desc = RE_CDEM.sub(RE_EMCD, desc)
  desc = RE_EMPH.sub(RE_BOLD, desc)
  desc = str(md("\n".join(RE_DESC.findall(desc)), heading_style="ATX", bullets="-"))
  desc = desc.replace("\n\n\n", "\n\n")
  desc = desc.replace("\n\n```", "\n```")
  return desc, inpt.text.rstrip()


if Path.cwd().absolute() == Path(__file__).parent.absolute():
  advent_dir = Path.cwd().parent / "python"
  if advent_dir.is_dir():
    os.chdir(advent_dir)

now = pendulum.now()
for year in trange(2024, now.year + 1, desc="year", ncols=120):
  cd = Path(f"advent{year}")
  cd.mkdir(exist_ok=True)
  for day in trange(
    1,
    (25 if (year, now.month) != (now.year, 12) or now.day > 25 else now.day if now.hour >= 5 else now.day - 1) + 1,  # noqa: PLR2004
    desc="day",
    leave=False,
  ):
    code = cd / f"day{day}.py"
    data = cd / f"day{day}.txt"
    desc = cd / f"day{day}.md"
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
    if not desc.read_text().strip() or (
      "--- Part Two ---" not in desc.read_text() and "print(\n  ...," not in code.read_text().strip()
    ):
      description, _ = download(year, day)
      desc.write_text(description, encoding="utf8", newline="\n")
      sleep(0.5)
