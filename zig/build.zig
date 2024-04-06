const std = @import("std");
const fs = std.fs;
const mem = std.mem;
const cwd = std.fs.cwd;
const debug = std.debug;

pub fn build(b: *std.Build) void {
    const target = b.standardTargetOptions(.{});
    const optimize = b.standardOptimizeOption(.{});

    const Problem = struct {
        year: []const u8,
        day: []const u8,
    };
    const problems = [_]Problem{
        .{ .year = "2023", .day = "day25" },
        .{ .year = "2023", .day = "day24" },
        .{ .year = "2023", .day = "day23" },
        .{ .year = "2023", .day = "day22" },
        .{ .year = "2023", .day = "day21" },
        .{ .year = "2023", .day = "day20" },
        .{ .year = "2023", .day = "day19" },
        .{ .year = "2023", .day = "day18" },
        .{ .year = "2023", .day = "day17" },
        .{ .year = "2023", .day = "day16" },
        .{ .year = "2023", .day = "day15" },
        .{ .year = "2023", .day = "day14" },
        .{ .year = "2023", .day = "day13" },
        .{ .year = "2023", .day = "day12" },
        .{ .year = "2023", .day = "day11" },
        .{ .year = "2023", .day = "day10" },
        .{ .year = "2023", .day = "day09" },
        .{ .year = "2023", .day = "day08" },
        .{ .year = "2023", .day = "day07" },
        .{ .year = "2023", .day = "day06" },
        .{ .year = "2023", .day = "day05" },
        .{ .year = "2023", .day = "day04" },
        .{ .year = "2023", .day = "day03" },
        .{ .year = "2023", .day = "day02" },
        .{ .year = "2023", .day = "day01" },
        .{ .year = "2023", .day = "all" },

        .{ .year = "2022", .day = "day25" },
        .{ .year = "2022", .day = "day24" },
        .{ .year = "2022", .day = "day23" },
        .{ .year = "2022", .day = "day22" },
        .{ .year = "2022", .day = "day21" },
        .{ .year = "2022", .day = "day20" },
        .{ .year = "2022", .day = "day19" },
        .{ .year = "2022", .day = "day18" },
        .{ .year = "2022", .day = "day17" },
        .{ .year = "2022", .day = "day16" },
        .{ .year = "2022", .day = "day15" },
        .{ .year = "2022", .day = "day14" },
        .{ .year = "2022", .day = "day13" },
        .{ .year = "2022", .day = "day12" },
        .{ .year = "2022", .day = "day11" },
        .{ .year = "2022", .day = "day10" },
        .{ .year = "2022", .day = "day09" },
        .{ .year = "2022", .day = "day08" },
        .{ .year = "2022", .day = "day07" },
        .{ .year = "2022", .day = "day06" },
        .{ .year = "2022", .day = "day05" },
        .{ .year = "2022", .day = "day04" },
        .{ .year = "2022", .day = "day03" },
        .{ .year = "2022", .day = "day02" },
        .{ .year = "2022", .day = "day01" },
        .{ .year = "2022", .day = "all" },

        .{ .year = "2021", .day = "day25" },
        .{ .year = "2021", .day = "day24" },
        .{ .year = "2021", .day = "day23" },
        .{ .year = "2021", .day = "day22" },
        .{ .year = "2021", .day = "day21" },
        .{ .year = "2021", .day = "day20" },
        .{ .year = "2021", .day = "day19" },
        .{ .year = "2021", .day = "day18" },
        .{ .year = "2021", .day = "day17" },
        .{ .year = "2021", .day = "day16" },
        .{ .year = "2021", .day = "day15" },
        .{ .year = "2021", .day = "day14" },
        .{ .year = "2021", .day = "day13" },
        .{ .year = "2021", .day = "day12" },
        .{ .year = "2021", .day = "day11" },
        .{ .year = "2021", .day = "day10" },
        .{ .year = "2021", .day = "day09" },
        .{ .year = "2021", .day = "day08" },
        .{ .year = "2021", .day = "day07" },
        .{ .year = "2021", .day = "day06" },
        .{ .year = "2021", .day = "day05" },
        .{ .year = "2021", .day = "day04" },
        .{ .year = "2021", .day = "day03" },
        .{ .year = "2021", .day = "day02" },
        .{ .year = "2021", .day = "day01" },
        .{ .year = "2021", .day = "all" },

        .{ .year = "2020", .day = "day25" },
        .{ .year = "2020", .day = "day24" },
        .{ .year = "2020", .day = "day23" },
        .{ .year = "2020", .day = "day22" },
        .{ .year = "2020", .day = "day21" },
        .{ .year = "2020", .day = "day20" },
        .{ .year = "2020", .day = "day19" },
        .{ .year = "2020", .day = "day18" },
        .{ .year = "2020", .day = "day17" },
        .{ .year = "2020", .day = "day16" },
        .{ .year = "2020", .day = "day15" },
        .{ .year = "2020", .day = "day14" },
        .{ .year = "2020", .day = "day13" },
        .{ .year = "2020", .day = "day12" },
        .{ .year = "2020", .day = "day11" },
        .{ .year = "2020", .day = "day10" },
        .{ .year = "2020", .day = "day09" },
        .{ .year = "2020", .day = "day08" },
        .{ .year = "2020", .day = "day07" },
        .{ .year = "2020", .day = "day06" },
        .{ .year = "2020", .day = "day05" },
        .{ .year = "2020", .day = "day04" },
        .{ .year = "2020", .day = "day03" },
        .{ .year = "2020", .day = "day02" },
        .{ .year = "2020", .day = "day01" },
        .{ .year = "2020", .day = "all" },

        .{ .year = "2019", .day = "day25" },
        .{ .year = "2019", .day = "day24" },
        .{ .year = "2019", .day = "day23" },
        .{ .year = "2019", .day = "day22" },
        .{ .year = "2019", .day = "day21" },
        .{ .year = "2019", .day = "day20" },
        .{ .year = "2019", .day = "day19" },
        .{ .year = "2019", .day = "day18" },
        .{ .year = "2019", .day = "day17" },
        .{ .year = "2019", .day = "day16" },
        .{ .year = "2019", .day = "day15" },
        .{ .year = "2019", .day = "day14" },
        .{ .year = "2019", .day = "day13" },
        .{ .year = "2019", .day = "day12" },
        .{ .year = "2019", .day = "day11" },
        .{ .year = "2019", .day = "day10" },
        .{ .year = "2019", .day = "day09" },
        .{ .year = "2019", .day = "day08" },
        .{ .year = "2019", .day = "day07" },
        .{ .year = "2019", .day = "day06" },
        .{ .year = "2019", .day = "day05" },
        .{ .year = "2019", .day = "day04" },
        .{ .year = "2019", .day = "day03" },
        .{ .year = "2019", .day = "day02" },
        .{ .year = "2019", .day = "day01" },
        .{ .year = "2019", .day = "all" },

        .{ .year = "2018", .day = "day25" },
        .{ .year = "2018", .day = "day24" },
        .{ .year = "2018", .day = "day23" },
        .{ .year = "2018", .day = "day22" },
        .{ .year = "2018", .day = "day21" },
        .{ .year = "2018", .day = "day20" },
        .{ .year = "2018", .day = "day19" },
        .{ .year = "2018", .day = "day18" },
        .{ .year = "2018", .day = "day17" },
        .{ .year = "2018", .day = "day16" },
        .{ .year = "2018", .day = "day15" },
        .{ .year = "2018", .day = "day14" },
        .{ .year = "2018", .day = "day13" },
        .{ .year = "2018", .day = "day12" },
        .{ .year = "2018", .day = "day11" },
        .{ .year = "2018", .day = "day10" },
        .{ .year = "2018", .day = "day09" },
        .{ .year = "2018", .day = "day08" },
        .{ .year = "2018", .day = "day07" },
        .{ .year = "2018", .day = "day06" },
        .{ .year = "2018", .day = "day05" },
        .{ .year = "2018", .day = "day04" },
        .{ .year = "2018", .day = "day03" },
        .{ .year = "2018", .day = "day02" },
        .{ .year = "2018", .day = "day01" },
        .{ .year = "2018", .day = "all" },

        .{ .year = "2017", .day = "day25" },
        .{ .year = "2017", .day = "day24" },
        .{ .year = "2017", .day = "day23" },
        .{ .year = "2017", .day = "day22" },
        .{ .year = "2017", .day = "day21" },
        .{ .year = "2017", .day = "day20" },
        .{ .year = "2017", .day = "day19" },
        .{ .year = "2017", .day = "day18" },
        .{ .year = "2017", .day = "day17" },
        .{ .year = "2017", .day = "day16" },
        .{ .year = "2017", .day = "day15" },
        .{ .year = "2017", .day = "day14" },
        .{ .year = "2017", .day = "day13" },
        .{ .year = "2017", .day = "day12" },
        .{ .year = "2017", .day = "day11" },
        .{ .year = "2017", .day = "day10" },
        .{ .year = "2017", .day = "day09" },
        .{ .year = "2017", .day = "day08" },
        .{ .year = "2017", .day = "day07" },
        .{ .year = "2017", .day = "day06" },
        .{ .year = "2017", .day = "day05" },
        .{ .year = "2017", .day = "day04" },
        .{ .year = "2017", .day = "day03" },
        .{ .year = "2017", .day = "day02" },
        .{ .year = "2017", .day = "day01" },
        .{ .year = "2017", .day = "all" },

        .{ .year = "2016", .day = "day25" },
        .{ .year = "2016", .day = "day24" },
        .{ .year = "2016", .day = "day23" },
        .{ .year = "2016", .day = "day22" },
        .{ .year = "2016", .day = "day21" },
        .{ .year = "2016", .day = "day20" },
        .{ .year = "2016", .day = "day19" },
        .{ .year = "2016", .day = "day18" },
        .{ .year = "2016", .day = "day17" },
        .{ .year = "2016", .day = "day16" },
        .{ .year = "2016", .day = "day15" },
        .{ .year = "2016", .day = "day14" },
        .{ .year = "2016", .day = "day13" },
        .{ .year = "2016", .day = "day12" },
        .{ .year = "2016", .day = "day11" },
        .{ .year = "2016", .day = "day10" },
        .{ .year = "2016", .day = "day09" },
        .{ .year = "2016", .day = "day08" },
        .{ .year = "2016", .day = "day07" },
        .{ .year = "2016", .day = "day06" },
        .{ .year = "2016", .day = "day05" },
        .{ .year = "2016", .day = "day04" },
        .{ .year = "2016", .day = "day03" },
        .{ .year = "2016", .day = "day02" },
        .{ .year = "2016", .day = "day01" },
        .{ .year = "2016", .day = "all" },

        .{ .year = "2015", .day = "day25" },
        .{ .year = "2015", .day = "day24" },
        .{ .year = "2015", .day = "day23" },
        .{ .year = "2015", .day = "day22" },
        .{ .year = "2015", .day = "day21" },
        .{ .year = "2015", .day = "day20" },
        .{ .year = "2015", .day = "day19" },
        .{ .year = "2015", .day = "day18" },
        .{ .year = "2015", .day = "day17" },
        .{ .year = "2015", .day = "day16" },
        .{ .year = "2015", .day = "day15" },
        .{ .year = "2015", .day = "day14" },
        .{ .year = "2015", .day = "day13" },
        .{ .year = "2015", .day = "day12" },
        .{ .year = "2015", .day = "day11" },
        .{ .year = "2015", .day = "day10" },
        .{ .year = "2015", .day = "day09" },
        .{ .year = "2015", .day = "day08" },
        .{ .year = "2015", .day = "day07" },
        .{ .year = "2015", .day = "day06" },
        .{ .year = "2015", .day = "day05" },
        .{ .year = "2015", .day = "day04" },
        .{ .year = "2015", .day = "day03" },
        .{ .year = "2015", .day = "day02" },
        .{ .year = "2015", .day = "day01" },
        .{ .year = "2015", .day = "all" },
    };
    const years = [_][]const u8{ "2015", "2016", "2017", "2018", "2019", "2020", "2021", "2022", "2023" };

    const run_step = b.step("run", "Run all the days");
    var runyear_step: [years.len]*std.build.Step = undefined;
    inline for (years, 0..) |year, i| {
        runyear_step[i] = b.step("run" ++ year, "Run days from " ++ year);
    }

    const toolbox = b.createModule(.{ .source_file = .{ .path = "toolbox.zig" } });

    for (problems) |pb| {
        const path = b.fmt("{s}/{s}.zig", .{ pb.year, pb.day });

        const exe = b.addExecutable(.{
            .name = pb.day,
            .root_source_file = .{ .path = path },
            .target = target,
            .optimize = optimize,
        });

        exe.addModule("toolbox", toolbox);

        b.installArtifact(exe);

        const run_cmd = b.addRunArtifact(exe);
        run_step.dependOn(&run_cmd.step);

        for (runyear_step, 0..) |step, i| {
            if (mem.eql(u8, years[i], pb.year))
                step.dependOn(&run_cmd.step);
        }
    }

    const test_step = b.step("test", "Test all days");
    var testyear_step: [years.len]*std.build.Step = undefined;
    inline for (years, 0..) |year, i| {
        testyear_step[i] = b.step("test" ++ year, "Test days from " ++ year);
    }
    {
        for (problems) |pb| {
            if (mem.eql(u8, pb.day, "all")) {
                const path = b.fmt("{s}/all.zig", .{pb.year});
                const test_cmd = b.addTest(.{
                    .root_source_file = .{ .path = path },
                    .target = target,
                    .optimize = optimize,
                });
                test_cmd.addModule("toolbox", toolbox);
                test_step.dependOn(&test_cmd.step);
                for (testyear_step, 0..) |step, i| {
                    if (mem.eql(u8, years[i], pb.year))
                        step.dependOn(&test_cmd.step);
                }
            }
        }
    }
}
