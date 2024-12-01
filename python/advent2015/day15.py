from itertools import product, repeat
from math import prod
from operator import mul
from pathlib import Path

from parse import parse

lines = Path("day15.txt").read_text().splitlines()

ingredients = {}  # ingredient
calories = {}  # calories
for line in lines:
  if p := parse("{}: capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}", line):
    i, c, d, f, t, e = p.fixed
    ingredients[i] = (c, d, f, t)
    calories[i] = e


def clamp(n):
  return max(n, 0)


def score_for_rationed_ingredient(i, a):
  return tuple(map(mul, i, repeat(a)))


def score_for_ratios(r):
  return prod(map(clamp, map(sum, zip(*map(score_for_rationed_ingredient, ingredients.values(), r), strict=False))))


def exact_calories_at_ratio(r, c=500):
  return sum(map(mul, calories.values(), r)) == c


def ratio(T):
  return filter(lambda r: sum(r) == 100, product(range(1, T), repeat=len(ingredients)))


r = max(ratio(100), key=score_for_ratios)
c = max(filter(exact_calories_at_ratio, ratio(100)), key=score_for_ratios)

print(score_for_ratios(r), score_for_ratios(c))
