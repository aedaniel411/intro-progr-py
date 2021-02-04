import numpy as np

def pedirSudoku():
    matriz = np.zeros((9,9))

    for ren in range(9) : 
        for col in range(9) :
            matriz[ren, col] = int(input("sudoku[{:2.0f},{:2.0f}]".format(ren,col)))

    return matriz 

def mostrarSudoku(matriz) :
    for ren in range(9) : 
        for col in range(9) :
            if matriz[ren,col] == 0 :
                print("    ", end='')
            else: 
                print("{0:4.0f}".format(matriz[ren, col]), end='')
        print()
