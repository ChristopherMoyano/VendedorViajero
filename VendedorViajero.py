import numpy as np
import pandas as pd
import sys

def LimpiezaDatos(entrada):
    matrizCoordenadas = pd.read_table(entrada, header=None, delim_whitespace=True, skiprows=6, skipfooter=1)
    matrizCoordenadas = matrizCoordenadas.drop(columns=0,axis=1).to_numpy

    return matrizCoordenadas

def CrearMatrizDistancia(matrizCoordenadas):
    
if len(sys.argv)==7:
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