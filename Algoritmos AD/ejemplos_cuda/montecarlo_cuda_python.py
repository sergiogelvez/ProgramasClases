# Integración por Montecarlo (método del valor medio) con CUDA Python (cuda.core)
#   I = integral_a^b f(x) dx  ~  (b - a) * promedio de f(x_i),  x_i ~ U(a, b)
# Ejemplo: f(x) = 4 / (1 + x^2) en [0, 1]  ->  I = pi
# Para no depender de los encabezados de cuRAND al compilar con NVRTC,
# cada hilo usa un generador xorshift32 muy simple.
# Instalar: pip install cuda-python cupy-cuda12x
import math
import numpy as np
import cupy as cp

try:
    from cuda.core import Device, LaunchConfig, Program, ProgramOptions, launch
except ImportError:  # versiones anteriores de cuda.core
    from cuda.core.experimental import Device, LaunchConfig, Program, ProgramOptions, launch

codigo = r"""
__device__ double f(double x)
{
    return 4.0 / (1.0 + x * x);
}

extern "C" __global__
void montecarlo(double *sumas, double a, double b,
                int muestras_por_hilo, unsigned int semilla)
{
    int id = blockIdx.x * blockDim.x + threadIdx.x;

    unsigned int s = semilla ^ (id * 2654435761u);  // semilla distinta por hilo
    if (s == 0) s = 1;

    double suma = 0.0;
    for (int i = 0; i < muestras_por_hilo; i++) {
        s ^= s << 13;  s ^= s >> 17;  s ^= s << 5;  // xorshift32
        double u = s / 4294967296.0;                // uniforme en [0, 1)
        suma += f(a + (b - a) * u);
    }
    sumas[id] = suma;
}
"""

# 1. Preparar la GPU y compilar el kernel
dev = Device()
dev.set_current()
stream = dev.create_stream()

prog = Program(codigo, code_type="c++", options=ProgramOptions(arch=f"sm_{dev.arch}"))
kernel = prog.compile("cubin").get_kernel("montecarlo")

# 2. Parámetros
a, b = 0.0, 1.0
hilos_por_bloque = 256
bloques = 256
total_hilos = hilos_por_bloque * bloques
muestras_por_hilo = 1000

d_sumas = cp.empty(total_hilos, dtype=cp.float64)
dev.sync()

# 3. Lanzar el kernel
config = LaunchConfig(grid=bloques, block=hilos_por_bloque)
launch(stream, config, kernel, d_sumas.data.ptr,
       np.float64(a), np.float64(b), np.int32(muestras_por_hilo), np.uint32(1234))
stream.sync()

# 4. Reducción final y resultado
n = total_hilos * muestras_por_hilo
integral = (b - a) * float(d_sumas.sum()) / n
print(f"Muestras: {n}")
print(f"Integral ~ {integral:.8f}   (exacto {math.pi:.8f}, error {abs(integral - math.pi):.2e})")
