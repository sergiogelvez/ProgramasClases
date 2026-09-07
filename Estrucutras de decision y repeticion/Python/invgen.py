entrada = input("Que quiere invertir?: ")
salida = ""

for i in range(len(entrada)) :
    print(entrada[i])
    salida = entrada[i] + salida

if salida == entrada :
    print("Palindromo")
else :
    print("No es palindromo")

print(salida)