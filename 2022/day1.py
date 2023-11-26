from pathlib import Path

print(
  max(elves := sorted(
    map(lambda elf: sum(map(int, elf.split())),
        Path("day1.txt").read_text().split("\n\n")),
    reverse = True,
  )),
  sum(elves[:3]),
)
