import sugar, math, algorithm
include prelude

var elves = collect(newSeq):
  for elf in "day1.txt".readFile.split("\n\n"):
    sum elf.split.map parseInt
elves.sort

echo &"{elves[elves.maxIndex]} {elves[elves.maxIndex-2..elves.maxIndex].sum}"
