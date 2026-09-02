import statistics as stat


A = [4, 7, 6, 2, 0, 9, 3, 9, 0, 1, 2, 1, 4, 0, 1, 5, 9, 6, 7, 7]

print(A)

moda1 = stat.mode(A)
moda2 = stat.multimode(A)

print(moda1)
print(moda2)