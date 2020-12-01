i={}
for x in map(int, open("day1.txt").readlines()):
  if x not in i:
    i[2020-x]=x
  else:
    print(f"{x = }, {i[x] = }, {x + i[x] = }, {x * i[x] = }")
    break