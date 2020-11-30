import numpy as np

a = np.zeros([24,80])
b = np.zeros([24,80])

def contarvecinos(nren,ncol):
    suma = 0
    for r in range (nren-1, nren + 2) :
        for c in range (ncol-1, ncol + 2) :
            suma = suma + a[r,c]
    return suma - a[nren, ncol]

def nuevoEdo(edoactual, vecinosvivos):
    ne = 0
    if edoactual == 0 :
        if vecinosvivos == 3 :
            ne = 1
    else : 
        if vecinosvivos == 2 or vecinosvivos == 3 :
            ne = 1
        else :
            ne = 0
    return ne 

def escribe () :
    for ren in range(24) :
        for col in range(80) :
            if a[ren,col] == 0 :
                print(" ", end='')
            else :
                print("*", end='')
        print()

print (a)
a[5,5] = 1
escribe()

