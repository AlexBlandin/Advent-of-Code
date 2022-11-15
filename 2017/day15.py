from pathlib import Path

a, b, *_ = Path("day15.txt").read_text().splitlines()
a, b = int(a.split()[-1]), int(b.split()[-1])
a, b = 65, 8921

def lower_16_bits(x: int):
  return x & 2**16 -1

