from itertools import pairwise
from pathlib import Path

numbers = list(map(int, Path("day1.txt").read_text().strip()))

circular = [*numbers, numbers[0]]
twocular = numbers + numbers[: len(numbers) // 2]

print(
  sum([a for a, b in pairwise(circular) if a == b]),
  sum([a for a, b in zip(twocular, twocular[len(numbers) // 2:], strict=False) if a == b]),
)
