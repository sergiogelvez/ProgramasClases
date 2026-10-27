#include <charconv>
#include <cmath>
#include <cstddef>
#include <iostream>
#include <limits>
#include <new>
#include <random>
#include <string>
#include <system_error>
#include <vector>
#include <omp.h>

using Matriz = std::vector<double>;

void multiplicar_serial(const Matriz& a, const Matriz& b, Matriz& c,
                        int filas_a, int columnas_a, int columnas_b)
{
    for (int i = 0; i < filas_a; ++i) {
        for (int j = 0; j < columnas_b; ++j) {
            double suma = 0.0;
            for (int k = 0; k < columnas_a; ++k) {
                suma += a[static_cast<std::size_t>(i) * columnas_a + k] *
                        b[static_cast<std::size_t>(k) * columnas_b + j];
            }
            c[static_cast<std::size_t>(i) * columnas_b + j] = suma;
        }
    }
}

void multiplicar_openmp(const Matriz& a, const Matriz& b, Matriz& c,
                        int filas_a, int columnas_a, int columnas_b)
{
    #pragma omp parallel for collapse(2) schedule(static)
    for (int i = 0; i < filas_a; ++i) {
        for (int j = 0; j < columnas_b; ++j) {
            double suma = 0.0;
            for (int k = 0; k < columnas_a; ++k) {
                suma += a[static_cast<std::size_t>(i) * columnas_a + k] *
                        b[static_cast<std::size_t>(k) * columnas_b + j];
            }
            c[static_cast<std::size_t>(i) * columnas_b + j] = suma;
        }
    }
}

void imprimir_matriz(const char* nombre, const Matriz& matriz,
                     int filas, int columnas)
{
    std::cout << nombre << ":\n";
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            std::cout << matriz[static_cast<std::size_t>(i) * columnas + j]
                      << '\t';
        }
        std::cout << '\n';
    }
}

int main(int argc, char* argv[])
{
    if (argc != 2) {
        std::cerr << "Uso: " << argv[0] << " N\n";
        return 1;
    }

    const std::string argumento = argv[1];
    int n = 0;
    const auto parseo = std::from_chars(
        argumento.data(), argumento.data() + argumento.size(), n);
    if (parseo.ec != std::errc{} ||
        parseo.ptr != argumento.data() + argumento.size() || n <= 0) {
        std::cerr << "N debe ser un entero positivo.\n";
        return 1;
    }
    const auto dimension = static_cast<std::size_t>(n);
    if (dimension > std::numeric_limits<std::size_t>::max() / dimension) {
        std::cerr << "N es demasiado grande para reservar las matrices.\n";
        return 1;
    }

    const auto cantidad = dimension * dimension;
    Matriz a, b, c_serial, c_openmp;
    if (cantidad > a.max_size()) {
        std::cerr << "N es demasiado grande para reservar las matrices.\n";
        return 1;
    }
    try {
        a.resize(cantidad);
        b.resize(cantidad);
        c_serial.resize(cantidad);
        c_openmp.resize(cantidad);
    } catch (const std::bad_alloc&) {
        std::cerr << "No se pudo reservar memoria para las matrices.\n";
        return 1;
    }

    std::random_device semilla;
    std::mt19937 generador(semilla());
    std::uniform_int_distribution<int> valor_aleatorio(0, 9);
    for (std::size_t i = 0; i < cantidad; ++i) {
        a[i] = valor_aleatorio(generador);
        b[i] = valor_aleatorio(generador);
    }

    std::cout << "Multiplicando matrices aleatorias de " << n << " x " << n
              << ".\n";
    double inicio = omp_get_wtime();
    multiplicar_serial(a, b, c_serial, n, n, n);
    const double tiempo_serial = omp_get_wtime() - inicio;

    inicio = omp_get_wtime();
    multiplicar_openmp(a, b, c_openmp, n, n, n);
    const double tiempo_openmp = omp_get_wtime() - inicio;

    bool resultados_iguales = true;
    for (std::size_t i = 0; i < cantidad; ++i) {
        if (std::abs(c_serial[i] - c_openmp[i]) > 1e-9) {
            resultados_iguales = false;
            break;
        }
    }

    if (n <= 10) {
        imprimir_matriz("A", a, n, n);
        imprimir_matriz("B", b, n, n);
        imprimir_matriz("Resultado", c_openmp, n, n);
    } else {
        std::cout << "Matrices omitidas en pantalla porque N es mayor que 10.\n";
    }
    std::cout << "Resultados iguales: " << (resultados_iguales ? "si" : "no")
              << '\n';
    std::cout << "Tiempo serial:  " << tiempo_serial << " segundos\n";
    std::cout << "Tiempo OpenMP:  " << tiempo_openmp << " segundos ("
              << omp_get_max_threads() << " hilos maximos)\n";

    return resultados_iguales ? 0 : 1;
}
