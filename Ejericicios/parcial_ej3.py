"""
Se te da una lista de strings nombres y otra llamada edad que consta de 
enteros positivos distintos. Ambas matrices tienen una longitud de n. 
Para cada índice i, nombres [i] y edad [i] denota el nombre y la altura de la persona i. 
Devuelve los nombres ordenados en orden descendente por la edad de las personas.
-
Input: nombres = ["Mary","John","Emma"], edad = [37,9,18]
-
Output: ["John", "Emma", "Mary"]
-
Explicación: John es el menor, seguido de Emma y Mary.
"""

nombres = ["Mary","John","Emma"]
edad = [37,9,18]

def ordenar(nombres, edad):
    lista_sin_orden=[]

    for i in range(len(edad)):
        nombre_edad=(nombres[i], edad[i])
        lista_sin_orden.append(nombre_edad)

    lista_ordenada=sorted(lista_sin_orden, key=lambda x: x[1], reverse=True)
    nombresord=[]
    for nombre, edad in lista_ordenada:
        nombresord.append(nombre)
    
    return nombresord

print(ordenar(nombres,edad))
    
"""
key=lambda x: x[1]:

El argumento key especifica una función que se utilizará para extraer la "clave" de ordenación 
de cada elemento de la lista.
En este caso, se utiliza una función anónima lambda que se define de la siguiente manera:
lambda x: x[1]
lambda indica que se está definiendo una función anónima.
x es el argumento de la función (en este caso, representa un elemento de la lista lista,
 que es una tupla (nombre, edad)).
x[1] indica que la función debe devolver el segundo elemento de la tupla x, que es la edad.
En resumen, key=lambda x: x[1] le dice a sorted() que debe utilizar la edad de cada persona como 
clave para ordenar la lista.
3. reverse=True:

El argumento reverse=True indica que la lista debe ordenarse en orden descendente, es decir, 
de mayor a menor edad.
En conjunto:

ordenados = sorted(lista, key=lambda x: x[1], reverse=True)
Esta línea de código toma la lista lista (que contiene tuplas (nombre, edad)), 
la ordena en orden descendente según la edad (utilizando key=lambda x: x[1] y reverse=True), 
y guarda la nueva lista ordenada en la variable ordenados.
"""

