with open("day18.txt", encoding="utf8") as o:
  lines = [line.strip() for line in o]

results, log = [], []
for line in lines:
  # what I want to detect is that "you have mixed + and * within the same brackets / at top-level" and only do "bracketing" then
  # this currently inserts it "dumbly"

  result = []
  for nex, val, prev in zip([*line.split()[1:], None], line.split(), [None, *line.split()], strict=False):
    if val[0].isdigit() and nex in {"+", "*"} and prev in {"+", "*"}:
      result.append(f"{val})")
    elif val[0].isdigit() and nex in {"+", "*"}:
      result.append(f"({val}")  # replace "<val>" with "(<val>"
    elif val[0].isdigit() and prev in {"+", "*"} and val[-1] != ")":
      result.append(f"{val})")  # replace "<val>" with "<val>)"
    else:
      result.append(val)
  result = " ".join(result)
  result = "(" * (result.count(")") - result.count("(")) + result + ")" * (result.count("(") - result.count(")"))
  results.append(eval(result))  # so a nice idea, wrong results
  log.append((result, eval(result)))

print(log[:3])
print(sum(results))
