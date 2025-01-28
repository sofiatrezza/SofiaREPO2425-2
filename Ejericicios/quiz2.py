"""
 Escribir un programa que cuente las palabras que hay en una frase y las devuelva dentro de una lista
 o undiccionario (escoja una de las dos estructura de datos). También tiene que devolver una lista
 con las palabras que aparecen más de una vez. Por ejemplo si se le pasa la frase:
 Ejemplo input:
 La caracola está enterrada al lado de otra caracola de color
 Ejemplos de output con lista:
 [[‘La’, 1], [‘caracola’, 2], [‘está’, 1], [‘enterrada’, 1], [‘al’, 1], [‘lado’, 1], [‘de’, 2], [‘otra’, 1], [‘color’, 1]]
 Ejemplos de output con diccionario:
 {'La': 1, 'caracola': 2, 'está': 1, 'enterrada': 1, 'al': 1, 'lado': 1, 'de': 2, 'otra': 1, 'color': 1}
 Ejemplo de lista con palabras repetidas:
 ['caracola', 'de'
"""
#pedimos al usuario que ingese una frase
frase = input('Ingrese una frase >>> ')
# convertimos la frase a minúsculas y dividirla en palabras
palabras = frase.lower().split() #esto es como una lista
print(palabras)

# creamos un diccionario para contar las frecuencias
conteo_palabras = {}
#llamamos a cada una de las palabras de la variable que definimos 
for palabra in palabras:
    #las agregamos al diccionario
    # .get() verifica si la palabra ya existe y la agrega al diccionario, y cada vez que consiga otra
    #la va a agregar aumentando el "contador" (por eso se coloca el 0) y el +1
    conteo_palabras[palabra] = conteo_palabras.get(palabra, 0) + 1

# creamos una lista de pares en la que incertamos el diccionario (palabra, frecuencia)
# .items() toma los valores del diccionrio como key:value (pares)
#key: palabra - value: frecuencia
lista_palabras = list(conteo_palabras.items())

#creamos una lista para obtener las palabras repetidas
# encontramos las palabras que se repiten más de una vez
palabras_repetidas = []
#palabra,frecuencia porque son pares de datos (tuplas)
for palabra, frecuencia in lista_palabras:
    if frecuencia>1:
        palabras_repetidas.append(palabra)

print("Resultado en lista:", lista_palabras)
print("Resultado en diccionario:", conteo_palabras)
print("Palabras repetidas:", palabras_repetidas)