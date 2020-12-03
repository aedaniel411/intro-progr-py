import numpy as np

def aceleraciones():
    # Inicializar en cero todas las aceleraciones
    a = np.zeros( (27) )

    # Calcular aceleración del planeta i
    for i in range (9) :
        indexi = 3 * i
        xi = r[indexi]
        yi = r[indexi + 1]
        zi = r[indexi + 2]
        
        invrp = ( 1.0 / np.sqrt (xi**2.0 + yi**2.0 + zi**2.0) )**3.0 

        # Aceleración del sol sobre el planeta i
        a[indexi] = a[indexi] - Ms * xi * invrp
        a[indexi + 1] = a[indexi + 1] - Ms * yi * invrp
        a[indexi + 2] = a[indexi + 2] - Ms * zi * invrp
        
        # Aceleración entre planetas k e i
        for k in range (i + 1, 9):
            indexk = 3 * k
            xk = r[indexk]
            yk = r[indexk + 1]
            zk = r[indexk + 2]
            
            invrpk = ( 1.0 / np.sqrt((xk - xi)**2.0 + (yk - yi)**2.0 + (zk - zi)**2.0) )** 3.0
            
            # Aceleración de planeta k sobre i
            a[indexi] = a[indexi] - M[k] * (xi - xk) * invrpk
            a[indexi + 1] = a[indexi + 1] - M[k] * (yi - yk) * invrpk
            a[indexi + 2] = a[indexi + 2] - M[k] * (zi - zk) * invrpk
            
            # Aceleración de planeta i sobre k 
            a[indexk] = a[indexk] - M[i] * (xk - xi) * invrpk
            a[indexk + 1] = a[indexk + 1] - M[i] * (yk - yi) * invrpk
            a[indexk + 2] = a[indexk + 2] - M[i] * (zk - zi) * invrpk

Ms = 39.428
M = np.array ([6.547 × 10−6, 9.652 × 10−5, 1.185 × 10−4,......])   
r = np.array ([0.387098,0,0,0.723332,0,0.... ]) 
v = np.array ([0,0.723332,0, 0,7.38415,0,......])        


