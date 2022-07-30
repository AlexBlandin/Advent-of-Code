from pathlib import Path
from json import loads

lines = Path("data/day12.txt").read_text().splitlines()

db = loads(lines[0])

def rsum(x):
  if isinstance(x, int):
    return x
  elif isinstance(x, dict):
    return sum(map(rsum, x.keys())) + sum(map(rsum, x.values()))
  elif isinstance(x, list):
    return sum(map(rsum, x))
  else:
    return 0

def redsum(x):
  if isinstance(x, int):
    return x
  elif isinstance(x, dict):
    if "red" in x.values(): return 0 # that's literally it
    return sum(map(redsum, x.keys())) + sum(map(redsum, x.values()))
  elif isinstance(x, list):
    return sum(map(redsum, x))
  else:
    return 0

print(rsum(db), redsum(db))
