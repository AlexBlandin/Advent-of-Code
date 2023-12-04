from pathlib import Path

r, g, b = 12, 13, 14
lines = Path("day2.txt").read_text().splitlines()
sm, pw = 0, 0
for line in lines:
  rm, gm, bm = 0, 0, 0
  game, sets = line.split(": ", maxsplit=1)
  rgb_allow = True
  for shown in sets.split("; "):
    reds, greens, blues = 0, 0, 0
    for col in shown.split(", "):
      match col.split():
        case [n, "red"]:
          reds += int(n)
        case [n, "green"]:
          greens += int(n)
        case [n, "blue"]:
          blues += int(n)
    rm, gm, bm = max(rm, reds), max(gm, greens), max(bm, blues)
    if reds > r or greens > g or blues > b:
      rgb_allow = False
  if rgb_allow:
    sm += int(game.split(maxsplit=1)[1])
  pw += rm * gm * bm
print(sm, pw)
