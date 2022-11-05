from pathlib import Path

stream = Path("day9.txt").read_text().strip()
cancel, garbage = False, False
depth, score, removed = 0, 0, 0

for i, c in enumerate(stream):
  if cancel:
    cancel = False
    continue
  match c:
    case "!" if garbage:
      cancel = True
    case ">" if garbage:
      garbage = False
    case "<" if not garbage:
      garbage = True
    case "{" if not garbage:
      depth += 1
      score += depth
    case "}" if not garbage:
      depth -= 1
    case "," if not garbage:
      pass
    case _ if garbage:
      removed += 1

print(score, removed)
