#include <concepts>
#include <iostream>
#include <ranges>
#include <vector>

// Restricción con Concepts: solo acepta tipos enteros
template <std::integral IntType>
[[nodiscard]] constexpr auto generate_pascal(IntType num_rows) 
    -> std::vector<std::vector<IntType>> 
{
    if (num_rows <= 0) return {};

    std::vector<std::vector<IntType>> triangle;
    triangle.reserve(static_cast<std::size_t>(num_rows));

    for (IntType i = 0; i < num_rows; ++i) {
        std::size_t row_size = static_cast<std::size_t>(i + 1);
        auto& current_row = triangle.emplace_back(row_size, IntType{1});

        // Iteración sobre los elementos intermedios mediante vistas
        for (std::size_t j : std::views::iota(std::size_t{1}, row_size - 1)) {
            const auto& prev_row = triangle[static_cast<std::size_t>(i - 1)];
            current_row[j] = prev_row[j - 1] + prev_row[j];
        }
    }

    return triangle;
}

int main() {
    const auto triangle = generate_pascal(5);

    for (const auto& row : triangle) {
        for (const auto val : row) {
            std::cout << val << ' ';
        }
        std::cout << '\n';
    }

    return 0;
}
