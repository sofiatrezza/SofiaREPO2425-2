"""
Dado un arreglo de enteros con índice 0 llamado nums, encuentra un arreglo de enteros con índice 
0 llamado answer donde:
-	answer.length == nums.length.
-	answer[i] = |leftSum[i] - rightSum[i]|.
Donde:
-	leftSum[i] es la suma de elementos a la izquierda del índice i en el arreglo nums.
 Si no hay tal elemento, leftSum[i] = 0. 
-	rightSum[i] es la suma de elementos a la derecha del índice i en el arreglo nums. 
Si no hay tal elemento, rightSum[i] = 0.
Devuelve el arreglo answer.
-	Input: nums = [10,4,8,3]
-	Output: [15,1,11,22]
-	Explicación:
-	 El arreglo leftSum es [0, 0+10, 10+4, 10+4+8] -> [0,10,14,22]  
-	 El arreglo rightSum es [4+8+3, 8+3, 3, 0] -> [15,11,3,0].
-	 El arreglo answer es [|0 - 15|,|10 - 11|,|14 - 3|,|22 - 0|] = [15,1,11,22].

"""

nums = [10,4,8,3]
answer=[0]*len(nums)

def resuelve(nums):
    answer=[0]*len(nums)
    for i in range(len(nums)):
        leftSum=0
        for izq in range(i):
            leftSum+=nums[izq]

        rightSum=0
        for der in range(i+1, len(nums)):
            rightSum+=nums[der]

        answer[i]=abs(leftSum-rightSum)
    return answer


print(resuelve(nums))