while m!=p:
#   p=deepcopy(m)
#   for y,row in enumerate(m):
#     for x,s in enumerate(row):
#       if s==False and sees(x,y).count(True)==0:
#         m[y][x]=True
#       elif s and sees(x,y).count(True)>=5:
#         m[y][x]=False