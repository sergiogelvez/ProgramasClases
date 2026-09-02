from csv import reader
import math as m
import statistics as stat
import os

estaturas = []
sexos = []
# leer un archivo de estaturas
cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
#print("Files in %r: %s" % (cwd, files)) 
ruta = os.path.dirname(os.path.realpath(__file__))
#print("Path del script" + ruta)

# importante: cambiar estaturas.txt por el archivo correspondiente
with open(ruta + "/estatura_par.txt", 'r') as archivo_lectura:
    csv = reader(archivo_lectura)
    # ir fila a fila
    for fila in csv:
        # hacer algo con cada fila, asumo que cada fila tiene un solo valor

        ## recordar el split
        estaturas.append(float(fila[0]))

with open(ruta + "/sexo_par.txt", 'r') as archivo_lectura:
    csv = reader(archivo_lectura)
    # ir fila a fila
    for fila in csv:
        # hacer algo con cada fila, asumo que cada fila tiene un solo valor
        sexos.append(int(fila[0]))

for i in range(0,len(estaturas)):
    print(str(estaturas[i]) + ", " + str(sexos[i]))
print(len(estaturas))
print(len(sexos))


print(stat.mean(estaturas))
print(stat.variance(estaturas))
