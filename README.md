# VendedorViajero
 se utilizara un modelo metahuristico basado en una colonia de hormigas para buscar una solución para este problema

 >[!important]
>Recuerda instalar las bibliotecas **Numpy** **Scipy** **Pandas** con:
> ```
> pip3 install Numpy.
>```
> ```
> pip3 install Scipy.
>```
> ```
> pip3 install Pandas.
>```

## Funcionamiento basico del codigo
### Metodología

>1. Se utiliza un algoritmo de optimización de colonias de hormigas, en el cual se tiene un solución inicial de manera aleatoria, el cual tiene un costo determinado por la distancia que hay entre los nodos.
>
>2. una vez obtenido la solución inicial y el costo se procede a formar una colonia de hormigas, las cuales parten un nodo inicial aleatorio y de alli van decidiendo que nodo tomar a partir de las siguientes formulas:
>   ```math
>   j_0 = \begin{cases}\arg \max_{j \in N_k(i)} \{ \tau_{ij} \cdot \eta_{ij}^\beta \} & \text{con probabilidad } q_0 \\J_{\text{random}} & \text{con probabilidad } (1 - q_0)\end{cases} 
>   ```
> donde:
>
>- $`j_0 `$ : es el próximo nodo a ser alcanzado.
>
>- $`N_k(i)`$ : es el conjunto de nodos en el vecindario del nodo $` i `$ para la $` {k}^{th} `$ hormiga.
>
>- $`\tau_{ij}`$: es el valor de la feromona en el segmento $` ij `$.
>
>- $`\eta_{ij}`$: es el valor de la heurística en el segmento $` ij `$.
>
>- $`\beta `$:es el peso del valor de la heurística.
>
>- $`q_0 `$: es un valor de probabilidad límite predefinido $` 0 \leq q_0 \leq 1 `$.
>
>- $` J_{\text{random}}`$:es un valor elegido randomicamente con una función de probabilidad dada por la siguiente ecuación :
>
>  ```math
>   S(p_{ij}^k) = \begin{cases}\frac{\tau_{ij} \cdot \eta_{ij}^\beta}{\sum_{j \in N_k(i)} \tau_{ij} \cdot \eta_{ij}^\beta} & \text{si } j \in N_k(i) \\ 0 & \text{en otro caso} \end{cases}
>  ```
>  donde:
>
> - $` p_{ij}^k`$ : es la probabilidad de elegir el próximo nodo $`j`$ desde $`i`$ para la $`k^{th}`$ hormiga.
>
> - $`S()`$ : es algún mecanismo de selección tal como el de la ruleta o torneo.
>
>3. Luego de encontrar el nodo siguiente a visitar, se actualiza la feromona de manera local con la siguiente formula:
> ```math
>\tau_{ij}^t = (1 - \alpha) \tau_{ij}^{t-1} + \alpha \tau_{ij}^0
> ```
> donde:
>
> - $`\tau_{ij}^0`$: es el valor inicial de feromona puesto en el segmento $`ij`$
>
>4. Una vez obtenido el orden de todos los nodos a visitar, si existe una mejor solución que la inicial,
>se actualiza el costo, de tal forma que el mejor costo sea el menor valor obtenido entre todas las rutas que tomaron cada una de las hormigas.
>5. Una vez obtenido el mejor costo se actualiza la feremona de la siguiente forma:
> ```math
>\tau_{ij}^t = (1 - \alpha) \tau_{ij}^{t-1} + \alpha \Delta
> ```
> donde:
> - $`\tau_{ij}^t`$ : es el nivel de feromona en el tiempo $`t`$.
> - $`\alpha `$:es el factor de evaporación de feromona.
> - $`\Delta `$: es el refuerzo positivo de feromona perteneciente a la mejor solución $`(0 \text{ ó } \Delta)`$.
>6. este proceso se repite hasta llegar a la iteración final.

### Que colocar en la terminal:

>[!Tip]
> en la terminal colocar:
>```
>[nombre.py] [semilla] [tamaño colonia] [iteracion] [tasa de evaporacion] [Beta] [q0] [nombre del archivo a leer]
>```
>
### integrantes:
- Matias Olave
- Debora Huerta
- Christopher Moyano







