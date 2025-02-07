"""
1. Dada una secuencia no-ordenada de n enteros, hallar el segundo-menor
"""
numeros=[12, 5, 23, 9, 1, 15]
numeros_ordenados=sorted(numeros)
print(f'el segundo menor numero es {numeros_ordenados[1]}')

"""
2. Suponga una lista de 100 números que representan las notas de un grupo de
estudiantes, realice un algoritmo que determine:
a. El promedio de notas del salón
b. Cuántos alumnos aprobaron
c. Cuántos alumnos reprobaron
"""
notas=[33, 6, 34, 3, 9, 64, 19, 49, 23, 76, 90, 100, 0, 75, 12, 12, 71, 28, 57,\
        37, 27, 64, 6, 60, 58, 22, 98, 35, 94, 1, 84, 84, 44, 73, 85, 64, 62, 62,\
            53, 17, 19, 47, 39, 90, 59, 28, 30, 65, 29, 15, 77, 61, 19, 5, 69, 80,\
                  95, 48, 4, 38, 78, 61, 50, 53, 64, 77, 12, 10, 42, 10, 42, 37, 44,\
                    94, 6, 11, 17, 51, 45, 84, 72, 56, 65, 81, 93, 17, 76, 63, 99, 52,\
                          81, 39, 100, 18, 47, 21, 90, 27, 35, 19]
suma=0
aprobados=[]
reprobados=[]
for nota in notas:
    suma+=nota
    if nota>=50:
        aprobados.append(nota)
    elif nota<=50:
        reprobados.append(nota)

promedio=suma/len(notas)
print(f'el promedio de la seccion es {promedio}')
print(f'el numero de estudiantes aprobados es {len(aprobados)} de 100')
print(f'el numero de estudiantes reprobados es {len(reprobados)} de 100')

"""
3. Dada una lista de números enteros y un objetivo entero, devuelve índices de
los dos números de modo que sumen el objetivo.
a. Puede suponer que cada entrada tendría exactamente una solución y
no se puede usar el mismo elemento dos veces.
b. Puede devolver la respuesta en cualquier orden.
Entrada: nums = [2,7,11,15], objetivo = 9
Salida: [0,1]
Explicación: Como nums[0] + nums[1] == 9, devolvemos [0, 1].
"""
nums = [2,7,11,15]
objetivo=9
for i in range(len(nums)-1):
    for j in range(i+1, len(nums)):
        if nums[i]+nums[j]==objetivo:
            print(f'la suma de {nums[i]} + {nums[j]} = {objetivo} y sus indices son [{i},{j}] respectivamente')

"""
4. Dada una lista de números enteros, devuelve el número de buenos pares.
Un par (i, j) se dice bueno si nums[i] == nums[j] e i < j.
Entrada: nums = [1,2,3,1,1,3]
Salida: 4
"""  
numeros = [1,2,3,1,1,3]
pares_buenos=[]
for a in range(len(numeros)-1):
    for b in range(a+1, len(numeros)):
        if numeros[a]==numeros[b] and a<b:
            pares_buenos.append((a,b))
            print(f'el numero de pares buenos es {len(pares_buenos)} y sus indices son {pares_buenos}')

"""
5. Dada la lista nums, para cada nums[i] averigüe cuántos números de la lista son
más pequeños que él. Es decir, para cada nums[i] tienes que contar el número
de j válidos tales que j != i y que nums[j] < nums[i].
Devuelve la respuesta en una matriz.
Entrada: nums = [8,1,2,2,3]
Salida: [4,0,1,1,3]
"""

nume = [8,1,2,2,3]
cont=0
nume_menores=[]

for c in range(len(nume)):
    cont = 0  # Reinicia el contador para cada elemento
    for d in range(len(nume)):
        if c != d and nume[d] < nume[c]:
            cont += 1
    nume_menores.append(cont)  # Añade el conteo para el elemento actual

print(nume_menores)
