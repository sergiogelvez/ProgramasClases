import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import scipy as sp
import datetime
import math as m


def Llegada(t):
    lmda = 5
    valor = -m.log(rnd.random())/lmda
    return (t + valor)
    #return (t + rnd.expovariate(lmda))

def Atencion(t):
    lmda = 0.2
    return (t + rnd.expovariate(lmda))


t = 0
tSalida = np.inf
nLlegadas = 0
nSalidas = 0

#tMax = 60 * 60 * 4
tMax =  10
tLlegada = Llegada(0.0) # primera llegada.
n = 0

tMaxReal = 0

historicoLlegadas = []
historicoSalidas = []
print("Tiempo de salida: {}".format(tSalida))
historicoLlegadas.append(tLlegada)
continuar = True

while continuar :    
    print("Llegada de persona número {} - tiempo : {} en minutos".format(nLlegadas, t))
    print("Personas en la cola: {}".format(n))
    if (tLlegada < tSalida and tLlegada < tMax):
        print("Caso 1")
        t = tLlegada
        nLlegadas += 1
        n+=1
        tLlegada = Llegada(t)
        if n == 1: 
            tSalida = Atencion(t)
        historicoLlegadas.append(t)
        # acá código del caso en que hay esperando y no se sabe la salida
    elif (tSalida < tLlegada and tSalida < tMax):
        # aca el código para cuando la salida es anterior a la próxima llegada.
        t = tSalida
        n -= 1
        nSalidas += 1
        if n == 0:
            tSalida = np.inf
        else:
            tSalida = Atencion(t)
        historicoSalidas.append(t)
        print("Caso 2")
    elif min(tLlegada, tSalida) > tMax and n > 0 :
        # caso tres, fin del tiempo, gente en la cola
        t = tSalida
        n -= 1
        nSalidas += 1
        if n > 0:
            tSalida = Atencion(t)
        historicoSalidas.append(t)
        print("Caso 3")
        
    elif min(tLlegada, tSalida) > tMax and n == 0 :
        # caso cuatro, fin del tiempo, ya no hay gente en la cola
        tMaxReal = max( t - tMax, 0 )
        print("Caso 4")
        continuar = False

print("Salí del bucle sin fin")
print("Los tiempos de llegada fueron: {}".format(historicoLlegadas))
print("Los tiempos de salida fueron: {}".format(historicoSalidas))
print("El tiempo de atención por encima de los {} minutos iniciales fue {} minutos".format(tMax, tMaxReal))
print("Número de llegadas: {}".format(nLlegadas))
print("Número de salidas: {}".format(nSalidas))

