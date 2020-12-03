m=[]
for line in open("day3.txt").readlines():
  m.append([0 if c=="." else 1 for c in line.strip()])
for i,l in enumerate(m):
  m[i] = l*128
T=1
for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]:
  x,y=0,0
  t=0
  while y < len(m):
    t+=m[y][x]
    x,y = x+r,y+d
  T *= t
print(T)
