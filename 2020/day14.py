m0,m1,bits,mem1,mem2,lines=-1,0,[],{},{},[tuple(map(str.strip,s.split("="))) for s in open("data/day14.txt").readlines()]
def mask(v, bits):
  if len(bits): return [v | (1<<bits[0]), v & ~(1<<bits[0])] + mask(v,bits[1:]) + mask(v | (1<<bits[0]),bits[1:]) + mask(v & ~(1<<bits[0]),bits[1:])
  else: return []
for op,val in lines:
  if op=="mask": m0,m1 = int(val.replace("X","1"),2),int(val.replace("X","0"),2)
  else: mem1[int(op[4:].replace("]",""))]=int(val)&m0|m1
for op,val in lines:
  if op=="mask":
    m1,m0 = int(val.replace("X","0"),2),int(val.replace("1","0").replace("X","1"),2)
    bits = [i for i,v in enumerate(reversed(val)) if v=="X"]
  else:
    v = int(op[4:].replace("]","")) | m1
    for addr in set(mask(v,bits)): mem2[addr]=int(val)
print(sum(mem1.values()), sum(mem2.values()))