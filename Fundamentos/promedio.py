import statistics as st

n = int(input("Numero de elementos a ingresar: "))
A = []
for i in range(n):
    valor = float(input("Introduzca un valor: "))
    A.append(valor)

print(A)
promedio = st.mean(A)
print(promedio)

suma = 0.0
for i in range(n):
    suma = suma + A[i]

promedio = suma / n
print(promedio)

suma = 0.0
for elem in A:
    suma += elem # suma = suma + elem

promedio = suma / n
print(promedio)
