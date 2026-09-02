import math as m
import statistics as st
from matplotlib import scale
import matplotlib.pyplot as plt
import numpy as np
import random as rnd
import scipy.stats as sp

N = 100 # numero de números a generar
mu = 5 # localización
s = 2 # escala
X = []
for i in range(N):
    U = rnd.random()
    x = mu + s * m.log( U / (1-U) )
    # print(x)
    X.append(x)

generados = np.array(X)
#print(generados)
n = len(generados)
#print(n) # para este ejemplo n = N, pero ajá
h = m.ceil(m.log(n)/m.log(2)) + 1 # h categorias por la formula de sturgess
observados, limitesh = np.histogram(generados, h)
#print(observados.sum())
centrosh = []
for i in range(len(limitesh) - 1):
    ch = (limitesh[i+1] - limitesh[i])/2 + limitesh[i]
    centrosh.append(ch)

#centrosh2 = [(limitesh[i+1] - limitesh[i])/2 + limitesh[i] for i in range(len(limitesh) - 1)]
probs = [sp.logistic.cdf(limitesh[i+1], loc = mu, scale = s) - sp.logistic.cdf(limitesh[i], loc = mu, scale = s) for i in range(len(limitesh) - 1)]
esperados = n*np.array(probs)
print("Probabilidades de las categorías:")
print(probs)
print("Numero de categorías")
print(len(probs))
print(h)
print("Valores esperados para las categorías")
print(esperados)
print("La suma de los esperados es {}".format(esperados.sum()))
xj = np.arange(-2, 10, 0.01)
yj = sp.logistic.pdf(xj, loc = mu, scale = s)
# plt.plot(xj, yj)
# plt.show()
yj = sp.logistic.cdf(xj, loc = mu, scale = s)
# plt.plot(xj, yj)
# plt.show()
chis = (observados - esperados)**2 / esperados
chi2 = chis.sum()
print("Valor del estadístico de prueba para comparar con chi2: {}".format(chi2))
print("Valor límite para 0.05: {}".format(sp.chi2.ppf(1-0.05, h - 3)))
print("Valor de probabilidad en chi2 para el estadístico: {}".format(sp.chi2.cdf(chi2, h - 3)))
if chi2 < sp.chi2.ppf(1-0.05, h - 3):
    print("Los datos parecen provenir de una distribución logística con loc={} y escala={}".format(mu, s))
else:
    print("Los datos no cumplen con la distribución logísitica seleccionada")
#print(centrosh)
#print(centrosh2)
#print(limitesh)
plt.bar( centrosh, observados)
plt.show()
plt.bar( centrosh, esperados)
plt.show()
