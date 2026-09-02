import numpy as np
import matplotlib.pyplot as plt
import math as m

def regresion_lineal_manual(x, y):
    n = len(x)
    sx = sum(x)
    sy = sum(y)
    sxy = sum(x*y)
    sxx = sum(x**2)

    b = ((n * sxy) - (sx * sy)) / ( n * (sxx) - (sx**2) )
    a = ( sy*(sxx) - (sxy * sx) ) / ( (n * sxx) - (sx ** 2) )

    print(a, b)

    y2 = a + b * x
    return y2

def regresion_polinomica(x, y):
    model = np.poly1d(np.polyfit(x, y, 2))
    y2 = model(x)
    return y2

x = np.linspace(-10, 10, 100)
print(x)
y = np.random.rand(len(x)) + np.sin(x)
print(y)

valida = False

while not valida:
    entrada = input("Introduzca un número correspondiente a una opción: 1 - Lineal manual, 2 - Cuadrática ")
    match entrada:
        case '1':
            y2 = regresion_lineal_manual(x, y)
            valida = True
        case '2':
            y2 = regresion_polinomica(x, y)
            valida = True
        case other:
            valida = False


print(y2)
plt.plot(x, y, "*g")
plt.plot(x, y2, "-r")
plt.show()