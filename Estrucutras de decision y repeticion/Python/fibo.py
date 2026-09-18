#num_terminos = int(input("Cuantos términos de la meravigliosa serie de Fibonacci: "))
num_termino = int(input("Cuál término de la meravigliosa serie de Fibonacci voglia: "))

penultimo = 0
ultimo = 1

if num_termino <= 2 :
    if num_termino == 2: 
        print(ultimo)
    else :
        print(penultimo)
else :
    for i in range(3, num_termino + 1) :
        suma = penultimo + ultimo
        penultimo = ultimo
        ultimo = suma
        if i == num_termino:
            print(ultimo)