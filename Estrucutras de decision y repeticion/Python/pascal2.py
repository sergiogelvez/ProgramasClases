import math as m

filas = int(input("Cuantas filas quiere calcular: "))

i = 0
while i <= filas :
    j = 0
    while j <= i :
        n = i
        r = j
        # calcular factorial de n
        factn = m.factorial(n)
        #factorial de r
        factr = m.factorial(r)
        factnr = m.factorial(n - r)
        
        # calculo del numero
        ncomb = (factn)/(factr * factnr)
        print(f"({i},{j})={ncomb}", end=" ")
        
        j = j + 1
    print("")
    i = i + 1
