entrada = input("Que frase quiere invertir?: ")
salida = ""

palabras = entrada.split(" ")

for i in range(len(palabras)) :
    #print(palabras[i])
    salida = palabras[i] + " " + salida

print(salida)