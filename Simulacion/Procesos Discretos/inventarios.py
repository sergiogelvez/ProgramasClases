import matplotlib.pyplot as plt
import numpy as np
import random as rnd
from regex import W
import scipy as sp
import datetime
import math as m


def Llegada(t):
    lmda = 5
    valor = -m.log(rnd.random())/lmda
    return (t + valor)
    #return (t + rnd.expovariate(lmda))

def Entrega(t):
    lmda = 0.2
    return (t + rnd.expovariate(lmda))

def UnidadesCompra():
    maximoUnidadesPed = 10 # un valor arbitrario para el ejemplo
    unidades = int(maximoUnidadesPed * rnd.random())
    return unidades


Tmax = 100 # dias?
t = 0
n = 100 #unidades iniciales
ped = 0

Imax = 500
Imin = 20

t0 = 0
t1 = np.inf

H = 0.0 # costo de tener inventario
h = 10 # pesos por día en el inventario.
R = 0.0 # ganancia
r = 350 # ganancia por unidad
C = 0.0 # costos de pedido
c = 200 # costo por unidad pedida
c0 = 0.0 # costo por pedido (independiente de las unidades)

L = 3 # dias para que llegue el pedido


while ( t < Tmax):
    if ( t0 < t1 ):
        H = H + (t0 - t) * h * n
        t = t0
        D = UnidadesCompra()
        print("Se hace una venta de {} unidades en el tiempo {}. Quedan {} unidades en el inventario".format(D, t, n))
        w = min(D, n)
        R = R + w * r
        n = n - w
        if (n < Imin and ped == 0):
            ped = Imax - n    
            t1 = t + L
            print("Se hace un pedido de {} unidades, llegara en el tiempo {}".format(ped, t1))
        t0 = Llegada(t)
    elif ( t1 < t0 ):
        H = H + ( t1 - t ) * h * n
        t = t1
        C = C + c * ped
        n = n + ped
        ped = 0
        t1 = np.inf

ganancia = ( R - H - C ) / Tmax
print("La ganancia fue de {} unidades monetarias, en un periodo de {} unidades de tiempo. {} unidades en el inventario".format(ganancia, Tmax, n))
print("Ganancias totales por ventas: {}".format(R))
print("Costos totales por inventario: {}".format(H))
print("Costos totales por pedidos: {}".format(C))

