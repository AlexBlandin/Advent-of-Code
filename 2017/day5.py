from pathlib import Path

jump = list(map(int, Path("day5.txt").read_text().splitlines()))
i, step = 0, 0
while 0 <= i < len(jump):
  j = jump[i]
  jump[i] += 1
  i += j
  step += 1

jump = list(map(int, Path("day5.txt").read_text().splitlines()))
i, stumble = 0, 0
while 0 <= i < len(jump):
  j = jump[i]
  jump[i] += 1 if j < 3 else -1
  i += j
  stumble += 1

print(step, stumble)
