m=[[None if c == "." else False for c in line.strip()] for line in open("data/day11.txt").readlines()]
for l in m: print("".join("." if c==None else "#" if c else "L" for c in l))