func generatePascal<T: BinaryInteger>(numRows: T) -> [[T]] {
    guard numRows > 0 else { return [] }
    
    var triangle: [[T]] = []
    triangle.reserveCapacity(Int(numRows))
    
    for i in 0..<Int(numRows) {
        var row = Array(repeating: T(1), count: i + 1)
        if i > 1 {
            let prevRow = triangle[i - 1]
            for j in 1..<i {
                row[j] = prevRow[j - 1] + prevRow[j]
            }
        }
        triangle.append(row)
    }
    
    return triangle
}

let triangle = generatePascal(numRows: 5)
for row in triangle {
    print(row.map { String($0) }.joined(separator: " "))
}
