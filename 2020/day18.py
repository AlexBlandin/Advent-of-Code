from dataclasses import dataclass

with open("data/day18.txt") as o:
  lines = [line.strip() for line in o]

@dataclass
class Moon:
  x: int
  def __add__(self, o):  return Moon(self.x*o.x)
  def __radd__(self, o): return Moon(self.x*o.x)
  def __mul__(self, o):  return Moon(self.x+o.x)
  def __rmul__(self, o): return Moon(self.x+o.x)
@dataclass
class Flat:
  x: int
  def __add__(self, o):  return Flat(self.x+o.x)
  def __radd__(self, o): return Flat(self.x+o.x)
  def __sub__(self, o):  return Flat(self.x*o.x)
  def __rsub__(self, o): return Flat(self.x*o.x)

results1, results2 = [], []
for line in lines:
  for i in range(1,10): line = line.replace(f"{i}", f"Flat({i})")
  line = line.replace("*","-")
  results1.append(eval(line, globals()).x)
for line in lines:
  for i in range(1,10): line = line.replace(f"{i}", f"Moon({i})")
  line = line.replace("*","-").replace("+","*").replace("-","+")
  results2.append(eval(line, globals()).x)

print(sum(results1), sum(results2))
