"""
Realice una función que dado un arreglo nums que contiene n números 
distintos en el rango [0, n], devuelve el único número que falta en el rango y no está 
presente en el arreglo. - - 
Input:  nums = [3,0,1] 
Ouput: 2 
- 
Explicación:  
n = 3 ya que hay 3 números, por lo que todos los números están en el 
rango [0,3]. El número 2 es el que falta en el rango ya que no aparece 
en nums.
"""

nums=[3,0,1]

def numero_que_falta(nums):
    n=len(nums)
    for i in range(n):
        if i not in nums:
            numero=i
            print(f'el rango va de 0-{n} y el numero que falta es {numero}')

print(numero_que_falta(nums))