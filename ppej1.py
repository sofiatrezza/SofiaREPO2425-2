"""
Realice una función que dado un arreglo de números enteros nums y un 
número entero k, devuelva True si existen dos índices distintos i y j en el arreglo tales 
que nums[i] == nums[j] y abs(i - j) <= k. - - 
Input: nums = [1,2,3,1], k = 3 
Output: True 
"""
nums=[1,2,3,1]
k=3

def funcion(nums,k):
    for i in range(len(nums)-1):
        for j in range(i+1,len(nums)):
            if nums[i]==nums[j] and abs(i-j)<=k:
                return True
            
print(funcion(nums,k))
