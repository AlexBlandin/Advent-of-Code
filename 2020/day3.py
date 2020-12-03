T, m = 1, [[0 if c=="." else 1 for c in line.strip()] for line in open("day3.txt").readlines()]
for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
  x,y,t = 0,0,0
  for y in range(0,len(m),d):
    t += m[y][x]
    x = (x+r)%31
  T *= t
  if (r,d)==(3,1): print(t)
print(T)
