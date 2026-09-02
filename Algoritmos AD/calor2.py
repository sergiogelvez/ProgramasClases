#include <iostream>
#include <cmath>

import matplotlib.pyplot as plt
import numpy as np
import math


def uInicial(x) :
    #return math.sqrt(math.sin(x)**2)
    return 0

dt = 0.1
m = 100
nsteps = 100
largo = 200
dx = largo / m
tmax = nsteps * dt
    #std::cout << " El dx es " << dx << " el dt es " << dt << " y el tiempo máximo es " << tmax << " \n";

    
if (dt <= (dx * dx) / 2) :
    U = np.zeros([m, nsteps])

    for i in range(m):
        U[i, 0] = uInicial(i * dx)
    
    # condiciones de frontera

    for j in range(0,nsteps):
        U[0, j] = 200
        U[m - 1, j] = 0

    # bucle principal
    for j in range (nsteps-1):
        for i in range(1,m-1):
            U[i, j + 1] = U[i, j] + (20) * (dt / (dx * dx)) * (U[i + 1, j] - 2 * U[i, j] + U[i - 1, j])
    print(U)
    plt.imshow(U.T, cmap='hot')
    plt.colorbar()
    plt.show()
    

else:
    
    print("Los parámetros de dx y dt no permiten la convergencia.  Fin del programa")
    
