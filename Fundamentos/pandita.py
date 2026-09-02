import pandas as pd
import matplotlib.pyplot as plt

data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

#load data into a DataFrame object:
df = pd.DataFrame(data)

print("*** Impresión de todo el dataframe ***")
print(df) 

print("*** numero de filas con len() ***")
print(len(df))

print("*** Impresión de la fila 0 ***")
print(df.loc[0])

print("*** Acceder a una fila que no existe ***")
try:
    print(df.loc[4])
except :
    print(f"La fila {4} no existía")

# imprimir fila a fila, una por una
print("*** Impresión fila a fila ***")
for i in range(len(df)):
    print(df.loc[i])    


# imprimir un conjunto, la diferencia es que acá es un dataframe el resultado:

#use a list of indexes:
print("*** Impresión de un subconjunto ***")
print(df.loc[[0, 1]])

# Leer un archivo separado por comas
subdir = "./Programas Clase 2022-[1 2]/Fundamentos/"
archivo = subdir + 'datos2.csv'
df2 = pd.read_csv(archivo, delimiter=';')

print(df2) 
print(df2["age"])

plt.plot(df2["age"], df2["height"], "g*")
plt.show()



## tutorial https://likegeeks.com/pandas-tutorial/, hacerlo en colab o en un .py