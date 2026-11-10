# Integración por Montecarlo (método del valor medio) con Numba CUDA
#   I = integral_a^b f(x) dx  ~  (b - a) * promedio de f(x_i),  x_i ~ U(a, b)
# Ejemplo: f(x) = 4 / (1 + x^2) en [0, 1]  ->  I = pi
# Instalar: pip install numba-cuda
import math
import numpy as np
from numba import cuda
from numba.cuda.random import create_xoroshiro128p_states, xoroshiro128p_uniform_float64


@cuda.jit(device=True)
def f(x):
    return 4.0 / (1.0 + x * x)


# Cada hilo toma 'muestras_por_hilo' puntos aleatorios y guarda la suma de f(x)
@cuda.jit
def montecarlo(estados, sumas, a, b, muestras_por_hilo):
    i_hilo = cuda.grid(1)
    suma = 0.0
    for _ in range(muestras_por_hilo):
        x = a + (b - a) * xoroshiro128p_uniform_float64(estados, i_hilo)
        suma += f(x)
    sumas[i_hilo] = suma


a, b = 0.0, 1.0
hilos_por_bloque = 256
bloques = 256
total_hilos = hilos_por_bloque * bloques
muestras_por_hilo = 1000

# Un estado del generador aleatorio por hilo
estados = create_xoroshiro128p_states(total_hilos, seed=1234)
d_sumas = cuda.device_array(total_hilos, dtype=np.float64)

montecarlo[bloques, hilos_por_bloque](estados, d_sumas, a, b, muestras_por_hilo)

# Reducción final en la CPU
sumas = d_sumas.copy_to_host()
n = total_hilos * muestras_por_hilo
integral = (b - a) * sumas.sum() / n
print(f"Muestras: {n}")
print(f"Integral ~ {integral:.8f}   (exacto {math.pi:.8f}, error {abs(integral - math.pi):.2e})")
