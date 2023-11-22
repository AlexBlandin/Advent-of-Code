from functools import reduce
from pathlib import Path

(x, y, d), (sx, sy, wx, wy) = reduce(
  lambda o, t: ( # noqa: PLC3002
    lambda x, y, d, i, v: ((x if i not in "EWF" else x + v if i == "E" or (i == "F" and d == 0) else x - v if i == "W" or (i == "F" and d == 2) else x),
                           (y if i not in "NSF" else y + v if i == "N" or (i == "F" and d == 3) else y - v
                            if i == "S" or (i == "F" and d == 1) else y), (d if i not in "LR" else (d + v // 90) % 4 if i == "R" else (d - v // 90) % 4))
  )(*o, *t), [(line[0], int(line.strip()[1:])) for line in Path("day12.txt").read_text().splitlines()], (0, 0, 0)
), reduce(
  lambda o, t: ( # noqa: PLC3002
    lambda sx, sy, wx, wy, i, v: ((sx if i != "F" else wx * v + sx), (sy if i != "F" else wy * v + sy), (
      wx if i == "F" else wx + v if i == "E" else wx - v if i == "W" else (-wx if v == 180 else -wy)
      if (i == "L" and v != 270) or (i == "R" and v == 270) else (-wx if v == 180 else wy) if (i == "R" and v != 270) or (i == "L" and v == 270) else wx
    ), (
      wy if i == "F" else wy + v if i == "N" else wy - v if i == "S" else (-wy if v == 180 else wx)
      if (i == "L" and v != 270) or (i == "R" and v == 270) else (-wy if v == 180 else -wx) if (i == "R" and v != 270) or (i == "L" and v == 270) else wy
    ))
  )(*o, *t), [(line[0], int(line.strip()[1:])) for line in Path("day12.txt").read_text().splitlines()], (0, 0, 10, 1)
)
print(abs(x) + abs(y), abs(sx) + abs(sy))
