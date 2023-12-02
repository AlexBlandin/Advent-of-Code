from pathlib import Path
from string import ascii_letters

print(
  sum(
    map(
      lambda rucksack: sum(
        filter(
          None,
          map(
            {c: n for c, n in zip(ascii_letters, range(1, 53), strict=True)}.get,
            set(rucksack[: len(rucksack) // 2]) & set(rucksack[len(rucksack) // 2:]),
          ),
        )
      ),
      rucksacks := Path("day3.txt").read_text().splitlines(),
    )
  ),
  sum(
    map(
      lambda a, b, c: sum(
        filter(
          None,
          map(
            {c: n for c, n in zip(ascii_letters, range(1, 53), strict=True)}.get,
            set(a) & set(b) & set(c),
          ),
        )
      ),
      rucksacks[::3],
      rucksacks[1::3],
      rucksacks[2::3],
    )
  ),
)
