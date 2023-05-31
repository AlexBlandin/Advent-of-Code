from pathlib import Path

G = bytearray(Path("day12.txt").read_bytes()).splitlines()
W, H, S, E, (bS, bE, ba, bz) = len(G[0]), len(G), (0, 0), (0, 0), b"SEaz"
for y, row in enumerate(G):
  for x, v in enumerate(row):
    if v == bS:
      S = (x, y)
    elif v == bE:
      E = (x, y)
G[S[1]][S[0]] = ba
G[E[1]][E[0]] = bz

D = [[W*H for _ in range(W)] for _ in range(H)] # store the distance to E
D[E[1]][E[0]] = 0 # E has 0 distance to itself

changed = True
while changed: # flood fill, the secret sauce
  changed = False
  for y, (row, rod) in enumerate(zip(G, D)):
    for x, (v, d) in enumerate(zip(row, rod)):
      if w := [(a, b) for a, b in [(x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)] if 0 <= a < W and 0 <= b < H and G[b][a] <= G[y][x] + 1]:
        m = min(w, key = lambda xy: D[xy[1]][xy[0]])
        md = D[m[1]][m[0]]
        if d > md + 1:
          D[y][x] = md + 1
          changed = True

c, n = S, D[S[1]][S[0]]
for y, (row, rod) in enumerate(zip(G, D)): # we COULD store all at ba in a list, but effort
  for x, (v, d) in enumerate(zip(row, rod)):
    if v == ba and d < n:
      c, n = (x, y), d

print(D[S[1]][S[0]], D[c[1]][c[0]])
