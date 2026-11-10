# Multiplicación de matrices C = A * B con Numba CUDA
# Instalar: pip install numba-cuda
import math
import numpy as np
from numba import cuda


# Cada hilo calcula un elemento C[fila, col]
@cuda.jit
def matmul(A, B, C):
    col, fila = cuda.grid(2)  # cuda.grid(2) devuelve (x, y)
    if fila < C.shape[0] and col < C.shape[1]:
        suma = 0.0
        for k in range(A.shape[1]):
            suma += A[fila, k] * B[k, col]
        C[fila, col] = suma


N = 512
A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)

# Copiar a la GPU
dA = cuda.to_device(A)
dB = cuda.to_device(B)
dC = cuda.device_array((N, N), dtype=np.float32)

# Bloques de 16x16 hilos
bloque = (16, 16)
malla = (math.ceil(N / 16), math.ceil(N / 16))
matmul[malla, bloque](dA, dB, dC)

# Traer el resultado y verificar contra NumPy
C = dC.copy_to_host()
print("¿Resultado correcto?", np.allclose(C, A @ B, rtol=1e-3))
