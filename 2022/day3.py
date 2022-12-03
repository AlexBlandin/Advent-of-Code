from itertools import chain
from pathlib import Path
from string import ascii_uppercase, ascii_lowercase

print(sum(map(lambda rucksack: sum(map(dict(chain(zip(ascii_lowercase, range(1, 27)), zip(ascii_uppercase, range(27, 53)))).get, set(rucksack[:len(rucksack)//2]) & set(rucksack[len(rucksack)//2:]))), rucksacks := Path("day3.txt").read_text().splitlines())), sum(map(lambda a, b, c: sum(map(dict(chain(zip(ascii_lowercase, range(1, 27)), zip(ascii_uppercase, range(27, 53)))).get, set(a) & set(b) & set(c))), rucksacks[::3], rucksacks[1::3], rucksacks[2::3])))
