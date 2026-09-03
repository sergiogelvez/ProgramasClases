entrada = input("Frase: ")
salida = ""

for i in range(len(entrada)) :
    if entrada[i] == 'h' :
        salida = salida + 'f'
    elif  entrada[i] == 'H' :
        salida = salida + 'F'
    else :
        salida = salida + entrada[i]

print(salida)