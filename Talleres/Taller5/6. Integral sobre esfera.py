import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta
from scipy import integrate
from tqdm import tqdm

#Se utilizó el código de clase para guia

#Como es una esfera, el z también cambia de acuerdo a phi y pi, por eso por por parametros solo se va recibir N y R. 
def CreateEsfera( N, R ): 
    
    X = np.zeros(N)
    Y = np.zeros_like(X)
    Z = np.zeros_like(X)
    
    for i in tqdm(range(N)): 
        u = np.random.rand()
        r = R*u**(1/2)
        
        phi = np.random.uniform(0,2*np.pi)
        
        X[i] = r*np.sin(phi)*np.cos(np.pi)
        Y[i] = r*np.sin(phi)*np.sin(np.pi)
        Z[i] = r*np.cos(phi)
    
    return X,Y,Z
  
#Integral sobre la esfera:
def funcion(R):
    return np.exp(phi). #phi= raiz de x^2+y^2+z^2
 
