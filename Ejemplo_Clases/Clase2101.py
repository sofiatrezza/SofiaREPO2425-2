#listas
#indexing- se puede referir a un elemento de la lista con un numero y siempre empieza en 0

semana=['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
print(type(semana))
#>>list
print(semana[1]) #en el rango de la lista
#>>martes
#se pueden buscar con indices negativos y va de atras hacia adelante
print(semana[-1])
#>>domingo

#slicing- sublistas-subrange
print(semana[4:7]) #va a imprimir del 4 al 7
#>>['viernes', 'sabado', 'domingo']
#el 7 es el ultimo elemento de la lista, se debe tomar en cuenta el rango

#los subrange en python el primer numero es inclusivo y el ultimo es exclusivo
print(semana[4:6]) #va a imprimir del 4 al 6
#>>['viernes', 'sabado']

#si no se cual es el final de la lista puede dejarse en blanco y va a leer desde el primer numero hasta el final
#o viceversa
print(semana[4:]) #va a imprimir del 4 hasta el final
#>>['viernes', 'sabado', 'domingo']
print(semana[:4]) #va a imprimir del 4 hasta el final
#>>['lunes', 'martes', 'miercoles', 'jueves']

#in- es para saber si ese elemento o palabra esta en un str -tiene que ser exacto
user_name='@saman_courses'
print('@' in user_name)
#>>True
if '@' in user_name:
    print(user_name)
else:
    print('@'+user_name)

#se puede usar en listas
nums=[1,2,3,4,5]
if 6 not in nums: #estoy preguntando si no esta 
    print('Not here!')

#se pueden cambiar los datos de la lista' son mutables
semana[2]='miércoles'
print(semana)
#>>['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sabado', 'domingo']

#se puede hacer una copia para asegurar la lista
semana_copy=semana
semana_copy[3]='juernes'
print(semana_copy)
#>>['lunes', 'martes', 'miércoles', 'juernes', 'viernes', 'sabado', 'domingo']
#pero se va a cambiar la lista original
#para hacer una copia real se debe hacer un ciclo para que se vayan almacenando los datos

#metodos para listas
grades=[20,18,5,10,13,13,14,3,9]
#busca el menor numero de la lista
print(min(grades))
#>> 3

#busca el mayor numero de la lista
print(max(grades))
#>> 20

#te dice el laro de la lista, la cantidad de elementos
print(len(grades))
#>> 9

#ordena la lista de menor a mayor
print(sorted(grades))

#buscar en python tutorials

#iterador
ciudades=['Caracas','Valencia','Margarita','Maracay']
for ciudad in ciudades: #VARIABLE DE ITERACION- ciudad
    print(ciudad)
    #>> Caracas
    # Valencia
    # Margarita
    # Maracay

#range
for i in range(1,10): #start- primer numero/ stop- ultimo
    print(i)

#step- condiciona- es el tercer numero
for i in range(1,10,2):
    print(i)

