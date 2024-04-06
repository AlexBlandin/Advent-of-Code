include prelude

var s1 = 0
var s2 = 0
for line in "day2.txt".lines:
  let elf = int(line[0]) - int('A') + 1
  let me = int(line[2]) - int('X') + 1
  var t1 = me
  var t2 = me * 3 - 3
  if elf mod 3 + 1 == me: t1 += 6
  elif elf == me: t1 += 3
  else: t1 += 0
  if me == 3: t2 += elf mod 3 + 1
  elif me == 2: t2 += elf
  elif elf != 1: t2 += (elf + 2) mod 3
  else: t2 += 3
  s1 += t1
  s2 += t2

echo s1, " ", s2
