angulo = int(input("Angulo en grados: "))
x = (180 * angulo) /  3.14159
suma = 0 
nterminos = int(input("Numero de términos: "))
for i in range(nterminos) :
    fact = 1
    i = 1
    lim = 2 * i + 1
    while i <= lim :
        fact = fact * i
        i = i + 1
    suma = suma + (((-1) ** i) * (x ** (lim) )) / fact

print(suma)