from collections import deque
from pathlib import Path
from typing import Any, NamedTuple

lines = Path("day18.txt").read_text().splitlines()

# registers a, b, f, i, p, *constants, snds, pc, running
# registers abfip were already convert()ed so are 0..4
# we handle the constant numbers by making constant registers for each number that shows up
# ironically, this is like how python has a constant address for each number
LIVE, PC, SNDS = -1, -2, -3  # so we can address them

REGS = [0, 0, 0, 0, 0, 0]  # the base registers, each progam later gets their own copy
RLUT = dict(zip("abfip0", range(len(REGS)), strict=True))


def convert(s: str):
  if s in RLUT:
    return RLUT[s]
  i = len(REGS)
  RLUT[s] = i
  REGS.append(int(s))
  return i


class OP(NamedTuple):
  code: str
  reg: int
  val: int

  def __call__(self, *args: Any, **kwds: Any):
    return self.__getattribute__(self.code).__call__(*args, **kwds)

  def set(self, regs: list[int], *_):
    regs[self.reg] = regs[self.val]

  def add(self, regs: list[int], *_):
    regs[self.reg] += regs[self.val]

  def mul(self, regs: list[int], *_):
    regs[self.reg] *= regs[self.val]

  def mod(self, regs: list[int], *_):
    regs[self.reg] %= regs[self.val]

  def jgz(self, regs: list[int], *_):
    if regs[self.reg] > 0:
      regs[PC] += regs[self.val] - 1

  def snd(self, regs: list[int], rcvq: deque[int], *_):
    rcvq.append(regs[self.val])
    regs[SNDS] += 1

  def rcv(self, regs: list[int], sndq: deque[int], rcvq: deque[int]):
    if sndq is rcvq:  # just a trick for part 1, so we can exit early
      if regs[self.reg]:
        regs[SNDS], regs[LIVE] = rcvq.popleft(), False
    elif len(rcvq):
      regs[self.reg], regs[LIVE] = rcvq.popleft(), True
    else:
      regs[LIVE] = False
      regs[PC] -= 1  # "spinlock" only we skip most time that passes while deadlocked


def op(code: str, reg: str, val=None, *_) -> OP:
  return OP(code=code, reg=convert(reg), val=convert(val or reg))


ops = [op(*line.split()) for line in lines]
REGS += [0, 0, True]
a, b, c, qa, qb, qc = REGS[:], REGS[:], REGS[:], deque(maxlen=1), deque(), deque()
c[convert("p")] = 1

while a[LIVE]:
  ops[a[PC]](a, qa, qa)
  a[PC] += 1

while b[LIVE] or c[LIVE]:
  while b[LIVE]:
    ops[b[PC]](b, qc, qb)
    b[PC] += 1
  while c[LIVE]:
    ops[c[PC]](c, qb, qc)
    c[PC] += 1
  ops[b[PC]](b, qc, qb)
  b[PC] += 1
  ops[c[PC]](c, qb, qc)
  c[PC] += 1

print(a[SNDS], c[SNDS])
