# VendedorViajero
 se utilizara un modelo metahuristico basado en una colonia de hormigas para buscar una solución para este problema

 >[!important]
>Recuerda instalar las bibliotecas **Numpy** **Scipy** **Pandas** con:
> pip3 install Numpy.
> pip3 install Scipy
> pip3 install Pandas
>

## Funcionamiento basico del codigo
### Metodología

>1. Se utiliza un algoritmo de optimización de colonias de hormigas, en el cual se tiene un solución inicial de manera aleatoria, el cual tiene un costo determinado por la distancia que hay entre los nodos.
>
>2. una vez obtenido la solución inicial y el costo se procede a formar una colonia de hormigas, las cuales parten un nodo inicial aleatorio y de alli van decidiendo que nodo tomar a partir de las siguientes formulas:
>   ```math
>   j_0 = \begin{cases}\arg \max_{j \in N_k(i)} \{ \tau_{ij} \cdot \eta_{ij}^\beta \} & \text{con probabilidad } q_0 \\J_{\text{random}} & \text{con probabilidad } (1 - q_0)\end{cases} 
>   ```
>donde:
>
>- $`j_0 `$ : es el próximo nodo a ser alcanzado.
>
>- $`N_k(i)`$ : es el conjunto de nodos en el vecindario del nodo $` i `$ para la $` {k}^{th} `$ hormiga.
>
>- $`\tau_{ij}`$: es el valor de la feromona en el segmento $` ij `$.
>
>- $`\eta_{ij}`$: es el valor de la heurística en el segmento $` ij `$.
>
>- $`\beta `$: Parámetro que controla la importancia de la visibilidad en la decisión.
>
>- $`q_0 `$: Probabilidad de seleccionar el valor que maximiza el producto de $` \tau_{ij} \cdot \eta_{ij}^\beta `$.
>
>- $` J_{\text{random}}`$: Representa una selección aleatoria de $` j `$ en caso de no seleccionar el máximo, con probabilidad $` 1 - q_0 `$.





