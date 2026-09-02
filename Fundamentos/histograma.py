import pandas as pd
import numpy as np
import math as m
import matplotlib.pyplot as plt

patho = "Programas Clase 2022-[1 2]/Fundamentos/"
archivo = "SLOFEPB.xlsx"
print(patho + archivo)

df = pd.read_excel(patho + archivo)

#print(df)

datos = df['Log Pb']

print(datos)

n = len(datos)

bins = m.ceil(m.log2(n)) + 1

print(bins)

histo, clases = np.histogram(datos, bins)

histo2, clases2, parches = plt.hist(datos, bins)
plt.show()

#plt.bar(clases, histo)
plt.show()



print(histo)
print(clases)
print(histo2)
print(clases2)
print(parches)