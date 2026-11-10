// Multiplicación de matrices C = A * B en CUDA C (versión ingenua)
// Compilar: nvcc matmul.cu -o matmul
#include <stdio.h>
#include <stdlib.h>

// Cada hilo calcula un elemento C[fila][col]
__global__ void matmul(const float *A, const float *B, float *C, int N)
{
    int fila = blockIdx.y * blockDim.y + threadIdx.y;
    int col  = blockIdx.x * blockDim.x + threadIdx.x;

    if (fila < N && col < N) {
        float suma = 0.0f;
        for (int k = 0; k < N; k++)
            suma += A[fila * N + k] * B[k * N + col];
        C[fila * N + col] = suma;
    }
}

int main(void)
{
    int N = 512;
    size_t bytes = N * N * sizeof(float);

    // Matrices en el host (CPU)
    float *A = (float *)malloc(bytes);
    float *B = (float *)malloc(bytes);
    float *C = (float *)malloc(bytes);
    for (int i = 0; i < N * N; i++) {
        A[i] = 1.0f;
        B[i] = 2.0f;
    }

    // Matrices en el device (GPU)
    float *dA, *dB, *dC;
    cudaMalloc(&dA, bytes);
    cudaMalloc(&dB, bytes);
    cudaMalloc(&dC, bytes);
    cudaMemcpy(dA, A, bytes, cudaMemcpyHostToDevice);
    cudaMemcpy(dB, B, bytes, cudaMemcpyHostToDevice);

    // Bloques de 16x16 hilos; suficientes bloques para cubrir la matriz
    dim3 bloque(16, 16);
    dim3 malla((N + 15) / 16, (N + 15) / 16);
    matmul<<<malla, bloque>>>(dA, dB, dC, N);

    // Traer el resultado (cudaMemcpy espera a que termine el kernel)
    cudaMemcpy(C, dC, bytes, cudaMemcpyDeviceToHost);

    // Como A = 1 y B = 2, todo elemento de C debe valer 2*N
    printf("C[0][0] = %.1f   C[N-1][N-1] = %.1f   (esperado %.1f)\n",
           C[0], C[N * N - 1], 2.0f * N);

    cudaFree(dA); cudaFree(dB); cudaFree(dC);
    free(A); free(B); free(C);
    return 0;
}
