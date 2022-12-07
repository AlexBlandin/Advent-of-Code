from dataclasses import dataclass
from pathlib import Path

@dataclass
class File:
  path: Path
  size: int
  dir: bool = False

cwd, files = Path(), {Path(): File(Path(), 0, True)}
for line in Path("day7.txt").read_text().splitlines():
  match line.split():
    case ["$", "cd", "/"]:
      cwd = Path()
    case ["$", "cd", ".."]:
      cwd = cwd.parent
    case ["$", "cd", subdir]:
      cwd = file = cwd / subdir
      files[file] = File(file, 0, True)
    case ["dir", subdir]:
      file = cwd / subdir
      files[file] = File(file, 0, True)
    case [filesize, filename] if filesize.isnumeric():
      file, filesize = cwd / filename, int(filesize)
      files[file] = File(file, filesize)
      files[cwd].size += filesize

for dir in sorted(filter(lambda file: file.dir, files.values()), key=lambda dir: len(dir.path.parents), reverse=True):
  files[dir.path.parent].size += dir.size
free_up = sum(file.size for file in files.values() if not file.dir) - (70000000 - 30000000)

print(sum(file.size for file in files.values() if file.dir and file.size <= 100000), min(file.size for file in files.values() if file.dir and file.size >= free_up))
