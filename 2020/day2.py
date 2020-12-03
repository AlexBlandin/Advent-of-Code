from parse import parse

f = [p for n,x,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("day2.txt").readlines()) if n <= p.count(l) <= x]
print(len(f))

f = [p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("day2.txt").readlines()) if (p[a-1]==l and p[b-1]!=l) or (p[a-1]!=l and p[b-1]==l)]
print(len(f))
