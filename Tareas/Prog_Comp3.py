"""
Sofia Trezza
Seccion 2
Programacion Competitiva 3
En un plano cartesiano, todos los puntos pueden ser identificados por tuplas (x,y). 
Escriba una función que, dado un punto p y un conjunto de puntos ps, indique cuál, 
de los puntos de ps, es el más cercano a p. Use la siguiente fórmula para hallar la distancia 
entre dos puntos:

d=√(x₁−x₂)²+(y₁−y₂)²

Donde x1 y y1 son los miembros de la tupla de p, y x2 y y2 son los del punto de ps que se está 
comparando. Use math.sqrt() si necesita la raíz cuadrada.

Ejemplo 1:
Entrada: p = (0,0); ps = {(-2,1), (1,1), (2,1), (1,2), (3,2), (5,1)}
Salida: (1,1)
"""
import math 
p = (0,0)
ps = [(-2,1), (1,1), (2,1), (1,2), (3,2), (5,1)]
results= []

def cercano(p):
    for tupla in ps:
        x2=tupla[0]
        y2=tupla[1]
        aux=((p[0]-x2)**2)+((p[1]-y2)**2)
        square=math.sqrt(aux)
        results.append(square)

    min_index= results.index(min(results))
    punto_mas_cercano=ps[min_index]
    print(f'El punto mas cercano a la coordenada {p} es {punto_mas_cercano}')

print(cercano(p))

