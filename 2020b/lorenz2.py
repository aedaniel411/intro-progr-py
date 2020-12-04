# importar modulos
import numpy as np
import matplotlib.pyplot as plt 
from mpl_toolkits import mplot3d
from matplotlib import animation

# Definir datos
x = [0.5]
y = [0.5]
z = [0.5]

a = 10.0
b = 28.0
c = 8.0 / 3.0
t = 0.01

for i in range(5000) :
    x.append( (a * (y[i] - x[i]) )       * t + x[i] )
    y.append( (x[i] * (b - z[i]) - y[i]) * t + y[i] )
    z.append( (x[i] * y[i] - c * z[i])   * t + z[i] )

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
