from modulosudoku import pedirSudoku
import numpy as np
import modulosudoku as msdk

matriz = np.zeros((9,9))

matriz = msdk.pedirSudoku()

msdk.mostrarSudoku(matriz)

archivo = input ("nombre de archivo a guardar? ")
np.savetxt(archivo, matriz,)
