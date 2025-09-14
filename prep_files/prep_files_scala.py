#!/usr/bin/env -S uv run -qqs
# /// script
# requires-python = ">=3.11"
# dependencies = [
#   "attrs",
#   "cattrs",
#   "tqdm",
#   "requests",
#   "markdownify",
# ]
# ///
#
"""
A single file Python script requiring only `uv` to run, no Python install required.

Copyright 20xx Alex
"""

import re
import tomllib
from datetime import date
from functools import cache
from pathlib import Path
from time import sleep

import requests
from markdownify import markdownify as md
from tqdm.auto import trange

fmt = """import scala.io.Source
import collection.mutable
val file = Source.fromFile("day{day}.txt")
val lines = file.getLines.toArray

@main
def solve() = {{
  s"Hello! ${{42}}"
}}

@main
def test() = {{
  s"Tests! ${{24}}"
}}

file.close
"""
r"/.+?(?=abc)/"

CONFIG = "config.toml"
RE_DESC = re.compile(r"<article class=\"day-desc\">(.+?)</article>", re.DOTALL)


@cache
def download(year: int, day: int):
  with open(CONFIG, "rb") as cfg:
    session = tomllib.load(cfg)["session"]
  text = requests.get(f"https://adventofcode.com/{year}/day/{day}", cookies={"session": session})
  inpt = requests.get(f"https://adventofcode.com/{year}/day/{day}/input", cookies={"session": session})
  if not inpt.ok or not text.ok:
    for response in inpt, text:
      if response.status_code == 404:
        raise FileNotFoundError(response.text)
      raise RuntimeError(response.status_code, response.content)
  return md("\n".join(RE_DESC.findall(text.text)), heading_style="ATX", bullets="-").replace(
    "\n\n\n", "\n\n"
  ), inpt.text.rstrip()


today = date.today()
for year in trange(2015, today.year + 1, desc="year"):
  dir = Path(str(year))
  dir.mkdir(exist_ok=True)
  for day in trange(
    1,
    (25 if (year, today.month) != (today.year, 12) else today.day) + 1,
    desc="day",
    leave=False,
  ):
    code = dir / f"day{day}.sc"
    data = dir / f"day{day}.txt"
    desc = dir / f"day{day}.md"
    if not code.is_file():
      code.touch()
    if not data.is_file():
      data.touch()
    if not desc.is_file():
      desc.touch()

    if not code.read_text().strip():
      code.write_text(fmt.format(day=day), encoding="utf8", newline="\n")
    if not data.read_text().strip():
      _, input_data = download(year, day)
      data.write_text(input_data, encoding="utf8", newline="\n")
      sleep(0.5)
    if not desc.read_text().strip():
      description, _ = download(year, day)
      desc.write_text(description, encoding="utf8", newline="\n")
      sleep(0.5)
