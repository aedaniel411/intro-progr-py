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
        do k = i + 1, 9 !Aceleraci´on entre planetas k e i
        indexk = 3 ∗ k
        xk = r(indexk − 2); yk = r(indexk − 1); zk = r(indexk)
        inverpk = (1/SQRT ((xk − xi)
        2 + (yk − yi)
        2 + (zk − zi)
        2
        ))3
        —— Aceleraci´on de planeta k sobre i ——
        a(indexi − 2) = a(indexi − 2) − Mk ∗ (xi − xk) ∗ invrpk
        a(indexi − 1) = a(indexi − 1) − Mk ∗ (yi − xk) ∗ invrpk
        a(indexi) = a(indexi) − Mk ∗ (zi − xk) ∗ invrpk
        —— Aceleraci´on de planeta i sobre k ——
        a(indexk − 2) = a(indexk − 2) − Mi ∗ (xk − xi) ∗ invrpk
        a(indexk − 1) = a(indexk − 1) − Mi ∗ (yk − yi) ∗ invrpk
        a(indexk) = a(indexk) − Mi ∗ (zk − zi) ∗ invrpk
        end do
