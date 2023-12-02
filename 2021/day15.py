from functools import partial
from operator import itemgetter
from pathlib import Path
from math import inf

path = list(map(list, map(partial(map, int), Path("day15.txt").read_text().splitlines())))
path = [
  [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
  [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
  [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
  [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
  [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
  [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
  [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
  [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
  [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
  [2, 3, 1, 1, 9, 4, 4, 5, 8, 1],
]
width, height = len(path[0]), len(path)
visited: set[tuple[int, int]] = set()


def legal(x: int, y: int, width: int = width, height: int = height):
  return 0 <= x < width and 0 <= y < height


def risk(x: int, y: int, path: list[list[int]] = path):
  return path[y][x]


def increase(x: int, y: int, score: int, path: list[list[int]] = path):
  path[y][x] += score
  return path[y][x]


def neighbours(x: int, y: int, visited: set[tuple[int, int]] = visited):
  return [(px, py) for px, py in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)] if legal(px, py) and (px, py) not in visited]


def pick(x: int, y: int):
  return min([((px, py), risk(px, py)) for px, py in neighbours(x, y)], key=itemgetter(1))


def depth(x: int, y: int, path: list[list[int]] = path, visited: set[tuple[int, int]] = visited, target: tuple[int, int] = (width - 1, height - 1)):
  if (x, y) in visited:
    return inf
  visited.add((x, y))
