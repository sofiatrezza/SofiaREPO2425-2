"""
 Pregunta4(5puntos)
 Dado un arreglo de enteros nums de 2nenteros,agrupe estos enteros enn
 pares (a1,b1), (a2,b2), ..., (an,bn) de tal forma que la suma de min(ai,bi) para todos
 sea máxima. Devuelve la suma maximizada.
 -Input:nums=[1,4,3,2]
 -Output:4
 -Explicación:
 Todas las posibles emparejamientos (ignorando el orden de los
 elementos)son:
 1. (1,4),(2,3)->min(1,4)+min(2,3)=1+2=3
 2. (1,3),(2,4)->min(1,3)+min(2,4)=1+2=3
 3. (1,2),(3,4)->min(1,2)+min(3,4)=1+3=4
 Entonces la suma máxima posible es 4
"""
nums=[1,4,3,2]

def suma_pares_maxima(nums):
    nums.sort()

    suma_maxima=0
    for i in range(0,len(nums),2):
        suma_maxima+=nums[i]
    
    return f'la suma maxima posible es {suma_maxima}'


print(suma_pares_maxima(nums))