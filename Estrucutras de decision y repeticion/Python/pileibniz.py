import math as m

tolerancia = float(input("Ingrese la tolerancia: "))

suma = 0
i = 0

while abs(m.pi / 4 - suma) > tolerancia:
    suma += ( (-1) ** i)/(2 * i + 1)
    i += 1
    
pi = suma * 4

print(f"La aproximacion de pi es {pi}, con {i} terminos de la serie")    