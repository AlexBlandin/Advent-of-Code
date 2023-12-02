from functools import cmp_to_key
from operator import itemgetter
from pathlib import Path
from json import loads

lines = Path("day13.txt").read_text().splitlines()
lefts, rights = list(map(loads, lines[::3])), list(map(loads, lines[1::3]))
packets = lefts + rights + [[[2]], [[6]]]


def all_ordered(left, right):
  return next(filter(lambda x: x is not None, map(ordered, left, right)), None)


def ordered(left, right) -> bool | None:  # noqa: PLR0911
  match left, right:
    case int(left), int(right) if left < right:
      return True
    case int(left), int(right) if left > right:
      return False
    case int(left), list(right):
      return ordered([left], right)
    case list(left), int(right):
      return ordered(left, [right])
    case list(left), list(right) if len(left) < len(right):
      if (o := all_ordered(left, right)) is not None:
        return o
      return True
    case list(left), list(right) if len(left) > len(right):
      if (o := all_ordered(left, right)) is not None:
        return o
      return False
    case list(left), list(right):
      return all_ordered(left, right)


def ordered_cmp(left, right):
  match ordered(left, right):
    case True:
      return -1
    case False:
      return 1
    case None:
      return 0


packets.sort(key=cmp_to_key(ordered_cmp))
print(
  sum(map(itemgetter(0), filter(itemgetter(1), enumerate(map(ordered, lefts, rights), 1)))),
  (packets.index([[2]]) + 1) * (packets.index([[6]]) + 1),
)
