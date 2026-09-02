import multiprocessing as mp
import time
import math as m
import numpy as np   

# class Gato(multiprocessing.Process):
#     def __init__(self, id):
#         super(Gato, self).__init__()
#         self.id = id

#     def term(self, x):
#         return (((-1)**x) / (2*x + 1) )

#     def run(self):
#         time.sleep(1)
#         print("I'm the process with id: {}".format(self.id))


def term(x):
    return (((-1)**x) / (2*x + 1) )

if __name__ == '__main__':
    procs = 8
    terms = 1000000
    inicio = time.perf_counter()
    suma = 0.0
    terminos = []
    for i in range(1000):
        p = mp.Process(target=term, args=(i,))
        p.start()
        terminos.append(p.run())
    fin = time.perf_counter()
    # calculo del tiempo para un solo proceso
    suma = sum(terminos)
    print(f"Pi es {4*suma}")
    print(f'El tiempo de ejecución para {terms} términos fue {fin - inicio} segundos')

