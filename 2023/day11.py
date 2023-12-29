from pathlib import Path

grid = [[c == "#" for c in line] for line in Path("day11.txt").read_text().splitlines()]
ys2pad = {y for y, row in enumerate(grid) if not any(row)}.intersection
xs2pad = {y for y, col in enumerate(zip(*grid, strict=True)) if not any(col)}.intersection
stars = [(x, y) for y, row in enumerate(grid) for x, b in enumerate(row) if b]
pairs = [list(map(range, map(min, a, b), map(max, a, b))) for a in stars for b in stars if a < b]

print(
  sum(len(xs) + len(ys) + len(xs2pad(xs)) + len(ys2pad(ys)) for xs, ys in pairs),
  sum(len(xs) + len(ys) + 999999 * (len(xs2pad(xs)) + len(ys2pad(ys))) for xs, ys in pairs),
)
