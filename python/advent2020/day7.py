from pathlib import Path

parent = {}
child = {
  outer: dict(inner + [parent.setdefault(i, set()).add(outer) for i, c in inner] * 0)
  for outer, inner in [
    (
      outer,
      [
        (i[0], int(i[1]))
        for i in (
          tuple(reversed(i.strip().split(" ", 1)))
          for i in inner.replace("bags", "").replace("bag", "").replace(".", "").split(",")
        )
      ]
      if "other" not in inner
      else [],
    )
    for outer, inner in [tuple(rule.split(" bags contain ", 1)) for rule in Path("day7.txt").read_text().splitlines()]
  ]
}
s, ln = set(parent.setdefault("shiny gold", set())), len(parent["shiny gold"])
while len(s := s.union(*[parent[i] for i in s if i in parent])) > ln:
  ln = len(s)


def r(c):
  return 0 if child[c] == {} else sum(v * r(i) + v for i, v in child[c].items())


print(ln, r("shiny gold"))

# print(child["shiny gold"])
# print(child)
# def p(c):
#   if child[c]!={}:
#     print(c, child[c])
#     for i in child[c]:
#       p(i)
# p("shiny gold")
"""
shiny gold {'dark olive': '1', 'vibrant plum': '2'}
dark olive {'faded blue': '3', 'dotted black': '4'}
vibrant plum {'faded blue': '5', 'dotted black': '6'}
"""
"""
shiny gold {'dark red': '2'}
dark red {'dark orange': '2'}
dark orange {'dark yellow': '2'}
dark yellow {'dark green': '2'}
dark green {'dark blue': '2'}
dark blue {'dark violet': '2'}
"""
"""
shiny gold {'vibrant orange': '3', 'plaid silver': '3'}
vibrant orange {'bright tan': '3', 'shiny teal': '5', 'dotted crimson': '4', 'posh cyan': '2'}
bright tan {'faded purple': '5', 'dotted gray': '3'}
faded purple {'striped fuchsia': '4', 'mirrored fuchsia': '3', 'dotted gray': '2', 'muted coral': '4'}
striped fuchsia {'dim cyan': '3'}
dotted gray {'dull violet': '5', 'dark plum': '5', 'bright indigo': '2', 'wavy bronze': '2'}
dull violet {'dotted purple': '1'}
dotted purple {'plaid salmon': '1', 'bright indigo': '2'}
muted coral {'vibrant plum': '1', 'plaid salmon': '4', 'bright indigo': '2'}
vibrant plum {'dim cyan': '4', 'pale maroon': '3'}
pale maroon {'striped fuchsia': '3', 'plaid silver': '5', 'shiny teal': '4'}
striped fuchsia {'dim cyan': '3'}
dotted gray {'dull violet': '5', 'dark plum': '5', 'bright indigo': '2', 'wavy bronze': '2'}
dull violet {'dotted purple': '1'}
dotted purple {'plaid salmon': '1', 'bright indigo': '2'}
dotted crimson {'plaid silver': '2', 'drab plum': '5'}
posh cyan {'shiny coral': '5', 'bright indigo': '5', 'plaid silver': '2'}
shiny coral {'dull violet': '5', 'bright tan': '3', 'muted orange': '3', 'shiny indigo': '3'}
dull violet {'dotted purple': '1'}
dotted purple {'plaid salmon': '1', 'bright indigo': '2'}
bright tan {'faded purple': '5', 'dotted gray': '3'}
faded purple {'striped fuchsia': '4', 'mirrored fuchsia': '3', 'dotted gray': '2', 'muted coral': '4'}
striped fuchsia {'dim cyan': '3'}
dotted gray {'dull violet': '5', 'dark plum': '5', 'bright indigo': '2', 'wavy bronze': '2'}
dull violet {'dotted purple': '1'}
dotted purple {'plaid salmon': '1', 'bright indigo': '2'}
muted coral {'vibrant plum': '1', 'plaid salmon': '4', 'bright indigo': '2'}
vibrant plum {'dim cyan': '4', 'pale maroon': '3'}
pale maroon {'striped fuchsia': '3', 'plaid silver': '5', 'shiny teal': '4'}
striped fuchsia {'dim cyan': '3'}
dotted gray {'dull violet': '5', 'dark plum': '5', 'bright indigo': '2', 'wavy bronze': '2'}
dull violet {'dotted purple': '1'}
dotted purple {'plaid salmon': '1', 'bright indigo': '2'}
muted orange {'dull violet': '2', 'striped beige': '4', 'plaid salmon': '1', 'mirrored fuchsia': '3'}
dull violet {'dotted purple': '1'}
dotted purple {'plaid salmon': '1', 'bright indigo': '2'}
shiny indigo {'dotted green': '4'}
dotted green {'wavy bronze': '4', 'dull violet': '3', 'striped beige': '2'}
dull violet {'dotted purple': '1'}
dotted purple {'plaid salmon': '1', 'bright indigo': '2'}
"""
