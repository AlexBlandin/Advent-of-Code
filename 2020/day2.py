from parse import parse

*f, = filter(lambda nxlp: nxlp[0] <= nxlp[3].count(nxlp[2]) <= nxlp[1], map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("day2.txt").readlines()))
print(len(f))

c = 0
for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("day2.txt").readlines()):
  if (p[a-1]==l and p[b-1]!=l) or (p[a-1]!=l and p[b-1]==l):
    c += 1
print(c)