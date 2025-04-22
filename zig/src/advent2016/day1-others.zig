const std = @import("std");

pub fn main() !void {
    const stdout = std.io.getStdOut().writer();
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    const limit = 1 * 1024 * 1024;
    const text = try std.fs.cwd().readFileAlloc(allocator, "day1.txt", limit);
    defer allocator.free(text);

    const V = struct {
        x: i32,
        y: i32,
    };
    const dirs = [_]V{
        .{ .x = 0, .y = -1 },
        .{ .x = 1, .y = 0 },
        .{ .x = 0, .y = 1 },
        .{ .x = -1, .y = 0 },
    };

    var map: [1000 * 1000]u1 = [1]u1{0} ** (1000 * 1000);
    var p = V{ .x = 500, .y = 500 };
    var edir: u2 = 0;

    var it = std.mem.tokenize(u8, text, " ,\n");
    blk: while (it.next()) |insn| {
        var d: i32 = std.fmt.parseInt(i32, insn[1..], 10) catch unreachable;
        switch (insn[0]) {
            'L' => edir -%= 1,
            'R' => edir +%= 1,
            else => unreachable,
        }

        while (d > 0) : (d -= 1) {
            map[@as(usize, @intCast(p.x + 1000 * p.y))] = 1;
            p.x += dirs[edir].x;
            p.y += dirs[edir].y;
            if (map[@as(usize, @intCast(p.x + 1000 * p.y))] != 0) {
                try stdout.print("pos= {}  d= {}\n", .{ p, std.math.absCast(p.x) + std.math.absCast(p.y) });

                break :blk;
            }
        }
    }

    p.x -= 500;
    p.y -= 500;
    try stdout.print("pos= {}  d= {}\n", .{ p, std.math.absCast(p.x) + std.math.absCast(p.y) });
}
