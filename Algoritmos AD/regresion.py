'''
La idea es calcular los parámetros del modelo: Y = a * x + b

los valores se calculan de la siguiente manera:

b = (((n*sum(x*y)) - (sum(x)*sum(y))) / ( n*(sum(x**2)) - (sum(x))**2 )

a = ( (sum(y)*(sum(x)**2) - (sum(x*y) * sum(x)) / ( (n*sum(x**2)) - (sum(x) ** 2) )

'''

import numpy as np
import matplotlib.pyplot as plt
import math as m

x = [*range(-1, 10, 1)]
print(x)
y = [i**2 for i in x]
print(y)

''' 
Forma manual, con listas.
'''

n = len(x)
sx = sum(x)
sy = sum(y)
sxy = sum([ x[i]*y[i] for i in range(n) ])
sxx = sum([ i**2 for i in x ])


b = ((n * sxy) - (sx * sy)) / ( n * (sxx) - (sx**2) )
a = ( sy*(sxx) - (sxy * sx) ) / ( (n * sxx) - (sx ** 2) )

print(a, b)

y2 = []
for i in range(n):
    y2.append(a + b * x[i])

print(y2)

plt.plot(x, y, "*g")
plt.plot(x, y2, "-r")
plt.show()