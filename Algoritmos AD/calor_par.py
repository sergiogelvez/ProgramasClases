#include <iostream>
#include <cmath>

import numpy as np
import math
import matplotlib.pyplot as plt    # print(f"posición i={i}, para t={t}")
from matplotlib.animation import ArtistAnimation 
import multiprocessing as multi
import time

def uInicial(x) :
    #return math.sqrt(math.sin(x)**2)
    # retornar un valor en kelvin, pero no quiero ponerme existencial, así que 0 celsius -> 273 K
    return 273

def calcular_T(U, i_inicial, i_final, t, alpha, max_i):
    if i_inicial <= 0 :
        liminf = i_inicial + 1
    else :
        liminf = i_inicial
    if i_final >= max_i :
        limsup = i_final - 1
    else :
        limsup = i_final
    for i in range(liminf, limsup):
        U[t + 1, i] = U[t, i] + alpha * (U[t, i + 1] - 2 * U[t, i] + U[t, i - 1])
    #print("Proceso Nro {}".format(multi.current_process().name), end=' ' )

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

n_procs = 2 # numero de procesos en paralelo

dpart = pasos_x // n_procs



print("Inicio de la simulación :: datos de simulación")
print(f"dx = {dx}")
print(f"dt = {dt}")
print(f"Tiempo máximo de simulación es: {tmax} segundos")
print(f"Número de procesos paralelos: {n_procs}")
print(f"Elementos en X a calcular por proceso: {dpart}")

for p in range(n_procs):
    print(f"Particion número {p}, límites: {p * dpart} a {(p + 1) * dpart}")

if __name__ == '__main__':
    if not (dt <= (dx * dx) / 2) :
        print("Los parámetros de dx y dt no permiten la convergencia.  Fin del programa")
        exit(1)

    arr = multi.Array('d', np.zeros(pasos_t * pasos_x, dtype='float64'), lock=False)
    arr_lock = multi.Lock()
    #U = np.zeros([pasos_t, pasos_x])
    print(f"Malla de simulación de ({pasos_t},{pasos_x})")
    # recordar, el primer indice es el tiempo (fila -> tiempo), y el segundo la x (columna -> espacio)
    # condición inicial de la barra
    U = np.frombuffer(arr, dtype='float64').reshape(pasos_t, pasos_x)
    print(U[0, :])
    U[0, :] = uInicial(U[0, :]) # mapear la función a la primera fila usando cortes
    print(U[0, :])

    # condiciones de frontera
    U[:, 0] = 473
    U[:, pasos_x - 1] = 473

    #recordar que si quiero incluir el 0 y el x = largo, hay que agregar un espacio más
    print( U[:, 0], U[:, pasos_x - 1])
    print( len(U[:, 0]), len(U[:, pasos_x - 1]))


    # vector de posiciones en x para graficar
    x_vec = np.linspace(0, largo, pasos_x)

    plt.plot(x_vec, U[0])

    alpha = k * (dt / (dx * dx))

    temp_ini = time.perf_counter_ns()

    # primero el ciclo del tiempo
    t = 0 # se empieza en 0 porque el método evalúa en tiempo t para escribir respuesta en t + 1
    while t < pasos_t - 1 :
        #print(f"t = { t * dt }")
        # Ahora el ciclo que recorre la longitud de la barra

        # Area a paralelizar
        # ruedita U[t + 1, i] = U[t, i] + k * (dt / (dx * dx)) * (U[t, i + 1] - 2 * U[t, i] + U[t, i - 1])
        # subdividir en ranguitos
        

        procesos_nicholson = []
   
        for p in range(n_procs):
            Proc = multi.Process(target=calcular_T, args=(U, p * dpart, (p+1) * dpart, t, alpha, pasos_x))
            #calcular_T(U=U, i_inicial=p * dpart, i_final= (p+1) * dpart, t = t, alpha= alpha  )
            #print(f"Llamar a calcular desde {p * dpart} hasta {(p+1) * dpart}, para t={t}")
            Proc.start()
            procesos_nicholson.append(Proc)

        # los joins
        for p in procesos_nicholson:
        #    print(p.pid)
            p.join()

        procesos_nicholson.clear()

        print(".", end='')
        # fin de area a paralelizar

        t += 1

    temp_fin = time.perf_counter_ns()
    print(temp_fin - temp_ini)

    print("")
    print("Resultado final de U")    
    print(U[pasos_t - 1, :])
    print(procesos_nicholson)

    

