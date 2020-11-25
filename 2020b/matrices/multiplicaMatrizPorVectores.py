# -*- coding: utf-8 -*-
"""
multiplicación de matrices 
No es elemento a elemento
sin usar la duncion de numpy y/o el operador de @

Por medio de vectores
"""

import numpy as np

a = np.array([ [1, 1], [0, 1] ])
b = np.array([ [1, 0], [1, 1] ])

c = np.zeros((len(a),len(b[0,:])))

for ren in range(len(c)) :
    for col in range(len(c[0,:])) :
        #print (ren, col, a[ren,:], b[:,col], a[ren,:] * b[:,col],  sum(a[ren,:] * b[:,col]))
        c[ren,col] = sum(a[ren,:] * b[:,col])

print(c)
