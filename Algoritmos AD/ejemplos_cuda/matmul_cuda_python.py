# Multiplicación de matrices C = A * B con CUDA Python (cuda.core)
# El kernel se escribe en CUDA C y se compila en tiempo de ejecución (NVRTC).
# CuPy se usa solo para reservar y copiar memoria en la GPU.
# Instalar: pip install cuda-python cupy-cuda12x
import numpy as np
import cupy as cp

try:
    from cuda.core import Device, LaunchConfig, Program, ProgramOptions, launch
except ImportError:  # versiones anteriores de cuda.core
    from cuda.core.experimental import Device, LaunchConfig, Program, ProgramOptions, launch

codigo = r"""
extern "C" __global__
void matmul(const float *A, const float *B, float *C, int N)
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
"""

# 1. Preparar la GPU y compilar el kernel
dev = Device()
dev.set_current()
stream = dev.create_stream()

prog = Program(codigo, code_type="c++", options=ProgramOptions(arch=f"sm_{dev.arch}"))
kernel = prog.compile("cubin").get_kernel("matmul")

# 2. Datos: se crean en la CPU y se copian a la GPU
N = 512
A = np.random.rand(N, N).astype(np.float32)
B = np.random.rand(N, N).astype(np.float32)
dA = cp.asarray(A)
dB = cp.asarray(B)
dC = cp.empty_like(dA)
dev.sync()  # esperar a que terminen las copias

# 3. Lanzar el kernel: bloques de 16x16 hilos
bloque = (16, 16)
malla = ((N + 15) // 16, (N + 15) // 16)
config = LaunchConfig(grid=malla, block=bloque)
launch(stream, config, kernel, dA.data.ptr, dB.data.ptr, dC.data.ptr, np.int32(N))
stream.sync()

# 4. Verificar contra NumPy
C = cp.asnumpy(dC)
print("¿Resultado correcto?", np.allclose(C, A @ B, rtol=1e-3))
