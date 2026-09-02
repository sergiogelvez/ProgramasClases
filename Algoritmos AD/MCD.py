import math as m

a = int(input("Introduzca por favor el primer número:"))
b = int(input("Introduzca por favor el primer número:"))

n = min(a, b)
mcd = 0

for i in range(1, n + 1):
    if (a%i==0 and b%i==0):
        mcd = i

print(f'El resultado del mcd de {a} y {b} es {mcd}')

