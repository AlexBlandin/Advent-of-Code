from itertools import starmap
from pathlib import Path

print(
  next(
    filter(
      None,
      starmap(
        lambda i, tup: i if len(set(tup)) == 4 else None, enumerate(zip(data := Path("day6.txt").read_text(), data[1:], data[2:], data[3:], strict = True), 4)
      )
    )
  ),
  next(filter(None, starmap(lambda i, tup: i if len(set(tup)) == 14 else None, enumerate(zip(*[data[o:] for o in range(14)], strict = True), 14)))),
)
