from pathlib import Path

lines = Path("data/day10.txt").read_text().splitlines()
corruption_score, discarded_score = 0, []
for line in lines:
  s, n = [], {"(":0,"[":0,"{":0,"<":0}
  for c in line:
    match c:
      case "(" | "[" | "{" | "<":
        s.append(c)
        n[c] += 1
      case ")" | "]" | "}" | ">":
        if s[-1]+c in {"()","[]","{}","<>"}:
          n[s.pop()] -= 1
        else:
          corruption_score += {")":3,"]":57,"}":1197,">":25137}[c]
          break
  else: # incomplete
    score = 0
    for c in s[::-1]:
      score *= 5
      score += {"(":1,"[":2,"{":3,"<":4}[c]
    discarded_score.append(score)

discarded_score = sorted(discarded_score)[len(discarded_score)//2]
print(corruption_score, discarded_score)
