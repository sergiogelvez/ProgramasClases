import random as rnd
import numpy as np

val_p = np.arange(1,11,1)
val_q = np.arange(1,11,1)

pj = np.array([0.11, 0.12, 0.09, 0.08, 0.12, 0.10, 0.09, 0.09, 0.10, 0.10])

cociente = pj / (1/10)

print("Valor de pj: ", end='')
print(pj)

print("Valor de pj/qj: ", end='')
print(cociente)

c=np.max(cociente)
print(c)

n = 10 # numero de aleatorios generados

print("Generar " + str(n) + " números:")

for i in range(n):
    aceptacion = False
    while (aceptacion == False):
        y = int(rnd.random()*10) + 1
        U = rnd.random()
        pos = np.where(val_p == y)
        if U <= (pj[pos])/(c*(1/10)):
            x = y
            aceptacion = True
    print(x)
