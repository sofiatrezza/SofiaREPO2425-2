"""
Pregunta3(5puntos)
 Senosdaunalistanumsdeenterosquerepresentaunalistacodificadacon
 "metroencoding".Considere cada par adyacente de elementos
 [freq,val]=[nums[2i],nums[2i+1]](coni>=0).
 Para cada uno de estos pares, existen freq elementos con valor val
 concatenados en una sublista. Concatena todas las sublistas de izquierda a derecha
 para generar la lista descomprimida. Devuelva la lista descomprimida.-
 Input:nums=[1,2,3,4]-Ouput: [2,4,4,4]-Explicación:
 El primer par [1,2] significaque tenemos freq=1 y val =2 así que
 generamos la matriz [2].
 El segundopar [3,4] significa que tenemos freq=3 y val=4 así que
 generamos [4,4,4].
 Al final laconcatenación[2]+[4,4,4]es[2,4,4,4]
"""

nums=[1,2,3,4]

def lista_descomprimida(nums):
    tuplas=[]
    for i in range(0,len(nums)-1,2):
        tuplas.append((nums[i],nums[i+1]))

    matriz=[]
    for tupla in tuplas:
        for i in range(len(tupla)-1):
            freq=tupla[i] 
            val=tupla[i+1]
            for j in range(freq):
                matriz.append(val)
    return matriz

print(lista_descomprimida(nums))