from pathlib import Path

cwd, size, dirs = Path(), {Path(): 0}, {Path()}
for line in Path("day7.txt").read_text().splitlines():
  match line.split():
    case ["$", "cd", "/"]:
      cwd = Path()
    case ["$", "cd", ".."]:
      cwd = cwd.parent
    case ["$", "cd", subdir]:
      cwd /= subdir
    case ["dir", subdir]:
      file = cwd / subdir
      size[file] = 0
      dirs.add(file)
    case [filesize, filename] if filesize.isnumeric():
      file, filesize = cwd / filename, int(filesize)
      size[file], size[cwd] = filesize, size[cwd] + filesize

for path in sorted([path for path in size if path in dirs], key=lambda path: len(path.parents), reverse=True):
  size[path.parent] += size[path]
free_up = sum(filesize for path, filesize in size.items() if path not in dirs) - 40000000

print(sum(filesize for path, filesize in size.items() if path in dirs and filesize <= 100000), min(filesize for path, filesize in size.items() if path in dirs and filesize >= free_up))
