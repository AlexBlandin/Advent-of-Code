with open("data/day5.txt") as o: print(list(set(range((s:=sorted([int(s[:7].replace("B","1").replace("F","0"),2)*8+int(s[7:-1].replace("R","1").replace("L","0"),2) for s in o.readlines()]))[0],s[-1]+1)) - set(s))[0])