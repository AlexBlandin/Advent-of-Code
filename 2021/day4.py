from pathlib import Path
lines = Path("data/day4.txt").read_text().splitlines()
order = {int(k):set() for k in lines[0].split(",")}
lines = lines[2:]
boards = [[[int(c) for c in r.split()] for r in b] for b in zip(lines[0::6],lines[1::6],lines[2::6],lines[3::6],lines[4::6])]
boardsets = [{a for b in board for a in b} for board in boards]
for i, bs in enumerate(boardsets):
  for b in bs:
    if b in order: order[b].add(i)
scores, seen, won = [], set(), set()
for k, bk in order.items():
  seen.add(k)
  for i in bk:
    boardsets[i].remove(k)
    five_in_a_row = lambda row: len(set(row)&seen)==5
    if i not in won and (any(filter(five_in_a_row, boards[i])) or any(filter(five_in_a_row, zip(*boards[i])))):
      scores.append(k * sum(boardsets[i]))
      won.add(i)

print(scores[0], scores[-1])
