#include <iostream>
#include <cmath>

import matplotlib.pyplot as plt
import numpy as np
import math
from matplotlib.animation import ArtistAnimation 
import time 

def uInicial(x) :
    #return math.sqrt(math.sin(x)**2)
    # retornar un valor en kelvin, pero no quiero ponerme existencial, así que 0 celsius -> 273 K
    return 273


# nomenclatura:
# calcular los delta a partir de las características físicas de la simulación
# ojo, t: tiempos, T: temperaturas, x: posición en x en la barra, i con x, j con t

tmax = 60  # segundos
largo = 50000 # metros

pasos_t = 1000
pasos_x = 50000

dt = tmax / pasos_t
dx = largo / pasos_x

k = .466 # constante 

print("Inicio de la simulación :: datos de simulación")
print(f"dx = {dx}")
print(f"dt = {dt}")
print(f"Tiempo máximo de simulación es: {tmax} segundos")

if (dt <= (dx * dx) / 2) :
    U = np.zeros([pasos_t, pasos_x])
    print(f"Malla de simulación de ({pasos_t},{pasos_x})")
    # recordar, el primer indice es el tiempo (fila -> tiempo), y el segundo la x (columna -> espacio)
    # condición inicial de la barra
    #print(U[0, :])
    U[0, :] = uInicial(U[0, :]) # mapear la función a la primera fila usando cortes
    #print(U[0, :])
    
    # condiciones de frontera
    U[:, 0] = 473
    U[:, pasos_x - 1] = 473

    #recordar que si quiero incluir el 0 y el x = largo, hay que agregar un espacio más
    #print( U[:, 0], U[:, pasos_x - 1])
    #print( len(U[:, 0]), len(U[:, pasos_x - 1]))
    
    
    # vector de posiciones en x para graficar
    x_vec = np.linspace(0, largo, pasos_x)

    plt.plot(x_vec, U[0])
    
    temp_ini = time.perf_counter_ns()
    # primero el ciclo del tiempo
    t = 0 # se empieza en 0 porque el método evalúa en tiempo t para escribir respuesta en t + 1
    while t < pasos_t - 1 :
        #print(f"t = { t * dt }")
        # Ahora el ciclo que recorre la longitud de la barra
        for i in range(1, pasos_x - 1):
            # print(f"posición i={i}, para t={t}")
            
            U[t + 1, i] = U[t, i] + k * (dt / (dx * dx)) * (U[t, i + 1] - 2 * U[t, i] + U[t, i - 1])
        print(".", end='')
        #fig.add_axes(ax)
        """ plt.xlim(0, largo)
        plt.ylim(273, 500)
        plt.plot(x_vec, U[t, :], 'b')
        plt.ylabel("Temperatura (K)")
        plt.xlabel("Distancia sobre la barra (m)")
        plt.pause(.001)
        
        #ax.pause(.001)
        plt.cla() """
        
        t += 1

    temp_fin = time.perf_counter_ns()
    print(temp_fin - temp_ini)

    """ plt.xlim(0, largo)
    plt.ylim(273, 500)    
    plt.plot(x_vec, U[pasos_t - 1, :], 'b')
    plt.ylabel("Temperatura (K)")
    plt.xlabel("Distancia sobre la barra (m)")
    plt.show() """
    
    print(U)
    print(U[pasos_t - 1, :])
    plt.imshow(U.T, cmap='hot')
    plt.colorbar()
    plt.show()

    

else:
    
    print("Los parámetros de dx y dt no permiten la convergencia.  Fin del programa")
    
