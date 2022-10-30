from itertools import count
from math import prod

with open("day3.txt") as m: print(sum(m.read(m.seek(y*32+x)*0+1)=="#" for x,y in zip(map(lambda x:x%31, count(0,3)), range(0,323))), prod([sum(m.read(m.seek(y*32+x)*0+1)=="#" for x,y in zip(map(lambda x:x%31, count(0,r)), range(0,323,d))) for r,d in [(1,1),(3,1),(5,1),(7,1),(1,2)]]))
