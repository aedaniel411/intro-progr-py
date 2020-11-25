import numpy as np

a = np.zeros([24,80])
b = np.zeros([24,80])

def nuevo_edo(nren,ncol):
    suma = 0
    for r in range (nren-1, nren + 2) :
        for c in range (ncol-1, ncol + 2) :
            suma = suma + a[r,c]
    suma = suma - a[nren, ncol]



print (a)
