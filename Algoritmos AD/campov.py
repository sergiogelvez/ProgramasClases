import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm
  
# Meshgrid
x, y = np.meshgrid(np.linspace(-5, 5, 10), 
                   np.linspace(-5, 5, 10))
print(x)
print(type(x))
print(x.shape)
print(y)
print(type(y))
print(np.linspace(-5, 5, 10))
print(np.arange(-5, 5, 1))
# Directional vectors
u = -y/np.sqrt(x**2 + y**2)
v = x/(x**2 + y**2)
  
# Plotting Vector Field with QUIVER
plt.quiver(x, y, u, v, color='g')
plt.title('Vector Field')
  
# Setting x, y boundary limits
plt.xlim(-7, 7)
plt.ylim(-7, 7)
  
# Show plot with grid
plt.grid()
plt.show()

### otra forma de hacer la gráfica

# 1D arrays
x = np.arange(-5,5,0.1)
y = np.arange(-5,5,0.1)
  
# Meshgrid
X,Y = np.meshgrid(x,y)
  
# Assign vector directions
Ex = (X + 1)/((X+1)**2 + Y**2) - (X - 1)/((X-1)**2 + Y**2)
Ey = Y/((X+1)**2 + Y**2) - Y/((X-1)**2 + Y**2)
  
# Depict illustration
plt.figure(figsize=(10, 10))
plt.streamplot(X,Y,Ex,Ey, density=1.4, linewidth=None, color='#A23BEC')
plt.plot(-1,0,'-or')
plt.plot(1,0,'-og')
plt.title('Electromagnetic Field')
  
# Show plot with grid
plt.grid()
plt.show()



#### campo escalar
Z = X * np.sinc(X ** 2 + Y ** 2) 

plt.pcolormesh(X, Y, Z, cmap = cm.gray) 
plt.show()