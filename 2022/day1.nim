import sugar, math, algorithm
include prelude

var elves = "day1.txt".readFile.split("\n\n").map(elf => sum elf.split.map parseInt)
elves.sort

echo &"{elves[high(elves)]} {elves[high(elves)-2..high(elves)].sum}"
