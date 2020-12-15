m=[19,0,5,1,10,13] # [0,3,6] or
sm,im=set(m[:-1]),{n:i for i,n in enumerate(m,1)}
for i in range(len(m),2020):
  l=m[-1]
  if l not in sm:
    m+=[0]
    sm.add(l)
    im[l]=i
  else:
    a=i-im[l]
    im[l]=i
    m+=[a]
print(m[-1],end=" ")

m=[19,0,5,1,10,13] # [0,3,6] or
sm,im=set(m[:-1]),{n:i for i,n in enumerate(m,1)}
for i in range(len(m),30000000):
  l=m[-1]
  if l not in sm:
    m+=[0]
    sm.add(l)
    im[l]=i
  else:
    a=i-im[l]
    im[l]=i
    m+=[a]
print(m[-1])