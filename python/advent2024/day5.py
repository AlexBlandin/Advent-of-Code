from functools import cmp_to_key
from pathlib import Path

lines = Path("day5.txt").read_text().splitlines()
switch = lines.index("")
page_order = {tuple(map(int, line.split("|"))) for line in lines[:switch]}
updates = [list(map(int, line.split(","))) for line in lines[switch + 1 :]]
LUT_SORT = cmp_to_key(lambda x, y: -1 if (x, y) in page_order else 1 if (y, x) in page_order else 0)
ordered = [sorted(pages, key=LUT_SORT) for pages in updates]

print(
  sum(pages[len(pages) // 2] for pages, order in zip(updates, ordered) if pages == order),
  sum(order[len(order) // 2] for pages, order in zip(updates, ordered) if pages != order),
)
