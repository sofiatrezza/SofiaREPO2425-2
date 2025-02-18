"""
 Pregunta 1 (5 puntos)
 Un streng, es un string que está presente solo una vez en una lista. Dada una
 lista de strings arr y un entero k, devuelve el k-ésimo streng presente en arr. Si hay
 menos de k streng, devuelva una cadena vacía "". Tenga en cuenta que las strengs
 se consideran en el orden en que aparecen en la lista.--
Input: arr = ["d","b","c","b","c","a"], k = 2
 Output: "a"
 Explicación:
 Los únicos dos strings distintos en arr son "d" y "a".
 "d" aparece de 1ro.
 "a" aparece de 2do.
 Como k == 2, "a" es el resultado
"""

arr = ["d","b","c","b","c","a"]
k = 2

#creamos un diccionario en el que vamos a almacenar los strings 
# y la cantidad de veces que se repiten
strings={}
for string in arr:
    #revisa si la variable esta, si esta, entonces aumenta la frecuenta
    if string in strings:
        strings[string]+=1 #se agrega la variable y se le asigna el numero de veces que se aumento
    #si no esta, entonces la agrega con una fecuencia de 1
    else:
        strings[string]=1 #si solo lo consigue una vez, la frecuencia es 1

#creamos una lista donde agregaremos los strings unicos
strings_unicos=[]
#esta es la manera de acceder a key:value de un diccionario
for string, frecuencia in strings.items():
    #si value=1 es decir de la frecuencia es 1
    if frecuencia==1:
        #entonces agrega el string a la lista
        strings_unicos.append(string)
print(f'los strings repetidos son {strings_unicos}')

#buscamos el string en la lista segun la posicion k
k_string= strings_unicos[k-1]
print(f'el {k}do string repetido es {k_string}')