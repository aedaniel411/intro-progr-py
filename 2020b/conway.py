import numpy as np
import os, time

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
    #os.system("sleep 0.5") #en windows "timeout 1"
    time.sleep(0.5)
    os.system("clear")
    for ren in range(14) :
        for col in range(80) :
            if a[ren,col] == 0 :
                print(" ", end='')
            else :
                print("*", end='')
        print()

a = np.random.randint(0,2,[15,81])
a[:,0] = 0
a[0,:] = 0
a[:,80] = 0
a[14,:] = 0 

while 1 == 1 :
    escribe()
    b = np.zeros([14,80])

    for ren in range(1,13) :
        for col in range(1,79) :
            n = contarvecinos(ren,col)
            b[ren,col] = nuevoEdo(a[ren,col],n)

    a = b 