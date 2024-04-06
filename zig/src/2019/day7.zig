const std = @import("std");
const mem = std.mem;
const expect = std.testing.expect;
const print = std.debug.print;
const ArrayList = std.ArrayList;

const Sol = struct { p1: i32 = 0, p2: i32 = 0 }; // change to []u8 if needed
const input: []const u8 = @embedFile("day7.txt");

fn day7(str: []const u8, allocator: mem.Allocator) !Sol {
    _ = allocator;
    _ = str;
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    print("Input: {s}\n", .{input});

    const start = std.time.nanoTimestamp();
    const sol = try day7(input, allocator);
    const end = std.time.nanoTimestamp();
    const elapsed = end - start;

    print("Solutions: {} {}\n", sol);
    print("Elapsed: {}ns", .{elapsed});
}

const test_alloc = std.testing.allocator;

test "examples" {
    try expect((try day7("abc", test_alloc)).p1 != 0);
    try expect((try day7("abc", test_alloc)).p2 != 0);
}

test "answers" {
    try expect((try day7(input, test_alloc)).p1 != 0);
    try expect((try day7(input, test_alloc)).p2 != 0);
}
