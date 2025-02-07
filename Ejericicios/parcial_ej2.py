"""
Realiza una función que reciba una lista de enteros nums, y devuelva la 
cantidad de número de pares buenos. Un par (i, j) se llama bueno si nums[i] == nums[j] y i < j.
- Input: nums = [1,2,3,1,1,3]
- Output: 4
- Explicación: Hay 4 pares buenos: (0, 3), (0, 4), (3, 4), (2, 5) si el índice de la
lista comienza en .0, es decir es 0 – indexado
"""

nums = [1,2,3,1,1,3]

def es_par_bueno(nums):
    pares_buenos=[]
    for i in range(len(nums)-1):
        for j in range((i+1),len(nums)):
            if nums[i]==nums[j] and i<j:
                par=(i,j)
                pares_buenos.append(par)
    
    resultado=f'hay {len(pares_buenos)} pares buenos y son {pares_buenos}'
    return resultado

print(es_par_bueno(nums))

