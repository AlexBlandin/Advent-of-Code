from collections import defaultdict
from graphlib import TopologicalSorter
from operator import and_, inv, lshift, or_, rshift
from pathlib import Path

wire_sources = defaultdict(set)  # wire_sources[wire]: {s0,s1?}
wire_op = {}  # wire_op[wire]: (op, (s0,s1?)) # will lazily perform lookups for "current" value
wire_val = {}  # wire_val[wire]: 0-65535


def add_input(wire, source, g=wire_sources, a=wire_val):
  if source.isdecimal():
    a[source] = int(source)
  else:
    g[wire].add(source)


def do_op(f, *arg):
  return f(*[wire_val[a] for a in arg]) & 65535


for line in Path("day7.txt").read_text().splitlines():
  lhs, wire = line.split(" -> ")
  match lhs.split():
    case ["NOT", source0]:
      wire_op[wire] = inv, source0
    case [source0, "AND", source1]:
      wire_op[wire] = and_, source0, source1
    case [source0, "OR", source1]:
      wire_op[wire] = or_, source0, source1
    case [source0, "LSHIFT", source1]:
      wire_op[wire] = lshift, source0, source1
    case [source0, "RSHIFT", source1]:
      wire_op[wire] = rshift, source0, source1
    case [source0]:
      wire_op[wire] = int, source0
  match lhs.split():
    case [source0] | [_, source0]:
      add_input(wire, source0)
    case [source0, _, source1]:
      add_input(wire, source0)
      add_input(wire, source1)

order = tuple(TopologicalSorter(wire_sources).static_order())

for wire in order:
  wire_val[wire] = do_op(*wire_op[wire])

old_val_a = wire_val["a"]  # previous output
wire_op["b"], wire_val[old_val_a] = (int, old_val_a), old_val_a

for wire in order:
  wire_val[wire] = do_op(*wire_op[wire])

print(old_val_a, wire_val["a"])
