from pathlib import Path

print(
  max(
    elves := sorted(
      (sum(map(int, elf.split())) for elf in Path("day1.txt").read_text().split("\n\n")),
      reverse=True,
    ),
  ),
  sum(elves[:3]),
)
