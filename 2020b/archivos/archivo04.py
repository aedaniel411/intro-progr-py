import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit

def f(x, a, b):
    return a / x**b

archivo = np.loadtxt('datos01.dat')
res , mat = curve_fit(f, archivo[:,0],archivo[:,1])
print (mat)

x = np.linspace(min(archivo[:,0]),max(archivo[:,0]),50)
y = f(x,res[0],res[1]) 

plt.scatter(archivo[:,0],archivo[:,1], color='red')
plt.plot(x,y,color='blue')
plt.show()

