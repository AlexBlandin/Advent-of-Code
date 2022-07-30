from parse import parse

print(len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("data/day2.txt").readlines()) if a <= p.count(l) <= b]), len([p for a,b,l,p in map(lambda l: parse("{:d}-{:d} {:l}: {}", l).fixed, open("data/day2.txt").readlines()) if (p[a-1]==l) != (p[b-1]==l)]))
