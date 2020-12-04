import numpy as np
import matplotlib.pyplot as plt 
from scipy.optimize import curve_fit
import pandas as pd

def f(x, a, b):
    return a / x**b

#archivo = np.loadtxt('datos01.dat')
datos = pd.read_excel('datos01.xlsx')
#print (datos)

res , mat = curve_fit(f, datos['m'],datos['klux'])
print (mat)

x = np.linspace(min(datos['m']),max(datos['m']),50)
y = f(x,res[0],res[1])  

plt.scatter(datos['m'],datos['klux'], color='red')
plt.plot(x,y,color='blue')
plt.show()

