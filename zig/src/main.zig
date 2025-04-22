const std = @import("std");
const print = std.debug.print;

pub fn main() !void {
    // Read a file line by line
    var file = try std.fs.cwd().openFile("foo.txt", .{});
    defer file.close();

    var buf_reader = std.io.bufferedReader(file.reader());
    var in_stream = buf_reader.reader();

    var buf: [1024]u8 = undefined;
    while (try in_stream.readUntilDelimiterOrEof(&buf, '\n')) |line| {
        _ = line;
    }

    // find a needle in a haystack
    const text = "abcdef";
    const needle = 'e';
    const match: ?usize = for (text, 0..) |x, idx| {
        if (x == needle) break idx;
    } else null;
    _ = match;

    // Just quickly show some nice vector stuff
    const V = @Vector(4, u8);
    const B = @Vector(4, bool);
    const Ones: V = @splat(1);
    const Zeroes: V = @splat(0);
    const x: V = @select(u8, @as(B, @splat(true)), Ones, Zeroes);
    const y: V = @select(u8, @as(B, @splat(false)), Ones, Zeroes);
    const a = x & y;
    print("{}\n", .{a});
}
