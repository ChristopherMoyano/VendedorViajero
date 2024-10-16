import numpy as np
import pandas as pd
import sys
from scipy.spatial import distance_matrix

def LimpiezaDatos(entrada):
    matrizCoordenadas = pd.read_table(entrada, header=None, delim_whitespace=True, skiprows=6, skipfooter=2)
    matrizCoordenadas = matrizCoordenadas.drop(columns=0,axis=1).to_numpy()

    return matrizCoordenadas

def CrearMatrizHeuristica(matrizDistancia):
    matrizHeuristica = np.full_like(matrizDistancia,fill_value=1/matrizDistancia,dtype=float)
    np.fill_diagonal(matrizHeuristica,0)
    return matrizHeuristica

def CrearPrimeraSolucion(n):
    Solucion = np.arange(n)
    np.random.shuffle(Solucion)
    return Solucion

def CrearCosto(Solucion, matrizDistancia):
    suma =0
    for i in range(0,Solucion.shape[0]-1,1):
        for j in range(1,Solucion.shape[0],1):
            suma += matrizDistancia[Solucion[i],Solucion[j]]
    suma += matrizDistancia[Solucion[Solucion.shape[0]-1],0]
    return suma

def CrearMatrizFeromonaInicial(Costo,n):
    Matriz = np.ones((n,n),float)
    Matriz = (1/(n*Costo))*Matriz
    np.fill_diagonal(Matriz,0)
    return Matriz

def CrearColonia(col,n):
    Matriz = np.zeros((col,n),int)
    for i in range(col):
        Matriz[i][0] = np.random.randint(n)
    return Matriz
        
    
if len(sys.argv)==8:
    semilla = int(sys.argv[1])
    col = int(sys.argv[2]) #tamaño de la colonia
    ite = int(sys.argv[3]) #iteracion  
    tev = float(sys.argv[4]) #tasa de evaporacion
    B = float(sys.argv[5]) #Beta valor real entre 2 y 5
    q0 = float(sys.argv[6]) #q0: valor real entre 0 y 1
    entrada = sys.argv[7] #nombre del archivo a leer
    print(semilla, col, ite, tev, B, q0, entrada)
else:
    print("Error en la entrada de los parámetros")
    print("Los parámetros a ingresar son: Semilla TamañoColonia Iteraciones TasaDeEvaporacion Beta q0 nombreArchivo")
    sys.exit(0)

np.random.seed(semilla)
matrizCoordenadas = LimpiezaDatos(entrada)
matrizDistancia = distance_matrix(matrizCoordenadas,matrizCoordenadas)
matrizHeuristica = CrearMatrizHeuristica(matrizDistancia)
primeraSolucion = CrearPrimeraSolucion(matrizHeuristica.shape[0])
Costo = CrearCosto(primeraSolucion,matrizDistancia)
MatrizFeromonaInicial = CrearMatrizFeromonaInicial(Costo,matrizHeuristica.shape[0])
Colonia = CrearColonia(col,matrizHeuristica.shape[0])
print(Colonia)



