// Integración por Montecarlo (método del valor medio) en CUDA C
//   I = integral_a^b f(x) dx  ~  (b - a) * promedio de f(x_i),  x_i ~ U(a, b)
// Ejemplo: f(x) = 4 / (1 + x^2) en [0, 1]  ->  I = pi
// Compilar: nvcc montecarlo.cu -o montecarlo
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <curand_kernel.h>

__device__ double f(double x)
{
    return 4.0 / (1.0 + x * x);
}

// Cada hilo toma 'muestras_por_hilo' puntos aleatorios y guarda la suma de f(x)
__global__ void montecarlo(double *sumas, double a, double b,
                           int muestras_por_hilo, unsigned long long semilla)
{
    int id = blockIdx.x * blockDim.x + threadIdx.x;

    curandState estado;
    curand_init(semilla, id, 0, &estado);   // una secuencia distinta por hilo

    double suma = 0.0;
    for (int i = 0; i < muestras_por_hilo; i++) {
        double x = a + (b - a) * curand_uniform_double(&estado);
        suma += f(x);
    }
    sumas[id] = suma;
}

int main(void)
{
    double a = 0.0, b = 1.0;
    int hilos_por_bloque = 256;
    int bloques = 256;
    int total_hilos = hilos_por_bloque * bloques;
    int muestras_por_hilo = 1000;

    double *d_sumas;
    cudaMalloc(&d_sumas, total_hilos * sizeof(double));

    montecarlo<<<bloques, hilos_por_bloque>>>(d_sumas, a, b, muestras_por_hilo, 1234ULL);

    double *sumas = (double *)malloc(total_hilos * sizeof(double));
    cudaMemcpy(sumas, d_sumas, total_hilos * sizeof(double), cudaMemcpyDeviceToHost);

    // Reducción final en la CPU
    double total = 0.0;
    for (int i = 0; i < total_hilos; i++)
        total += sumas[i];

    double n = (double)total_hilos * muestras_por_hilo;
    double integral = (b - a) * total / n;

    printf("Muestras: %.0f\n", n);
    printf("Integral ~ %.8f   (exacto %.8f, error %.2e)\n",
           integral, M_PI, fabs(integral - M_PI));

    cudaFree(d_sumas);
    free(sumas);
    return 0;
}
