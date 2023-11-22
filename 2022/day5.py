from itertools import starmap
from operator import itemgetter
from pathlib import Path

inpt = Path("day5.txt").read_text().split("\n\n", maxsplit = 1)
crane1 = list(filter(None, map(lambda s: list(filter(str.isalpha, s)), map(reversed, zip(*inpt[0].splitlines()[:-1], strict = True)))))
crane2 = list(map(list, crane1))
moves = list(starmap(lambda n, a, b: (n, a - 1, b - 1), map(lambda m: map(int, filter(str.isnumeric, m)), map(str.split, inpt[1].splitlines()))))
for n, a, b in moves:
  for _ in range(n):
    crane1[b].append(crane1[a].pop())
for n, a, b in moves:
  crane2[b] += crane2[a][-n:]
  crane2[a] = crane2[a][:-n]
print("".join(map(itemgetter(-1), crane1)), "".join(map(itemgetter(-1), crane2)))

# or, as a one-liner

print(
  "" * (
    0 if (
      crane1 := list(
        map(
          list, crane2 := list(
            filter(
              None,
              map(
                lambda s: list(filter(str.isalpha, s)),
                map(reversed, zip(*(inpt := Path("day5.txt").read_text().split("\n\n", maxsplit = 1))[0].splitlines()[:-1], strict = True))
              )
            )
          )
        )
      ),
      list(
        starmap(
          lambda n, a, b: [crane1[b].append(crane1[a].pop()) for _ in range(n)], moves :=
          list(starmap(lambda n, a, b: (n, a - 1, b - 1), map(lambda m: map(int, filter(str.isnumeric, m)), map(str.split, inpt[1].splitlines()))))
        )
      ), list(starmap(lambda n, a, b: (crane2[b].extend(crane2[a][-n:]), [crane2[a].pop() for _ in range(n)]), moves))
    ) else 0
  ) + "".join(map(itemgetter(-1), crane1)),
  "".join(map(itemgetter(-1), crane2)),
)
