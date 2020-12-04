import numpy as np

def aceleraciones():
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

def velocidades (v, a, dt):
    return v + a * dt


def posiciones (r, v, dt):
    return r + v * dt 

Ms = 39.428
M = np.array ([6.547*10.0**(-6), 9.652*10.0**(-5), 1.185*10.0**(-4),
    1.272 *10.0**(-5), 3.764 *10.0**(-2),1.127*10.0**(-2),
    1.721 *10.0**(-3), 2.030 *10.0**(-3),2.775 *10.0**(-7)])   

#M = np.array([0.000006547, 0.00009652,0.0001185, 
#              0.00001272, 0.03764, 0.01127, 
#              0.001721, 0.002030, 0.0000002775])

r = np.array([0.387098,0,0, 0.723332,0,0, 1.000000,0,0,
    1.523689,0,0, 5.202758,0,0, 9.542824,0,0, 
    19.19206,0,0, 30.06893,0,0, 39.4817,0,0])
v = np.array([0.0,10.0934,0.0, 0.0,7.38415,0.0, 0,6.27978,0.0, 
    0.0, 5.08792,0.0, 0,2.75311,0.0, 0,2.03257,0.0, 
    0.0,1.43348,0.0, 0.0,1.14525,0.0, 0.0,0.99945, 0.0])   
a = np.zeros( (27) )
dt = 0.01

x = []

for n in range(5000):
    # Inicializar en cero todas las aceleraciones
    a = np.zeros( (27) )
    aceleraciones()

    v = velocidades(v,a,dt)

    r = posiciones(r,v,dt)

    x.append(r)

#graficar x
print(x)
