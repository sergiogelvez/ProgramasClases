import csv


def media(A):
    n = len(A)
    suma = 0
    for i in range(n):
        suma += A[i]
    if n > 0 :
        return suma / n
    else:
        return 0


path = "/home/sgelvez/linuxProjekte/MaterialClases/Arreglos/datos.csv"
archivo = open(path)

lineas = archivo.readlines()
print(lineas)

Tabla = []
for i,linea in enumerate(lineas):
    if i > 0:
        fila = linea.strip().split(";")
        print(fila[4])
        if fila[4] != "NA" :
            fila_f = [float(fila[4]), float(fila[1])]
        # si hay NA en la altura lo descartamos
            Tabla.append(fila_f)

print(Tabla)
print(type(Tabla))
print(len(Tabla))

Estaturas = [i[0] for i in Tabla]
Edades = [i[1] for i in Tabla]

print(Estaturas)
print(len(Estaturas))
prom = media(Estaturas)

print(f"la media es {prom}")

'''with open(path, "r") as csvfile:
    reader_variable = csv.reader(csvfile, delimiter=";")
    for row in reader_variable:
        print(row)
'''
