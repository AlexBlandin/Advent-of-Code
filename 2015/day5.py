from pathlib import Path
from itertools import pairwise
from string import ascii_lowercase as alphabet

vowels = set("aeiou")
doubles = set(map("".join, zip(alphabet, alphabet, strict=True)))
bad = {"ab", "cd", "pq", "xy"}


def is_oldnice(line, vowels=vowels, doubles=doubles, bad=bad):
  good_vowels = len([c for c in line if c in vowels]) >= 3
  pairs = set(map("".join, pairwise(line)))
  good_pairs = len(pairs & doubles) >= 1
  good_bads = len(pairs & bad) == 0
  return good_vowels and good_pairs and good_bads


def is_nice(line):
  pairs = list(map("".join, pairwise(line)))
  bunch = {(p, q) for i, p in enumerate(pairs) for j, q in enumerate(pairs) if p == q and j not in {i, i + 1, i - 1}}
  good_pairs = len(bunch) >= 1
  repeats = {(a, b) for i, a in enumerate(line) for j, b in enumerate(line) if a == b and j in {i + 2, i - 2}}
  good_repeats = len(repeats) >= 1
  return good_pairs and good_repeats


lines = Path("day5.txt").read_text().splitlines()
oldnice = list(filter(is_oldnice, lines))
newnice = list(filter(is_nice, lines))
print(len(oldnice), len(newnice))
