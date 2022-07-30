from pathlib import Path

pos = list(map(int, Path("data/day7.txt").read_text().split(",")))
# pos = [16,1,2,0,4,2,7,1,2,14]
deltas = {p: sum(abs(p - q) for q in pos) for p in range(min(pos), max(pos) + 1)}
alignment = min(deltas, key = deltas.get)

def tri(n):
  return (n * (n + 1)) // 2

trideltas = {p: sum(tri(abs(p - q)) for q in pos) for p in range(min(pos), max(pos) + 1)}
trialignment = min(trideltas, key = trideltas.get)
print(deltas[alignment], trideltas[trialignment])
