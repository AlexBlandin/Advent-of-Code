from pathlib import Path

lines = Path("day4.txt").read_text().splitlines()
order = {int(k): set() for k in lines[0].split(",")}
boardlines = lines[2::6], lines[3::6], lines[4::6], lines[5::6], lines[6::6]
boards = [[[int(c) for c in r.split()] for r in b] for b in zip(*boardlines, strict=True)]
boardsets = [{a for b in board for a in b} for board in boards]
for i, bs in enumerate(boardsets):
  for b in bs:
    if b in order:
      order[b].add(i)
score, seen = {}, set()
for k, bk in order.items():
  seen.add(k)
  for i in bk:

    def fiveinarow(row):
      return len(set(row) & seen) == 5

    if i not in score and (any(filter(fiveinarow, boards[i])) or any(filter(fiveinarow, zip(*boards[i], strict=True)))):
      score[i] = k * sum(boardsets[i] - seen)
scores = list(score.values())
print(scores[0], scores[-1])
