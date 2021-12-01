from pathlib import Path
lines = Path("data/day1.txt").read_text().splitlines()
lines = [int(line) for line in lines]
from operator import gt
from functools import reduce
print(sum(map(gt,lines[1:],lines)), sum(map(gt,map(sum, zip(lines[1::],lines[2::],lines[3::])),map(sum, zip(lines,lines[1::],lines[2::])))))
