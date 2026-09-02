import numpy as np
import numba
from numba import cuda
import math
from time import perf_counter

print(np.__version__)
print(numba.__version__)

cuda.detect()


'''
__global__ void MatMulKernel(Matrix A, Matrix B, Matrix C) {
	// each thread compute one element of C
	// by acumulating results into Cvalue
	double Cvalue = 0;
	int row = blockIdx.y * blockDim.y + threadIdx.y;
	int col = blockIdx.x * blockDim.x + threadIdx.x;
	for (int e = 0; e < A.width; ++e) {
		Cvalue = Cvalue + A.elements[row *A.width + e] * B.elements[e * B.width + col];
	}
	C.elements[row * C.width + col] = Cvalue;
}
'''

@cuda.jit
def matmul( A, B, C, n, m, p):
    row = cuda.threadIdx.y + cuda.blockDim.y * cuda.blockIdx.y
    col = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    if row < n and col < p:
        cvalue = 0
        for e in range(m):
            cvalue = cvalue + A[row * n + e] * B[e * m + col]
        C[row * n + col] = cvalue

# Example 1.2: Add arrays
""" @cuda.jit
def add_array(a, b, c):
    i = cuda.threadIdx.x + cuda.blockDim.x * cuda.blockIdx.x
    if i < a.size:
        c[i] = a[i] + b[i] """

n = 2048
m = 2048
p = 2048


a = np.random.randint(0, 10, n * m)
b = np.random.randint(0, 10, m * p)
#a = np.arange(N, dtype=np.float32)
#b = np.arange(N, dtype=np.float32)

dev_a = cuda.to_device(a)
dev_b = cuda.to_device(b)

dev_c = cuda.device_array(n * p)

a = np.resize(a, (n, m))
b = np.resize(b, (m, p))

t_inicio = perf_counter()
c = a @ b
t_final = perf_counter()
print(f"Tiempo en CPU, numpy: {t_final -t_inicio } seg")

print(c)
cuda 
threadsperblock = (16, 16)
blockspergrid_x = math.ceil(n / threadsperblock[0])
blockspergrid_y = math.ceil(p / threadsperblock[1])
blockspergrid = (blockspergrid_x, blockspergrid_y)
# Note that
#     blocks_per_grid == ceil(N / threads_per_block)
# ensures that blocks_per_grid * threads_per_block >= N

t_inicio = perf_counter()
matmul[blockspergrid,  threadsperblock](dev_a, dev_b, dev_c, n, m, p)
t_final = perf_counter()
print(f"Tiempo en GPU: {t_final -t_inicio } seg")

t_inicio = perf_counter()
matmul[blockspergrid,  threadsperblock]( dev_b, dev_a, dev_c, n, m, p)
t_final = perf_counter()
print(f"Tiempo en GPU, segunda vuelta: {t_final -t_inicio } seg")


nc = dev_c.copy_to_host()



nc = np.resize(nc, (n, p))

print(nc)

print(np.allclose(nc, c))

#  True