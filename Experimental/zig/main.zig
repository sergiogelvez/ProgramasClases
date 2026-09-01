const std = @import("std");

fn generatePascal(comptime T: type, allocator: std.mem.Allocator, num_rows: usize) ![][]T {
    if (num_rows == 0) return &[_][]T{};

    var triangle = try allocator.alloc([]T, num_rows);
    errdefer allocator.free(triangle);

    for (0..num_rows) |i| {
        const row_size = i + 1;
        var row = try allocator.alloc(T, row_size);
        errdefer allocator.free(row);

        row[0] = 1;
        row[row_size - 1] = 1;

        for (1..i) |j| {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
        }

        triangle[i] = row;
    }

    return triangle;
}

pub fn main() !void {
    var gpa = std.heap.GeneralPurposeAllocator(.{}){};
    defer _ = gpa.deinit();
    const allocator = gpa.allocator();

    const num_rows: usize = 5;
    const triangle = try generatePascal(i32, allocator, num_rows);
    defer {
        for (triangle) |row| allocator.free(row);
        allocator.free(triangle);
    }

    const stdout = std.io.getStdOut().writer();
    for (triangle) |row| {
        for (row) |val| {
            try stdout.print("{d} ", .{val});
        }
        try stdout.print("\n", .{});
    }
}
