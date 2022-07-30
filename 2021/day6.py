from collections import deque
from pathlib import Path

ages = list(map(int, Path("data/day6.txt").read_text().split(",")))
sim = deque(ages.count(i) for i in range(9))

def step(sim: deque):
  sim.append(sim.popleft())
  sim[-3] += sim[-1]

for _ in range(80):
  step(sim)
after80days = sum(sim)
for _ in range(256 - 80):
  step(sim)
after256days = sum(sim)
print(after80days, after256days)
