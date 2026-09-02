op1 = int(input("Operador 1: "))
op2 = int(input("Operador 2: "))

try :
    op3 = int(input("Operador 3: "))
    division = op1 / op2
    print(f"Resultado: {division}")
except ZeroDivisionError :
    print("Error!!! Division por cero")
except ValueError:
    print("El valor del operando no es un numero valido")


