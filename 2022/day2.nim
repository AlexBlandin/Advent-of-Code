import sugar, math, algorithm
include prelude

type Score = (int, int)
proc initScore(line: string): Score =
  case line:
  of "A X":
    result = (1 + 3, 2 + 0)
  of "A Y":
    result = (1 + 6, 1 + 3)
  of "A Z":
    result = (1 + 0, 3 + 6)
  of "B X":
    result = (2 + 0, 1 + 0)
  of "B Y":
    result = (2 + 3, 2 + 3)
  of "B Z":
    result = (2 + 6, 3 + 6)
  of "C X":
    result = (3 + 6, 2 + 0)
  of "C Y":
    result = (3 + 0, 3 + 3)
  of "C Z":
    result = (3 + 3, 1 + 6)

var 
  strategy1 = 0
  strategy2 = 0

for line in "day2.txt".lines:
  let score = line.initScore
  strategy1 += score[0]
  strategy2 += score[1]
