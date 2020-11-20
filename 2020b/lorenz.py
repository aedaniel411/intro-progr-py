# importar modulos
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
from matplotlib import animation

# Definir datos
x = []
y = []
z = []

a = 10.0
b = 28.0
c = 8.0 / 3.0
t = 0.01

x1 = 0.5
y1 = 0.5
z1 = 0.5

for i in range(5000) :
    x2 = (a * (y1 - x1) )     * t + x1
    y2 = (x1 * (b - z1) - y1) * t + y1
    z2 = (x1 * y1 - c * z1)   * t + z1

    x1 = x2
    y1 = y2
    z1 = z2

    x.append(x1)
    y.append(y1)
    z.append(z1)

# definir grafica
fig = plt.figure(20)
ax = fig.gca(projection="3d")

def actualiza(i) :
    ax.clear()
    #plt.ylim (0.0 - margeny, ymax + margeny)
    #plt.xlim (0.0 - margenx, xmax + margenx)
    ax.plot3D (x[:i], y[:i], z[:i])

#ax.plot3D (x, y, z)
# funicion de animar 
ani = animation.FuncAnimation(fig,actualiza,range(len(x)), interval=1,repeat=True)
plt.show()
