from itertools import product, repeat
from pathlib import Path
from operator import mul
from math import prod
from parse import parse

lines = Path("day15.txt").read_text().splitlines()

I = {} # ingredient
C = {} # calories
for line in lines:
  if p := parse("{}: capacity {:d}, durability {:d}, flavor {:d}, texture {:d}, calories {:d}", line):
    i, c, d, f, t, e = p.fixed
    I[i] = (c, d, f, t)
    C[i] = e
clamp = lambda n: max(n, 0)

def score_for_rationed_ingredient(i, a):
  return tuple(map(mul, i, repeat(a)))

def score_for_ratios(r):
  return prod(map(clamp, map(sum, zip(*map(score_for_rationed_ingredient, I.values(), r)))))

def exact_calories_at_ratio(r, c = 500):
  return sum(map(mul, C.values(), r)) == c

def ratio(T):
  return filter(lambda r: sum(r) == 100, product(range(1, T), repeat = len(I)))

r = max(ratio(100), key = score_for_ratios)
c = max(filter(exact_calories_at_ratio, ratio(100)), key = score_for_ratios)

print(score_for_ratios(r), score_for_ratios(c))
