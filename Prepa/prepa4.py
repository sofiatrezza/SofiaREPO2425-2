"""

Dada una matriz 5x5 de números enteros, determine el producto de las sumas de cada 
columna y fila correspondiente, es decir, el producto de la primera fila por la primera 
columna, la segunda fila por la segunda columna, etc. Si el producto es cuadrado perfecto, 
imprimir True, si no lo es, imprimir False.
Input:
"""


matriz = [
[3, 4, 1, 4, 0],
[9, 8, 4, 0, 5],
[6, 2, 7, 5, 3],
[5, 3, 8, 6, 1],
[4, 5, 2, 8, 6]
]

filas=len(matriz) #numero de filas
columnas=len(matriz[0]) #numero de columnas

suma_filas=0
suma_columnas=0
sumas_filas=[]
sumas_columnas=[]

for i in range(filas):
    suma_filas=0
    suma_columnas=0
    for j in range(columnas):
        #la i se vuelve un elemento estatico
        suma_columnas+=matriz[j][i]
        suma_filas+=matriz[i][j]
