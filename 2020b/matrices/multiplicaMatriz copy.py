# -*- coding: utf-8 -*-
"""
multiplicación de matrices 
No es elemento a elemento
sin usar la duncion de numpy y/o el operador de @

Por medio de vectores
"""

renA = int (input ("Cuantos renglones para A:"))
n = int(input("cuantas columnas para A y renglones B:"))
colB = int(input("cuantas columnas para B:"))

a = [ [0] * n for i in range(renA) ]
b = [ [0] * colB for i in range(n) ]
c = [ [0] * colB for i in range(renA) ]

#pedir datos matriz a
for i in range(renA) :
    for j in range(n) :
        a[i][j]=int(input("A:"))

#pedir datos matriz b
for i in range(n) :
    for j in range(colB) :
        b[i][j]=int(input("B:"))


#- Aqui se hace l a Multiplicacion 
for i in range(renA) :
   for j in range(colB) :
      sumatoria = 0 
      for r in range(n) :
         sumatoria = sumatoria + (a[i][r] * b[r][j])

      c[i][j] = sumatoria
      
# Mostrar datos
for i in range(renA) :

   for j in range(colB) :
      print("%5d"%(c[i][j]), end='')
   
   print()
