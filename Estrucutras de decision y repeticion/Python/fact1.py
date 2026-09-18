numero = int(input("Numero para sacar factorial: "))

fact = 1
while numero > 0 :
    fact = fact * numero
    numero = numero - 1
    
print(fact)