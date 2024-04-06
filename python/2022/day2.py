from itertools import starmap
from pathlib import Path

print(
  sum(
    starmap(
      lambda elf, me: me + (6 if (elf, me) in {(1, 2), (2, 3), (3, 1)} else 3 if elf == me else 0),
      hands := list(
        starmap(
          lambda elf, me: (ord(elf) - ord("A") + 1, ord(me) - ord("X") + 1),
          map(str.split, Path("day2.txt").read_text().splitlines()),
        )
      ),
    ),
  ),
  sum(
    starmap(
      lambda elf, me: [0, [0, 3, 1, 2][elf], 3 + elf, [0, 8, 9, 7][elf]][me],
      hands,
    ),
  ),
)
