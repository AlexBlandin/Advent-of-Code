from math import ceil
e,s = tuple(map(str.strip,open("data/day13.txt").readlines()))
e,s = int(e), [int(i) if i!="x" else None for i in s.split(",")]
bus = [(ceil(e/i)*i,i) for i in s if i]
mes = [((b-o)%b, b) for o,b in enumerate(s) if b] # ((T+o)%b == 0) === (T%b == (o:=(b-o)%b))
m=max([(o,i) for o,i in enumerate(s) if i], key=lambda t:t[1])
contest = next(T for T in reversed(range(ceil(10**14/m[1])*m[1],ceil(10**15/m[1])*m[1], m[1])) if all(T%b==o for o,b in mes)) # takes 26s max at magic 1op 4GHz (1047729918510 between 10**14 and 10**15 at 859 step)
print((min(bus)[0]-e)*min(bus)[1], contest-m[0])

# print(", ".join(f"n%{b} == {o}" for o,b in mes)) # just plug into WA
# n%19 == 0, n%41 == 32, n%859 == 840, n%23 == 19, n%13 == 7, n%17 == 15, n%29 == 10, n%373 == 323, n%37 == 24
# n = 1361317053288127m + 905694340256752     (so constant is earliest result aka m=0 aka intersection)
# print((min(bus)[0]-e)*min(bus)[1], 905694340256752) # thanks WA