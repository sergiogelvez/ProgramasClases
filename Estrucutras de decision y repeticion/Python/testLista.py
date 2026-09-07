A = []

num = int(input("Numero elementos: "))

for _ in range(num):
    A.append(int(input("elemento?: ")))

pares = [x for x in A if x % 2 == 0]
impares = [y for y in A if y % 2 == 1]

print(A)
print(pares)
print(impares)

prompar = sum(pares) / len(pares)
promimpar = sum(impares) / len(impares)

print(f"El promedio de los pares es {prompar}")
print(f"El promedio de los impares es {promimpar}")

Pares = []
Impares = []

for i in range(len(A)) :
    if A[i] % 2 == 0 :
        Pares.append(A[i])
    else :
        Impares.append(A[i])

print(Pares)
print(Impares)