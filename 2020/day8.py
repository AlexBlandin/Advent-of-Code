with open("data/day8.txt") as o: b=[l.strip().split()+[True] for l in o.readlines()]
h=set()
a,c=0,0
while c not in h and c<len(b):
  i=b[c]
  h.add(c)
  c+=1
  if i[0]=="acc":
    a+=int(i[1])
  elif i[0]=="jmp":
    c+=int(i[1])-1
p=a
for s, op in enumerate(b):
  if op[0] in ["jmp", "nop"]:
    pb,b[s] = b[s],"jmp" if b[s]=="nop" else "nop"
    h=set()
    a,c=0,0
    while c not in h and c<len(b):
      i=b[c]
      h.add(c)
      c+=1
      if i[0]=="acc":
        a+=int(i[1])
      elif i[0]=="jmp":
        c+=int(i[1])-1
    b[s]=pb
    if c >= len(b):
      print(p,a)
      break
