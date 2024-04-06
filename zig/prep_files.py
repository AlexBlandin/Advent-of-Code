from datetime import date
from pathlib import Path

fmt_day = """const std = @import("std");
const mem = std.mem;
const expect = std.testing.expect;
const print = std.debug.print;
const ArrayList = std.ArrayList;

const Sol = struct { p1: i32 = 0, p2: i32 = 0 }; // change to []u8 if needed
const input: []const u8 = @embedFile("day{day}.txt");

fn day{day}(str: []const u8, allocator: mem.Allocator) !Sol {
    _ = allocator;
    _ = str;
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    print("Input: {s}\\n", .{input});

    const start = std.time.nanoTimestamp();
    const sol = try day{day}(input, allocator);
    const end = std.time.nanoTimestamp();
    const elapsed = end - start;

    print("Solutions: {} {}\\n", sol);
    print("Elapsed: {}ns", .{elapsed});
}

const test_alloc = std.testing.allocator;

test "examples" {
    try expect((try day{day}("abc", test_alloc)).p1 != 0);
    try expect((try day{day}("abc", test_alloc)).p2 != 0);
}

test "answers" {
    try expect((try day{day}(input, test_alloc)).p1 != 0);
    try expect((try day{day}(input, test_alloc)).p2 != 0);
}
"""

fmt_all = """"""

for year in range(2015, date.today().year + 1):
  dir = Path(__file__).parent / "src" / str(year)
  if not dir.exists():
    dir.mkdir(exist_ok=True)
  for day in range(1, 26):
    zig = dir / f"day{day}.zig"
    data = dir / f"day{day}.txt"
    zig.touch()
    data.touch()
    if zig.read_text().strip() == "":
      zig.write_text(fmt_day.replace("{day}", str(day)), encoding="utf8", newline="\n")
    if data.read_text().strip() == "":
      data.write_text("", encoding="utf8", newline="\n")
