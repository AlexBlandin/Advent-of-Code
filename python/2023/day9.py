from collections import deque
from itertools import pairwise, starmap
from operator import neg, sub
from pathlib import Path

lines = Path("day9.txt").read_text().splitlines()
sequences = [[deque(map(int, line.split()))] for line in lines]
for seqs in sequences:
  while set(seqs[-1]) != {0}:
    seqs.append(deque(map(neg, starmap(sub, pairwise(seqs[-1])))))
  for prev, seq in pairwise(seqs[::-1]):
    seq.append(seq[-1] + prev[-1])
    seq.appendleft(seq[0] - prev[0])

print(sum(seqs[0][-1] for seqs in sequences), sum(seqs[0][0] for seqs in sequences))
