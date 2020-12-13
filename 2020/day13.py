from math import ceil
from itertools import count
estimate,schedule=tuple(map(str.strip,open("data/day13.txt").readlines()))
estimate,schedule=int(estimate), [int(i) if i!="x" else None for i in schedule.split(",")]
times=[(ceil(estimate/i)*i,i) for i in schedule if i]
es = [(o,b) for o,b in enumerate(schedule) if b]
contest=next((T for T in range(ceil(10**14/schedule[0])*schedule[0],10**16, schedule[0]) if all((T+o)%b==0 for o,b in es)))
print((min(times)[0]-estimate)*min(times)[1], contest)