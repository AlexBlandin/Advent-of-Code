from functools import cache
from typing import NamedTuple, Self


class Hex(NamedTuple):  # noqa: PLR0904
  """A Hexagon, defined as a cube analogue in the space (q,r,s) where q + r + s == 0"""

  q: int | float
  r: int | float
  s: int | float

  def __post_init__(self):
    assert round(self.q + self.r + self.s) == 0, "q + r + s must equal 0"

  def __add__(self, other: Self):
    return Hex(self.q + other.q, self.r + other.r, self.s + other.s)

  def __sub__(self, other: Self):
    return Hex(self.q - other.q, self.r - other.r, self.s - other.s)

  def __mul__(self, scale: float):
    return Hex(self.q * scale, self.r * scale, self.s * scale)

  @property
  def rotate_left(self):
    return Hex(-self.s, -self.q, -self.r)

  @property
  def rotate_right(self):
    return Hex(-self.r, -self.s, -self.q)

  def __lshift__(self, n: int):
    return self if n <= 0 else (self.rotate_left << (n - 1))

  def __rshift__(self, n: int):
    return self if n <= 0 else (self.rotate_right >> (n - 1))

  @staticmethod
  @cache
  def directions():
    return (Hex(1, 0, -1), Hex(1, -1, 0), Hex(0, -1, 1), Hex(-1, 0, 1), Hex(-1, 1, 0), Hex(0, 1, -1))

  @staticmethod
  @cache
  def diagonals():
    return (Hex(2, -1, -1), Hex(1, -2, 1), Hex(-1, -1, 2), Hex(-2, 1, 1), Hex(-1, 2, -1), Hex(1, 1, -2))

  @staticmethod
  @cache
  def direction(direction: int):
    return Hex.directions()[direction]

  def neighbour(self, direction: int):
    return self + Hex.directions()[direction]

  @property
  def nn(self):
    """Move north"""
    return self + Hex(0, -1, 1)  # 2

  @property
  def ss(self):
    """Move south"""
    return self + Hex(0, 1, -1)  # 5

  @property
  def nw(self):
    """Move northwest"""
    return self + Hex(-1, 0, 1)  # 3

  @property
  def ne(self):
    """Move northeast"""
    return self + Hex(1, -1, 0)  # 1

  @property
  def sw(self):
    """Move southwest"""
    return self + Hex(-1, 1, 0)  # 4

  @property
  def se(self):
    """Move southeast"""
    return self + Hex(1, 0, -1)  # 0

  @property
  def neighbours(self):
    d = Hex.directions()
    return (self + d[0], self + d[1], self + d[2], self + d[3], self + d[4], self + d[5])

  def diagonal_neighbour(self, diagonal: int):
    return self + Hex.diagonals()[diagonal]

  @property
  def diagonal_neighbours(self):
    d = Hex.diagonals()
    return (self + d[0], self + d[1], self + d[2], self + d[3], self + d[4], self + d[5])

  def __abs__(self):
    return (abs(self.q) + abs(self.r) + abs(self.s)) // 2

  def distance(self, other: Self):
    """How many steps along the shortest path to the other hexagon"""
    return abs(self - other)

  def __round__(self):
    qi, ri, si = int(round(self.q)), int(round(self.r)), int(round(self.s))
    qd, rd, sd = abs(qi - self.q), abs(ri - self.r), abs(si - self.s)
    if qd > rd and qd > sd:
      qi = -ri - si
    elif rd > sd:
      ri = -qi - si
    else:
      si = -qi - ri
    return Hex(qi, ri, si)

  def lerp(self, other: Self, t: float):
    return Hex(self.q * (1.0 - t) + other.q * t, self.r * (1.0 - t) + other.r * t, self.s * (1.0 - t) + other.s * t)

  def linedraw(self, other: Self) -> list[Self]:
    N = round(self.distance(other))
    a_nudge = Hex(self.q + 1e-06, self.r + 1e-06, self.s - 2e-06)
    b_nudge = Hex(other.q + 1e-06, other.r + 1e-06, other.s - 2e-06)
    step = 1.0 / max(N, 1)
    return [round(a_nudge.lerp(b_nudge, step * i)) for i in range(N + 1)]  # type: ignore

  @property
  def reflect_q(self):
    return Hex(self.q, self.s, self.r)

  @property
  def reflect_r(self):
    return Hex(self.s, self.r, self.q)

  @property
  def reflect_s(self):
    return Hex(self.r, self.q, self.s)

  def range(self, N: int):
    """Given a range N, which hexes are within N steps from here?"""
    return [self + Hex(q, r, -q - r) for q in range(-N, N + 1) for r in range(max(-N, -q - N), min(+N, -q + N) + 1)]

  def reachable(self, movement: int):
    """Given a number of steps that can be made, which hexes are reachable?"""
    visited: set[Hex] = {self}  # set of hexes
    fringes: list[list[Hex]] = []  # array of arrays of hexes
    fringes.append([self])

    for k in range(2, movement + 1):
      fringes.append([])
      for hex in fringes[k - 1]:
        for dir in range(6):
          neighbour = hex.neighbour(dir)
          if neighbour not in visited:  # and not neighbour.blocked:
            visited.add(neighbour)
            fringes[k].append(neighbour)

    return visited

  def ring(self, radius: int):
    results: list[Hex] = []
    # this code doesn't work for radius == 0; can you see why?
    hex = self + self.direction(4) * radius
    for d in range(6):
      for _ in range(radius):
        results.append(hex)
        hex = hex.neighbour(d)
    return results

  def spiral(self, radius: int):
    results: list[Hex] = [self]
    for k in range(radius + 1):
      results += self.ring(k)
    return results


# Tests
def complain(*args):
  print(*args)


def equal_hex(name: str, a: Hex, b: Hex):
  if not (a.q == b.q and a.s == b.s and a.r == b.r):
    complain(name, a, b)


def equal_any(name: str, a, b):
  if a != b:
    complain(name, a, b)


def equal_hex_array(name: str, a: list[Hex], b: list[Hex]):
  equal_any(name, len(a), len(b))
  for i in range(0, len(a)):
    equal_hex(name, a[i], b[i])


def test_hex_arithmetic():
  equal_hex("hex_add", Hex(4, -10, 6), Hex(1, -3, 2) + Hex(3, -7, 4))
  equal_hex("hex_subtract", Hex(-2, 4, -2), Hex(1, -3, 2) - Hex(3, -7, 4))
  equal_hex("hex_scale", Hex(2, 4, -6), Hex(1, 2, -3) * 2)


def test_hex_direction():
  equal_hex("hex_direction", Hex(0, -1, 1), Hex.direction(2))


def test_hex_neighbor():
  equal_hex("hex_neighbour", Hex(1, -3, 2), Hex(1, -2, 1).neighbour(2))


def test_hex_diagonal():
  equal_hex("hex_diagonal", Hex(-1, -1, 2), Hex(1, -2, 1).diagonal_neighbour(3))


def test_hex_distance():
  equal_any("hex_distance", 7, Hex(3, -7, 4).distance(Hex(0, 0, 0)))


def test_hex_rotate_right():
  equal_hex("hex_rotate_right", Hex(1, -3, 2).rotate_right, Hex(3, -2, -1))
  equal_hex("hex_rotate_right 1", Hex(1, -3, 2) >> 1, Hex(3, -2, -1))
  equal_hex("hex_rotate_right 2", Hex(1, -3, 2) >> 2, Hex(3, -2, -1).rotate_right)


def test_hex_rotate_left():
  equal_hex("hex_rotate_left", Hex(1, -3, 2).rotate_left, Hex(-2, -1, 3))
  equal_hex("hex_rotate_left 1", Hex(1, -3, 2) << 1, Hex(-2, -1, 3))
  equal_hex("hex_rotate_left 2", Hex(1, -3, 2) << 2, Hex(-2, -1, 3).rotate_left)


def test_hex_round():
  # Pylance doesn't recognise when `round(number: SupportsRound[_T@round], ndigits: SupportsIndex) -> _T@round` is satisfied, so thinks it has to produce `int`
  a = Hex(0.0, 0.0, 0.0)
  b = Hex(1.0, -1.0, 0.0)
  c = Hex(0.0, -1.0, 1.0)
  equal_hex("hex_round 1", Hex(5, -10, 5), round(Hex(0.0, 0.0, 0.0).lerp(Hex(10.0, -20.0, 10.0), 0.5)))  # type: ignore
  equal_hex("hex_round 2", round(a), round(a.lerp(b, 0.499)))  # type: ignore
  equal_hex("hex_round 3", round(b), round(a.lerp(b, 0.501)))  # type: ignore
  equal_hex(
    "hex_round 4",
    round(a),  # type: ignore
    round(Hex(a.q * 0.4 + b.q * 0.3 + c.q * 0.3, a.r * 0.4 + b.r * 0.3 + c.r * 0.3, a.s * 0.4 + b.s * 0.3 + c.s * 0.3)),  # type: ignore
  )
  equal_hex(
    "hex_round 5",
    round(c),  # type: ignore
    round(Hex(a.q * 0.3 + b.q * 0.3 + c.q * 0.4, a.r * 0.3 + b.r * 0.3 + c.r * 0.4, a.s * 0.3 + b.s * 0.3 + c.s * 0.4)),  # type: ignore
  )


def test_hex_linedraw():
  equal_hex_array(
    "hex_linedraw", [Hex(0, 0, 0), Hex(0, -1, 1), Hex(0, -2, 2), Hex(1, -3, 2), Hex(1, -4, 3), Hex(1, -5, 4)], Hex(0, 0, 0).linedraw(Hex(1, -5, 4))
  )


def test_all():
  test_hex_arithmetic()
  test_hex_direction()
  test_hex_neighbor()
  test_hex_diagonal()
  test_hex_distance()
  test_hex_rotate_right()
  test_hex_rotate_left()
  test_hex_round()
  test_hex_linedraw()


if __name__ == "__main__":
  test_all()
  print("All tests complete.")
