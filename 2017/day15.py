from pathlib import Path

sa, sb, *_ = Path("day15.txt").read_text().splitlines()
sa, sb = int(sa.split()[-1]), int(sb.split()[-1])
# sa, sb = 65, 8921
ma, mb = 16807, 48271
ca, cb = -4, -8
divisor = 2147483647


def g(s: int, m: int, d: int = divisor, cheat: int = 0):
  if cheat:
    while True:
      if s & cheat == s:
        yield s
      s = (s * m) % d
  while True:
    yield s
    s = (s * m) % d


def judge(mill: int, ga, gb):
  return sum(1 for _ in range(mill * 10**6 + 1) if (next(ga) & 0xFFFF) == (next(gb) & 0xFFFF))


print(judge(40, g(sa, ma), g(sb, mb)), judge(5, g(sa, ma, cheat=ca), g(sb, mb, cheat=cb)))
