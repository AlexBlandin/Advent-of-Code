from pathlib import Path

D = dict(zip("UDLRN", zip(range(4), [(0, -1), (0, 1), (-1, 0), (1, 0), (0, 0)])))
moves = [(D[d], int(n)) for d, n in map(str.split, Path("day9.txt").read_text().splitlines())]
moves = [(D["R"], 4), (D["U"], 4), (D["L"], 3), (D["D"], 1), (D["R"], 4), (D["D"], 1), (D["L"], 5), (D["R"], 2)]

rel_to_step: dict[tuple[int, int], int] = dict(
  zip(((-1, -1), (0, -1), (1, -1), (-1, 0), (0, 0), (1, 0), (-1, 1), (0, 1), (1, 1)), range(9))
)
# (-1,-1) ( 0,-1) ( 1,-1)
# (-1, 0) ( 0, 0) ( 1, 0)
# (-1, 1) ( 0, 1) ( 1, 1)

# step[rel_to_step[T_rel]][v: UDLR.values] = T_rel_new # relative (x,y) space around H
step: list[list[tuple[tuple[int, int], int]]] = [
  [((-1, 0), -1), ((0, -1), 3), ((0, -1), 0), ((-1, 0), 1), ((-1, -1), -1)],
  [((0, 0), -1), ((0, -1), 1), ((1, -1), -1), ((-1, -1), -1), ((0, -1), -1)],
  [((1, 0), -1), ((0, -1), 2), ((1, 0), 1), ((0, -1), -1), ((1, -1), -1)],
  [((-1, 1), -1), ((-1, -1), -1), ((0, 0), -1), ((-1, 0), 3), ((-1, 0), -1)],
  [((0, 1), -1), ((0, -1), -1), ((1, 0), -1), ((-1, 0), -1), ((0, 0), -1)],
  [((1, 1), -1), ((1, -1), -1), ((1, 0), 2), ((0, 0), -1), ((1, 0), -1)],
  [((0, 1), 3), ((-1, 0), -1), ((0, 1), -1), ((-1, 0), 0), ((-1, 1), -1)],
  [((0, 1), 0), ((0, 0), -1), ((1, 1), -1), ((-1, 1), -1), ((0, 1), -1)],
  [((0, 1), 2), ((1, 0), -1), ((1, 0), 0), ((0, 1), -1), ((1, 1), -1)],
] # TODO: augment with tail's "direction" so we can carry forward

knots: list[tuple[int, int]] = [(0, 0) for i in range(10)]
v1, v9 = {knots[1]}, {knots[9]}
for (d, (x, y)), n in moves: # moves contains the initial d
  for _ in range(n):
    for i, ((hx, hy), (tx, ty)) in list(enumerate(zip(knots[:], knots[1:]), 1)): # copy so don't need to go backwards
      knots[i], d = step[rel_to_step[hx - tx, hy - ty]][d] # the issue is everything moves in d, which is wrong
      if i == 1: v1.add(knots[i])
      if i == 9: v9.add(knots[i])
    hx, hy = knots[0]
    knots[0] = hx + x, hy + y

print(len(v1), len(v9))
