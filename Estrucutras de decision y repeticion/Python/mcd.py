valor1 = int(input("Introduzca un valor: "))
valor2 = int(input("Introduzca un valor: "))

if valor1 == valor2 :
    print(f"El mcd es {valor1}")
elif valor1 < valor2 :
    for i in range(1, valor1 + 1):
        if valor1 % i == 0 and valor2 % i == 0 :
            mcd = i
    print(f"El mcd es {mcd}")
else :
    for i in range(1, valor2 + 1):
            if valor1 % i == 0 and valor2 % i == 0 :
                mcd = i
    print(f"El mcd es {mcd}")
