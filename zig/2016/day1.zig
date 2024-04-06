const std = @import("std");
const mem = std.mem;
const expect = std.testing.expect;
const print = std.debug.print;
const ArrayList = std.ArrayList;

const Sol = struct { p1: i32 = 0, p2: i32 = 0 };
const input: []const u8 = @embedFile("day1.txt");

// N    +y     227      [1]
//W E -x  +x  0  205  >>   <<
// S    -y      0       [0]

const Coord: type = @Vector(2, i32); // x,y
const Index: type = @Vector(2, u8); // x,y but unsigned, for use in Grid
const Row: type = u206; // 205 + 1
const Grid: type = @Vector(227 + 1, Row);
const Turn = enum { R, L };
const Op = struct { d: Turn, n: u8 };
const Dir = enum {
    N,
    S,
    E,
    W,
    fn face(facing: Dir, turn: Turn) Dir {
        return if (turn == .L) switch (facing) {
            .N => .W,
            .S => .E,
            .E => .N,
            .W => .S,
        } else switch (facing) {
            .N => .E,
            .S => .W,
            .E => .S,
            .W => .N,
        };
    }
    fn move(facing: Dir, n: u8) Coord {
        return Coord{ n, n } * switch (facing) {
            .N => Coord{ 0, 1 },
            .S => Coord{ 0, -1 },
            .E => Coord{ 1, 0 },
            .W => Coord{ -1, 0 },
        };
    }
    fn offset(facing: Dir, n: u8) Index {
        return Index{ n, n } * switch (facing) {
            .N, .S => Index{ 0, 1 },
            .E, .W => Index{ 1, 0 },
        };
    }
};

fn day1(str: []const u8, allocator: mem.Allocator) !Sol {
    var sol = Sol{};
    var ops = std.ArrayList(Op).init(allocator);
    defer ops.deinit();

    var tokens = std.mem.tokenizeAny(u8, str, ", \n");
    while (tokens.next()) |tok| {
        var op: Op = undefined;
        op.d = if (tok[0] == 'R') .R else .L;
        op.n = @intCast(std.fmt.parseUnsigned(u32, tok[1..], 10) catch unreachable);
        try ops.append(op);
    }

    // var max = Coord{ 0, 0 }; // not needed
    var min = Coord{ 0, 0 };
    { // Part 1
        var xy = Coord{ 0, 0 };
        var d = Dir.N;
        for (ops.items) |op| {
            d = d.face(op.d);
            xy += d.move(op.n);
            min = @min(min, xy);
            // max = @max(max, xy);
        }
        sol.p1 = @intCast(@reduce(.Add, @abs(xy)));
    }
    // max: { 35, 221 } min: { -170, -6 } del: { 205, 227 }
    // print("max: {} min: {} del: {}\n", .{ max, min, @abs(max - min) });

    var grid: Grid = @splat(0);
    const ones: Grid = @splat(1);
    const zero: Grid = @splat(0);
    comptime var rows: Grid = undefined;
    comptime for (0..@typeInfo(Grid).Vector.len) |i| {
        rows[i] = i;
    };
    { // Part 2
        var xy = Index{ @intCast(@abs(min[0])), @intCast(@abs(min[1])) }; // 0,0 offset, so we stay in bounds
        var d = Dir.N;
        const loc = search: for (ops.items, 0..) |op, opid| {
            _ = opid;
            d = d.face(op.d);
            const x = xy[0];
            const y = xy[1];
            const n = d.offset(op.n); // how far do we try to go
            const v = @reduce(.Add, n);

            switch (d) {
                .E, .W => { // easy row time, East is high bits (<<), West is low bits (>>)
                    // how many steps we will take ((1 << v) - 1) << 1, so 000001 << v:3 = 000001000 -1 = 00000111 << 1 = 000001110
                    // offset the span from our starting position (x)
                    // heading East is ((1 << v) - 1) << 1 + x, 000001110 << x:0 = 00000111o, 000001110 << x:1 = 00000111o0 (where o is our start)
                    // heading West is (x), ((1 << v) - 1) << 1 + x - (v + 1), 000001110 << x:4-v:3 = 0000o1110, 000001110 << x:5-v:3 = 000o11100
                    // since the difference is just -(v+1) we can inline an if to handle that ((1 << v) - 1) << 1 + x - (if (d == .W) v + 1 else 0);
                    const span: Row = ((@as(Row, 1) << @intCast(v)) - 1) << 1 + x - (if (d == .W) v + 1 else 0);
                    const view: Row = grid[y] & span; // what our grid looks like under the span

                    if (view != 0) { // we overlapped with our tail (it's like snake, right?)
                        // print("{}: {} v = {} {s} {b:0>227}\n", .{ opid, xy, v, @tagName(d), view });
                        break :search Coord{
                            @as(i32, if (d == .E) // if heading East, then we came from the West, so our starting position is in the low bits, get the nearest to that
                                std.math.log2_int(Row, view & -%view) // lowest set bit
                            else
                                std.math.log2_int(Row, view & ~(span >> 1)) // highest set bit
                            ),
                            y,
                        };
                    }
                    grid[y] = grid[y] | span;
                },
                .N, .S => { // North is upper rows (grid[Grid.len-1]), South is lower rows (grid[0])
                    const upper = if (d == .N) y + v else y - 1;
                    const lower = if (d == .S) y - v else y + 1;
                    const cupp = @select(Row, rows <= @as(Grid, @splat(upper)), ones, zero);
                    const clow = @select(Row, rows >= @as(Grid, @splat(lower)), ones, zero);
                    const clip = clow & cupp;
                    const span = clip * ones << @splat(x);
                    const view = grid & span; // what our grid looks like under the span
                    const mask = @as(Row, 1) << x; // extract the x coordinate

                    if (@reduce(.Or, view) != 0) {
                        if (d == .N) { // go up from lower rows
                            for (lower..upper + 1) |i| {
                                if (view[i] & mask != 0) {
                                    // print("{}: {} v = {} {s} {b:0>227}\n", .{ opid, xy, v, @tagName(d), view[i] });
                                    break :search Coord{ x, @intCast(i) };
                                }
                            }
                        } else { // go down from upper rows
                            var i = upper;
                            while (i >= lower) : (i -= 1) {
                                if (view[i] & mask != 0) {
                                    // print("{}: {} v = {} {s} {b:0>227}\n", .{ opid, xy, v, @tagName(d), view[i] });
                                    break :search Coord{ x, @intCast(i) };
                                }
                            }
                        }
                    }

                    grid |= span;
                },
            }

            xy = if (d == .N or d == .E) xy + n else xy - n; // if we didn't break, move xy and carry on!
        } else min;
        sol.p2 = @reduce(.Add, @as(Coord, loc) - min);
        for (0..@typeInfo(Grid).Vector.len) |i| {
            print("{b:0>227}\n", .{grid[i]});
        }
    }
    return sol;
}

pub fn main() !void {
    var arena = std.heap.ArenaAllocator.init(std.heap.page_allocator);
    defer arena.deinit();
    const allocator = arena.allocator();

    print("Input: {s}\n", .{input});

    const start = std.time.nanoTimestamp();
    const sol = try day1(input, allocator);
    const end = std.time.nanoTimestamp();
    const elapsed = end - start;

    print("Solutions: {} {} (p2 should be 158)\n", sol);
    print("Elapsed: {}ns", .{elapsed});
}

const test_alloc = std.testing.allocator;

test "examples" {
    try expect((try day1("R2, L3", test_alloc)).p1 == 5);
    try expect((try day1("R2, R2, R2", test_alloc)).p1 == 2);
    try expect((try day1("R5, L5, R5, R3", test_alloc)).p1 == 12);
    try expect((try day1("R8, R4, R4, R8", test_alloc)).p2 == 4);
}

test "answers" {
    try expect((try day1(input, test_alloc)).p1 == 298);
    try expect((try day1(input, test_alloc)).p2 == 158);
}
