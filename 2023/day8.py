from pathlib import Path

lines = Path("day8.txt").read_text().replace("= ", "").replace("(", "").replace(",", "").replace(")", "").splitlines()
lines = (
  """RL

AAA = (BBB, CCC)
BBB = (DDD, EEE)
CCC = (ZZZ, GGG)
DDD = (DDD, DDD)
EEE = (EEE, EEE)
GGG = (GGG, GGG)
ZZZ = (ZZZ, ZZZ)""".replace("= ", "")
  .replace("(", "")
  .replace(",", "")
  .replace(")", "")
  .splitlines()
)
leftright, lines = lines[0], lines[2:]
print(lines)
