from itertools import chain, starmap
from pathlib import Path
from string import ascii_uppercase, ascii_lowercase

print(sum(map(lambda items: sum(dict(chain(zip(ascii_lowercase, range(1, 27)), zip(ascii_uppercase, range(27, 53))))[item] for item in items), common := list(map(lambda rucksack: set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:]), rucksacks := Path("day3.txt").read_text().splitlines())))), sum(map(lambda items: sum(dict(chain(zip(ascii_lowercase, range(1, 27)), zip(ascii_uppercase, range(27, 53))))[item] for item in items), starmap(lambda a, b, c: set(a) & set(b) & set(c), zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3])))))
