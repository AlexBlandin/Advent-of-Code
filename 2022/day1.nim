import sugar, math, algorithm
include prelude

var elves = collect(newSeq):
  for elf in "day1.txt".readFile.split("\n\n"):
    sum elf.split.map parseInt
elves.sort

echo &"{elves[high(elves)]} {elves[high(elves)-2..high(elves)].sum}"
