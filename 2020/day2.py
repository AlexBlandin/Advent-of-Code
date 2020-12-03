from parse import parse

f = [p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("day2.txt").readlines()) if a <= p.count(l) <= b]
print(len(f))

f = [p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("day2.txt").readlines()) if (p[a-1]==l) != (p[b-1]==l)]
print(len(f))
