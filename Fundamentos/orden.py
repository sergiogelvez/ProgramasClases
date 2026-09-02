import random as rnd

n = 20
A = []
for i in range(n):
    A.append(int(100 * rnd.random()))

print(A)

for i in range(n):
    for j in range(0 , n - i - 1 ):
        if A[j] > A[j + 1]:
            ''' temp = A[j]
            A[j] = A[j + 1]
            A[j + 1] = temp '''
            A[j], A[j+1] = A[j+1], A[j]

print(A)

B = A[:n//2]
print(B)