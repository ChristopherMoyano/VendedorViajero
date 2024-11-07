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
    Solucion = np.arange(1,n+1)
    np.random.shuffle(Solucion)
    return Solucion

def CrearCosto(Solucion, matrizDistancia):
    suma =0
    for i in range(0,Solucion.shape[0]-2,1):
        suma+=matrizDistancia[Solucion[i]-1,Solucion[i+1]-1]
    suma += matrizDistancia[Solucion[Solucion.shape[0]-1]-1,0]
    return suma

def CrearMatrizFeromonaInicial(Costo,n):
    Matriz = np.ones((n,n),float)
    Matriz = (1/(n*Costo))*Matriz
    np.fill_diagonal(Matriz,0)
    return Matriz

def CrearColonia(col,n):
    Matriz = np.zeros((col,n),int)
    for i in range(col):
        Matriz[i][0] = np.random.randint(1,n+1)
    return Matriz

def Transicion_1(Feromona, Heuristica,B,hormigas,q0,Feromona_inicial,tev):
    mascara = np.ones((hormigas.shape[0],hormigas.shape[1]),int)
    for i in range(hormigas.shape[0]):
        for j in range(hormigas.shape[1]):
            if hormigas[i][j] != 0:
                mascara[i][hormigas[i][j]-1] = 0  
    for i in range(hormigas.shape[0]):
        for j in range(hormigas.shape[1]-1):
            random = np.random.rand()
            if (random <= q0):
                vector_aux = np.power(Heuristica[hormigas[i][j]-1],B)*Feromona[hormigas[i][j]-1]*mascara[i]
                pos_max = np.random.choice(np.where(vector_aux == np.max(vector_aux))[0])   #si me tira error en esta linea borrar un [0]
                hormigas[i][j+1] = pos_max + 1
                mascara[i][pos_max] = 0
            else:
                nodo = Transicion_2(Feromona,Heuristica,B,hormigas,mascara,i,j)
                hormigas[i][j+1] = nodo + 1
                mascara[i][nodo] = 0
            Actualizar_feromona_local(Feromona,tev,Feromona_inicial,hormigas[i][j]-1,hormigas[i][j+1]-1)
    return hormigas


#implementar la ruleta
def Transicion_2(Feromona,Heuristica,B,hormigas,mascara,i,j):
    suma_total= np.sum(np.power(Heuristica[hormigas[i][j]-1],B)*Feromona[hormigas[i][j]-1]*mascara[i])
    ruleta = (np.power(Heuristica[hormigas[i][j]-1],B)*Feromona[hormigas[i][j]-1]*mascara[i])/suma_total
    for k in range(1,ruleta.shape[0]):
        ruleta[k]=ruleta[k]+ruleta[k-1]
    random = np.random.rand()
    for k in range(ruleta.shape[0]):
        if random < ruleta[k]:
            return k

def Actualizar_feromona_local(Feromona,tev,Feromona_inicial,hormiga,nodo):
    Feromona[hormiga][nodo] = Feromona[hormiga][nodo]*(1-tev) + tev *Feromona_inicial[hormiga][nodo]
    return Feromona

    
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
Mejor_Solucion = CrearPrimeraSolucion(matrizHeuristica.shape[0])
Mejor_Costo = CrearCosto(Mejor_Solucion,matrizDistancia)
print(Mejor_Costo)
MatrizFeromonaInicial = CrearMatrizFeromonaInicial(Mejor_Costo,matrizHeuristica.shape[0])
Feromona = MatrizFeromonaInicial
Colonia = CrearColonia(col,matrizHeuristica.shape[0])
iteracion =0
while(iteracion<ite):
    hormigas = Transicion_1(Feromona,matrizHeuristica,B,Colonia,q0,MatrizFeromonaInicial,tev)
    for i in range(col):
        NuevoCosto = CrearCosto(hormigas[i],matrizDistancia)
        if NuevoCosto < Mejor_Costo:
            Mejor_Costo = NuevoCosto   ##supuesto mejor costo 7542
            Mejor_Solucion = hormigas[i]
    Feromona = (1-tev)*Feromona
    delta = 1/Mejor_Costo
    for i in range(Mejor_Solucion.shape[0]-1):
        Feromona[Mejor_Solucion[i]-1,Mejor_Solucion[i+1]-1]+= delta
        Feromona[Mejor_Solucion[i+1]-1,Mejor_Solucion[i]-1] += delta
    Feromona[Mejor_Solucion[0]-1,Mejor_Solucion[Mejor_Solucion.shape[0]-1]-1] +=delta
    Feromona[Mejor_Solucion[Mejor_Solucion.shape[0]-1]-1,Mejor_Solucion[0]-1] +=delta
    print(Mejor_Costo)
    iteracion+=1



