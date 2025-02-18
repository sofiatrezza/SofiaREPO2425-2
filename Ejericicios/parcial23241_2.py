"""
 Pregunta 2 (5 puntos)
 Dada una lista ordenada de enteros distintos y un valor objetivo, devuelve el
 índice si el objetivo se encuentra. Si no, devuelve el índice donde estaría si se
 insertará en orden.--
 Input: nums = [1,3,5,6], target = 5
 Output: 2
"""

nums = [1,3,5,6]
target = 5

def buscar_indice(nums, target):
    for index, num in enumerate(nums):
        if num==target:
            print(index)

for i in range(len(nums)):
    if target not in nums:
        nums.append(target)
        nums.sort()

buscar_indice(nums, target)

        