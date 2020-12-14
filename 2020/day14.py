m0,m1,mem1,mem2,lines=-1,0,{},{},[tuple(map(str.strip,s.split("="))) for s in open("data/day14-1.txt").readlines()]
for op,val in lines:
  if op=="mask": m0,m1 = int(val.replace("X","1"),2),int(val.replace("X","0"),2)
  else: mem1[int(op[4:].replace("]",""))]=int(val)&m0|m1
for op,val in lines:
  if op=="mask": m1,m0 = int(val.replace("X","0"),2), val
  else:
    for addr in (int(op[4:].replace("]",""))|m1): mem2[addr]=int(val)
print(sum(mem1.values()))