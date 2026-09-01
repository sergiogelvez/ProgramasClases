fn generate_pascal<T>(num_rows: usize) -> Vec<Vec<T>>
where
    T: Copy + From<u8> + std::ops::Add<Output = T>,
{
    if num_rows == 0 {
        return Vec::new();
    }

    let mut triangle: Vec<Vec<T>> = Vec::with_capacity(num_rows);

    for i in 0..num_rows {
        let mut row = vec![T::from(1); i + 1];
        if i > 1 {
            for j in 1..i {
                row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j];
            }
        }
        triangle.push(row);
    }

    triangle
}

fn main() {
    let triangle: Vec<Vec<i32>> = generate_pascal(5);
    for row in &triangle {
        for val in row {
            print!("{} ", val);
        }
        println!();
    }
}
