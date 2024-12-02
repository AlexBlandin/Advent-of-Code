from itertools import pairwise
from pathlib import Path

lines = Path("day2.txt").read_text().splitlines()

reports = {tuple(map(int, line.split())) for line in lines}
# ruff: noqa: PLR2004
safe_reports = {
  report
  for report in reports
  if (
    all(a <= b and 1 <= abs(a - b) <= 3 for a, b in pairwise(report))
    or all(a >= b and 1 <= abs(a - b) <= 3 for a, b in pairwise(report))
  )
}
safe_ish_reports = safe_reports | {
  report
  for report in reports.difference(safe_reports)
  if any(
    all(a <= b and 1 <= abs(a - b) <= 3 for a, b in pairwise(redacted))
    or all(a >= b and 1 <= abs(a - b) <= 3 for a, b in pairwise(redacted))
    for redacted in ((*report[:i], *report[i + 1 :]) for i in range(len(report)))
  )
}

print(
  len(safe_reports),
  len(safe_ish_reports),
)
