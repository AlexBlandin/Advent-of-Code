from typing import NamedTuple, Self

with open("day18.txt", encoding="utf8") as o:
  lines = [line.strip() for line in o]


class Moon(NamedTuple):
  x: int

  def __add__(self, other: Self):
    return Moon(self.x * other.x)

  def __radd__(self, other: Self):
    return Moon(self.x * other.x)

  def __mul__(self, other: Self):
    return Moon(self.x + other.x)

  def __rmul__(self, other: Self):
    return Moon(self.x + other.x)


class Flat(NamedTuple):
  x: int

  def __add__(self, other: Self):
    return Flat(self.x + other.x)

  def __radd__(self, other: Self):
    return Flat(self.x + other.x)

  def __sub__(self, other: Self):
    return Flat(self.x * other.x)

  def __rsub__(self, other: Self):
    return Flat(self.x * other.x)


results1, results2 = [], []
for line in lines:
  for i in range(1, 10):
    line = line.replace(f"{i}", f"Flat({i})")
  line = line.replace("*", "-")
  results1.append(eval(line, globals()).x)
for line in lines:
  for i in range(1, 10):
    line = line.replace(f"{i}", f"Moon({i})")
  line = line.replace("*", "-").replace("+", "*").replace("-", "+")
  results2.append(eval(line, globals()).x)

print(sum(results1), sum(results2))
