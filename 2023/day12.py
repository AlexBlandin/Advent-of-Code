from collections.abc import Generator
from enum import Enum
from itertools import product
from pathlib import Path
from typing import Any


class Status(Enum):
  Damaged = "#"
  Operational = "."
  Unknown = "?"

  def __repr__(self) -> str:
    return self.value


def solve(row: list[Status], acc: list[int]):
  """The idea here is to take the `O(n^2)` masks of damaged runs (in order) and match those
  rather than the direct `O(2^n)` backtracking over `n` variables/unknowns.

  we can then explore every unknown `?` by placing masks in order (skipping any adjacent/covered unknown), for example:

  - `.??..??...?##.` `1,1,3` (input)
  - `0b1` `0b1` `0b111` (masks)
  - `10011001110001` (operational)
  - `00000000000110` (damaged)
  - `01100110001000` (unknown)
  - `01100111000000: continue` (never explored if we guarantee `0b111`'s position / don't place adjacent unknowns)
  - `01100000001110: continue` (never explored as we don't place adjacent unknowns)
  - `01000100001110: yield`
  - `00100100001110: yield`
  - `01000010001110: yield`
  - `00100010001110: yield`
  - `00000110001110: continue` (never explored as we don't place adjacent unknowns)
  - `01000111100000: continue` (never explored if we guarantee `0b111`'s position / don't place adjacent unknowns)
  - `00100111100000: continue` (never explored if we guarantee `0b111`'s position / don't place adjacent unknowns)
  - `000000000011111: continue` (never explored as we don't place adjacent unknowns)
  """
  # if we can guarantee any in runs, put them in place already
  # so if there's a run of 6 in damaged and in acc, that's placed already? issue, how do we tombstone so order of runs is preserved?
  # one answer, for runs have a list of "guaranteed" which just tags if that run has been guaranteed,
  # which is just used when checking when to place that specific run, otherwise it's not touched and order is preserved
  damaged, unknown, operational = 0, 0, 0
  # if cand & operational: continue # should never place a damaged spring where we know there's a working spring
  for i, spring in enumerate(row):
    match spring:
      case Status.Damaged:
        damaged |= 1 << i
      case Status.Unknown:
        unknown |= 1 << i
      case Status.Operational:
        operational |= 1 << i
  maybe = damaged | unknown
  masks: list[int] = [2**a - 1 for a in acc]

  def bits(n: int):
    return list(map(int, reversed(bin(n)[2:].rjust(len(row), "0"))))

  def bitmasks2enums(damaged: int, unknown: int):
    return [Status.Damaged if d else Status.Unknown if u else Status.Operational for d, u in zip(bits(damaged), bits(unknown), strict=False)]

  def valid(cand: int):
    return account(bitmasks2enums(cand | damaged, 0), acc) == acc

  def recursion(frm: int, next_mask: int, cand: int):
    if valid(cand):
      # print(
      #   bits(cand),
      #   bits(cand | damaged),
      #   frm,
      #   next_mask,
      #   "(yield)",
      #   "".join(bitmasks2enums(cand | damaged, 0)),
      #   account(bitmasks2enums(cand | damaged, 0), acc),
      #   sep="\t",
      # )
      yield cand | damaged
    elif frm < len(row) and next_mask < len(masks):
      for i in range(frm, len(row)):
        if (1 << i) & maybe and not (m := masks[next_mask] << i) & operational and not m.bit_length() > len(row):
          if m & unknown:
            yield from recursion(i + 2, next_mask + 1, cand | m)
          elif m & damaged == m:  # skip mask if it's fully accounted for already
            yield from recursion(i, next_mask + 1, cand)
    else: ...
    # print(
    #   bits(cand),
    #   bits(cand | damaged),
    #   frm,
    #   next_mask,
    #   "(invalid)",
    #   "".join(bitmasks2enums(cand | damaged, 0)),
    #   account(bitmasks2enums(cand | damaged, 0), acc),
    #   sep="\t",
    # )

  # print("".join(row), acc, *map(bits, masks))
  yield from recursion(0, 0, 0)


def solve_old(row: list[Status], acc: list[int]) -> Generator[list[Status], Any, None]:
  # the performance issue is that we don't eliminate things that can't fit early, so we're just exploring 2*N for N variables on each line
  # so the way we do subst doesn't really work?
  # I need to go "well, this part of subst just can't work, so don't explore deeper"
  # ...
  for subst in map(list, product([Status.Damaged, Status.Operational], repeat=row.count(Status.Unknown))):
    cand = [subst.pop() if r is Status.Unknown else r for r in row]
    run = account(cand, acc)
    if run and (run[:-1] if run[-1] == 0 else run) == acc:
      yield cand


def account(cand: list[Status], acc: list[int]) -> list[int]:  # noqa: ARG001
  run: list[int] = [0]
  for spring in cand:
    if spring is Status.Damaged:
      run[-1] += 1
    elif run[-1] != 0:
      run.append(0)
    # if run[:-1] != acc[: len(run) - 1]:
    #   continue
  return run if run[-1] else run[:-1]


def to_status(rows: list[str]) -> list[list[Status]]:
  return [list(map(Status, row)) for row in rows]


def to_accounts(accs: list[str]) -> list[list[int]]:
  return [list(map(int, acc.split(","))) for acc in accs]


lines = Path("day12.txt").read_text().splitlines()
_lines = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()
splits = list(map(str.split, lines))
rows = [line[0] for line in splits]
accounts = [line[1] for line in splits]
unfolded_rows = ["?".join([line[0]] * 5) for line in splits]
unfolded_accounts = [",".join([line[1]] * 5) for line in splits]

print(
  sum(len(set(cands)) for cands in map(solve, to_status(rows), to_accounts(accounts))),
  # sum(len(set(cands)) for cands in map(solve, to_status(unfolded_rows), to_accounts(unfolded_accounts))),
)
