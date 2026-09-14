#include "stdlib.h"
#include "stdio.h"
#include "math.h"
#include "time.h"

// Matrices are stored in row-major order:
// M(row, col) = *(M.elements + row * M.width + col)

typedef struct {
	int width;
	int height;
	float* elements;
} Matrix;

// thread block size
// #define BLOCK_SIZE 16
#define BLOCK_SIZE 4

// Forward declaration of the matrix multiplication kernel
__global__ void MatMulKernel(const Matrix A, const Matrix B, Matrix C);

// Matrix multiplication - host code
// Matrix dimensions are assumed to be multiples of BLOCK_SIZE
void MatMul(const Matrix A, const Matrix B, Matrix C) {
	// load A and B to devic memory
	Matrix d_A;
	d_A.width = A.width;
	d_A.height = A.height;
	size_t size = A.width * A.height * sizeof(float);
	cudaMalloc(&d_A.elements, size);
	cudaMemcpy(d_A.elements, A.elements, size, cudaMemcpyHostToDevice);
	Matrix d_B;
	d_B.width = B.width;
	d_B.height = B.height;
	size = B.width * B.height * sizeof(float);
	cudaMalloc(&d_B.elements, size);
	cudaMemcpy(d_B.elements, B.elements, size, cudaMemcpyHostToDevice);
	// allocate C in device memory 
	Matrix d_C;
	d_C.width = C.width;
	d_C.height = C.height;
	printf("\n\n  dimensiones de C (antes del kernel): %d, %d\n",C.width,C.height);
	size = C.width * C.height * sizeof(float);
	cudaMalloc(&d_C.elements, size);
	// invoke kernel
	dim3 dimBlock(BLOCK_SIZE, BLOCK_SIZE);
	dim3 dimGrid(B.width / dimBlock.x, A.height / dimBlock.y);
	MatMulKernel<<<dimGrid,dimBlock>>>(d_A,d_B,d_C);
	// Read C from device memory
	cudaMemcpy(C.elements, d_C.elements, size, cudaMemcpyDeviceToHost);
	// porqueria
	int i,j;
	printf("\n\n  dimensiones de C: %d, %d\n",C.height,C.width);
	for (i=0; i< C.width ; ++i) {
		for (j=0; j < C.height; ++j) {
			//printf("\n\n%f", C.elements[i*C.width+j]);
		}
	}
	
	
	// free device memory
	cudaFree(d_A.elements);
	cudaFree(d_B.elements);
	cudaFree(d_C.elements);
}

// Matrix multiplication kernel called by MatMul()
__global__ void MatMulKernel(Matrix A, Matrix B, Matrix C) {
	// each thread compute one element of C
	// by acumulating results into Cvalue
	float Cvalue = 0;
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	int col = blockIdx.x * blockDim.x + threadIdx.x;
	for (int e = 0; e < A.width; ++e) {
		Cvalue = Cvalue + A.elements[row *A.width + e] * B.elements[e * B.width + col];
	}
	C.elements[row * C.width + col] = Cvalue;
}



int main( int argc, char** argv) {
	Matrix A, B, C;
	float MAT[8][8];
	float MAT2[8][8];
	float MATA[8][8];
	float MATB[8][8];
	// vamos al ejemplo de la matriz cuadrada, 8x8
	A.width = 8;
	B.width = 8;
	C.width = 8;
	A.height = 8;
	B.height = 8;
	C.height = 8;
	int count = 0;
	int i, j, k;
	float temp;
	printf("\n\n\n\n\n");
	printf("\n************************************\n");
	printf("Prueba de multiplicacion de matrices");
	printf("\n************************************\n");
	for (i=0; i< A.width ; ++i) {
		for (j=0; j < A.height; ++j) {
			temp = rand()%10*1.0;
			MAT[i][j]=temp;
			MATA[i][j]=temp;
		}
	}
	printf("\n\n -- Matriz A --\n");
	for (i=0; i< A.width ; ++i) {
		printf("\n");
		for (j=0; j < A.height; ++j) {
			printf(" %3.2f ",MAT[i][j]);
			count++;
		}
		printf("\n");
	}
	printf("\nContador = %d", count);
	size_t size = A.width*A.height*sizeof(float);
	A.elements = (float*)malloc(size);
	for (i=0; i< A.width ; ++i) {
		for (j=0; j < A.height; ++j) {
			A.elements[i*A.width+j]=MAT[i][j];
		}
	}
	// ahora la B
	count = 0;
	for (i=0; i< B.width ; ++i) {
		for (j=0; j < B.height; ++j) {
			temp = rand()%10*1.0;
			MAT[i][j]=temp;
			MATB[i][j]=temp ;
		}
	}
	printf("\n\n -- Matriz B --\n");
	for (i=0; i< B.width ; ++i) {
		printf("\n");
		for (j=0; j < B.height; ++j) {
			printf(" %3.2f ",MAT[i][j]);
			count++;
		}
		printf("\n");
	}
	printf("\nContador = %d", count);
	size = B.width*B.height*sizeof(float);
	B.elements = (float*)malloc(size);
	for (i=0; i< B.width ; ++i) {
		for (j=0; j < B.height; ++j) {
			B.elements[i*B.width+j]=MAT[i][j];
		}
	}
	// pasar la mat a la funcion MulMat
	C.elements = (float*)malloc(size);
	// aca hay que incluir el codigo que lleva control del tiempo
	clock_t tinicio, t_GPU;
	float tg,tc;
	tinicio=clock();
	//
	MatMul(A,B,C);
	//
	t_GPU=clock();
	tg = ((float)t_GPU-(float)tinicio)/CLOCKS_PER_SEC;
	printf("\n\ntiempo de procesamiento (GPU): %6.3f s\n\n",tg);
	// aca se calculó el tiempo de la GPU
	
	for (i=0; i< C.width ; ++i) {
		for (j=0; j < C.height; ++j) {
			MAT[i][j]=C.elements[i*C.width+j];
		}
	}
	printf("\n -- Matrix resultante (GPU) --\n");
	for (i=0; i< C.width ; ++i) {
		printf("\n");
		for (j=0; j < C.height; ++j) {
			printf(" %3.2f ",MAT[i][j]);
		}
		printf("\n");
	}
	// aca vamos a realizar la multiplicacion de matrices mediante la cpu.
	// se analizaran los resultados.
	tinicio=clock();
	//
	for (i=0; i<8; ++i) {
		for (j=0; j<8; ++j) {
			MAT2[i][j]=0;
			for(k=0;k<8;k++) {
				MAT2[i][j]=MAT2[i][j]+MATA[i][k]*MATB[k][j];
			}
		}
	}
	//
	t_GPU=clock();
	tc = ((float)t_GPU-(float)tinicio)/CLOCKS_PER_SEC;
	printf("\n\ntiempo de procesamiento (CPU): %6.3f s\n\n",tc);
	printf("\n -- Matrix resultante (CPU) --\n");
	for (i=0; i< C.width ; ++i) {
		printf("\n");
		for (j=0; j < C.height; ++j) {
			printf(" %3.2f ",MAT2[i][j]);
		}
		printf("\n");
	}
}
