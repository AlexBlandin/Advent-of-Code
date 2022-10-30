from pathlib import Path
from parse import parse

lines = Path("day4.txt").read_text().splitlines()
for line in lines:
  if p := parse("", line):
    p.fixed

