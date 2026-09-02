import random as rnd
import math as m
import statistics as st
import numpy as np

n = 20
list = []
for i in range(n):
    list.append(int(100 * rnd.random()))
suma = 0
print(list)
for i in range(n):
    suma = suma + list[i]
promedio = suma / n
print(promedio)
promedio = st.mean(list)
print(promedio)

print("Version con numpy arrays")

array = np.array(list)
print(array)
promedio = np.mean(array)
print(promedio)

suma = np.sum(array)
promedio = suma / n
print(promedio)

suma = sum(list)
promedio = suma / n
print(promedio)
