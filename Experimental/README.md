# Triángulo de Pascal - Comparativa Multilenguaje

Este paquete incluye la implementación del algoritmo del Triángulo de Pascal en 7 lenguajes de programación:

1. **C (C99):** Manejo manual de memoria (`malloc`/`free`) y punteros.
2. **C++20:** Uso de `std::vector` (RAII), `std::ranges::views::iota` y Concepts (`std::integral`).
3. **Swift:** Semántica de valor, genéricos con protocolo `BinaryInteger`.
4. **Rust:** Propiedad (*ownership*), genéricos restringidos por *traits* y `Vec`.
5. **Go:** *Slices* nativos, genéricos con `constraints.Integer`.
6. **Odin:** Enfoque orientado a datos, memoria explícita con arreglos dinámicos (`[dynamic]T`).
7. **Zig:** Manejo explícito de asignadores (`std.mem.Allocator`) y errores en tiempo de compilación (`comptime`).

### Comandos de Compilación / Ejecución:

- **C:** `gcc -std=c99 -Wall -Wextra main.c -o pascal_c && ./pascal_c`
- **C++:** `g++ -std=c++20 -Wall -Wextra main.cpp -o pascal_cpp && ./pascal_cpp`
- **Swift:** `swift main.swift`
- **Rust:** `rustc main.rs -o pascal_rs && ./pascal_rs`
- **Go:** `go run main.go`
- **Odin:** `odin run main.odin -file`
- **Zig:** `zig run main.zig`
