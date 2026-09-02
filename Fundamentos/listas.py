'''
A = [ 1, 3, 7, 4, 5, 9]
print(A)
print(A[-2])
print(A[2])
print(A[0:3])
print(A[1:-3])
#print(A[9])
A.append("Gato")
print(A)
B = ["Gato", "Perro", "Nutria", "Morsa"]
print(B)

for i in range(5):
    print(i)

for animal in B:
    print(animal)

print(len(B))

for i, animal in enumerate(B):
    print("Posicion " + str(i) + " : " + animal)

n = len(B)

for i in range(n):
    print(B[i])

'''

nombre = "Niceforo"
print(nombre)
print(nombre[4])

encontrado = False
for i in range(len(nombre)):
    if nombre[i] == 'w':
        encontrado = True

if encontrado:
    print("Si hay una w")
else:
    print("No hay w")
        

