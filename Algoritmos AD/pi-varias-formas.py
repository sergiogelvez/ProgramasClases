from time import perf_counter
import numpy as np
from numba import jit, njit, prange, threading_layer, set_num_threads


def piLeibniz( n ):
    suma = 0
    for i in range(n):
        suma += (((-1)**i) / (2*i + 1) )
    return suma

@jit(nopython = True)
def numba_piLeibniz( n ):
    suma = 0
    for i in range(n):
        suma += (((-1)**i) / (2*i + 1) )
    return suma

@jit(nopython = True)
def numba_numpy_piLeibniz( n ):
    terminos = np.arange(n)
    suma = np.sum(((-1)**terminos) / (2*terminos + 1) )
    return suma

@njit(parallel = True)
def numba_prange_piLeibniz( n ):
    set_num_threads(4)
    suma = 0
    for i in prange(n):
        suma += (((-1)**i) / (2*i + 1) )
    return suma

n_terminos = 10000000
# se toman tiempos
t_inicio = perf_counter()
# método a evaluar
pi = 4 * piLeibniz(n_terminos)
# tiempo final
t_final = perf_counter()
t_transc = t_final - t_inicio
print("Método directo, solo python, un def.")
pi_exp = pi
pi_teo = np.pi
error = 100 * abs((pi_exp - pi_teo) / pi_teo)
print(f"El valor hallado es {pi}. Se demoró {t_transc}s.  El error fue de {error}%")

# Segundo método:  numpy

# se toman tiempos
t_inicio = perf_counter()
# método a evaluar
terminos = np.arange(n_terminos)
pi = 4 * np.sum(((-1)**terminos) / (2*terminos + 1) )
# tiempo final
t_final = perf_counter()
t_transc = t_final - t_inicio
print("Método numpy, solo python, no def.")
pi_exp = pi
pi_teo = np.pi
error = 100 * abs((pi_exp - pi_teo) / pi_teo)
print(f"El valor hallado es {pi}. Se demoró {t_transc}s.  El error fue de {error}%")

# Tercer método: python numba jit

# se toman tiempos
t_inicio = perf_counter()
# método a evaluar
pi = 4 * numba_piLeibniz(n_terminos)
# tiempo final
t_final = perf_counter()
t_transc = t_final - t_inicio
print("Método numba, jit nopython, un def.")
pi_exp = pi
pi_teo = np.pi
error = 100 * abs((pi_exp - pi_teo) / pi_teo)
print(f"El valor hallado es {pi}. Se demoró {t_transc}s.  El error fue de {error}%")

# Tercer método: python numba jit agregado

# se toman tiempos

t_inicio = perf_counter()
# método a evaluar
pi = 4 * numba_piLeibniz(n_terminos)
# tiempo final
t_final = perf_counter()
t_transc = t_final - t_inicio
print("Método numba, jit nopython, un def. Precompilado")
pi_exp = pi
pi_teo = np.pi
error = 100 * abs((pi_exp - pi_teo) / pi_teo)
print(f"El valor hallado es {pi}. Se demoró {t_transc}s.  El error fue de {error}%")

# Cuarto método: python numpy numba jit 

# se toman tiempos
t_inicio = perf_counter()
# método a evaluar
pi = 4 * numba_numpy_piLeibniz(n_terminos)
# tiempo final
t_final = perf_counter()
t_transc = t_final - t_inicio
print("Método numba y numpy, jit nopython, un def.")
pi_exp = pi
pi_teo = np.pi
error = 100 * abs((pi_exp - pi_teo) / pi_teo)
print(f"El valor hallado es {pi}. Se demoró {t_transc}s.  El error fue de {error}%")

# Quinto método: python numba njit prange

# se toman tiempos
t_inicio = perf_counter()
# método a evaluar
pi = 4 * numba_prange_piLeibniz(n_terminos)
# tiempo final
t_final = perf_counter()
t_transc = t_final - t_inicio
print("Método numba prange, jit nopython, un def.")
pi_exp = pi
pi_teo = np.pi
error = 100 * abs((pi_exp - pi_teo) / pi_teo)
print(f"El valor hallado es {pi}. Se demoró {t_transc}s.  El error fue de {error}%")
print("Threading layer chosen: %s" % threading_layer())

