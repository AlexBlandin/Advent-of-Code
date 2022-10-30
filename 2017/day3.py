from itertools import takewhile, count
from pathlib import Path
from math import ceil, sqrt

position = int(Path("day3.txt").read_text().strip()) # hi Ulam
spokes = list(takewhile(lambda n: n <= position, (ceil((n**2 + n + 1) / 4) for n in count())))
spokes += [ceil(((len(spokes))**2 + (len(spokes)) + 1) / 4)]
print(ceil((sqrt(position)-1)/2) + min(abs(position - spokes[-1]), abs(position - spokes[-2])), )
