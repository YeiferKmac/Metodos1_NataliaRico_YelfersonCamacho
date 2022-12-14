#4 Calcular todas las raices reales de los primeros 20 polinomios de Legendre

import numpy as np
import sympy as sym

def Legendre(n):  
    x = sym.Symbol('x')
    y = sym.Symbol('y')
    ecuacion = sym.diff(y,x,n)*((x^2-1)^n)/(2^n* np.math.factorial(n))
    return ecuacion 

solucion = []
n=20
for i in range(n+1):
    solucion.append(GetLegendre(i))

    print (solucion)
