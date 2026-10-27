
#include <omp.h>
#include <errno.h>
#include <limits.h>
#include <stdint.h>
#include <stdio.h>
#include <stdlib.h>
#include <time.h>

static int obtener_cantidad(int filas, int columnas, size_t *cantidad)
{
    if (filas <= 0 || columnas <= 0 ||
        (size_t)filas > SIZE_MAX / (size_t)columnas) {
        return 0;
    }

    *cantidad = (size_t)filas * (size_t)columnas;
    return *cantidad <= SIZE_MAX / sizeof(double);
}

static void multiplicar_serial(const double *a, const double *b, double *c,
                               int filas_a, int columnas_a, int columnas_b)
{
    for (int i = 0; i < filas_a; ++i) {
        for (int j = 0; j < columnas_b; ++j) {
            double suma = 0.0;
            for (int k = 0; k < columnas_a; ++k) {
                suma += a[(size_t)i * columnas_a + k] *
                        b[(size_t)k * columnas_b + j];
            }
            c[(size_t)i * columnas_b + j] = suma;
        }
    }
}

static void multiplicar_openmp(const double *a, const double *b, double *c,
                               int filas_a, int columnas_a, int columnas_b)
{
    #pragma omp parallel for collapse(2) schedule(static)
    for (int i = 0; i < filas_a; ++i) {
        for (int j = 0; j < columnas_b; ++j) {
            double suma = 0.0;
            for (int k = 0; k < columnas_a; ++k) {
                suma += a[(size_t)i * columnas_a + k] *
                        b[(size_t)k * columnas_b + j];
            }
            c[(size_t)i * columnas_b + j] = suma;
        }
    }
}

static void imprimir_matriz(const char *nombre, const double *matriz,
                            int filas, int columnas)
{
    printf("%s:\n", nombre);
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            printf("%8.0f", matriz[(size_t)i * columnas + j]);
        }
        putchar('\n');
    }
}

int main(int argc, char *argv[])
{
    if (argc != 2) {
        fprintf(stderr, "Uso: %s N\n", argv[0]);
        return EXIT_FAILURE;
    }

    errno = 0;
    char *fin;
    long valor_n = strtol(argv[1], &fin, 10);
    if (errno != 0 || fin == argv[1] || *fin != '\0' ||
        valor_n <= 0 || valor_n > INT_MAX) {
        fprintf(stderr, "N debe ser un entero positivo.\n");
        return EXIT_FAILURE;
    }

    const int n = (int)valor_n;
    size_t cantidad;

    if (!obtener_cantidad(n, n, &cantidad)) {
        fprintf(stderr, "N es demasiado grande para reservar las matrices.\n");
        return EXIT_FAILURE;
    }

    double *a = malloc(cantidad * sizeof(*a));
    double *b = malloc(cantidad * sizeof(*b));
    double *c_serial = malloc(cantidad * sizeof(*c_serial));
    double *c_openmp = malloc(cantidad * sizeof(*c_openmp));
    if (a == NULL || b == NULL || c_serial == NULL || c_openmp == NULL) {
        fprintf(stderr, "No se pudo reservar memoria para las matrices.\n");
        free(a);
        free(b);
        free(c_serial);
        free(c_openmp);
        return EXIT_FAILURE;
    }

    srand((unsigned int)time(NULL));
    for (size_t i = 0; i < cantidad; ++i) {
        a[i] = rand() % 10;
        b[i] = rand() % 10;
    }

    printf("Multiplicando matrices aleatorias de %d x %d.\n", n, n);
    double inicio = omp_get_wtime();
    multiplicar_serial(a, b, c_serial, n, n, n);
    double tiempo_serial = (omp_get_wtime() - inicio) * 1000000000;

    multiplicar_openmp(a, b, c_openmp, n, n, n);
    inicio = omp_get_wtime();
    multiplicar_openmp(a, b, c_openmp, n, n, n);
    double tiempo_openmp = (omp_get_wtime() - inicio) * 1000000000;

    int resultados_iguales = 1;
    for (size_t i = 0; i < cantidad; ++i) {
        if (c_serial[i] != c_openmp[i]) {
            resultados_iguales = 0;
            break;
        }
    }

    if (n <= 10) {
        imprimir_matriz("A", a, n, n);
        imprimir_matriz("B", b, n, n);
        imprimir_matriz("Resultado", c_openmp, n, n);
    } else {
        printf("Matrices omitidas en pantalla porque N es mayor que 10.\n");
    }
    printf("Resultados iguales: %s\n", resultados_iguales ? "si" : "no");
    printf("Tiempo serial:  %.6f nanosegundos\n", tiempo_serial);
    printf("Tiempo OpenMP:  %.6f nanosegundos (%d hilos maximos)\n",
           tiempo_openmp, omp_get_max_threads());

    free(a);
    free(b);
    free(c_serial);
    free(c_openmp);
    return resultados_iguales ? EXIT_SUCCESS : EXIT_FAILURE;
}
