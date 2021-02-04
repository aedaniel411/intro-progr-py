import numpy as np

#myLista = [1,2,3,4,5]
myArray = np.array([1,2,3,4,5])
print (myArray, type(myArray))

myLista2 = [6,7,8,9,10]
myArray2 = np.array(myLista2)
print (myArray2, type(myArray2))

#listaSuma = myLista + myLista2
arraySuma = myArray + myArray2

print(arraySuma)

