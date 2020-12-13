from math import ceil
from itertools import count
e,s = tuple(map(str.strip,open("data/day13.txt").readlines()))
e,s = int(e), [int(i) if i!="x" else None for i in s.split(",")]
bus = [(ceil(e/i)*i,i) for i in s if i]
mes = [((b-o)%b, b) for o,b in enumerate(s) if b] # ((T+o)%b == 0) === (T%b == (O:=(b-o)%b))
contest = next((T for T in range(ceil(10**14/s[0])*s[0],10**16, s[0]) if all(T%b==o for o,b in mes)))
print((min(bus)[0]-e)*min(bus)[1], contest)