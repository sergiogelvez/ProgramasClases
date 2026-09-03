import math

a = float(input("Porfa el a: "))
b = float(input("Introduzca el b: "))
n = int(input("Cuantos pasos? (n): "))
dx = (b - a) / n
suma = 0
x = a
while x <= b :
    x = x + dx
    y = math.sin(x) ** 2 + x
    suma = suma + y * dx
print(f"el valor de la suma de riemann entre {a} y {b} para sin^2(x) + x es {suma}")
