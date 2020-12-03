from itertools import count
from functools import reduce
from operator import mul
m = [[0 if c=="." else 1 for c in line.strip()] for line in open("day3.txt").readlines()]
t = [sum(m[y][x] for x,y in zip(map(lambda x:x%31, count(0,r)), range(0,323,d))) for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]]
print(t[1])
print(reduce(mul,t))

# or, just part 2 with file io as 1liner, no preproc just horrific seeks
with open("day3.txt") as m: print(reduce(mul, [sum(m.read(m.seek(y*32+x)*0+1)=="#" for x,y in zip(map(lambda x:x%31, count(0,r)), range(0,323,d))) for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]]))
