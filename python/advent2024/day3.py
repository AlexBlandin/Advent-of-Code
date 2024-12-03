import re
from pathlib import Path

program = "".join(Path("day3.txt").read_text().splitlines())
mul_re = re.compile(r"mul\((\d+),(\d+)\)")
remove_re = re.compile(r"(?:don't\(\).*?(?=don't\(\)|do\(\)))")

print(
  sum(int(a) * int(b) for a, b in mul_re.findall(program)),
  sum(int(a) * int(b) for a, b in mul_re.findall("".join(remove_re.split(program)))),
)
