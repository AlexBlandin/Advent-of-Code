from pathlib import Path

lines = Path("day8.txt").read_text(encoding = "latin1").splitlines()
mem, esc, original = 0, 0, sum(map(len, lines))
for i, line in enumerate(lines):
  el, rl = eval(line), '"\\"' + repr(line)[2:-2].replace('"', '\\"') + '\\""'
  mem += len(el)
  esc += len(rl)
print(original - mem, esc - original)
