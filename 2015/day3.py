with open("day3.txt") as o:
  move = {"^": (1, 0), "<": (0, -1), ">": (0, 1), "v": (-1, 0)}
  moves = [move[m] for m in o.read().strip()]
pos = (0, 0)
visited = {pos}
for m in moves:
  pos = pos[0] + m[0], pos[1] + m[1]
  visited.add(pos)
spos, rpos = (0, 0), (0, 0)
nvisit = {spos}
for m in moves[::2]:
  spos = spos[0] + m[0], spos[1] + m[1]
  nvisit.add(spos)
for m in moves[1::2]:
  rpos = rpos[0] + m[0], rpos[1] + m[1]
  nvisit.add(rpos)
print(len(visited), len(nvisit))
