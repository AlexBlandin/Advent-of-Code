include prelude

var 
  s1 = 0
  s2 = 0

for line in "day2.txt".lines:
  let
    elf = int(line[0]) - int('A') + 1
    me = int(line[2]) - int('X') + 1
  s1 += me
  if elf mod 3 + 1 == me:
    s1 += 6
  elif elf == me:
    s1 += 3
  else:
    s1 += 0
  s2 += me * 3 - 3
  if me == 3: s2 += elf mod 3 + 1
  elif me == 2: s2 += elf
  elif elf != 1: s2 += (elf + 2) mod 3
  else: s2 += 3

echo &"{s1} {s2}"
