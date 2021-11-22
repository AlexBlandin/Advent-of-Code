from graphlib import TopologicalSorter as topo
from parse import parse
with open("data/day7.txt") as o:
  lines = [line.strip() for line in o.readlines()]

G = {} # G[w] = {s0,s1,...}
O = {} # O[w] = op(x) # ops lazily perform lookups for "current" value
A = {} # A[w] = uint16 # the value of a wire, initialised to 0

def add_input(G, A, w, s):
  A[w] = 0
  if s.isdecimal(): A[s] = int(s) # a constant
  else:
    if w not in G: G[w] = set()
    G[w].add(s)

for line in lines:
  if p := parse("NOT {} -> {}", line):
    s0, w = p.fixed
    add_input(G, A, w, s0)
    O[w] = s0, lambda s: ~A[s]
  elif p := parse("{} AND {} -> {}", line):
    s0, s1, w = p.fixed
    add_input(G, A, w, s0); add_input(G, A, w, s1)
    O[w] = (s0, s1), lambda s: A[s[0]] & A[s[1]]
  elif p := parse("{} OR {} -> {}", line):
    s0, s1, w = p.fixed
    add_input(G, A, w, s0); add_input(G, A, w, s1)
    O[w] = (s0, s1), lambda s: A[s[0]] | A[s[1]]
  elif p := parse("{} LSHIFT {} -> {}", line):
    s0, s1, w = p.fixed
    add_input(G, A, w, s0); add_input(G, A, w, s1)
    O[w] = (s0,s1), lambda s: A[s[0]]<<A[s[1]] & 65535
  elif p := parse("{} RSHIFT {} -> {}", line):
    s0, s1, w = p.fixed
    add_input(G, A, w, s0); add_input(G, A, w, s1)
    O[w] = (s0,s1), lambda s: A[s[0]]>>A[s[1]]
  elif p := parse("{} -> {}", line):
    s0, w = p.fixed
    add_input(G, A, w, s0)
    O[w] = s0, lambda s: A[s]

order = tuple(topo(G).static_order())
for e, (s, o) in zip(order, map(O.get, order)):
  A[e] = o(s)

old_a = A["a"] # previous output
for e in order: A[e] = 0 # reset
O["b"] = old_a, lambda s: old_a

for e, (s, o) in zip(order, map(O.get, order)):
  A[e] = o(s)

print(old_a, A["a"])
