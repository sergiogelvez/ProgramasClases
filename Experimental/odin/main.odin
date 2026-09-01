package main

import "core:fmt"

generate_pascal :: proc($T: typeid, num_rows: int) -> [dynamic][dynamic]T {
    triangle := make([dynamic][dynamic]T, 0, num_rows)
    if num_rows <= 0 do return triangle

    for i in 0..<num_rows {
        row_size := i + 1
        row := make([dynamic]T, row_size)
        
        row[0] = 1
        row[row_size - 1] = 1

        for j in 1..<i {
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        }

        append(&triangle, row)
    }

    return triangle
}

main :: proc() {
    triangle := generate_pascal(int, 5)
    defer {
        for row in triangle do delete(row)
        delete(triangle)
    }

    for row in triangle {
        for val in row {
            fmt.printf("%d ", val)
        }
        fmt.println()
    }
}
