const std = @import("std");
const print = std.debug.print;

const Pos: type = @Vector(2, i32); // {x,y}
const Turn = enum { R, L };
const Op = struct { turn: Turn, forward: u8 };
const Dir = enum {
    N, // Advent of Code 2016, Day 1, Part 1
    S, //  N    +y
    E, // W E -x  +x
    W, //  S    -y
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
    fn move(facing: Dir, n: u8) Pos {
        return Pos{ n, n } * switch (facing) {
            .N => Pos{ 0, 1 },
            .S => Pos{ 0, -1 },
            .E => Pos{ 1, 0 },
            .W => Pos{ -1, 0 },
        };
    }
};

fn part1(ops: []Op) u32 {
    var pos = Pos{ 0, 0 };
    var dir = Dir.N;
    for (ops) |op| {
        dir = dir.face(op.turn);
        pos += dir.move(op.forward);
    }
    return @intCast(@reduce(.Add, @abs(pos)));
}

pub fn main() !void {
    //const input = "R1, L3, R5, R5, R5, L4, R5, R1, R2, L1, L1, R5, R1, L3, L5, L2, R4, L1, R4, R5, L3, R5, L1, R3, L5, R1, L2, R1, L5, L1, R1, R4, R1, L1, L3, R3, R5, L3, R4, L4, R5, L5, L1, L2, R4, R3, R3, L185, R3, R4, L5, L4, R48, R1, R2, L1, R1, L4, L4, R77, R5, L2, R192, R2, R5, L4, L5, L3, R2, L4, R1, L5, R5, R4, R1, R2, L3, R4, R4, L2, L4, L3, R5, R4, L2, L1, L3, R1, R5, R5, R2, L5, L2, L3, L4, R2, R1, L4, L1, R1, R5, R3, R3, R4, L1, L4, R1, L2, R3, L3, L2, L1, L2, L2, L1, L2, R3, R1, L4, R1, L1, L4, R1, L2, L5, R3, L5, L2, L2, L3, R1, L4, R1, R1, R2, L1, L4, L4, R2, R2, R2, R2, R5, R1, L1, L4, L5, R2, R4, L3, L5, R2, R3, L4, L1, R2, R3, R5, L2, L3, R3, R1, R3";
    const input = "R5, L5, R5, R3"; // can get away with way simpler if this is all we have to parse, but above has 3 digit numbers
    const ops = comptime parse: {
        var buf: [(input.len + 2) >> 2]Op = undefined; // upper bound of size, so we slice out as needed for ops
        var i: u32 = 0;
        var tokens = std.mem.tokenizeAny(u8, input, ", ");
        while (tokens.next()) |tok| {
            buf[i] = Op{
                .turn = if (tok[0] == 'R') .R else .L,
                .forward = std.fmt.parseUnsigned(u8, tok[1..], 10) catch unreachable,
            };
            i += 1;
        }
        break :parse buf[0..i];
    };

    const solution = part1(ops);
    print("{}", .{solution}); // 298 or 12
}