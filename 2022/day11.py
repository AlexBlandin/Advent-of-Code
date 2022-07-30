from pathlib import Path
from parse import parse

lines = Path("data/day11.txt").read_text().splitlines()
for line in lines:
  if p := parse("", line):
    p.fixed

