angulo = int(input("Angulo en grados: "))
x = (angulo * 3.14159) / 180
print(x)
suma = 0 
nterminos = int(input("Numero de términos: "))
for i in range(nterminos) :
    fact = 1
    j = 1
    lim = 2 * i + 1
    while j <= lim :
        fact = fact * j
        j = j + 1
    #print(fact)
    suma = suma + (((-1) ** i) * (x ** (lim) )) / fact

print(suma)