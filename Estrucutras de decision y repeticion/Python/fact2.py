import math as m

numero = int(input("Numero para sacar factorial: "))

fact = 1
i = 1

while i <= numero :
    fact = fact * i
    i = i + 1
    
print(fact)
print(m.factorial(numero))