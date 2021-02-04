import numpy as np

matriz1 = np.array( [ [1, 2, 3], [4, 5, 6], [7, 8, 9] ] )
print (matriz1)

matriz2 = np.array([ [9,8,7], [6,5,4], [3,2,1] ])
print (matriz2)

print (matriz1 + matriz2)
print (matriz1 - matriz2)
print (matriz1 * matriz2)
print()

print (matriz1 @ matriz2)
print()
print (matriz1.dot(matriz2))