from pathlib import Path
from json import loads


def rsum(x):
  match x:
    case int(x):
      return x
    case dict(x):
      return sum(map(rsum, x.keys())) + sum(map(rsum, x.values()))
    case list(x):
      return sum(map(rsum, x))
    case _:
      return 0


def redsum(x):
  match x:
    case int(x):
      return x
    case dict(x):
      if "red" in x.values():
        return 0  # that's literally it
      return sum(map(redsum, x.keys())) + sum(map(redsum, x.values()))
    case list(x):
      return sum(map(redsum, x))
    case _:
      return 0


db = loads(Path("day12.txt").read_text())
print(rsum(db), redsum(db))
