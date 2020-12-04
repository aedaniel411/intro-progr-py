try:
    archivito = open('datos01.dat','r')
except:
    print ('Error al intentar abrir el archivo')
    exit()
    
lista = archivito.readlines()

matrizTexto=[]
for renglon in lista :
    e = renglon.split()
    matrizTexto.append(e)

archivito.close()

matrizNumeros=[]
for ren in matrizTexto:
    lnum = []
    for col in ren:
        lnum.append(float(col))
    
    matrizNumeros.append(lnum)

x=[]
y=[]
for ren in matrizNumeros:
    x.append(ren[0])
    y.append(ren[1])

import matplotlib.pyplot as plt

plt.scatter(x,y,color='red')
plt.show()