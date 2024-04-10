from operator import itemgetter
from pathlib import Path


def join(s: list):
  return "".join(map(str, s))


def solve(s: str):
  nums = dict(
    zip(
      [
        *map(str, range(1, 9 + 1)),
        "one",
        "two",
        "three",
        "four",
        "five",
        "six",
        "seven",
        "eight",
        "nine",
      ],
      list(map(str, range(1, 9 + 1))) * 2,
      strict=True,
    ),
  )
  n_min, _ = min(filter(lambda n: n[1] > -1, ((n, s.find(n)) for n in nums)), key=itemgetter(1))
  n_max, _ = max(filter(lambda n: n[1] > -1, ((n, s.rfind(n)) for n in nums)), key=itemgetter(1))
  return int(nums[n_min]) * 10 + int(nums[n_max])


lines = Path("day1.txt").read_text().splitlines()
print(
  sum(
    map(
      int,
      map(
        join,
        map(itemgetter(0, -1), list(filter(None, (list(map(int, filter(str.isnumeric, line))) for line in lines)))),
      ),
    )
  ),
  sum(map(solve, lines)),
)
