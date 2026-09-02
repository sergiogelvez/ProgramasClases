import math as m
import random as rnd
import numpy as np

# la base del método es asumir X y Y como funciones normales estandar, y R y Th (theta mayuscula) las 
# coordenadas polares del vector (X, Y) 

# se cambian a polares y se multiplican

# Del cambio con jacobiano salen una expresion que se puede reinterpretar como una multiplicación de 
# una uniforme y una exponencial

N = 100

# lo primero, generar los dos U entre 0,1

Z1 = []
Z2 = []

for i in range(N):
    U1 = rnd.random()
    U2 = rnd.random()
    # calcular R y Theta
    R = m.sqrt(-2*m.log(U1))
    Th = 2 * m.pi * U2
    # Calcular X y Y
    X = R * m.cos(Th)
    Y = R * m.sin(Th)
    Z1.append(X)
    Z2.append(Y)

print(str(N) + " valores de la primera normal estandar")
print(Z1)
# impresión de la primera normal estandar y luego de la segunda
input("Presione enter para seguir")
print(str(N) + " valores de la segunda normal estandar")
print(Z2)

print("Generadas por el método polar")
input("Presione enter para seguir")

Z3 = []
Z4 = []

count = 0

for i in range(N):
    aceptado = False
    while aceptado == False:
        V1, V2 = 2*rnd.random() - 1, 2*rnd.random() - 1
        S = V1**2 + V2**2
        #print("({},{})".format(V1, V2) + " generado")
        count += 1
        if ( S < 1):
            #print("Aceptada, valores generados: ", end='')
            X = m.sqrt((-2*m.log(S))/S)*V1
            Y = m.sqrt((-2*m.log(S))/S)*V2
            Z3.append(X)
            Z4.append(Y)
            print(str(X) + "," + str(Y))
            aceptado = True

print(str(N) + " valores de la primera normal estandar")
print(Z3)
# impresión de la primera normal estandar y luego de la segunda
input("Presione enter para seguir")
print(str(N) + " valores de la segunda normal estandar")
print(Z4)
print("Se generaron {} parejas de V1, V2".format(count))