import matplotlib.pyplot as plt
import numpy as np
import os

class espacio_simulacion:
    # metdos de la simulacion
    def __init__(self, nfilas, maxpresas, maxdepredadores, tmax ):
        self.cols = nfilas
        self.filas = nfilas
        self.max_depredadores = maxdepredadores
        self.max_presas = maxpresas
        self.t_nat_presas = 0.3
        self.t_nat_depredador = 0.2
        self.t_caza = 0.3
        self.t_competencia = 0.3
        self.T_MAX = tmax
        self.campo = np.zeros((self.filas, self.cols), dtype=int)
        self.campo_prox = np.zeros((self.filas, self.cols), dtype=int)
        

        i = 0
        while  i < self.max_depredadores :
            x = np.random.randint(0, self.cols)
            y = np.random.randint(0, self.filas)
            if self.campo[y, x] != 0:
                i = i - 1
            else :
                self.campo[y, x] = 1
            i += 1

        i = 0 
        while  i < self.max_presas :
            x = np.random.randint(0, self.cols)
            y = np.random.randint(0, self.filas)
            if self.campo[y, x] != 0:
                i = i - 1
            else :
                self.campo[y, x] = 2
            i += 1

        self.cacerias = 0
        self.nacimientos_presas = 0
        self.muertes_competencia = 0
        self.nacimientos_depredadores = 0
        
        self.debug_depredadores = 0

    def reporte_acciones(self):
        return self.cacerias, self.nacimientos_presas, self.muertes_competencia, self.nacimientos_depredadores

    def dir_a_coord(self, dir):
        # direcciones:
        # | 0 | 1 | 2 |
        # | 7 | x | 3 |
        # | 6 | 5 | 4 |
        match dir:
            case 0:
                return -1, -1
            case 1:
                return 0, -1
            case 2:
                return 1, -1
            case 3:
                return 1, 0
            case 4:
                return 1, 1
            case 5:
                return 0, 1
            case 6:
                return -1, 1
            case 7:
                return -1, 0
            
    def revisar_posicion(self, i, j):
        if self.campo[i, j] != 0:
            return False
        else:
            return True

    def contar_actores(self):
        # porción de código para contar depredadores y presas en un tiempo t
        presas_t = np.where(self.campo == 2)
        depredadores_t = np.where(self.campo == 1)
        vacios = np.where(self.campo == 0)
        return len(presas_t[0]), len(depredadores_t[0]), len(vacios[0])
    
    def reproduccion(self, i, j, tipo):
        if tipo == 1 :
            t_opuesto = 2
            tasa_nat = self.t_nat_depredador
        elif tipo == 2 :
            t_opuesto = 1
            tasa_nat = self.t_nat_presas
        else :
            print("Error inesperado, tipo de organismo incorrecto")
            return 0
        self.campo_prox[i, j] = tipo
        p = np.random.random()
        if p < tasa_nat :
            pos_valida = False
            pos_intentos = 0
            # reproducción
            # poner otra presa en una casilla adyacente al azar
            while not pos_valida and pos_intentos < 8 :
                temp_dir = np.random.randint(0, 8)
                temp_offset = s.dir_a_coord(temp_dir)
                #print(i + temp_offset[0], j + temp_offset[1] )

                # revisar que el offset no se salga de los bordes
                if (i + temp_offset[0] >=0 ) and (j + temp_offset[1] >=0) and (i + temp_offset[0]< self.filas) and (j + temp_offset[1] < self.cols) :
                    if self.revisar_posicion(i + temp_offset[0], j + temp_offset[1] ) :
                        self.campo_prox[i + temp_offset[0], j + temp_offset[1] ] = tipo
                        pos_valida = True
                        if tipo == 1:
                            self.nacimientos_depredadores += 1
                        else :
                            self.nacimientos_presas += 1
                    else :
                        pos_intentos += 1
                else :
                    print(f"No trates de nacer fuera del campo papu - ({i + temp_offset[0]},{j + temp_offset[1]})")


    def mov_presas(self, i, j):
        direccion = np.random.randint(0, 8)
        temp_of, temp_oc = self.dir_a_coord(direccion)
        # revisar bordes y existencia de otro actor
        if (i + temp_of >=0 ) and (j + temp_oc >=0) and (i + temp_of < self.filas) and (j + temp_oc < self.cols) :
            if self.campo[i + temp_of, j + temp_oc] == 0 :
                # esto representa que se movió a una casilla válida que estaba vacía
                self.campo_prox[i + temp_of, j + temp_oc] = 2
                self.campo_prox[i, j] = 0
            elif self.campo[i + temp_of, j + temp_oc] == 2 :
                # posibilidad de reproducirse
                self.campo_prox[i, j] = 2
                self.reproduccion(i, j, 2)
        else :
            print(f"No te golpees con la pared, papu - ({i},{j})")
            self.campo_prox[i, j] = 2

    def mov_depredadores(self, i, j):
        # movimiento de cada actor en cada celda:
        # reglas de prelación:
        # izquierda > derecha, arriba > abajo, presas se mueven antes que el depredador.  Muertes ocurren antes que nacimientos.
        # direcciones:
        # | 0 | 1 | 2 |
        # | 7 | x | 3 |
        # | 6 | 5 | 4 |
        direccion = np.random.randint(0, 8)
        #print(f'tiempo {t}, direccion {direccion}')
        temp_of, temp_oc = self.dir_a_coord(direccion)
        # revisar bordes y existencia de otro actor
        if (i + temp_of >=0 ) and (j + temp_oc >=0) and (i + temp_of < self.filas) and (j + temp_oc < self.cols) :
            if self.campo[i + temp_of, j + temp_oc] == 0 :
                # esto representa que se movió a una casilla válida que estaba vacía
                self.campo_prox[i + temp_of, j + temp_oc] = 1
                self.campo_prox[i, j] = 0
            elif self.campo[i + temp_of, j + temp_oc] == 2 :
                # posibilidad de cazar - jäger!
                p = np.random.random()
                if p < self.t_caza :
                    # casa exitosa
                    # borra el que estaba y se pone el en ese lugar
                    self.campo_prox[i + temp_of, j + temp_oc] = 1
                    # aca hay un lio!!!
                    self.campo_prox[i, j] = 0
                    #self.campo[i + temp_of, j + temp_oc] = 0
                    self.cacerias += 1
                    print("Muerte! depreda")
                else :
                    self.campo_prox[i, j] = 1
            elif self.campo[i + temp_of, j + temp_oc] == 1 :
                self.debug_depredadores += 1
                # posibilidad de reproducirse - o de matarse entre ellos
                self.campo_prox[i, j] = 1
                self.reproduccion(i, j, 1)
                p = np.random.random()
                if p < self.t_competencia :
                    # Me dio amsiedad por muchos depredadores!
                    self.campo_prox[i, j] = 0
                    #self.campo[i, j] = 0
                    self.muertes_competencia += 1
                    # Acá se pone la muerte por competencia
                else :
                    self.campo_prox[i, j] = 1
        else :
            print(f"No se de con la pared, vago - ({i},{j})")
            self.campo_prox[i, j] = 1        



# no curses porque no max power



DEP = []
PRE = []
VAC = []
CAC = []
NAP = []
COM = []
NAD = [] 
        
T = []

t = 0
n = 20
presas = 200
depredadores = 100
tmax = 200

s = espacio_simulacion(n, presas, depredadores, tmax)
# creación del espacio de simulación
# 0 - espacio vacio
# 1 - depredador
# 2 - presa


#ciclo principal
while t < s.T_MAX:
    # imprimir todo el tablero
    print(f"Paso de tiempo t={t}") 
    n = s.filas
    m = s.cols
    for i in range(n):
        print("[ ", end='')
        for j in range(m):
            print(s.campo[i, j], end=" ")
        print(" ]")
    
    for i in range(s.filas):
        for j in range(s.cols):
            
            # movimiento de cada actor en cada celda:
            # reglas de prelación:
            # izquierda > derecha, arriba > abajo, presas se mueven antes que el depredador.  Muertes ocurren antes que nacimientos.
            # direcciones:
            # | 0 | 1 | 2 |
            # | 7 | x | 3 |
            # | 6 | 5 | 4 |
            if s.campo[i, j] == 2:
                # reglas para las presas.
                s.mov_presas(i, j)
            elif s.campo[i, j] == 1:
                # reglas para los asesinos.
                #print(f"{i}, {j}")
                s.mov_depredadores(i, j)
                
    # contamos las presas y los depredadores.
    pre, dep, vac = s.contar_actores()
    cac, nap, com, nad = s.reporte_acciones()
    print(f'Presas={pre} - Depredadores={dep}')
    # esperar tecla y limpiar
    #input("Press Enter to continue...")
    os.system('clear')

    # añadimos a las listas para mirar al final
    PRE.append(pre)
    DEP.append(dep)
    VAC.append(vac)

    CAC.append(cac)
    NAP.append(nap)
    COM.append(com)
    NAD.append(nad)


    T.append(t)
    # campo_prox se vuelve el actual

    s.campo = s.campo_prox
    t += 1

print(f"Valores iniciales:")
print(f"depredadores={depredadores}")
print(f"presas={presas}")
print(f"vacios={n*n - (depredadores + presas)}")

print(f"Depredadores: {DEP}")
print(f"Presas: {PRE}")
print(f"Vacios: {VAC}")
print(f"Cacerias(t): {CAC}")
print(f"NacPresas(t): {NAP}")
print(f"Competencias(t): {COM}")
print(f"NacDepredadores(t): {NAD}")
print(f"Tiempo: {T}")


print(f"Muertes por cacería: {s.cacerias}")
print(f"Nacimientos de presas: {s.nacimientos_presas}")
print(f"Nacimientos de depredadores: {s.nacimientos_depredadores}")
print(f"Muertes por competencia: {s.muertes_competencia}")
print(f"Debug: {s.debug_depredadores}")

plt.plot(T, DEP, '-r', T, PRE, '-b')
plt.show()