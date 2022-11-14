from pathlib import Path

lines = dict(tuple(map(int, line.split())) for line in Path("day13.txt").read_text().replace(":","").splitlines())
