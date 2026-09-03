numero = int(input("Numero: "))
resultado = 0
while numero > 0 :
    residuo = numero % 10
    numero = numero // 10
    resultado = resultado * 10 + residuo
    print(f"El residuo es {residuo} y el numero va en {numero}, y el resultado va en {resultado}")
