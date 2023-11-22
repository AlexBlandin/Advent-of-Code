from pathlib import Path

N, S = int(Path("day17.txt").read_text()), 50000000
lst, pos, after2017, afterzero = [0], 0, 0, 0
for v in range(1, S + 1):
  pos = (pos + N) % v + 1
  if v == 2017:
    after2017 = lst[pos]
  elif v > 2017:
    if pos == 1:
      afterzero = v
    continue
  lst.insert(pos, v)

print(after2017, afterzero)
