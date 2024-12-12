import operator
from functools import reduce
from itertools import product
from pathlib import Path

lines = Path("day7.txt").read_text().splitlines()


def chain_call(funcs: list[callable]):
  _funcs = iter(funcs)

  def _chain_call(x, y):
    return next(_funcs)(x, y)

  return _chain_call


equations = [(int(test), list(map(int, values.split()))) for test, values in (line.split(": ") for line in lines)]

print(
  sum(
    test
    for test, values in equations
    if any(
      test == reduce(chain_call(ops), values) for ops in product((operator.add, operator.mul), repeat=len(values) - 1)
    )
  ),
  sum(
    test
    for test, values in equations
    if any(
      test == reduce(chain_call(ops), values)
      for ops in product((operator.add, operator.mul, lambda x, y: int(f"{x}{y}")), repeat=len(values) - 1)
    )
  ),
)
