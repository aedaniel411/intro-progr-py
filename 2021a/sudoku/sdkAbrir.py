import numpy as np
import modulosudoku as msdk

archivo = input ("nombre de archivo a abrir? ")
matriz = np.loadtxt(archivo)

msdk.mostrarSudoku(matriz)

matSol = (np.ones((9,9,9)) * (-10))

for pag in range(9):
    for ren in range(9):
        for col in range(9):
            if matriz[ren,col] == pag+1:
                #-- hacer todo el renglon
                matSol[pag, ren, 0:] = 0
                #-- hacer renglones en 0
                matSol[pag, 0:, col] = 0
                #-- para cuadrantes
                

#---- ver libro ---
for pag in range(9):
    for ren in range(9):
        for col in range(9):
            print ("{:4.0f}".format(matSol[pag,ren,col]), end='')
        print()
    print()
    print("--"+str(pag+2)+"--")


