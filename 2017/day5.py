from pathlib import Path

jumps = list(map(int, Path("day5.txt").read_text().splitlines()))
