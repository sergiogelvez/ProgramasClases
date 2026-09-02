# código para calcular los elementos de una sucesión de Fibonacci (Leonardo de Pisa)

# import numpy as np

n = int(input("Introduzca el número de elementos a calcular: "))
""" ultimo = np.int16(1)
penultimo = np.int16(1) """
ultimo = 1
penultimo = 1
if n > 2:
    print(f'{penultimo}', end = ' ')
    for i in range(n):
        print(f'{ultimo}', end = ' ')
        ultimo, penultimo = penultimo + ultimo, ultimo
else:
    print(f'{penultimo} {ultimo}')