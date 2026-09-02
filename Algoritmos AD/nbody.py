# basado en el ejemplo del artículo de n_body simulation de wikipedia.  Es un ejemplo "sencillo"

import numpy as np
import matplotlib.pyplot as plt

'''class Vector3D:
    def __init__(self, x, y, z) -> None:
        self.vec = np.array([x , y, z])

    def __str__(self):
        return f"{self.vec[0]}, {self.vec[1]}, {self.vec[2]}"
    
    def get(self):
        return self.vec

    
gato = Vector3D(0., 0., 5.)
print(gato)
print(gato.get())

gato.vec = np.zeros(3)

print(gato.vec)
'''
numero_planetas = 8
numero_asteroides = 0
n_cuerpos = numero_planetas + numero_asteroides + 1

entidades_orbitales = np.zeros( ( n_cuerpos , 7) )

# el sol será la primera entidad orbital
# se pone lo de los asteroides por si acaso

entidades_orbitales[0, :] = np.array([ 0.0,0.0,0.0,        0.0,0.0,0.0,      1.989e30 ]) # un cuerpo similar al sol
entidades_orbitales[1, :] = np.array([ 57.909e9,0.0,0.0,   0.0,47.36e3,0.0,  0.33011e24 ]) # un cuerpo similar a mercurio
entidades_orbitales[2, :] = np.array([ 108.209e9,0.0,0.0,  0.0,35.02e3,0.0,  4.8675e24 ])  # un cuerpo similar a venus
entidades_orbitales[3, :] = np.array([ 149.596e9,0.0,0.0,  0.0,29.78e3,0.0,  5.9724e24 ])  # un cuerpo similar a la tierra
entidades_orbitales[4, :] = np.array([ 227.923e9,0.0,0.0,  0.0,24.07e3,0.0,  0.64171e24 ]) # un cuerpo similar a marte
entidades_orbitales[5, :] = np.array([ 778.570e9,0.0,0.0,  0.0,13e3,0.0,     1898.19e24 ]) # un cuerpo similar a jupiter
entidades_orbitales[6, :] = np.array([ 1433.529e9,0.0,0.0, 0.0,9.68e3,0.0,   568.34e24 ])  # un cuerpo similar a saturno
entidades_orbitales[7, :] = np.array([ 2872.463e9,0.0,0.0, 0.0,6.80e3,0.0,   86.813e24 ])  # un cuerpo similar a urano
entidades_orbitales[8, :] = np.array([ 4495.060e9,0.0,0.0, 0.0,5.43e3,0.0,   102.413e24 ]) # un cuerpo similar a neptuno
# acá se continuaría con las definiciones de asteoides y todo eso 

# variables de control
t_0 = 0
t = t_0
dt = 86400
t_fin = 86400 * 365 * 10 # aproximadamente una decada en segundos
G = 6.67e-11 # constante gravitacional

'''

recordar que si cambiamos entidades_orbitales por e, las posiciones representan:

e[0] = e0; pos x
e[1] = e1; pos y
e[2] = e2; pos z
e[3] = e3; vel x
e[4] = e4; vel y
e[5] = e5; vel z
e[6] = e6; masa

'''

# truco muy chulo para graficar, temporal
trayectorias0 = []
trayectorias1 = []
trayectorias2 = []
trayectorias3 = []
trayectorias4 = []
trayectorias5 = []
trayectorias6 = []
trayectorias7 = []
trayectorias8 = []

print("Valores iniciales:")
print(entidades_orbitales)

# pasos para cada calculo de cada paso de tiempo
#    calculating the forces on each body
#    calculating the accelerations of each body ( a → {\vec {a}})
#    calculating the velocities of each body ( v → n = v → n − 1 + a → n {\displaystyle {\vec {v}}_{n}={\vec {v}}_{n-1}+{\vec {a}}_{n}})
#    calculating the new position of each body ( r → n + 1 = r → n + v → n {\displaystyle {\vec {r}}_{n+1}={\vec {r}}_{n}+{\vec {v}}_{n}})
cuente = 0

while (t < t_fin): #acá controlamos el número de pasos de tiempo
    for m1 in range(n_cuerpos): # for para recorrer cada cuerpo, m1 quiere decir, indice de masa 1
        a_g = np.array([0,0,0]) # aceleración para la masa m1, cabe recordar que cada masa será tenida en cuenta, luego este vector va a representar diferentes masas a medida que el for avanza
        for m2 in range(n_cuerpos): # for para recorrer cada cuerpo, esta vez para ser la masa 2
            # recordar que acá se va a medir la "influencia" de cada cuerpo m2 en m1. m1 y m2 no pueden ser iguales
            if m2 != m1:
                #r_vector = np.array([0,0,0]) # vector para calcular la distancia entre las dos masas
                '''
                r_vector.e[0] = orbital_entities[m1_idx].e[0] - orbital_entities[m2_idx].e[0];
                r_vector.e[1] = orbital_entities[m1_idx].e[1] - orbital_entities[m2_idx].e[1];
                r_vector.e[2] = orbital_entities[m1_idx].e[2] - orbital_entities[m2_idx].e[2];
                '''
                
                vector_r = entidades_orbitales[m1, :3] - entidades_orbitales[m2, :3]
                # norma del vector dirección entre las dos masas
                mag_r = np.sqrt(np.dot(vector_r, vector_r))
                # print(mag_r)
                # cálculo de la aceleración, basicamente se omite la masa de m1
                aceleracion = (-1.0 * G * (entidades_orbitales[m2, 6])) / (mag_r**2)
                # cálculo de los vectores unitarios y las proyecciones de la aceleración
                vector_ru = vector_r / mag_r
                # acá se acumulan los valores de acelaciones, recordar que a_g es del nivel del primer for, entonces se acumulan valores para cada paso del segundo for
                a_g = a_g + aceleracion * vector_ru
                # fin del if
            # fin del segundo for
        # acá se calculan las velocidades para el paso t
        entidades_orbitales[m1, 3:6] = entidades_orbitales[m1, 3:6] + a_g * dt 
        '''
        orbital_entities[m1_idx].e[3] += a_g.e[0] * dt;
        orbital_entities[m1_idx].e[4] += a_g.e[1] * dt;
        orbital_entities[m1_idx].e[5] += a_g.e[2] * dt;
        '''
        # fin del primer for 
    
    for m1 in range(n_cuerpos):
        # calculo de las posiciones para el tiempo t
        entidades_orbitales[m1, :3] = entidades_orbitales[m1, :3] + entidades_orbitales[m1, 3:6] * dt
    
    if t % (dt * 10)  == 0:
        # salvar puntos para trayectorias de los planetas y el sol. Que no se note que ya estaba cansado
        trayectorias0.append([entidades_orbitales[0, 0], entidades_orbitales[0, 1], entidades_orbitales[0, 2]])
        trayectorias1.append([entidades_orbitales[1, 0], entidades_orbitales[1, 1], entidades_orbitales[1, 2]])
        trayectorias2.append([entidades_orbitales[2, 0], entidades_orbitales[2, 1], entidades_orbitales[2, 2]])
        trayectorias3.append([entidades_orbitales[3, 0], entidades_orbitales[3, 1], entidades_orbitales[3, 2]])
        trayectorias4.append([entidades_orbitales[4, 0], entidades_orbitales[4, 1], entidades_orbitales[4, 2]])
        trayectorias5.append([entidades_orbitales[5, 0], entidades_orbitales[5, 1], entidades_orbitales[5, 2]])
        trayectorias6.append([entidades_orbitales[6, 0], entidades_orbitales[6, 1], entidades_orbitales[6, 2]])
        trayectorias7.append([entidades_orbitales[7, 0], entidades_orbitales[7, 1], entidades_orbitales[7, 2]])
        trayectorias8.append([entidades_orbitales[8, 0], entidades_orbitales[8, 1], entidades_orbitales[8, 2]])

    t += dt
    # fin del while

# fin de la simulación
print("Valores finales:")
print(entidades_orbitales)
print(cuente)
#print(trayectorias, len(trayectorias))

# convertir las listas en arrays para poder transponer.  No es lo más eficiente, pero es temporal
tray0 = np.array(trayectorias0)
tray1 = np.array(trayectorias1)
tray2 = np.array(trayectorias2)
tray3 = np.array(trayectorias3)
tray4 = np.array(trayectorias4)
tray5 = np.array(trayectorias5)
tray6 = np.array(trayectorias6)
tray7 = np.array(trayectorias7)
tray8 = np.array(trayectorias8)

plt.plot(tray0.T[0], tray0.T[1], "-y", tray1.T[0], tray1.T[1], "-g", tray2.T[0], tray2.T[1], "c-", tray3.T[0], tray3.T[1], "-b", tray4.T[0], tray4.T[1], "-r", tray5.T[0], tray5.T[1], "-y", tray6.T[0], tray6.T[1], "c-", tray7.T[0], tray7.T[1], "-g", tray8.T[0], tray8.T[1], "-b" )
plt.show()
#
