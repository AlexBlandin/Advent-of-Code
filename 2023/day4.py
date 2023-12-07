from pathlib import Path

wins_per = [len(set.intersection(*map(lambda s: set(s.split()), line.split(": ")[1].split(" | ")))) for line in Path("day4.txt").read_text().splitlines()]

copies = [1] * len(wins_per)
for i in range(len(wins_per)):
  c = copies[i]
  for j in range(i + 1, min(i + wins_per[i] + 1, len(wins_per))):
    copies[j] += c

print(sum(1 << (win - 1) if win else 0 for win in wins_per), sum(copies))
