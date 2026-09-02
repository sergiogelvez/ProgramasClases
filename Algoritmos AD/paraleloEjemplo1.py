import multiprocessing
import time
import math as m
import numpy as np   
  
def square(x):
    return (((-1)**x) / (2*x + 1) )
   
if __name__ == '__main__':
    procs = 8
    terms = 1000000
    inicio = time.perf_counter()
    # cálculo de pi básico
    suma = 0.0
    for i in range(terms):
        suma += ((-1)**i) / (2*i + 1) 
    fin = time.perf_counter()
    # calculo del tiempo para un solo proceso
    print(f"Pi es {4*suma}")
    print(f'El tiempo de ejecución para {terms} términos fue {fin - inicio} segundos')
    # acá se cálcula el valor mediante multiprocessing.Pool
    inicio = time.perf_counter()
    pool = multiprocessing.Pool()
    pool = multiprocessing.Pool(processes=procs)
    inputs = [*range(terms)]
    outputs = pool.map(square, inputs)
    #print("Input: {}".format(inputs))
    #print("Output: {}".format(outputs))
    result = 4 * sum(outputs)
    fin = time.perf_counter()
    print(f"Pi es {result}")
    print(f"Pi del sistema es {m.pi}")
    print(f'El tiempo de ejecución para {terms} términos y {procs} procesos fue {fin - inicio} segundos')
    error = (result - m.pi) / m.pi
    print(f"El error es {error*100:.10f}%")
    # calculando con numpy
    """ print("Bonus: numpy")
    inicio = time.perf_counter()
    i = np.arange(terms)
    serie = ((-1)**i) / (2*i + 1) 
    result = 4 * np.sum(serie)
    print(f"Pi es {result}")
    fin = time.perf_counter()
    print(f'El tiempo de ejecución, usando numpy, para {terms} términos fue {fin - inicio} segundos') """