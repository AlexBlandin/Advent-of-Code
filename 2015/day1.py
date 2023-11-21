from itertools import accumulate
from pathlib import Path

print((s := Path("day1.txt").read_text()).count("(") - s.count(")"), list(accumulate([1 if c == "(" else -1 for c in s if c in "()"])).index(-1) + 1)
