print(
  sum([len(set(g) - set("\n")) for g in open("data/day6.txt").read().split("\n\n")]),
  sum([
    len(set.intersection(*g))
    for g in [list(map(set, g.splitlines())) for g in open("data/day6.txt").read().split("\n\n")]
  ])
)
