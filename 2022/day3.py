from itertools import starmap, chain
from pathlib import Path
from string import ascii_uppercase, ascii_lowercase

print(sum(map(lambda rucksack: sum(dict(chain(zip(ascii_lowercase, range(1, 27)), zip(ascii_uppercase, range(27, 53))))[item] for item in (set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:]))), rucksacks := Path("day3.txt").read_text().splitlines())), sum(starmap(lambda a, b, c: sum(dict(chain(zip(ascii_lowercase, range(1, 27)), zip(ascii_uppercase, range(27, 53))))[item] for item in (set(a) & set(b) & set(c))), zip(rucksacks[::3], rucksacks[1::3], rucksacks[2::3]))))
