*l,=map(int, open("day1.txt").readlines())
i={}
for x in l:
  if x not in i:
    i[2020-x]=x
  else:
    print(f"{x = }, {i[x] = }, {x + i[x] = }, {x * i[x] = }")
    break

from itertools import combinations
from functools import reduce
from operator import mul
print(list(filter(lambda x:x[0]==2020, map(lambda x: (sum(x),reduce(mul,x)),combinations(l,3))))[0][1])

print()
print("Now for the obligatory oneliner")
[print(list(map(lambda x:x[1],filter(lambda x:x[0]==2020, map(lambda x: (sum(x),reduce(mul,x)),combinations(map(int, open("day1.txt").readlines()),n)))))[0]) for n in (2,3)]
