from cgitb import text
import random as rnd
import math as m
import numpy as np
import statistics as stat

lda = 1 # llegadas por segundo
tllegadas = []
tintrallegadas = []
T = 100.0 # tiempo total de llegada
L = 10000 # llegadas máximas
I = 0 # llegadas
t = 0.0 # tiempo evento actual
while t < T and I <= L:
    x = - ((1/lda)*m.log(rnd.random()))
    t = t + x
    #print("Llegada N° {} - tiempo: {}".format(I+1, t))
    I += 1
    tllegadas.append(t)
    tintrallegadas.append(x)

print(tllegadas)
media = stat.mean(tintrallegadas)
print("El promedio de tiempos de llegada es {}, el inverso es {}".format(media, 1/media))

nllegadas = []
t = 0
TE = int(T)
while( t < TE):
    i = 0
    p = m.exp(-lda)
    F = p
    parada = False
    while not (parada):
        U = rnd.random()
        if (U < F):
            x = i 
            parada = True
        else :
            p = (lda * p)/(i + 1)
            F = F + p
            i += 1
    #print(x)
    nllegadas.append(x)
    t += 1
print(len(nllegadas))
print(nllegadas)
media = stat.mean(nllegadas)
print("El promedio de llegadas en {} periodos de tiempo es: {}".format(T, media))