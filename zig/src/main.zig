const std = @import("std");
const print = std.debug.print;

pub fn main() !void {
    const V = @Vector(4, u8);
    const B = @Vector(4, bool);
    const Ones: V = @splat(1);
    const Zeroes: V = @splat(0);
    var x: V = @select(u8, @as(B, @splat(true)), Ones, Zeroes);
    var y: V = @select(u8, @as(B, @splat(false)), Ones, Zeroes);
    var a = x & y;
    print("{}\n", .{a});
}
