
import pandas as pd
import matplotlib.pyplot as plt
import statistics as st

# Esto solo va cuando hay un subdirectorio 
subdir = "./Programas Clase 2022-[1 2]/Fundamentos/"

archivo = subdir + "SLOFEPB.xlsx"
print(archivo)

df = pd.read_excel(archivo)

print(df.to_string()) 
print(df.info())
print(df.loc[5])
print(df["Y (km)"])

plt.plot(df["X (km)"], df["Y (km)"], "o")
plt.show()

print(st.median(df["Log Fe"]))

# hallar media, moda, mediana, desviación estándar, varianza
# sacar la regresión lineal por minimos cuadrados



