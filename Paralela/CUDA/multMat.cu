#include <math.h>
#include <stdlib.h>
#include <string.h>
#include <stdio.h>
#include <unistd.h>
#include <cuda_profiler_api.h>

typedef struct {
	int columnas;
	int filas;
	float* elementos;
} Matrix;

__global__ void matrixMult(Matrix A, Matrix B, Matrix C, int n, int m, int l) {
    // Each thread computes one element of C
    // by accumulating results into Cvalue
    float valorR = 0;
    int fila = blockIdx.y * blockDim.y + threadIdx.y;
    int columna = blockIdx.x * blockDim.x + threadIdx.x;
    for (int e = 0; e < m; ++e)
        valorR += A.elementos[n*fila + e] * B.elementos[e*m + columna];
    C.elementos[fila * l + columna] = valorR;
}

int main(int argc, char* argv[]) {
    // definiciones de argumentos 
    int option, N, M, L, debug = 0, soloKernel = 0, memoriaUnificada = 1;
    while ((option = getopt(argc, argv, "d:n:m:l:?:k:u:")) != -1) {
        switch (option) {
            case 'n':
            // Número total de filas de la primera matriz
            N = atoi(optarg);
            // printf("%s", optarg);
            break;
            case 'm':
            // Número de columnas de la primera matriz y de filas de la segunda
            M = atoi(optarg);
            break;
            case 'l':
            // Número de columnas de la segunda matriz
            L = atoi(optarg);
            break;
            case '?':
            // Mensaje de ayuda
            printf("-n <numero de filas matriz 1>, -m <numero de columnas matriz 1 / numero de filas matriz 2>, -l <numero de columnas matriz 2>, -? este mensaje, -sk perfilado solo kernel (diferente a 0), -d modo depuración (diferente a 0)\n");
            break;
            case 'k':
            // Perfilado solo kernel
            soloKernel = atoi(optarg);
            // strcpy(a_path, optarg);
            break;
            case 'd':
            // modo depuración
            debug = atoi(optarg);
            // strcpy(a_path, optarg);
            break;
            case 'u':
            // uso de memoria unificada
            memoriaUnificada = atoi(optarg);
            // strcpy(a_path, optarg);
            break;
        }
    }

    Matrix matriz1, matriz2, d_matriz1, d_matriz2;
    float elemento;
    Matrix matrizR, d_matrizR;
    size_t tamMatriz1 = sizeof(float)*N*M;
    size_t tamMatriz2 = sizeof(float)*M*L;
    size_t tamMatrizR = sizeof(float)*N*L;

    matriz1.filas = N;
    matriz1.columnas = M;
    matriz2.filas = M;
    matriz2.columnas = L;
    matrizR.filas = N;
    matrizR.columnas = L;

    // alistamiento de memoria para las matrices, modo normal, modo memoria
    // unificada
    if (memoriaUnificada == 0) {
        matriz1.elementos = (float *)malloc(tamMatriz1);
        matriz2.elementos = (float *)malloc(tamMatriz2);
        matrizR.elementos = (float *)malloc(tamMatrizR);
        cudaMalloc(&d_matriz1.elementos, tamMatriz1);
        cudaMalloc(&d_matriz2.elementos, tamMatriz2);
        cudaMalloc(&d_matrizR.elementos, tamMatrizR);
    } else {
        cudaMallocManaged(&d_matriz1.elementos, tamMatriz1);
        cudaMallocManaged(&d_matriz2.elementos, tamMatriz2);
        cudaMallocManaged(&d_matrizR.elementos, tamMatrizR);
    } 

    // generación de matriz aleatoria, con valores enteros
    int i, j;

    // matriz 1
    for (i=0; i< N ; ++i) {
		for (j=0; j < M; ++j) {
			elemento = rand()%10*1.0;
			if (memoriaUnificada == 0) { 
                matriz1.elementos[M*i+j]=elemento; 
            } else {
                d_matriz1.elementos[M*i+j]=elemento;
            }
		}
    }
    // generación de matriz aleatoria, con valores enteros
    // matriz 1
    for (i=0; i< M; ++i) {
		for (j=0; j < L; ++j) {
			elemento = rand()%10*1.0;
			if (memoriaUnificada == 0) {
                matriz2.elementos[L*i+j]=elemento;
            } else {
                d_matriz2.elementos[L*i+j]=elemento;
            }
		}
    }
    
    if (debug == 1) {
        // imprimir matrices
        printf("#### Primera matriz:\n\n");
        for (i=0; i< N ; ++i) {
            printf("(");
            for (j=0; j < M; ++j) {
                if (memoriaUnificada == 0) { 
                    printf("%3.2f  ",matriz1.elementos[M*i+j]);
                } else {
                    printf("%3.2f  ",d_matriz1.elementos[M*i+j]);
                }
            }
            printf(")\n");
        }
        printf("\n");
        printf("#### Segunda matriz:\n\n");
        for (i=0; i< M ; ++i) {
            printf("(");
            for (j=0; j < L; ++j) {
                if (memoriaUnificada == 0) { 
                    printf("%3.2f  ",matriz2.elementos[M*i+j]);
                } else {
                    printf("%3.2f  ",d_matriz2.elementos[M*i+j]);
                }
            }
            printf(")\n");
        }


    }

    // Multiplicación de las matrices mediante CPU
    int k;

    for (i=0 ; i<N; ++i) {
        for (j=0; j<L; ++j) {
            if (memoriaUnificada == 0) { 
                matrizR.elementos[L*i+j] = 0;
            } else {
                d_matrizR.elementos[L*i+j] = 0;
            }
            for (k=0; k<M; ++k) {
                if (memoriaUnificada == 0) { 
                    // printf("Calculando i=%d, j=%d\n",i,j);
                    matrizR.elementos[L*i+j] = matrizR.elementos[L*i+j] + matriz1.elementos[M*i+k] * matriz2.elementos[M*k+j];
                    // printf("valor %3.2f * %3.2f\n", matriz1[M*i+k], matriz2[L*k+j]);
                } else {
                    d_matrizR.elementos[L*i+j] = d_matrizR.elementos[L*i+j] + d_matriz1.elementos[M*i+k] * d_matriz2.elementos[M*k+j];
                }
            }
            // printf("Valor i=%d, j=%d : %3.2f\n",i,j,matrizR[L*i+j]);
        }
    }

    // Imprimir resultado CPU
    if (debug == 1) {
        // imprimir matrices
        printf("#### Resultado CPU:\n\n");
        for (i=0; i< N ; ++i) {
            printf("(");
            for (j=0; j < L; ++j) {
                if (memoriaUnificada == 0) { 
                    printf("%3.2f  ",matrizR.elementos[L*i+j]);
                } else {
                    printf("%3.2f  ",d_matrizR.elementos[L*i+j]);
                }
            }
            printf(")\n");
        }
    }



    if (memoriaUnificada == 0) {
        cudaMemcpy(d_matriz1.elementos, matriz1.elementos, tamMatriz1, cudaMemcpyHostToDevice);
        cudaMemcpy(d_matriz2.elementos, matriz2.elementos, tamMatriz2, cudaMemcpyHostToDevice);
    }

    // lanzamiento del kernel

    dim3 dimBlock(16, 16);
    dim3 dimGrid(L / dimBlock.x, N / dimBlock.y);

    matrixMult<<<dimGrid, dimBlock>>>(d_matriz1, d_matriz2, d_matrizR, N, M, L);

    cudaDeviceSynchronize();

    if (memoriaUnificada == 0) {
        cudaMemcpy(matrizR.elementos, d_matrizR.elementos, tamMatrizR, cudaMemcpyDeviceToHost);
    }

    // resultados kernel GPU
    if (debug == 1) {
        // imprimir matrices
        printf("#### Resultado GPU:\n\n");
        for (i=0; i< N ; ++i) {
            printf("(");
            for (j=0; j < L; ++j) {
                if (memoriaUnificada == 0) { 
                    printf("%3.2f  ",matrizR.elementos[L*i+j]);
                } else {
                    printf("%3.2f  ",d_matrizR.elementos[L*i+j]);
                }
            }
            printf(")\n");
        }
    }


}

