from operator import inv, or_, and_, lshift, rshift
from graphlib import TopologicalSorter as topo
from parse import parse
with open("data/day7.txt") as o:
  lines = [line.strip() for line in o.readlines()]

G = {} # G[w] = {s0,s1} # wire sources
O = {} # O[w] = op() # op() lazily perform lookups for "current" value
A = {} # the value of a wire

def add_input(G, A, w, s):
  if s.isdecimal(): A[s] = int(s)
  else: G.setdefault(w,set()).add(s)

def op(f, *arg):
  return f(*[A[a] for a in arg]) & 65535

for line in lines:
  lhs, w = line.split(" -> ")
  if p := parse("NOT {}", lhs):
    s0 = p.fixed[0]
    O[w] = inv, s0
  elif p := parse("{} AND {}", lhs):
    s0, s1 = p.fixed
    O[w] = and_, s0, s1
  elif p := parse("{} OR {}", lhs):
    s0, s1 = p.fixed
    O[w] = or_, s0, s1
  elif p := parse("{} LSHIFT {}", lhs):
    s0, s1 = p.fixed
    O[w] = lshift, s0, s1
  elif p := parse("{} RSHIFT {}", lhs):
    s0, s1 = p.fixed
    O[w] = rshift, s0, s1
  elif p := parse("{}", lhs):
    s0 = p.fixed[0]
    O[w] = lambda s: s, s0
  for s in p: add_input(G, A, w, s)

order = tuple(topo(G).static_order())
for e, (o, *s) in zip(order, map(O.get, order)):
  A[e] = op(o, *s)

old_a = A["a"] # previous output
O["b"], A[old_a] = (lambda s: s, old_a), old_a

for e, (o, *s) in zip(order, map(O.get, order)):
  A[e] = op(o, *s)

print(old_a, A["a"])
