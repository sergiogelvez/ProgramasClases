max = 20 # numero limite para buscar
num = 0 # numero evaluado en cada ciclo para ver si es primo
primos = [2]
for num in range(3,max,2):
    print(f'Numero a evaluar: {num}', end=' ')
    lim = num / 2
    i = 2
    div = 0
    while i < lim :
        if num % i == 0 :
            div += 1 # div = div + 1
        i = i + 1
    if div < 1 :
        print("Es primo")
        primos.append(num)
    else :
        print("No es primo")
print(f'El número de primos hallados entre 2 y {max} es {len(primos)}')
print("El conjunto de numeros primos hallados es " + str(primos))