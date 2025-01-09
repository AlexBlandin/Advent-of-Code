from itertools import groupby
from operator import itemgetter
from pathlib import Path

type XY = tuple[int, int]
lines = (
  Path("day8.txt").read_text().splitlines()[:0]
  or """
............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............
""".strip().splitlines()
)
"""
  # for 0      # for A       # mine       # true
......#....# ............ ......#....# ......#....#
...#....0... ...#....0... ...#....0... ...#....0...
.....0....#. ....#0...... ....#0....#. ....#0....#.
..#....0.... .......0.... ......#0.... ..#....0....
....0....#.. ....0....... ....0...#... ....0....#..
.#....#..... ......A..... .....#A..#.. .#....A.....
...#........ ............ ......#..... ...#........
#........... .......#.... .......#.... #......#....
........A... ........A... ........A... ........A...
.........A.. .........A.. .........A.. .........A..
............ ..........#. ..........#. ..........#.
............ ..........#. ...........# ..........#.
huh, so I've got it almost right, at least the top three rows are right, but after that, it's wrong.

what lines are there, what's the maths for co-ords (p1(x1,y1), p2(x2,y2)) -> (p3(x3, y3), p4(x4, y4))?
  horiz      vert      diag     adiag
......... ....A.... .A....... .......A.
......... ......... ......... .........
......... ....1.... ...1..... .....1...
.A.1.2.B. ......... ......... .........
......... ....2.... .....2... ...2.....
......... ......... ......... .........
......... ....B.... .......B. .B.......

x1 - x2, y1 - y2 = dx, dy (for horiz & vert, one of dx or dy = 0)
x3, y3 = x1 - |dx|, y1 - |dy|
x4, y4 = x2 + |dx|, y2 + |dy|

vert:

diag:

adiag:

"""

width, height = len(lines[0]), len(lines)
freqs = {f for row in lines for f in row if f != "."}
antenna: dict[XY, str] = {(x, y): f for x, row in enumerate(lines) for y, f in enumerate(row) if f != "."}
by_freq: dict[str, list[XY]] = {f: [(x, y) for x, y in antenna if lines[x][y] == f] for f in freqs}  # ugh.
freq_lines: dict[str, set[XY]] = {
  f: {
    (
      xdx,
      ydy,
    )  # f"  {x, y = } + {a, b = } -> {xdx, ydy = }\n    ({dx, dy = }, {x + dx, y + dy = }, {a - dx, b - dx = })"
    for x1, y1, x2, y2, dx, dy in (
      (x1, y1, x2, y2, abs(x1 - x2), abs(y1 - y2)) for i, (x1, y1) in enumerate(ants) for x2, y2 in ants[i + 1 :]
    )
    for xdx, ydy in (
      (x1 - dx, y1 - dy),
      (x2 + dx, y2 + dx),
      # (x + dx, y - dy),
      # (a - dx, b + dx),
      # (x - dx, y + dy),
      # (a + dx, b - dx),
      # (x - dx, y - dy),
      # (a + dx, b + dx),
    )
    if 0 <= ydy < width and 0 <= xdx < height
  }
  for f, ants in by_freq.items()
}

by_row = {int(k): list(v) for k, v in groupby(sorted(antenna), key=itemgetter(0))}
by_col = {int(k): list(v) for k, v in groupby(sorted(antenna, key=itemgetter(1, 0)), key=itemgetter(1))}
antinodes = set().union(*freq_lines.values())

for x in range(height):
  for y in range(width):
    xy = x, y
    s = "."
    if f := antenna.get(xy):
      s = f
    elif xy in antinodes:
      s = "#"
    print(s, end="")
  print()

print(
  len(set().union(*freq_lines.values())),
  ...,
)
