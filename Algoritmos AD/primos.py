import math as m

n = 11
i = 1
cont = 0
while i < n:
    if n % i == 0:
        cont += 1
    i += 1
if cont > 2:
    print("No es primo")
else:
    print("Es primo")
