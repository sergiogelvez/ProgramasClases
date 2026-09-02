import matplotlib.pyplot as plt
import numpy as np

n = 1000 # numero de pasos de tiempo
t0 = 0
tfinal = 100
theta = np.radians(45)
v0 = 100 # m/s
y0 = 50 # m
x0 = 0 # m, en el inicio de la gráfica
a = -9.8 # m/s2


dt = (tfinal - t0) / n

vy0 = v0 * np.sin(theta)
vx0 = v0 * np.cos(theta)



print(f"La velocidad inicial en x es {vx0} m/s")
print(f"La velocidad inicial en y es {vy0} m/s")


t = t0
x = x0
y = y0
vx = vx0
vy = vy0

T = [t]
X = [x]
Y = [y]

print(f"paso de tiempo: {dt}")
print(f"Para t = {t} | x = {x} | y = {y}")

while t < tfinal and y > 0: 
    vy = vy + a*dt
    y = y + vy * dt
    x = x + vx * dt
    t = t + dt
    print(f"Para t = {t} | x = {x} | y = {y}")
    X.append(x)
    Y.append(y)
    T.append(t)
    # vy0 = vy
    # y0 = y
    # x0 = x
print(X)
print(Y)
plt.plot(T, Y, "*r")
plt.show()
