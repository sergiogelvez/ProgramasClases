filas = int(input("Cuantas filas quiere calcular: "))

i = 0
while i <= filas :
    j = 0
    while j <= i :
        n = i
        r = j
        # calcular factorial de n
        factn = 1
        while n > 0:
            factn = factn * n 
            n = n - 1

        #factorial de r
        factr = 1
        while r > 0:
            factr = factr * r 
            r = r - 1

        nr = i - j
        factnr = 1
        while nr > 0:
            factnr = factnr * nr 
            nr = nr - 1

        # calculo del numero
        ncomb = (factn)/(factr * factnr)
        print(f"({i},{j})={ncomb}", end=" ")
        
        j = j + 1
    print("")
    i = i + 1
