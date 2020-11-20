# importar modulos
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation   

def compox (v, a):
    return v * np.cos(a)

def compoy (v, a):
    return v * np.sin(a)

v = 100 #float (input("Velocidad inicial "))
a = 45 #float (input("Angulo: "))
a = np.deg2rad (a)

g = 9.8
xmax = v ** 2.0 * np.sin(2.0 * a) / g 
ymax = v ** 2.0 * np.sin(a) ** 2.0  / (2.0 * g )
ttot = 2.0 * v * np.sin(a) / g
margenx = xmax * (0.10) 
margeny = ymax * (0.10)

t = np.linspace(0.0, ttot, 100)
y = compoy(v,a) * t - (1.0/2.0)*g * t**2.0
x = compox(v,a) * t

# definir gráfica
fig = plt.figure(20)
ax = fig.gca()

def actualiza(i) :
    ax.clear()
    plt.ylim (0.0 - margeny, ymax + margeny)
    plt.xlim (0.0 - margenx, xmax + margenx)
    ax.plot(x[:i], y[:i])

# funicion de animar 
ani = animation.FuncAnimation(fig,actualiza,range(len(x)), interval=5,repeat=True)
plt.show()