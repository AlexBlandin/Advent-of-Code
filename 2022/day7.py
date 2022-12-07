from dataclasses import dataclass
from pathlib import Path

lines = Path("day7.txt").read_text().splitlines()

@dataclass
class File:
  path: Path
  size: int
  dir: bool = False

files = {Path(): File(Path(), 0, True)}
cwd = Path()

for line in lines:
  match line.split():
    case ["$", "cd", "/"]:
      cwd = Path()
    case ["$", "cd", ".."]:
      cwd = cwd.parent
    case ["$", "cd", subdir]:
      cwd = file = cwd / subdir
      files[file] = File(file, 0, True)
    case ["$", "ls"]:
      continue
    case ["dir", subdir]:
      file = cwd / subdir
      files[file] = File(file, 0, True)
    case [filesize, filename] if filesize.isnumeric():
      file, filesize = cwd / filename, int(filesize)
      if file not in files:
        files[file] = File(file, filesize)
        files[cwd].size += filesize

for dir in sorted(filter(lambda file: file.dir, files.values()), key=lambda dir: len(dir.path.parents), reverse=True):
  files[dir.path.parent].size += dir.size # bottom up is the correct way

free_up = sum(file.size for file in files.values() if not file.dir) - (70000000 - 30000000)

print(sum(file.size for file in files.values() if file.dir and file.size <= 100000), min(file.size for file in files.values() if file.dir and file.size >= free_up))
