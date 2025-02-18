"""
diccionario={'a':0,'b':1,'c':0,'d':3}
max=4


claves=diccionario.keys()
salida=[0]*max
for c in claves:
    valor=diccionario[c]
    if valor<max:
        salida[valor] +=1

print(salida)
"""

nums=[3, 17, 8, 25, 2, 11]
def promedios(nums):
    suma_sin_ext=0
    suma=0
    if len(nums)<2:
        print('lista muy corta')
    media_todos=0
    media_sin_ext=0
    minimo=min(nums)
    mayor=max(nums)

    for i in range(len(nums)):
        suma+=nums[i]
    media_todos=suma/len(nums)
    
    nums.remove(minimo)
    nums.remove(mayor)
    print(nums)
    for j in range(len(nums)):
        suma_sin_ext+=nums[j]
    media_sin_ext=suma_sin_ext/ (len(nums))


    return(media_todos, media_sin_ext)

print(promedios(nums))
    
